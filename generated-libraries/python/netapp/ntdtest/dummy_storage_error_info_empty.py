from netapp.netapp_object import NetAppObject

class DummyStorageErrorInfoEmpty(NetAppObject):
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
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        Disk
        Attributes: key, non-creatable, non-modifiable
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _error_text = None
    @property
    def error_text(self):
        """
        Error Text
        Attributes: non-creatable, non-modifiable
        """
        return self._error_text
    @error_text.setter
    def error_text(self, val):
        if val != None:
            self.validate('error_text', val)
        self._error_text = val
    
    _error_id = None
    @property
    def error_id(self):
        """
        Error ID
        Attributes: non-creatable, non-modifiable
        """
        return self._error_id
    @error_id.setter
    def error_id(self, val):
        if val != None:
            self.validate('error_id', val)
        self._error_id = val
    
    _error_type = None
    @property
    def error_type(self):
        """
        Error Type
        Attributes: non-creatable, non-modifiable
        """
        return self._error_type
    @error_type.setter
    def error_type(self, val):
        if val != None:
            self.validate('error_type', val)
        self._error_type = val
    
    @staticmethod
    def get_api_name():
          return "dummy-storage-error-info-empty"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'disk-name',
            'error-text',
            'error-id',
            'error-type',
        ]
    
    def describe_properties(self):
        return {
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_text': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_type': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
