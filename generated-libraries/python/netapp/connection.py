from core_netapp.NaServer import NaServer
from core_netapp.NaElement import NaElement
from netapp_object import NetAppObject

class NaErrorResponse():
    def __init__(self, method, arguments, errno, reason):
        self.method = method
        self.arguments = arguments
        self.error_code = errno
        self.reason = reason

    def __repr__(self):
        return "{}(error_code={}, reason={}, method={}, arguments=<collapsed>)".format( self.__class__.__name__,
                                                                                        self.error_code,
                                                                                        self.reason,
                                                                                        self.method )

class NaResponse():

    @staticmethod
    def item_from_na_element( na_element, output_class, is_list, key ):
        if issubclass( output_class, NetAppObject ):
            if is_list:
                resp = []
                response_node = na_element.child_get( key )
                if response_node != None:
                    for c in response_node.children_get():
                        resp.append( output_class().from_na_element( c ) )
                return resp
            else:
                return output_class().from_na_element( na_element.child_get( key ).children_get()[0] )
        else:
            if is_list:
                resp = []
                for c in na_element.child_get( key ).children_get():
                    if output_class == int:
                        resp.append( na_element.child_get_int( key ) )
                    elif output_class == bool:
                        resp.append( na_element.child_get_string( key ) == "true" )
                    else:
                        resp.append( na_element.child_get_string( key ) )
                return resp
            else:
                if output_class == int:
                    return na_element.child_get_int( key )
                return na_element.child_get_string( key )

    @staticmethod
    def from_na_result( response, output ):
        if len( output.keys() ) == 1:
            key = output.keys()[0]
            output_class, is_list = output[ key ]
            return NaResponse.item_from_na_element( response, output_class, is_list, key )
        else:
            resp = {}
            for key in output.keys():
                output_class, is_list, _ = output[ key ]
                resp[ key ] = NaResponse.item_from_na_element( response.child_get( key ), output_class, is_list, key )
            return resp

class NaPagedResponse(NaResponse):
    def __init__(self, conn, method, arguments, returns, result):
        self.method = method
        self.arguments = arguments
        self.returns = returns
        self.result = result
        self.set_output( result )
        self.conn = conn
        self._has_more = True

    def set_output(self, value):
        if not isinstance( value, NaElement ):
            raise TypeError("Result must be of type NaElement. {} given.".format( value.__class__.__name__ ))
        self.output = NaResponse.from_na_result( value, self.returns )

    def has_more(self):
        return self._has_more

    def next(self, max_records=None):
        self.arguments['tag'] = self.result.child_get_string("next-tag")
        if max_records != None:
            self.arguments['max_records'] = max_records
        intermediate = self.conn.request( self.method, self.arguments, self.returns )
        if isinstance(intermediate, NaPagedResponse):
            self._has_more = True
            self.result = intermediate.result
            self.set_output( self.result )
        else:
            self._has_more = False
            self.result = intermediate
            self.output = intermediate
        return self

class NaConnection():

    def __init__(self,
                 host, username, password,
                 vserver="",
                 major_version=1,
                 minor_version=21,
                 server_type="Filer",
                 transport_type="HTTP"):

        self.server = NaServer( host, major_version, minor_version )
        self.server.set_server_type( server_type )
        self.server.set_admin_user( username , password )
        self.server.set_transport_type( transport_type )
        self.server.set_vserver( vserver )

    def request(self, method, arguments, output):
        
        api = NaElement( method )

        for key in arguments:
            if key not in ["desired_attributes", "max_records", "tag"]:
                value, api_type, type_info, is_list = arguments[ key ]
                arg_type_class, super_type_api_tag = type_info
                if value != None:
                    if not is_list:
                        if not isinstance(value, arg_type_class):
                            raise TypeError("{} value must be of type {}. {} given.".format( key, arg_type_class.__name__, arguments[key].__class__.__name__ ))
                        if isinstance(value, NetAppObject):
                            t = NaElement( api_type )
                            api.child_add( t )
                            t.child_add( value.as_na_element() )
                        else:
                            api.child_add_string( api_type, value )
                    else:
                        if not isinstance(value, list):
                            raise TypeError("{} value must be a list. {} given.".format( key, arguments[key].__class__.__name__ ))
                        else:
                            for item in value:
                                t = NaElement( api_type )
                                api.child_add( t )
                                if isinstance(item, NetAppObject):
                                    t2 = NaElement( super_type_api_tag )
                                    t.child_add( t2 )
                                    t2.child_add( item.as_na_element() )
                                else:
                                    t.child_add_string( super_type_api_tag, item )
        
        if 'desired_attributes' in arguments:

            values, api_type, type_info, is_list = arguments[ 'desired_attributes' ]
            class_da, super_type_api_tag_name = type_info

            validate_da = True
            if values == None:
                validate_da = False
                values = class_da.get_desired_attrs()
            
            xi = NaElement( api_type )
            api.child_add( xi )
            xi1 = NaElement( class_da.get_api_name() )
            xi.child_add(xi1)
            for attr in values:
                if validate_da:
                    class_da.is_desired_attr( attr )
                xi1.child_add_string(attr,"<{}>".format( attr ))

        if 'max_records' in arguments:
            if arguments['max_records'] != None:
                if isinstance(arguments['max_records'], int):
                    api.child_add_string("max-records", arguments['max_records'] )
                else:
                    raise TypeError("max_records value must be an int. {} given.".format( arguments['max_records'].__class__.__name__ ))

        if 'tag' in arguments:
            if arguments['tag'] != None:
                if isinstance(arguments['tag'], list) or isinstance(arguments['tag'], unicode):
                    api.child_add_string("tag", arguments['tag'] )
                else:
                    raise TypeError("tag value must be a list or unicode. {} given.".format( arguments['tag'].__class__.__name__ ))

        if len(output.keys()) > 0:
            result = self.server.invoke_elem( api )
            
            # Handle error respnse:
            if result.results_status() == "failed":
                return NaErrorResponse( method, arguments, result.results_errno(), result.results_reason() )
            
            # check if there's a next-tag element in the response,
            # if so, return paged resultset:
            next_tag = result.child_get_string("next-tag")
            if len( result.children_get() ) > 0:
                if next_tag != None:
                    return NaPagedResponse( self, method, arguments, output, result )
                return NaResponse.from_na_result( result, output )
        else:
            self.server.invoke_elem( api )