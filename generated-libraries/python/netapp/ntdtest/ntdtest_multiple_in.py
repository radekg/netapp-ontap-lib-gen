from netapp.ntdtest.group5_multiple_info import Group5MultipleInfo
from netapp.netapp_object import NetAppObject

class NtdtestMultipleIn(NetAppObject):
    """
    Default Input Typedef
    """
    
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
          return "ntdtest-multiple-in"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group1-stats',
            'zfield1',
        ]
    
    def describe_properties(self):
        return {
            'group1_stats': { 'class': Group5MultipleInfo, 'is_list': False, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
