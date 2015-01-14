from netapp.netapp_object import NetAppObject

class DummyCreateAsyncInfo(NetAppObject):
    """
    Contains error messages associated with back end disks.
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
    
    _volume = None
    @property
    def volume(self):
        """
        volume name
        Attributes: key, required-for-create, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _state = None
    @property
    def state(self):
        """
        State
        Attributes: non-creatable, non-modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _size = None
    @property
    def size(self):
        """
        Size
        Attributes: required-for-create, non-modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    _aggr = None
    @property
    def aggr(self):
        """
        Aggregate
        Attributes: key, required-for-create, non-modifiable
        """
        return self._aggr
    @aggr.setter
    def aggr(self, val):
        if val != None:
            self.validate('aggr', val)
        self._aggr = val
    
    @staticmethod
    def get_api_name():
          return "dummy-create-async-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'state',
            'size',
            'aggr',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'aggr': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
