from netapp.netapp_object import NetAppObject

class TestIntrinsicApis3(NetAppObject):
    """
    typedef for testing instrinsic api definitions.
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
    
    _field2 = None
    @property
    def field2(self):
        """
        Dummy/Generic Field 2 accepts any boolean
        Attributes: non-creatable, non-modifiable
        """
        return self._field2
    @field2.setter
    def field2(self, val):
        if val != None:
            self.validate('field2', val)
        self._field2 = val
    
    @staticmethod
    def get_api_name():
          return "test-intrinsic-apis-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field2',
        ]
    
    def describe_properties(self):
        return {
            'field2': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
