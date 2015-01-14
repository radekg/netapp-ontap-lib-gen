from netapp.netapp_object import NetAppObject

class ExtensionListInfo(NetAppObject):
    """
    Structure containing extension information.
    """
    
    _name_spec = None
    @property
    def name_spec(self):
        """
        Extension specification (including wild cards).
        Allowed are only DOS like, three character long
        extensions. The extensions are case insensitive.
        Supported wild card values: "???" to match any
        extension and "?" to match any character.
        Examples of allowed extension specifications:
        EXE
        ???
        ?XT
        P??
        """
        return self._name_spec
    @name_spec.setter
    def name_spec(self, val):
        if val != None:
            self.validate('name_spec', val)
        self._name_spec = val
    
    @staticmethod
    def get_api_name():
          return "extension-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name-spec',
        ]
    
    def describe_properties(self):
        return {
            'name_spec': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
