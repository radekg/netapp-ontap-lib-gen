from netapp.netapp_object import NetAppObject

class IscsiPortalAddressInfo(NetAppObject):
    """
    Configuration information about an inet-addres
    and port pair for a portal group.
    """
    
    _inet_address = None
    @property
    def inet_address(self):
        """
        inet-address.
        """
        return self._inet_address
    @inet_address.setter
    def inet_address(self, val):
        if val != None:
            self.validate('inet_address', val)
        self._inet_address = val
    
    _id = None
    @property
    def id(self):
        """
        ID of this portal group.
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _port = None
    @property
    def port(self):
        """
        The port that is being
        listened on for that address.
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-portal-address-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'inet-address',
            'id',
            'port',
        ]
    
    def describe_properties(self):
        return {
            'inet_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'id': { 'class': int, 'is_list': False, 'required': 'required' },
            'port': { 'class': int, 'is_list': False, 'required': 'required' },
        }
