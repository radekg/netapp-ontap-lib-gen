from netapp.test.test_intrinsic_apis_2 import TestIntrinsicApis2
from netapp.netapp_object import NetAppObject

class TestIntrinsicApis2ModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against test-intrinsic-apis-2 object.
    but were not modified due to some error.
    modified due to some error.
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
    
    _test_intrinsic_apis_2_key = None
    @property
    def test_intrinsic_apis_2_key(self):
        """
        The keys for the test-intrinsic-apis-2 object to which
        the modify operation applies.
        """
        return self._test_intrinsic_apis_2_key
    @test_intrinsic_apis_2_key.setter
    def test_intrinsic_apis_2_key(self, val):
        if val != None:
            self.validate('test_intrinsic_apis_2_key', val)
        self._test_intrinsic_apis_2_key = val
    
    @staticmethod
    def get_api_name():
          return "test-intrinsic-apis-2-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'test-intrinsic-apis-2-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'test_intrinsic_apis_2_key': { 'class': TestIntrinsicApis2, 'is_list': False, 'required': 'required' },
        }
