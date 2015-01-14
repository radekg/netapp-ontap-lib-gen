from netapp.ntdtest.ntdtest_iternoread_info import NtdtestIternoreadInfo
from netapp.netapp_object import NetAppObject

class NtdtestIternoreadModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against show noread object.
    not modified due to some error.
    to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
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
    
    _ntdtest_iternoread_key = None
    @property
    def ntdtest_iternoread_key(self):
        """
        The keys for the show noread object to which the modify
        operation applies.
        """
        return self._ntdtest_iternoread_key
    @ntdtest_iternoread_key.setter
    def ntdtest_iternoread_key(self, val):
        if val != None:
            self.validate('ntdtest_iternoread_key', val)
        self._ntdtest_iternoread_key = val
    
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
          return "ntdtest-iternoread-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'ntdtest-iternoread-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ntdtest_iternoread_key': { 'class': NtdtestIternoreadInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
