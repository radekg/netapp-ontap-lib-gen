from netapp.test.test_zapi_ro_view_5_info import TestZapiRoView5Info
from netapp.netapp_object import NetAppObject

class TestZapiRoView5DestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against test-zapi-ro-view-5 object.
    were not deleted due to some error.
    deleted due to some error.
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
    
    _test_zapi_ro_view_5_key = None
    @property
    def test_zapi_ro_view_5_key(self):
        """
        The keys for the test-zapi-ro-view-5 object to which the
        deletion applies.
        """
        return self._test_zapi_ro_view_5_key
    @test_zapi_ro_view_5_key.setter
    def test_zapi_ro_view_5_key(self, val):
        if val != None:
            self.validate('test_zapi_ro_view_5_key', val)
        self._test_zapi_ro_view_5_key = val
    
    @staticmethod
    def get_api_name():
          return "test-zapi-ro-view-5-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'test-zapi-ro-view-5-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'test_zapi_ro_view_5_key': { 'class': TestZapiRoView5Info, 'is_list': False, 'required': 'required' },
        }
