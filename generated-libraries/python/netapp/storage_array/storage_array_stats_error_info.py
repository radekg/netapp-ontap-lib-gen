from netapp.netapp_object import NetAppObject

class StorageArrayStatsErrorInfo(NetAppObject):
    """
    Contains error messages associated with array.
    """
    
    _error_text = None
    @property
    def error_text(self):
        """
        A description of the error being reported.
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
        A unique ID for each error returned.  ID is unique
        on a per API call basis only.
        Range: [0..2^32-1]
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
        Enum describing type of error.
        Range: [0..2^32-1]
        ARRAY_INCONSISTENT_LUN_ADDRESSING_METHOD   - 1. Array is using inconsistent LUN addressing schemes.
        ARRAY_DEVTYPE_ERROR                        - 2. Array has encountered a device class error.
        """
        return self._error_type
    @error_type.setter
    def error_type(self, val):
        if val != None:
            self.validate('error_type', val)
        self._error_type = val
    
    @staticmethod
    def get_api_name():
          return "storage-array-stats-error-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-text',
            'error-id',
            'error-type',
        ]
    
    def describe_properties(self):
        return {
            'error_text': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'error_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'error_type': { 'class': int, 'is_list': False, 'required': 'required' },
        }
