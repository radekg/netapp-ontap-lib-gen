from netapp.netapp_object import NetAppObject

class TestIntrinsicApis1(NetAppObject):
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
    
    _field3 = None
    @property
    def field3(self):
        """
        Dummy/Generic Field 3 accepts an integer
        Attributes: non-creatable, non-modifiable
        """
        return self._field3
    @field3.setter
    def field3(self, val):
        if val != None:
            self.validate('field3', val)
        self._field3 = val
    
    @staticmethod
    def get_api_name():
          return "test-intrinsic-apis-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field3',
        ]
    
    def describe_properties(self):
        return {
            'field3': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
