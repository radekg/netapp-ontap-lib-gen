from netapp.ntdtest.ntdtest_iterfrom_info import NtdtestIterfromInfo
from netapp.netapp_object import NetAppObject

class NtdtestIterfromDupeModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against iter from dupe object.
    not modified due to some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _ntdtest_iterfrom_dupe_key = None
    @property
    def ntdtest_iterfrom_dupe_key(self):
        """
        The keys for the iter from dupe object to which the
        modify operation applies.
        """
        return self._ntdtest_iterfrom_dupe_key
    @ntdtest_iterfrom_dupe_key.setter
    def ntdtest_iterfrom_dupe_key(self, val):
        if val != None:
            self.validate('ntdtest_iterfrom_dupe_key', val)
        self._ntdtest_iterfrom_dupe_key = val
    
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
          return "ntdtest-iterfrom-dupe-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-iterfrom-dupe-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_iterfrom_dupe_key': { 'class': NtdtestIterfromInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
