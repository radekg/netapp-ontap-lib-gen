from netapp.ntdtest.two_levels_down_list import TwoLevelsDownList
from netapp.netapp_object import NetAppObject

class OneLevelDownNonlist(NetAppObject):
    """
    One level deep and of non list type
    """
    
    _zfield4 = None
    @property
    def zfield4(self):
        """
        Generic/Dummy Field 4
        Attributes: required-for-create, non-modifiable
        """
        return self._zfield4
    @zfield4.setter
    def zfield4(self, val):
        if val != None:
            self.validate('zfield4', val)
        self._zfield4 = val
    
    _group2_stats = None
    @property
    def group2_stats(self):
        """
        Two levels deep and of list type
        """
        return self._group2_stats
    @group2_stats.setter
    def group2_stats(self, val):
        if val != None:
            self.validate('group2_stats', val)
        self._group2_stats = val
    
    @staticmethod
    def get_api_name():
          return "one-level-down-nonlist"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield4',
            'group2-stats',
        ]
    
    def describe_properties(self):
        return {
            'zfield4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group2_stats': { 'class': TwoLevelsDownList, 'is_list': True, 'required': 'optional' },
        }
