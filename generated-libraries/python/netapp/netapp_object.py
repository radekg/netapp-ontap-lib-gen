from netapp.core_netapp.NaElement import NaElement

class NetAppObject(object):

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr( self, key, kwargs[key] )
            else:
                raise AttributeError( "{} has no property {}.".format( self.__class__.__name__, key ) )

    def __repr__(self):
        prop_string = ", ".join(["{}={}".format(p[1:], v) for (p, v) in self.__dict__.iteritems() if v != None])
        return "{}({})".format( self.__class__.__name__, prop_string )

    def validate(self, property_name, val):
        _def = self.describe_properties()[ property_name ]
        if _def['is_list'] == True:
            if not isinstance( val, list ):
                raise TypeError( "Value for {} must be a list. {} given.".format( property_name, val.__class__.__name__ ) )
            else:
                for idx, item in enumerate(val):
                    if not isinstance( item, _def['class'] ):
                        raise TypeError( "List of values for {} must containt items of type {}. Found {} at index {}.".format( property_name, _def['class'].__name__, item.__class__.__name__, idx ) )
        else:
            if not isinstance( val, _def['class'] ):
                raise TypeError( "Value for {} must be of type {}. {} given.".format( property_name, _def['class'].__name__, val.__class__.__name__ ) )

    @classmethod
    def is_desired_attr(cls, attr):
        attrs = cls.get_desired_attrs()
        return attr in attrs

    def from_na_element(self, element):
        props = self.describe_properties()
        for p, v in props.iteritems():
            # Only process a property if there's ax XML child node for it:
            if element.child_get( p.replace("_", "-") ) != None:
                if v['class'] == basestring:
                    setattr(self, p, element.child_get_string( p.replace("_", "-") ) )
                elif v['class'] == int:
                    na_value = None
                    try:
                        na_value = element.child_get_int( p.replace("_", "-") )
                    except TypeError: # means there was no result for this field, maybe not in desired_fields?
                        pass
                    setattr(self, p, na_value )
                elif v['class'] == bool:
                    setattr(self, p, element.child_get_string( p.replace("_", "-") ) == "true" )
                else:
                    if v['is_list'] == True:
                        items = []
                        for c in element.child_get( p.replace("_", "-") ).children_get():
                            items.append( v['class']().from_na_element( c ) )
                        setattr(self, p, items )
                    else:
                        setattr(self, p, v['class']().from_na_element( element.child_get( p.replace("_", "-") ) ) )
        return self

    def as_na_element(self):
        element = NaElement( self.__class__.get_api_name() )
        for (p, v) in self.__dict__.iteritems():
            if v != None:
                if isinstance(v, NetAppObject):
                    element.child_add( v.as_na_element() )
                else:
                    element.child_add_string( p[1:].replace("_","-"), v )
        return element
