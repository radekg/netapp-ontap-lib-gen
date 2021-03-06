from netapp.test.test_intrinsic_apis_1 import TestIntrinsicApis1
from netapp.netapp_object import NetAppObject

class TestIntrinsicApis1DestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against test-intrinsic-apis-1 object.
    but were not deleted due to some error.
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
    
    _test_intrinsic_apis_1_key = None
    @property
    def test_intrinsic_apis_1_key(self):
        """
        The keys for the test-intrinsic-apis-1 object to which
        the deletion applies.
        """
        return self._test_intrinsic_apis_1_key
    @test_intrinsic_apis_1_key.setter
    def test_intrinsic_apis_1_key(self, val):
        if val != None:
            self.validate('test_intrinsic_apis_1_key', val)
        self._test_intrinsic_apis_1_key = val
    
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
          return "test-intrinsic-apis-1-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'test-intrinsic-apis-1-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'test_intrinsic_apis_1_key': { 'class': TestIntrinsicApis1, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
