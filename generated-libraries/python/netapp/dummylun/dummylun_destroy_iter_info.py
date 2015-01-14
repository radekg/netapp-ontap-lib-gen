from netapp.dummylun.dummylun_info import DummylunInfo
from netapp.netapp_object import NetAppObject

class DummylunDestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against dummylun object.
    deleted due to some error.
    some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    _dummylun_key = None
    @property
    def dummylun_key(self):
        """
        The keys for the dummylun object to which the deletion
        applies.
        """
        return self._dummylun_key
    @dummylun_key.setter
    def dummylun_key(self, val):
        if val != None:
            self.validate('dummylun_key', val)
        self._dummylun_key = val
    
    @staticmethod
    def get_api_name():
          return "dummylun-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'dummylun-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dummylun_key': { 'class': DummylunInfo, 'is_list': False, 'required': 'required' },
        }
