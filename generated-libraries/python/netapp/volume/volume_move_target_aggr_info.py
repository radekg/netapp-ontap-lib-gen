from netapp.netapp_object import NetAppObject

class VolumeMoveTargetAggrInfo(NetAppObject):
    """
    Compatible target aggregate information
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
    
    _storage_type = None
    @property
    def storage_type(self):
        """
        Storage Type
        Attributes: non-creatable, non-modifiable
        """
        return self._storage_type
    @storage_type.setter
    def storage_type(self, val):
        if val != None:
            self.validate('storage_type', val)
        self._storage_type = val
    
    _aggr_name = None
    @property
    def aggr_name(self):
        """
        Aggregate Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._aggr_name
    @aggr_name.setter
    def aggr_name(self, val):
        if val != None:
            self.validate('aggr_name', val)
        self._aggr_name = val
    
    _available_size = None
    @property
    def available_size(self):
        """
        Available size
        Attributes: non-creatable, non-modifiable
        """
        return self._available_size
    @available_size.setter
    def available_size(self, val):
        if val != None:
            self.validate('available_size', val)
        self._available_size = val
    
    @staticmethod
    def get_api_name():
          return "volume-move-target-aggr-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'storage-type',
            'aggr-name',
            'available-size',
        ]
    
    def describe_properties(self):
        return {
            'storage_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'available_size': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
