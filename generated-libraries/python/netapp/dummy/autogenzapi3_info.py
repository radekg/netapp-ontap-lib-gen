from netapp.netapp_object import NetAppObject

class Autogenzapi3Info(NetAppObject):
    """
    auto generated
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
    
    _id = None
    @property
    def id(self):
        """
        id of object
        Attributes: key, required-for-create, non-modifiable
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _name = None
    @property
    def name(self):
        """
        name of object
        Attributes: required-for-create, modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "autogenzapi3-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'id',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
