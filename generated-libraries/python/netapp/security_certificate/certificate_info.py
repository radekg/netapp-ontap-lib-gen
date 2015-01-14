from netapp.netapp_object import NetAppObject

class CertificateInfo(NetAppObject):
    """
    Information about a Digital Certificate
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
        Certificate Authority
        Attributes: key, required-for-create, non-modifiable
        """
        return self._certificate_authority
    @certificate_authority.setter
    def certificate_authority(self, val):
        if val != None:
            self.validate('certificate_authority', val)
        self._certificate_authority = val
    
    _hash_function = None
    @property
    def hash_function(self):
        """
        Hashing function used to sign the certificate. Default
        value is 'sha256'.
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "sha1"      ,
        <li> "sha256"    ,
        <li> "md5"
        </ul>
        """
        return self._hash_function
    @hash_function.setter
    def hash_function(self, val):
        if val != None:
            self.validate('hash_function', val)
        self._hash_function = val
    
    _email_address = None
    @property
    def email_address(self):
        """
        Email address of administrator. Default value is empty
        string.
        Attributes: required-for-create, non-modifiable
        """
        return self._email_address
    @email_address.setter
    def email_address(self, val):
        if val != None:
            self.validate('email_address', val)
        self._email_address = val
    
    _expiration_date = None
    @property
    def expiration_date(self):
        """
        Certificate Expiration Date
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_date
    @expiration_date.setter
    def expiration_date(self, val):
        if val != None:
            self.validate('expiration_date', val)
        self._expiration_date = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        Protocol
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ssl"
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _start_date = None
    @property
    def start_date(self):
        """
        Certificate Start Date
        Attributes: non-creatable, non-modifiable
        """
        return self._start_date
    @start_date.setter
    def start_date(self, val):
        if val != None:
            self.validate('start_date', val)
        self._start_date = val
    
    _country = None
    @property
    def country(self):
        """
        Name of the country. Default value is 'US'.
        Attributes: required-for-create, non-modifiable
        """
        return self._country
    @country.setter
    def country(self, val):
        if val != None:
            self.validate('country', val)
        self._country = val
    
    _locality = None
    @property
    def locality(self):
        """
        Name of the locality Default value is empty string.
        Attributes: required-for-create, non-modifiable
        """
        return self._locality
    @locality.setter
    def locality(self, val):
        if val != None:
            self.validate('locality', val)
        self._locality = val
    
    _expire_days = None
    @property
    def expire_days(self):
        """
        Number of days until expiration. Default value is '365'.
        Attributes: required-for-create, non-modifiable
        """
        return self._expire_days
    @expire_days.setter
    def expire_days(self, val):
        if val != None:
            self.validate('expire_days', val)
        self._expire_days = val
    
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
    
    _organization_unit = None
    @property
    def organization_unit(self):
        """
        Name of the unit. Example: IT, Finance. Default value is
        empty string.
        Attributes: required-for-create, non-modifiable
        """
        return self._organization_unit
    @organization_unit.setter
    def organization_unit(self, val):
        if val != None:
            self.validate('organization_unit', val)
        self._organization_unit = val
    
    _state = None
    @property
    def state(self):
        """
        Name of the state. Default value is empty string.
        Attributes: required-for-create, non-modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number of certificate.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _common_name = None
    @property
    def common_name(self):
        """
        Represents the domain name in FQDN form that specifies
        its exact location in the tree hierarchy of the Domain
        Name System (DNS).
        Attributes: key, required-for-create, non-modifiable
        """
        return self._common_name
    @common_name.setter
    def common_name(self, val):
        if val != None:
            self.validate('common_name', val)
        self._common_name = val
    
    _organization = None
    @property
    def organization(self):
        """
        Name of the organization. Default value is empty string.
        Attributes: required-for-create, non-modifiable
        """
        return self._organization
    @organization.setter
    def organization(self, val):
        if val != None:
            self.validate('organization', val)
        self._organization = val
    
    _public_certificate = None
    @property
    def public_certificate(self):
        """
        Public Key Certificate
        Attributes: non-creatable, non-modifiable
        """
        return self._public_certificate
    @public_certificate.setter
    def public_certificate(self, val):
        if val != None:
            self.validate('public_certificate', val)
        self._public_certificate = val
    
    _type = None
    @property
    def type(self):
        """
        Type of certificate.
        <p>
        Possible values:
        <ul>
        <li> 'server'       - Server certificate,
        <li> 'root_ca'      - Self-Signed Root CA,
        <li> 'client_ca'    - CA who signed user certificates
        on client',
        <li> 'server_ca'    - CA who signed user certificates
        on server',
        <li> 'server_chain' - Intermediate certificate for
        server authentication
        </ul>
        Attributes: key, required-for-create, non-modifiable
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _size = None
    @property
    def size(self):
        """
        Size of requested certificate in bits. Default value is
        '2048'.
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "512"  - 512 bits private key,
        <li> "1024" - 1024 bits private key,
        <li> "1536" - 1536 bits private key,
        <li> "2048" - 2048 bits private key
        </ul>
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    @staticmethod
    def get_api_name():
          return "certificate-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'certificate-authority',
            'hash-function',
            'email-address',
            'expiration-date',
            'protocol',
            'start-date',
            'country',
            'locality',
            'expire-days',
            'vserver',
            'organization-unit',
            'state',
            'serial-number',
            'common-name',
            'organization',
            'public-certificate',
            'type',
            'size',
        ]
    
    def describe_properties(self):
        return {
            'certificate_authority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hash_function': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'email_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'start_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'country': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'locality': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expire_days': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organization_unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'common_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organization': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'public_certificate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
