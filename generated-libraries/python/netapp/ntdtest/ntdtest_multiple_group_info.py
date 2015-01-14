from netapp.ntdtest.group1_multiple_info import Group1MultipleInfo
from netapp.netapp_object import NetAppObject

class NtdtestMultipleGroupInfo(NetAppObject):
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
          return "ntdtest-multiple-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group1-stats',
            'zfield1',
        ]
    
    def describe_properties(self):
        return {
            'group1_stats': { 'class': Group1MultipleInfo, 'is_list': False, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
