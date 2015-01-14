from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class TestFoldingInfo2(NetAppObject):
    """
    Test input typedef 2
    """
    
    _zfield5 = None
    @property
    def zfield5(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield5
    @zfield5.setter
    def zfield5(self, val):
        if val != None:
            self.validate('zfield5', val)
        self._zfield5 = val
    
    _zfield6 = None
    @property
    def zfield6(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield6
    @zfield6.setter
    def zfield6(self, val):
        if val != None:
            self.validate('zfield6', val)
        self._zfield6 = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-info-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5',
            'zfield6',
        ]
    
    def describe_properties(self):
        return {
            'zfield5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield6': { 'class': NtdtestInfo, 'is_list': False, 'required': 'optional' },
        }
