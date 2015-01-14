from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class NtdtestGroupInfo(NetAppObject):
    """
    Test Stuff
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
    
    _test_group_type = None
    @property
    def test_group_type(self):
        """
        Dummy Group Type accepts any string
        Attributes: non-creatable, non-modifiable
        """
        return self._test_group_type
    @test_group_type.setter
    def test_group_type(self, val):
        if val != None:
            self.validate('test_group_type', val)
        self._test_group_type = val
    
    _test_group_os_type = None
    @property
    def test_group_os_type(self):
        """
        Dummy OS Type accepts any string
        Attributes: non-creatable, non-modifiable
        """
        return self._test_group_os_type
    @test_group_os_type.setter
    def test_group_os_type(self, val):
        if val != None:
            self.validate('test_group_os_type', val)
        self._test_group_os_type = val
    
    _test_group_name = None
    @property
    def test_group_name(self):
        """
        Dummy Group Name accepts any string
        Attributes: key, non-creatable, non-modifiable
        """
        return self._test_group_name
    @test_group_name.setter
    def test_group_name(self, val):
        if val != None:
            self.validate('test_group_name', val)
        self._test_group_name = val
    
    _ntdtestlist = None
    @property
    def ntdtestlist(self):
        """
        Dummy Initiators accepts any string
        Attributes: non-creatable, non-modifiable
        """
        return self._ntdtestlist
    @ntdtestlist.setter
    def ntdtestlist(self, val):
        if val != None:
            self.validate('ntdtestlist', val)
        self._ntdtestlist = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'test-group-type',
            'test-group-os-type',
            'test-group-name',
            'ntdtestlist',
        ]
    
    def describe_properties(self):
        return {
            'test_group_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'test_group_os_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'test_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ntdtestlist': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
        }
