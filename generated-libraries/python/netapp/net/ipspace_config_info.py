from netapp.netapp_object import NetAppObject

class IpspaceConfigInfo(NetAppObject):
    """
    An IPSpace.
    """
    
    _ipspace_name = None
    @property
    def ipspace_name(self):
        """
        IPSpace name.
        """
        return self._ipspace_name
    @ipspace_name.setter
    def ipspace_name(self, val):
        if val != None:
            self.validate('ipspace_name', val)
        self._ipspace_name = val
    
    _interface_list = None
    @property
    def interface_list(self):
        """
        List of interface names in the ipspace.
        An ipspace with no members is possible.
        """
        return self._interface_list
    @interface_list.setter
    def interface_list(self, val):
        if val != None:
            self.validate('interface_list', val)
        self._interface_list = val
    
    @staticmethod
    def get_api_name():
          return "ipspace-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ipspace-name',
            'interface-list',
        ]
    
    def describe_properties(self):
        return {
            'ipspace_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'interface_list': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
