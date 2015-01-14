from netapp.ntdtest.test_folding_info_10 import TestFoldingInfo10
from netapp.netapp_object import NetAppObject

class NdtestFoldingGroupInfoAlt(NetAppObject):
    """
    Alternative top level typedef
    """
    
    _test_typedef_1 = None
    @property
    def test_typedef_1(self):
        """
        Test input typedef 1
        """
        return self._test_typedef_1
    @test_typedef_1.setter
    def test_typedef_1(self, val):
        if val != None:
            self.validate('test_typedef_1', val)
        self._test_typedef_1 = val
    
    _zfield1 = None
    @property
    def zfield1(self):
        """
        Generic/Dummy Field 1
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield1
    @zfield1.setter
    def zfield1(self, val):
        if val != None:
            self.validate('zfield1', val)
        self._zfield1 = val
    
    @staticmethod
    def get_api_name():
          return "ndtest-folding-group-info-alt"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'test-typedef-1',
            'zfield1',
        ]
    
    def describe_properties(self):
        return {
            'test_typedef_1': { 'class': TestFoldingInfo10, 'is_list': True, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
