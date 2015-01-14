from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class TestNtdtestMultipleArrayInfo5(NetAppObject):
    """
    Test input typedef 2
    """
    
    _zfield7 = None
    @property
    def zfield7(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield7
    @zfield7.setter
    def zfield7(self, val):
        if val != None:
            self.validate('zfield7', val)
        self._zfield7 = val
    
    _zfield8 = None
    @property
    def zfield8(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield8
    @zfield8.setter
    def zfield8(self, val):
        if val != None:
            self.validate('zfield8', val)
        self._zfield8 = val
    
    @staticmethod
    def get_api_name():
          return "test-ntdtest-multiple-array-info-5"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield7',
            'zfield8',
        ]
    
    def describe_properties(self):
        return {
            'zfield7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield8': { 'class': NtdtestInfo, 'is_list': False, 'required': 'optional' },
        }
