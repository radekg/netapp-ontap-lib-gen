from netapp.netapp_object import NetAppObject

class EurologicSpecificInfo(NetAppObject):
    """
    Vendor specific enclosure system information for
    Eurologic shelf.
    """
    
    _eurologic_backplane_byte = None
    @property
    def eurologic_backplane_byte(self):
        """
        Backplane byte for Eurologic shelf.
        """
        return self._eurologic_backplane_byte
    @eurologic_backplane_byte.setter
    def eurologic_backplane_byte(self, val):
        if val != None:
            self.validate('eurologic_backplane_byte', val)
        self._eurologic_backplane_byte = val
    
    _eurologic_backplane_id = None
    @property
    def eurologic_backplane_id(self):
        """
        Backplane identifier for Eurologic shelf.
        """
        return self._eurologic_backplane_id
    @eurologic_backplane_id.setter
    def eurologic_backplane_id(self, val):
        if val != None:
            self.validate('eurologic_backplane_id', val)
        self._eurologic_backplane_id = val
    
    _eurologic_application_version = None
    @property
    def eurologic_application_version(self):
        """
        Application version for Eurologic shelf.
        """
        return self._eurologic_application_version
    @eurologic_application_version.setter
    def eurologic_application_version(self, val):
        if val != None:
            self.validate('eurologic_application_version', val)
        self._eurologic_application_version = val
    
    _eurologic_cabinet_id = None
    @property
    def eurologic_cabinet_id(self):
        """
        Cabinet id for the Eurologic shelf.
        """
        return self._eurologic_cabinet_id
    @eurologic_cabinet_id.setter
    def eurologic_cabinet_id(self, val):
        if val != None:
            self.validate('eurologic_cabinet_id', val)
        self._eurologic_cabinet_id = val
    
    _eurologic_serial_no = None
    @property
    def eurologic_serial_no(self):
        """
        Serial number for the Eurologic shelf.
        """
        return self._eurologic_serial_no
    @eurologic_serial_no.setter
    def eurologic_serial_no(self, val):
        if val != None:
            self.validate('eurologic_serial_no', val)
        self._eurologic_serial_no = val
    
    _eurologic_kernel_version = None
    @property
    def eurologic_kernel_version(self):
        """
        Kernel version for Eurologic shelf.
        """
        return self._eurologic_kernel_version
    @eurologic_kernel_version.setter
    def eurologic_kernel_version(self, val):
        if val != None:
            self.validate('eurologic_kernel_version', val)
        self._eurologic_kernel_version = val
    
    _eurologic_backplane_function = None
    @property
    def eurologic_backplane_function(self):
        """
        Backplane function for Eurologic shelf.
        """
        return self._eurologic_backplane_function
    @eurologic_backplane_function.setter
    def eurologic_backplane_function(self, val):
        if val != None:
            self.validate('eurologic_backplane_function', val)
        self._eurologic_backplane_function = val
    
    @staticmethod
    def get_api_name():
          return "eurologic-specific-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'eurologic-backplane-byte',
            'eurologic-backplane-id',
            'eurologic-application-version',
            'eurologic-cabinet-id',
            'eurologic-serial-no',
            'eurologic-kernel-version',
            'eurologic-backplane-function',
        ]
    
    def describe_properties(self):
        return {
            'eurologic_backplane_byte': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'eurologic_backplane_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'eurologic_application_version': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'eurologic_cabinet_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'eurologic_serial_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'eurologic_kernel_version': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'eurologic_backplane_function': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
