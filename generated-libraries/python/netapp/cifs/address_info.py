from netapp.netapp_object import NetAppObject

class AddressInfo(NetAppObject):
    """
    Structure containing address information
    of servers.
    """
    
    _is_broken = None
    @property
    def is_broken(self):
        """
        If true, the address is not responding.
        """
        return self._is_broken
    @is_broken.setter
    def is_broken(self, val):
        if val != None:
            self.validate('is_broken', val)
        self._is_broken = val
    
    _is_multihomed = None
    @property
    def is_multihomed(self):
        """
        If true, the address is a multi-homed server.
        """
        return self._is_multihomed
    @is_multihomed.setter
    def is_multihomed(self, val):
        if val != None:
            self.validate('is_multihomed', val)
        self._is_multihomed = val
    
    _has_nossl = None
    @property
    def has_nossl(self):
        """
        If true, the protocol SSL is not supported.
        """
        return self._has_nossl
    @has_nossl.setter
    def has_nossl(self, val):
        if val != None:
            self.validate('has_nossl', val)
        self._has_nossl = val
    
    _hostname = None
    @property
    def hostname(self):
        """
        The resolved hostname of the IP address.
        """
        return self._hostname
    @hostname.setter
    def hostname(self, val):
        if val != None:
            self.validate('hostname', val)
        self._hostname = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        The IP address in canonical form.
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _is_primary = None
    @property
    def is_primary(self):
        """
        If true, the address is a primary server.
        """
        return self._is_primary
    @is_primary.setter
    def is_primary(self, val):
        if val != None:
            self.validate('is_primary', val)
        self._is_primary = val
    
    @staticmethod
    def get_api_name():
          return "address-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-broken',
            'is-multihomed',
            'has-nossl',
            'hostname',
            'ip-address',
            'is-primary',
        ]
    
    def describe_properties(self):
        return {
            'is_broken': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_multihomed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'has_nossl': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'hostname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_primary': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
