from netapp.ntdtest.group3_info import Group3Info
from netapp.ntdtest.group1_info import Group1Info
from netapp.ntdtest.group2_info import Group2Info
from netapp.netapp_object import NetAppObject

class NtdtestTopLevelInfo(NetAppObject):
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
    
    _list_11 = None
    @property
    def list_11(self):
        """
        Generic/Dummy Field 11
        Attributes: non-creatable, non-modifiable
        """
        return self._list_11
    @list_11.setter
    def list_11(self, val):
        if val != None:
            self.validate('list_11', val)
        self._list_11 = val
    
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
    
    _list_12 = None
    @property
    def list_12(self):
        """
        Generic/Dummy Field 12
        Attributes: non-creatable, non-modifiable
        """
        return self._list_12
    @list_12.setter
    def list_12(self, val):
        if val != None:
            self.validate('list_12', val)
        self._list_12 = val
    
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
          return "ntdtest-top-level-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'list-11',
            'group3-stats',
            'list-12',
            'group1-stats',
            'group2-stats',
        ]
    
    def describe_properties(self):
        return {
            'list_11': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group3_stats': { 'class': Group3Info, 'is_list': False, 'required': 'optional' },
            'list_12': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group1_stats': { 'class': Group1Info, 'is_list': False, 'required': 'optional' },
            'group2_stats': { 'class': Group2Info, 'is_list': False, 'required': 'optional' },
        }
