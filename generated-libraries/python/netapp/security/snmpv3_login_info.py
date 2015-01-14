from netapp.netapp_object import NetAppObject

class Snmpv3LoginInfo(NetAppObject):
    """
    SNMPv3 user login information for 'usm' authentication method
    """
    
    _engine_id = None
    @property
    def engine_id(self):
        """
        Authoritative entity's EngineID for the SNMPv3 user.
        This is required for creating SNMPv3 users (users for
        SNMPv3 INFORMs) with 'usm' authentication method only.
        This should be specified as a hexadecimal string.
        Engine ID with first bit set to 1 in first octet should
        have a minimum of 5 or maximum of 32 octets.
        Engine Id with first bit set to 0 in the first octet
        should be 12 octets in length.
        Engine Id cannot have all zeros in its address
        For e.g. 8000014603000000000000.
        Attributes: optional-for-create, non-modifiable
        """
        return self._engine_id
    @engine_id.setter
    def engine_id(self, val):
        if val != None:
            self.validate('engine_id', val)
        self._engine_id = val
    
    _authentication_protocol = None
    @property
    def authentication_protocol(self):
        """
        Authentication protocol for the snmp user.
        Possible values: 'none', 'md5', 'sha'. The default value
        is 'none'
        Attributes: optional-for-create, non-modifiable
        """
        return self._authentication_protocol
    @authentication_protocol.setter
    def authentication_protocol(self, val):
        if val != None:
            self.validate('authentication_protocol', val)
        self._authentication_protocol = val
    
    _privacy_password = None
    @property
    def privacy_password(self):
        """
        Password for the privacy protocol.
        This should be minimum 8 characters long. This is
        required for 'des' privacy protocol and not required for
        'none'.
        Attributes: optional-for-create, non-modifiable
        """
        return self._privacy_password
    @privacy_password.setter
    def privacy_password(self, val):
        if val != None:
            self.validate('privacy_password', val)
        self._privacy_password = val
    
    _privacy_protocol = None
    @property
    def privacy_protocol(self):
        """
        Privacy protocol for the snmp user.
        Possible values: 'none', 'des'. The default value is
        'none'.
        Attributes: optional-for-create, non-modifiable
        """
        return self._privacy_protocol
    @privacy_protocol.setter
    def privacy_protocol(self, val):
        if val != None:
            self.validate('privacy_protocol', val)
        self._privacy_protocol = val
    
    _authentication_password = None
    @property
    def authentication_password(self):
        """
        Password for the authentication protocol.
        This should be minimum 8 characters long. This is
        required for 'md5' and 'sha' authentication protocols and
        not required for 'none'.
        Attributes: optional-for-create, non-modifiable
        """
        return self._authentication_password
    @authentication_password.setter
    def authentication_password(self, val):
        if val != None:
            self.validate('authentication_password', val)
        self._authentication_password = val
    
    @staticmethod
    def get_api_name():
          return "snmpv3-login-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'engine-id',
            'authentication-protocol',
            'privacy-password',
            'privacy-protocol',
            'authentication-password',
        ]
    
    def describe_properties(self):
        return {
            'engine_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'authentication_protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privacy_password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privacy_protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'authentication_password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
