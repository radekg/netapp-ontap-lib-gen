from netapp.netapp_object import NetAppObject

class DummyStorageErrorInfo(NetAppObject):
    """
    Contains error messages associated with back end disks.
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
    
    _error_id = None
    @property
    def error_id(self):
        """
        Error ID
        Attributes: required-for-create, modifiable
        """
        return self._error_id
    @error_id.setter
    def error_id(self, val):
        if val != None:
            self.validate('error_id', val)
        self._error_id = val
    
    _lun_serial_number = None
    @property
    def lun_serial_number(self):
        """
        Serial Number
        Attributes: required-for-create, modifiable
        """
        return self._lun_serial_number
    @lun_serial_number.setter
    def lun_serial_number(self, val):
        if val != None:
            self.validate('lun_serial_number', val)
        self._lun_serial_number = val
    
    _error_text = None
    @property
    def error_text(self):
        """
        Error Text
        Attributes: required-for-create, modifiable
        """
        return self._error_text
    @error_text.setter
    def error_text(self, val):
        if val != None:
            self.validate('error_text', val)
        self._error_text = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        Disk
        Attributes: key, required-for-create, non-modifiable
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _error_type = None
    @property
    def error_type(self):
        """
        Error Type
        Attributes: required-for-create, modifiable
        """
        return self._error_type
    @error_type.setter
    def error_type(self, val):
        if val != None:
            self.validate('error_type', val)
        self._error_type = val
    
    _array_name = None
    @property
    def array_name(self):
        """
        Array Name
        Attributes: required-for-create, modifiable
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        UID
        Attributes: required-for-create, modifiable
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "dummy-storage-error-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-id',
            'lun-serial-number',
            'error-text',
            'disk-name',
            'error-type',
            'array-name',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'error_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lun_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_text': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_type': { 'class': int, 'is_list': False, 'required': 'optional' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
