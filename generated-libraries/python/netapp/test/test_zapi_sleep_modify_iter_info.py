from netapp.test.test_sleep_info import TestSleepInfo
from netapp.netapp_object import NetAppObject

class TestZapiSleepModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against test-zapi-sleep object.
    were not modified due to some error.
    due to some error.
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
    
    _test_zapi_sleep_key = None
    @property
    def test_zapi_sleep_key(self):
        """
        The keys for the test-zapi-sleep object to which the
        modify operation applies.
        """
        return self._test_zapi_sleep_key
    @test_zapi_sleep_key.setter
    def test_zapi_sleep_key(self, val):
        if val != None:
            self.validate('test_zapi_sleep_key', val)
        self._test_zapi_sleep_key = val
    
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
          return "test-zapi-sleep-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'test-zapi-sleep-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'test_zapi_sleep_key': { 'class': TestSleepInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
