from netapp.netapp_object import NetAppObject

class AutozapiviewInfo(NetAppObject):
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        vserver name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _id = None
    @property
    def id(self):
        """
        id of object
        Attributes: key, non-creatable, non-modifiable
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _joe = None
    @property
    def joe(self):
        """
        id of object
        Attributes: key, non-creatable, non-modifiable
        """
        return self._joe
    @joe.setter
    def joe(self, val):
        if val != None:
            self.validate('joe', val)
        self._joe = val
    
    @staticmethod
    def get_api_name():
          return "autozapiview-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'id',
            'joe',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'joe': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
