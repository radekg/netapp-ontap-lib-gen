from netapp.ntdtest.ntdtest_multiple_alternate_2 import NtdtestMultipleAlternate2
from netapp.netapp_object import NetAppObject

class NtdtestMultipleDefaultMethod1AlternateInfo(NetAppObject):
    """
    Information about the operation that was attempted/performed
    against ntdtest-multiple-default-method1 object.
    matched the query, but were not operated on due some error.
    were not operated on due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _ntdtest_multiple_default_method1_key = None
    @property
    def ntdtest_multiple_default_method1_key(self):
        """
        The keys for the ntdtest-multiple-default-method1 object
        to which the operation applies.
        """
        return self._ntdtest_multiple_default_method1_key
    @ntdtest_multiple_default_method1_key.setter
    def ntdtest_multiple_default_method1_key(self, val):
        if val != None:
            self.validate('ntdtest_multiple_default_method1_key', val)
        self._ntdtest_multiple_default_method1_key = val
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the operation caused an error.
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
    
    @staticmethod
    def get_api_name():
          return "ntdtest-multiple-default-method1-alternate-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-multiple-default-method1-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_multiple_default_method1_key': { 'class': NtdtestMultipleAlternate2, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
