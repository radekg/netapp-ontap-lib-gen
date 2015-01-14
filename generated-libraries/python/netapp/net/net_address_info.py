from netapp.netapp_object import NetAppObject

class NetAddressInfo(NetAppObject):
    """
    Holds host address information.
    """
    
    _address_info_flags = None
    @property
    def address_info_flags(self):
        """
        Specifies how returned sockaddr should be treated
        and how 'hostname' be treated.
        """
        return self._address_info_flags
    @address_info_flags.setter
    def address_info_flags(self, val):
        if val != None:
            self.validate('address_info_flags', val)
        self._address_info_flags = val
    
    _address_info_socket_type = None
    @property
    def address_info_socket_type(self):
        """
        Denotes the type of socket for which address will be
        used. For example:stream socket/datagram socket.
        """
        return self._address_info_socket_type
    @address_info_socket_type.setter
    def address_info_socket_type(self, val):
        if val != None:
            self.validate('address_info_socket_type', val)
        self._address_info_socket_type = val
    
    _address_info_family = None
    @property
    def address_info_family(self):
        """
        Denotes protocol family of the address.
        """
        return self._address_info_family
    @address_info_family.setter
    def address_info_family(self, val):
        if val != None:
            self.validate('address_info_family', val)
        self._address_info_family = val
    
    _canonical_name = None
    @property
    def canonical_name(self):
        """
        Canonical name for hostname.
        """
        return self._canonical_name
    @canonical_name.setter
    def canonical_name(self, val):
        if val != None:
            self.validate('canonical_name', val)
        self._canonical_name = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        Resolved IP address string.  May be IPv4 or IPv6.
        For example, 198.18.100.12 or
        fd20:8b1e:b255:104:230:48ff:fe8c:6326.  No hostname
        resolution.
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _address_info_transport_protocol = None
    @property
    def address_info_transport_protocol(self):
        """
        Denotes the type of transport protocol for which
        address will be used.
        """
        return self._address_info_transport_protocol
    @address_info_transport_protocol.setter
    def address_info_transport_protocol(self, val):
        if val != None:
            self.validate('address_info_transport_protocol', val)
        self._address_info_transport_protocol = val
    
    @staticmethod
    def get_api_name():
          return "net-address-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'address-info-flags',
            'address-info-socket-type',
            'address-info-family',
            'canonical-name',
            'ip-address',
            'address-info-transport-protocol',
        ]
    
    def describe_properties(self):
        return {
            'address_info_flags': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'address_info_socket_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address_info_family': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'canonical_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'address_info_transport_protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
