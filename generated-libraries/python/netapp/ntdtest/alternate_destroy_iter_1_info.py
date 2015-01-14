from netapp.ntdtest.ntdtest_multiple_group_info import NtdtestMultipleGroupInfo
from netapp.netapp_object import NetAppObject

class AlternateDestroyIter1Info(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against ntdtest-multiple-with-default
    object.
    query, but were not deleted due to some error.
    not deleted due to some error.
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
    
    _ntdtest_multiple_with_default_key = None
    @property
    def ntdtest_multiple_with_default_key(self):
        """
        The keys for the ntdtest-multiple-with-default object to
        which the deletion applies.
        """
        return self._ntdtest_multiple_with_default_key
    @ntdtest_multiple_with_default_key.setter
    def ntdtest_multiple_with_default_key(self, val):
        if val != None:
            self.validate('ntdtest_multiple_with_default_key', val)
        self._ntdtest_multiple_with_default_key = val
    
    @staticmethod
    def get_api_name():
          return "alternate-destroy-iter-1-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'ntdtest-multiple-with-default-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ntdtest_multiple_with_default_key': { 'class': NtdtestMultipleGroupInfo, 'is_list': False, 'required': 'required' },
        }
