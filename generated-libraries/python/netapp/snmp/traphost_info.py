from netapp.netapp_object import NetAppObject

class TraphostInfo(NetAppObject):
    """
    Information about a single registered trap host.
    """
    
    _host_name = None
    @property
    def host_name(self):
        """
        Name of the trap host given by the user. Can be one
        of the following: hostname, ip-address, or alias
        Hostname will be a fully qualified Domain Name.
        """
        return self._host_name
    @host_name.setter
    def host_name(self, val):
        if val != None:
            self.validate('host_name', val)
        self._host_name = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        IP address of the trap host.
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    @staticmethod
    def get_api_name():
          return "traphost-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'host-name',
            'ip-address',
        ]
    
    def describe_properties(self):
        return {
            'host_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
