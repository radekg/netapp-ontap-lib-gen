from netapp.netapp_object import NetAppObject

class VserverSslInfo(NetAppObject):
    """
    Information about SSL authentication for a Vserver
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _certificate_authority = None
    @property
    def certificate_authority(self):
        """
        Issuing Certificate Authority (CA) of server certificate.
        This field is required when you specify server-enabled as
        true.
        Attributes: non-creatable, modifiable
        """
        return self._certificate_authority
    @certificate_authority.setter
    def certificate_authority(self, val):
        if val != None:
            self.validate('certificate_authority', val)
        self._certificate_authority = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _certificate_serial_number = None
    @property
    def certificate_serial_number(self):
        """
        Serial number of certificate in hexadecimal format. This
        field is required when you specify server-enabled as
        true.
        Attributes: non-creatable, modifiable
        """
        return self._certificate_serial_number
    @certificate_serial_number.setter
    def certificate_serial_number(self, val):
        if val != None:
            self.validate('certificate_serial_number', val)
        self._certificate_serial_number = val
    
    _server_authentication_enabled = None
    @property
    def server_authentication_enabled(self):
        """
        Informs if SSL Server Authentication is enabled.
        Attributes: non-creatable, modifiable
        """
        return self._server_authentication_enabled
    @server_authentication_enabled.setter
    def server_authentication_enabled(self, val):
        if val != None:
            self.validate('server_authentication_enabled', val)
        self._server_authentication_enabled = val
    
    _common_name = None
    @property
    def common_name(self):
        """
        Represents the domain name in FQDN form that specifies
        its exact location in the tree hierarchy of the Domain
        Name System (DNS). This field is optional when you
        specify server-enabled as true.
        Attributes: non-creatable, modifiable
        """
        return self._common_name
    @common_name.setter
    def common_name(self, val):
        if val != None:
            self.validate('common_name', val)
        self._common_name = val
    
    _client_authentication_enabled = None
    @property
    def client_authentication_enabled(self):
        """
        Informs if SSL Client Authentication is enabled.
        Attributes: non-creatable, modifiable
        """
        return self._client_authentication_enabled
    @client_authentication_enabled.setter
    def client_authentication_enabled(self, val):
        if val != None:
            self.validate('client_authentication_enabled', val)
        self._client_authentication_enabled = val
    
    @staticmethod
    def get_api_name():
          return "vserver-ssl-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'certificate-authority',
            'vserver',
            'certificate-serial-number',
            'server-authentication-enabled',
            'common-name',
            'client-authentication-enabled',
        ]
    
    def describe_properties(self):
        return {
            'certificate_authority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'certificate_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_authentication_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'common_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'client_authentication_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
