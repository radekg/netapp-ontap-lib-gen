from netapp.ntdtest.ntdtest_extensive_group_info import NtdtestExtensiveGroupInfo
from netapp.netapp_object import NetAppObject

class NtdtestExtensiveModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against ntdtest-extensive object.
    were not modified due to some error.
    modified due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _ntdtest_extensive_key = None
    @property
    def ntdtest_extensive_key(self):
        """
        The keys for the ntdtest-extensive object to which the
        modify operation applies.
        """
        return self._ntdtest_extensive_key
    @ntdtest_extensive_key.setter
    def ntdtest_extensive_key(self, val):
        if val != None:
            self.validate('ntdtest_extensive_key', val)
        self._ntdtest_extensive_key = val
    
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
          return "ntdtest-extensive-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-extensive-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_extensive_key': { 'class': NtdtestExtensiveGroupInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
