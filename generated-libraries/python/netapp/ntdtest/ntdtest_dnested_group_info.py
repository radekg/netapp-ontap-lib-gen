from netapp.ntdtest.level1_info import Level1Info
from netapp.netapp_object import NetAppObject

class NtdtestDnestedGroupInfo(NetAppObject):
    """
    Top-Level Typedef containing 5 nested typedefs, all nested
    deeply
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
    
    _field_5 = None
    @property
    def field_5(self):
        """
        Dummy/Generic Field 5
        Attributes: non-creatable, non-modifiable
        """
        return self._field_5
    @field_5.setter
    def field_5(self, val):
        if val != None:
            self.validate('field_5', val)
        self._field_5 = val
    
    _level1 = None
    @property
    def level1(self):
        """
        1st nested typedef at level 1
        """
        return self._level1
    @level1.setter
    def level1(self, val):
        if val != None:
            self.validate('level1', val)
        self._level1 = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-dnested-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-5',
            'level1',
        ]
    
    def describe_properties(self):
        return {
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'level1': { 'class': Level1Info, 'is_list': False, 'required': 'optional' },
        }
