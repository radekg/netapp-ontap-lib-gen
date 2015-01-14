from netapp.ntdtest.ntdtest_multiple_out import NtdtestMultipleOut
from netapp.netapp_object import NetAppObject

class DefaultModifyIterInoutInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against ntdtest-multiple-with-inout object.
    query, but were not modified due to some error.
    not modified due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _ntdtest_multiple_with_inout_key = None
    @property
    def ntdtest_multiple_with_inout_key(self):
        """
        The keys for the ntdtest-multiple-with-inout object to
        which the modify operation applies.
        """
        return self._ntdtest_multiple_with_inout_key
    @ntdtest_multiple_with_inout_key.setter
    def ntdtest_multiple_with_inout_key(self, val):
        if val != None:
            self.validate('ntdtest_multiple_with_inout_key', val)
        self._ntdtest_multiple_with_inout_key = val
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the modify operation caused an error.
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
        Error description, if the modify operation caused an
        error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "default-modify-iter-inout-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-multiple-with-inout-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_multiple_with_inout_key': { 'class': NtdtestMultipleOut, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
