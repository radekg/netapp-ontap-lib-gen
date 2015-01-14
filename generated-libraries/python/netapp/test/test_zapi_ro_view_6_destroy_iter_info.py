from netapp.test.test_zapi_ro_view_6_info import TestZapiRoView6Info
from netapp.netapp_object import NetAppObject

class TestZapiRoView6DestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against test-zapi-ro-view-6 object.
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
    
    _test_zapi_ro_view_6_key = None
    @property
    def test_zapi_ro_view_6_key(self):
        """
        The keys for the test-zapi-ro-view-6 object to which the
        deletion applies.
        """
        return self._test_zapi_ro_view_6_key
    @test_zapi_ro_view_6_key.setter
    def test_zapi_ro_view_6_key(self, val):
        if val != None:
            self.validate('test_zapi_ro_view_6_key', val)
        self._test_zapi_ro_view_6_key = val
    
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
          return "test-zapi-ro-view-6-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'test-zapi-ro-view-6-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'test_zapi_ro_view_6_key': { 'class': TestZapiRoView6Info, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
