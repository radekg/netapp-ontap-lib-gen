from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.ntdtest.group3_multiple_info import Group3MultipleInfo
from netapp.netapp_object import NetAppObject

class NtdtestMultipleAlternate2(NetAppObject):
    """
    2nd alternative typedef for table
    """
    
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
    
    _group1_stats = None
    @property
    def group1_stats(self):
        """
        1st nested typedef at level 1
        """
        return self._group1_stats
    @group1_stats.setter
    def group1_stats(self, val):
        if val != None:
            self.validate('group1_stats', val)
        self._group1_stats = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-multiple-alternate-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield6',
            'group1-stats',
        ]
    
    def describe_properties(self):
        return {
            'zfield6': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'group1_stats': { 'class': Group3MultipleInfo, 'is_list': False, 'required': 'optional' },
        }
