import os

class GenerateNetAppPython():

    def __init__(self, categories, types, methods):
        self.categories = categories
        self.types = types
        self.methods = methods
        self.base_output_dir = "{}/../../generated-libraries/python/netapp/".format( os.path.dirname(os.path.realpath(__file__)) )
        self.class_to_category = {}

    def ensure_directory(self, folder_name):
        try:
            os.makedirs( "{}/{}".format(self.base_output_dir, folder_name) )
        except OSError as error:
            if error.args[0] == 17 or error.args[0] == 183:
                pass

    def as_method_name(self, string):
        return self.as_file_name( string )

    def as_file_name(self, string):
        return string.replace('-','_')

    def as_class_name(self, name):
        parts = name.split("-")
        out_parts = []
        for part in parts:
            out_parts.append( part.title() )
        return "".join( out_parts )

    def get_unique(self, items):
        keys = {}
        for item in items:
            keys[ item ] = 1;
        return keys.keys()

    def map_data_type(self, data_type):

        if data_type == "string" or data_type == "string[]":
            return [ "basestring", (True if data_type.endswith("[]") else False), None, None ]
        if data_type == "boolean" or data_type == "boolean[]":
            return [ "bool", (True if data_type.endswith("[]") else False), None, None ]
        if data_type == "integer" or data_type == "integer[]":
            return [ "int", (True if data_type.endswith("[]") else False), None, None ]
        lookup_type = None
        for k in self.types.keys():
            if self.types[ k ][ 'typedef' ] == data_type.replace("[]", ""):
                lookup_type = self.types[ k ]
                break
        if lookup_type != None:
            if 'type' in lookup_type:
                # The base type may be a simple type, in this case is may contain "optional", we do this split on every item:
                resp = self.map_data_type( lookup_type['type'][0].split(",")[0] )[0]
                return [ resp, data_type.endswith("[]"), None, data_type.replace('[]', '') ]
        singular_type_name = data_type.replace("[]", "")
        type_class_name = self.as_class_name( singular_type_name )
        return [ type_class_name,
                 (True if data_type.endswith("[]") else False),
                 "from netapp.{}.{} import {}".format( self.as_file_name( self.class_to_category[ type_class_name ] ),
                                                       self.as_file_name( singular_type_name ),
                                                       type_class_name ), None ]

    def map_types_to_categories(self):
        for k in self.types.keys():
            self.class_to_category[ self.as_class_name( self.types[ k ][ 'typedef' ] ) ] = self.types[ k ][ 'category' ]

    def generate(self):
        self.map_types_to_categories()
        for name in self.categories.keys():
            self.generate_category( self.categories[name] )
    
    def generate_category(self, category):
        self.ensure_directory( self.as_file_name( category['category'] ) )
        category_types = []
        for k in self.types:
            if self.types[ k ]['category'] == category['category']:
                category_types.append( self.types[ k ] )
        for t in category_types:
            self.generate_types( "{}/{}/{}.py".format( self.base_output_dir, self.as_file_name( category['category'] ), self.as_file_name(t['typedef']) ), t )
            self.generate_methods( "{}/{}/__init__.py".format( self.base_output_dir, self.as_file_name( category['category'] ) ), category )

    def generate_types(self, path, t):
        types = {}
        describe_properties_lines = []
        import_lines = []

        for key in t['element']:
            types[ key ] = t['element'][ key ]['type'][0]
            arg_required = "required"
            # There are types where the same property name exists a number of times.
            # These will give us duplicated entries in the type key.
            # We remove them below:
            if isinstance(types[key], list):
                types[key] = self.get_unique( types[ key ] )[0]
            types[ key ] = [ x.strip() for x in types[ key ].split(",") ]
            if len(types[ key ]) > 1:
                arg_required = types[ key ][ 1 ]
            
            arg_type, arg_is_list, requires_import, super_type = self.map_data_type( types[ key ][0] )

            if requires_import != None:
                import_lines.append( requires_import )
            describe_properties_lines.append("            '{}': {{ 'class': {}, 'is_list': {}, 'required': '{}' }},".format( key.replace("-", "_"), arg_type, arg_is_list, arg_required ) )

        lines = []
        for line in import_lines:
            if not line in lines:
                lines.append( line )
        
        top_type_base, _1, _2, _3 = self.map_data_type( t['typedef'] )
        is_netapp_type = True
        
        if top_type_base == self.as_class_name( t['typedef'] ):
            lines.append("from netapp.netapp_object import NetAppObject")
            lines.append("")
            lines.append("class {}(NetAppObject):".format( self.as_class_name( t['typedef'] ) ))
        else:
            is_netapp_type = False
            lines.append("class {}({}):".format( self.as_class_name( t['typedef'] ), top_type_base ))

        if 'desc' in t:
            lines.append("    \"\"\"")
            for desc in t['desc']:
                for line in desc.split("\n"):
                    if line.strip() != "":
                        lines.append("    {}".format( line ))
            lines.append("    \"\"\"")
        
        if is_netapp_type == True:

            for key in t['element']:
                lines.append("    ")
                lines.append("    _{} = None".format( key.replace("-", "_") ))
                lines.append("    @property")
                lines.append("    def {}(self):".format( key.replace("-", "_") ))
                if 'desc' in t['element'][ key ]:
                    lines.append("        \"\"\"")
                    for desc in t['element'][ key ]["desc"]:
                        for line in desc.split("\n"):
                            if line.strip() != "":
                                lines.append("        {}".format( line ))
                    lines.append("        \"\"\"")
                lines.append("        return self._{}".format( key.replace("-", "_") ))
                lines.append("    @{}.setter".format( key.replace("-", "_") ))
                lines.append("    def {}(self, val):".format( key.replace("-", "_") ))
                lines.append("        if val != None:")
                lines.append("            self.validate('{}', val)".format( key.replace("-", "_") ))
                lines.append("        self._{} = val".format( key.replace("-", "_") ))

            lines.append("    ")

        
            lines.append("    @staticmethod" )
            lines.append("    def get_api_name():" )
            lines.append("          return \"{}\"".format( t['typedef'] ) )

            lines.append("    ")
            lines.append("    @staticmethod" )
            lines.append("    def get_desired_attrs():" )
            lines.append("        return [" )
            for key in t['element']:
                lines.append("            '{}',".format(key))
            lines.append("        ]" )

        else:
            lines.append("    " )
            lines.append("    @staticmethod" )
            lines.append("    def get_api_name():" )
            lines.append("          return \"{}\"".format( t['typedef'] ) )
            lines.append("    " )

        with open(path, 'w') as the_file:
            for line in lines:
                the_file.write( "{}\n".format( line ) )

        if len( describe_properties_lines ) > 0:
            lines.append("    ")
            lines.append("    def describe_properties(self):" )
            lines.append("        return {" )
            for line in describe_properties_lines:
                lines.append( line )
            lines.append("        }" )
        with open(path, 'w') as the_file:
            for line in lines:
                the_file.write( "{}\n".format( line ) )

    def generate_methods(self, path, category):
        types_init = []
        with open(path, 'w') as the_file:
            the_file.write("from netapp.connection import NaConnection\n")

            for k in self.types:
                if self.types[ k ][ 'category' ] == category['category']:
                    the_file.write( "from {} import {} # {} properties\n".format( self.as_file_name( self.types[k]['typedef'] ),
                                                                                  self.as_class_name( self.types[k]['typedef'] ),
                                                                                  len(self.types[k]['element']) ) )
            the_file.write("\n")
            the_file.write("class {}Connection(NaConnection):\n".format( self.as_class_name( category['category'] ) ))

            category_methods = []
            for k in self.methods:
                if self.methods[k]['category'] == category['category']:
                    category_methods.append( self.methods[k] )

            for m in category_methods:

                the_file.write("    \n")

                _kwargs = []
                _input_descriptions = []

                if 'input' in m:
                    for key in m['input']:

                        working_type = m['input'][ key ]['type']
                        if isinstance(working_type, list):
                            working_type = m['input'][ key ]['type'][-1]

                        if 'optional' not in working_type:
                            _kwargs.append("{}".format( self.as_file_name( key ) ))

                            if 'desc' in m['input'][ key ]:
                                input_desc_lines = []
                                for line in m['input'][ key ]['desc']:
                                    if line.strip() != "":
                                        input_desc_lines.append( line.strip() )
                                _input_descriptions.append( { 'param': self.as_file_name( key ), 'doc': input_desc_lines } )

                    for key in m['input']:

                        working_type = m['input'][ key ]['type']
                        if isinstance(working_type, list):
                            working_type = m['input'][ key ]['type'][-1]

                        if 'optional' in working_type:
                            _kwargs.append("{}=None".format( self.as_file_name( key ) ))

                            if 'desc' in m['input'][ key ]:
                                input_desc_lines = []
                                for line in m['input'][ key ]['desc']:
                                    if line.strip() != "":
                                        input_desc_lines.append( line.strip() )
                                _input_descriptions.append( { 'param': self.as_file_name( key ), 'doc': input_desc_lines } )

                if len(_kwargs) > 0:
                    the_file.write("    def {}(self, {}):\n".format( self.as_method_name( m['api'] ), ", ".join( _kwargs ) ))
                else:
                    the_file.write("    def {}(self):\n".format( self.as_method_name( m['api'] ) ))

                if 'desc' in m:
                    the_file.write("        \"\"\"\n")
                    for desc in m['desc']:
                        for line in desc.split("\n"):
                            if line.strip() != "":
                                the_file.write("        {}\n".format( line ))
                    for input_doc in _input_descriptions:
                        the_file.write("        \n")
                        if len(input_doc['doc']) > 0:
                            the_file.write("        :param {}: {}\n".format( input_doc['param'], input_doc['doc'][0] ))
                            if len(input_doc['doc']) > 1:
                                for idx, line in enumerate(input_doc['doc']):
                                    if idx > 0:
                                        the_file.write("                {}\n".format( line ))
                        else:
                            the_file.write("        :param {}: not documented\n")
                    the_file.write("        \"\"\"\n")

                the_file.write("        return self.request( \"{}\", {{\n".format( m['api'] ))
                if 'input' in m:
                    for key in m['input']:
                        if key in ["max-records", "tag"]:
                            the_file.write("            '{}': {},\n".format( self.as_file_name( key ), self.as_file_name( key ) ))
                        else:
                            m['input'][ key ]['type'] = m['input'][ key ]['type']
                            if isinstance(m['input'][ key ]['type'], list):
                                m['input'][ key ]['type'] = m['input'][ key ]['type'][-1]
                            type_data = m['input'][ key ]['type'].split(',')
                            type_data = [ x.strip() for x in type_data ]
                            type_name, is_list, import_line, super_type = self.map_data_type( type_data[0] )
                            the_file.write("            '{}': [ {}, '{}', [ {}, '{}' ], {} ],\n".format( self.as_file_name( key ), self.as_file_name( key ), key, type_name, super_type, is_list ))
                the_file.write("        }, {\n" )

                if 'output' in m:
                    for key in m['output']:
                        if key not in ["next-tag", "num-records"]:
                            m['output'][ key ]['type'] = m['output'][ key ]['type']
                            if isinstance(m['output'][ key ]['type'], list):
                                m['output'][ key ]['type'] = m['output'][ key ]['type'][-1]
                            type_data = m['output'][ key ]['type'].split(",")
                            type_data = [ x.strip() for x in type_data ]
                            try:
                                type_name, is_list, import_line, super_type = self.map_data_type( type_data[0] )
                            except Exception as ex:
                                print 
                                print " !!!! OUTPUT: {} {} {}".format( m['api'], key, m['output'][ key ]['type'] )
                            the_file.write("            '{}': [ {}, {} ],\n".format( key, type_name, is_list ))
                the_file.write("        } )\n" )




