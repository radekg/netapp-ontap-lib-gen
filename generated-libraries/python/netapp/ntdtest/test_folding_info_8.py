from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class TestFoldingInfo8(NetAppObject):
    """
    Test input typedef 1
    """
    
    _zfield5_collapsed = None
    @property
    def zfield5_collapsed(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield5_collapsed
    @zfield5_collapsed.setter
    def zfield5_collapsed(self, val):
        if val != None:
            self.validate('zfield5_collapsed', val)
        self._zfield5_collapsed = val
    
    _zfield6_arrayof = None
    @property
    def zfield6_arrayof(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield6_arrayof
    @zfield6_arrayof.setter
    def zfield6_arrayof(self, val):
        if val != None:
            self.validate('zfield6_arrayof', val)
        self._zfield6_arrayof = val
    
    _zfield6_collapsed = None
    @property
    def zfield6_collapsed(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield6_collapsed
    @zfield6_collapsed.setter
    def zfield6_collapsed(self, val):
        if val != None:
            self.validate('zfield6_collapsed', val)
        self._zfield6_collapsed = val
    
    _zfield5_arrayof = None
    @property
    def zfield5_arrayof(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield5_arrayof
    @zfield5_arrayof.setter
    def zfield5_arrayof(self, val):
        if val != None:
            self.validate('zfield5_arrayof', val)
        self._zfield5_arrayof = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-info-8"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5-collapsed',
            'zfield6-arrayof',
            'zfield6-collapsed',
            'zfield5-arrayof',
        ]
    
    def describe_properties(self):
        return {
            'zfield5_collapsed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield6_arrayof': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'zfield6_collapsed': { 'class': NtdtestInfo, 'is_list': False, 'required': 'optional' },
            'zfield5_arrayof': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
