from netapp.ntdtest.group6_multiple_info import Group6MultipleInfo
from netapp.netapp_object import NetAppObject

class Group5MultipleInfo(NetAppObject):
    """
    1st nested typedef at level 1
    """
    
    _group4_stats = None
    @property
    def group4_stats(self):
        """
        2nd nested typedef at level 2
        """
        return self._group4_stats
    @group4_stats.setter
    def group4_stats(self, val):
        if val != None:
            self.validate('group4_stats', val)
        self._group4_stats = val
    
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
          return "group5-multiple-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group4-stats',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'group4_stats': { 'class': Group6MultipleInfo, 'is_list': False, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
