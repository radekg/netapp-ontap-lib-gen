from netapp.ntdtest.ntdtest_iterfrom_info_alt import NtdtestIterfromInfoAlt
from netapp.netapp_object import NetAppObject

class NtdtestIterfromAltModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against iter from object.
    modified due to some error.
    some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _ntdtest_iterfrom_alt_key = None
    @property
    def ntdtest_iterfrom_alt_key(self):
        """
        The keys for the iter from object to which the modify
        operation applies.
        """
        return self._ntdtest_iterfrom_alt_key
    @ntdtest_iterfrom_alt_key.setter
    def ntdtest_iterfrom_alt_key(self, val):
        if val != None:
            self.validate('ntdtest_iterfrom_alt_key', val)
        self._ntdtest_iterfrom_alt_key = val
    
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
          return "ntdtest-iterfrom-alt-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-iterfrom-alt-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_iterfrom_alt_key': { 'class': NtdtestIterfromInfoAlt, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
