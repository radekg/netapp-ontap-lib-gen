from netapp.cifs.address_info import AddressInfo
from netapp.netapp_object import NetAppObject

class ConnectionInfo(NetAppObject):
    """
    Structure containing information on the connection.
    """
    
    _preferred_address = None
    @property
    def preferred_address(self):
        """
        An address list of preferred servers.
        """
        return self._preferred_address
    @preferred_address.setter
    def preferred_address(self, val):
        if val != None:
            self.validate('preferred_address', val)
        self._preferred_address = val
    
    _connected_address = None
    @property
    def connected_address(self):
        """
        An address list of currently connected servers.
        """
        return self._connected_address
    @connected_address.setter
    def connected_address(self, val):
        if val != None:
            self.validate('connected_address', val)
        self._connected_address = val
    
    _other_address = None
    @property
    def other_address(self):
        """
        An address list of other servers.
        """
        return self._other_address
    @other_address.setter
    def other_address(self, val):
        if val != None:
            self.validate('other_address', val)
        self._other_address = val
    
    _favored_address = None
    @property
    def favored_address(self):
        """
        An address list of favored servers.
        """
        return self._favored_address
    @favored_address.setter
    def favored_address(self, val):
        if val != None:
            self.validate('favored_address', val)
        self._favored_address = val
    
    @staticmethod
    def get_api_name():
          return "connection-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'preferred-address',
            'connected-address',
            'other-address',
            'favored-address',
        ]
    
    def describe_properties(self):
        return {
            'preferred_address': { 'class': AddressInfo, 'is_list': True, 'required': 'optional' },
            'connected_address': { 'class': AddressInfo, 'is_list': True, 'required': 'optional' },
            'other_address': { 'class': AddressInfo, 'is_list': True, 'required': 'optional' },
            'favored_address': { 'class': AddressInfo, 'is_list': True, 'required': 'optional' },
        }
