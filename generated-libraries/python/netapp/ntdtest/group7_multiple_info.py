from netapp.ntdtest.group8_multiple_info import Group8MultipleInfo
from netapp.netapp_object import NetAppObject

class Group7MultipleInfo(NetAppObject):
    """
    1st nested typedef at level 1
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
    
    _group4_stats = None
    @property
    def group4_stats(self):
        """
        2nd nested typedef at level 1
        """
        return self._group4_stats
    @group4_stats.setter
    def group4_stats(self, val):
        if val != None:
            self.validate('group4_stats', val)
        self._group4_stats = val
    
    @staticmethod
    def get_api_name():
          return "group7-multiple-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5',
            'group4-stats',
        ]
    
    def describe_properties(self):
        return {
            'zfield5': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'group4_stats': { 'class': Group8MultipleInfo, 'is_list': False, 'required': 'optional' },
        }
