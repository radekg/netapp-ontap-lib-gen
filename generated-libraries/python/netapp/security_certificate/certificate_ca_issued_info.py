from netapp.netapp_object import NetAppObject

class CertificateCaIssuedInfo(NetAppObject):
    """
    Information about issued digital certificates
    by Self-Signed Root CA
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
        Attributes: key, non-creatable, non-modifiable
        """
        return self._certificate_authority
    @certificate_authority.setter
    def certificate_authority(self, val):
        if val != None:
            self.validate('certificate_authority', val)
        self._certificate_authority = val
    
    _status = None
    @property
    def status(self):
        """
        Status of certificate.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "active"    ,
        <li> "revoked"
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _expiration_date = None
    @property
    def expiration_date(self):
        """
        Certificate expiration date.
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_date
    @expiration_date.setter
    def expiration_date(self, val):
        if val != None:
            self.validate('expiration_date', val)
        self._expiration_date = val
    
    _locality = None
    @property
    def locality(self):
        """
        Name of the locality.
        Attributes: non-creatable, non-modifiable
        """
        return self._locality
    @locality.setter
    def locality(self, val):
        if val != None:
            self.validate('locality', val)
        self._locality = val
    
    _country = None
    @property
    def country(self):
        """
        Name of the country.
        Attributes: non-creatable, non-modifiable
        """
        return self._country
    @country.setter
    def country(self, val):
        if val != None:
            self.validate('country', val)
        self._country = val
    
    _revocation_date = None
    @property
    def revocation_date(self):
        """
        Certificate revocation date.
        Attributes: non-creatable, non-modifiable
        """
        return self._revocation_date
    @revocation_date.setter
    def revocation_date(self, val):
        if val != None:
            self.validate('revocation_date', val)
        self._revocation_date = val
    
    _email_addr = None
    @property
    def email_addr(self):
        """
        Email address of administrator.
        Attributes: non-creatable, non-modifiable
        """
        return self._email_addr
    @email_addr.setter
    def email_addr(self, val):
        if val != None:
            self.validate('email_addr', val)
        self._email_addr = val
    
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
        Name of the unit. Example: IT, Finance.
        Attributes: non-creatable, non-modifiable
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
        Name of the state.
        Attributes: non-creatable, non-modifiable
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
        Attributes: key, non-creatable, non-modifiable
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
        Attributes: non-creatable, non-modifiable
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
        Name of the organization.
        Attributes: non-creatable, non-modifiable
        """
        return self._organization
    @organization.setter
    def organization(self, val):
        if val != None:
            self.validate('organization', val)
        self._organization = val
    
    _ca_serial_number = None
    @property
    def ca_serial_number(self):
        """
        Serial number of CA certificate.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._ca_serial_number
    @ca_serial_number.setter
    def ca_serial_number(self, val):
        if val != None:
            self.validate('ca_serial_number', val)
        self._ca_serial_number = val
    
    @staticmethod
    def get_api_name():
          return "certificate-ca-issued-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'certificate-authority',
            'status',
            'expiration-date',
            'locality',
            'country',
            'revocation-date',
            'email-addr',
            'vserver',
            'organization-unit',
            'state',
            'serial-number',
            'common-name',
            'organization',
            'ca-serial-number',
        ]
    
    def describe_properties(self):
        return {
            'certificate_authority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'locality': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'country': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'revocation_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'email_addr': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organization_unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'common_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organization': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ca_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
