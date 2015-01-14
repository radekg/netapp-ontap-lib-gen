from netapp.netapp_object import NetAppObject

class PortnameAliasName(NetAppObject):
    """
    Aliases for this WWPN
    """
    
    _portname_alias = None
    @property
    def portname_alias(self):
        """
        Alias for the WWPN
        """
        return self._portname_alias
    @portname_alias.setter
    def portname_alias(self, val):
        if val != None:
            self.validate('portname_alias', val)
        self._portname_alias = val
    
    @staticmethod
    def get_api_name():
          return "portname-alias-name"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'portname-alias',
        ]
    
    def describe_properties(self):
        return {
            'portname_alias': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
