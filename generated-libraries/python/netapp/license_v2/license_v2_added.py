from netapp.netapp_object import NetAppObject

class LicenseV2Added(NetAppObject):
    """
    A license entry that was successfully added to the
    controller or the cluster.
    """
    
    _license_key = None
    @property
    def license_key(self):
        """
        License Key.
        Attributes: non-creatable, non-modifiable
        """
        return self._license_key
    @license_key.setter
    def license_key(self, val):
        if val != None:
            self.validate('license_key', val)
        self._license_key = val
    
    _package = None
    @property
    def package(self):
        """
        Package Name.
        Attributes: non-creatable, non-modifiable
        """
        return self._package
    @package.setter
    def package(self, val):
        if val != None:
            self.validate('package', val)
        self._package = val
    
    _expiration_time = None
    @property
    def expiration_time(self):
        """
        License expiration time. This value is
        only present in demo licenses. It is set
        to zero for permanent licenses such
        as standard and site licenses.
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_time
    @expiration_time.setter
    def expiration_time(self, val):
        if val != None:
            self.validate('expiration_time', val)
        self._expiration_time = val
    
    _customer_id = None
    @property
    def customer_id(self):
        """
        Customer Identification. This value is
        only present in site licenses. It is set
        to none for standard and demo licenses.
        Attributes: non-creatable, non-modifiable
        """
        return self._customer_id
    @customer_id.setter
    def customer_id(self, val):
        if val != None:
            self.validate('customer_id', val)
        self._customer_id = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial Number. This value is only present
        in standard licenses. It is set to none
        for site and demo licenses.
        Attributes: non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _package_description = None
    @property
    def package_description(self):
        """
        Description of the package.
        Attributes: non-creatable, non-modifiable
        """
        return self._package_description
    @package_description.setter
    def package_description(self, val):
        if val != None:
            self.validate('package_description', val)
        self._package_description = val
    
    _type = None
    @property
    def type(self):
        """
        License Type.
        Attributes: non-creatable, non-modifiable
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    @staticmethod
    def get_api_name():
          return "license-v2-added"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'license-key',
            'package',
            'expiration-time',
            'customer-id',
            'serial-number',
            'package-description',
            'type',
        ]
    
    def describe_properties(self):
        return {
            'license_key': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'customer_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
