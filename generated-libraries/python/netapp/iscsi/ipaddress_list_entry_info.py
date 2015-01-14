from netapp.netapp_object import NetAppObject

class IpaddressListEntryInfo(NetAppObject):
    """
    Information about a single IP Address
    """
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        IP address
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    @staticmethod
    def get_api_name():
          return "ipaddress-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ip-address',
        ]
    
    def describe_properties(self):
        return {
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
