from netapp.ntdtest.test_extensive_type_2 import TestExtensiveType2
from netapp.netapp_object import NetAppObject

class TestExtensiveType1(NetAppObject):
    """
    Test input typedef 1
    """
    
    _test_typedef_2 = None
    @property
    def test_typedef_2(self):
        """
        Test input typedef 2
        """
        return self._test_typedef_2
    @test_typedef_2.setter
    def test_typedef_2(self, val):
        if val != None:
            self.validate('test_typedef_2', val)
        self._test_typedef_2 = val
    
    _field_1 = None
    @property
    def field_1(self):
        """
        This is zapi description for field1.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    @staticmethod
    def get_api_name():
          return "test-extensive-type-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'test-typedef-2',
            'field-1',
        ]
    
    def describe_properties(self):
        return {
            'test_typedef_2': { 'class': TestExtensiveType2, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
