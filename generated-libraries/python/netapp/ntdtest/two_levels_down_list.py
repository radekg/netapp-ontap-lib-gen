from netapp.ntdtest.three_levels_down_list import ThreeLevelsDownList
from netapp.netapp_object import NetAppObject

class TwoLevelsDownList(NetAppObject):
    """
    Two levels deep and of list type
    """
    
    _group3_stats = None
    @property
    def group3_stats(self):
        """
        Theree levels deep and of list type
        """
        return self._group3_stats
    @group3_stats.setter
    def group3_stats(self, val):
        if val != None:
            self.validate('group3_stats', val)
        self._group3_stats = val
    
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
          return "two-levels-down-list"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group3-stats',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'group3_stats': { 'class': ThreeLevelsDownList, 'is_list': True, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
