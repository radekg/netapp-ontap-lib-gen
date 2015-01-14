from netapp.ntdtest.group3_view_info import Group3ViewInfo
from netapp.ntdtest.group1_view_info import Group1ViewInfo
from netapp.ntdtest.group4_view_info import Group4ViewInfo
from netapp.ntdtest.group2_view_info import Group2ViewInfo
from netapp.netapp_object import NetAppObject

class NtdtestViewGroupInfo(NetAppObject):
    """
    Top-Level Typedef containing 4 nested typedefs all at the same
    level
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _group3_stats = None
    @property
    def group3_stats(self):
        """
        3rd nested typedef at level 1
        """
        return self._group3_stats
    @group3_stats.setter
    def group3_stats(self, val):
        if val != None:
            self.validate('group3_stats', val)
        self._group3_stats = val
    
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
    
    _group4_stats = None
    @property
    def group4_stats(self):
        """
        4th nested typedef at level 1
        """
        return self._group4_stats
    @group4_stats.setter
    def group4_stats(self, val):
        if val != None:
            self.validate('group4_stats', val)
        self._group4_stats = val
    
    _group2_stats = None
    @property
    def group2_stats(self):
        """
        2nd nested typedef at level 1
        """
        return self._group2_stats
    @group2_stats.setter
    def group2_stats(self, val):
        if val != None:
            self.validate('group2_stats', val)
        self._group2_stats = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-view-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group3-stats',
            'group1-stats',
            'group4-stats',
            'group2-stats',
        ]
    
    def describe_properties(self):
        return {
            'group3_stats': { 'class': Group3ViewInfo, 'is_list': False, 'required': 'optional' },
            'group1_stats': { 'class': Group1ViewInfo, 'is_list': False, 'required': 'optional' },
            'group4_stats': { 'class': Group4ViewInfo, 'is_list': False, 'required': 'optional' },
            'group2_stats': { 'class': Group2ViewInfo, 'is_list': False, 'required': 'optional' },
        }
