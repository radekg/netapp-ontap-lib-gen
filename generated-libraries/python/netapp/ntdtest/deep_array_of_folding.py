from netapp.ntdtest.one_level_down_simple_1 import OneLevelDownSimple1
from netapp.ntdtest.one_level_down_nonlist import OneLevelDownNonlist
from netapp.ntdtest.one_level_down_simple_2 import OneLevelDownSimple2
from netapp.netapp_object import NetAppObject

class DeepArrayOfFolding(NetAppObject):
    """
    Added to test burt426912
    """
    
    _group0_stats = None
    @property
    def group0_stats(self):
        """
        1st Simple typedef one level down
        """
        return self._group0_stats
    @group0_stats.setter
    def group0_stats(self, val):
        if val != None:
            self.validate('group0_stats', val)
        self._group0_stats = val
    
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
    
    _group1_stats = None
    @property
    def group1_stats(self):
        """
        One level deep and of non list type
        """
        return self._group1_stats
    @group1_stats.setter
    def group1_stats(self, val):
        if val != None:
            self.validate('group1_stats', val)
        self._group1_stats = val
    
    _group2_stats = None
    @property
    def group2_stats(self):
        """
        2nd Simple typedef one level down
        """
        return self._group2_stats
    @group2_stats.setter
    def group2_stats(self, val):
        if val != None:
            self.validate('group2_stats', val)
        self._group2_stats = val
    
    @staticmethod
    def get_api_name():
          return "deep-array-of-folding"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group0-stats',
            'zfield1',
            'group1-stats',
            'group2-stats',
        ]
    
    def describe_properties(self):
        return {
            'group0_stats': { 'class': OneLevelDownSimple1, 'is_list': False, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group1_stats': { 'class': OneLevelDownNonlist, 'is_list': False, 'required': 'optional' },
            'group2_stats': { 'class': OneLevelDownSimple2, 'is_list': False, 'required': 'optional' },
        }
