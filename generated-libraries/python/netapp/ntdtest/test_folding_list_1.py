from netapp.ntdtest.test_folding_list_2 import TestFoldingList2
from netapp.netapp_object import NetAppObject

class TestFoldingList1(NetAppObject):
    """
    Test output typedef 1
    """
    
    _test_typedef_2 = None
    @property
    def test_typedef_2(self):
        """
        Test output typedef 2
        """
        return self._test_typedef_2
    @test_typedef_2.setter
    def test_typedef_2(self, val):
        if val != None:
            self.validate('test_typedef_2', val)
        self._test_typedef_2 = val
    
    _zfield2 = None
    @property
    def zfield2(self):
        """
        Generic/Dummy Field 2
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield2
    @zfield2.setter
    def zfield2(self, val):
        if val != None:
            self.validate('zfield2', val)
        self._zfield2 = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-list-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'test-typedef-2',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'test_typedef_2': { 'class': TestFoldingList2, 'is_list': True, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
