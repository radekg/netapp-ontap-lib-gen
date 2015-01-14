from netapp.netapp_object import NetAppObject

class NtdtestMultipleArraysInfo(NetAppObject):
    """
    ABC
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
    
    _field_1 = None
    @property
    def field_1(self):
        """
        Field 1
        Attributes: key, non-creatable, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Field 2
        Attributes: non-creatable, non-modifiable
        """
        return self._field_2
    @field_2.setter
    def field_2(self, val):
        if val != None:
            self.validate('field_2', val)
        self._field_2 = val
    
    _field_3 = None
    @property
    def field_3(self):
        """
        Field 3
        Attributes: non-creatable, non-modifiable
        """
        return self._field_3
    @field_3.setter
    def field_3(self, val):
        if val != None:
            self.validate('field_3', val)
        self._field_3 = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-multiple-arrays-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-1',
            'field-2',
            'field-3',
        ]
    
    def describe_properties(self):
        return {
            'field_1': { 'class': int, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
