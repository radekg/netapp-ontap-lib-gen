from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class TestFoldingInfo10(NetAppObject):
    """
    Test input typedef 1
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
    
    _zfield1_repeated = None
    @property
    def zfield1_repeated(self):
        """
        Generic/Dummy Field 1
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield1_repeated
    @zfield1_repeated.setter
    def zfield1_repeated(self, val):
        if val != None:
            self.validate('zfield1_repeated', val)
        self._zfield1_repeated = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-info-10"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5',
            'zfield6',
            'zfield1-repeated',
        ]
    
    def describe_properties(self):
        return {
            'zfield5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield6': { 'class': NtdtestInfo, 'is_list': False, 'required': 'optional' },
            'zfield1_repeated': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
