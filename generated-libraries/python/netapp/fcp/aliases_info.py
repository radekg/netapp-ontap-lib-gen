from netapp.netapp_object import NetAppObject

class AliasesInfo(NetAppObject):
    """
    A list of WWPNs and their aliases generated according
    to the input - alias, WWPN or nothing.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing the alias
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _aliases_wwpn = None
    @property
    def aliases_wwpn(self):
        """
        The FCP WWPN for which the alias is given
        """
        return self._aliases_wwpn
    @aliases_wwpn.setter
    def aliases_wwpn(self, val):
        if val != None:
            self.validate('aliases_wwpn', val)
        self._aliases_wwpn = val
    
    _aliases_alias = None
    @property
    def aliases_alias(self):
        """
        The 32-character alias for a given FCP WWPN
        """
        return self._aliases_alias
    @aliases_alias.setter
    def aliases_alias(self, val):
        if val != None:
            self.validate('aliases_alias', val)
        self._aliases_alias = val
    
    @staticmethod
    def get_api_name():
          return "aliases-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'aliases-wwpn',
            'aliases-alias',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aliases_wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'aliases_alias': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
