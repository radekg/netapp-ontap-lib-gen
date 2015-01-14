from netapp.netapp_object import NetAppObject

class ManagedFeatureStatusInfo(NetAppObject):
    """
    Status information about a managed feature.
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
    
    _status = None
    @property
    def status(self):
        """
        Status of a managed feature.
        Attributes: non-creatable, non-modifiable
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _feature_name = None
    @property
    def feature_name(self):
        """
        Managed feature name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._feature_name
    @feature_name.setter
    def feature_name(self, val):
        if val != None:
            self.validate('feature_name', val)
        self._feature_name = val
    
    _notes = None
    @property
    def notes(self):
        """
        Additional information about the managed feature status.
        Attributes: non-creatable, non-modifiable
        """
        return self._notes
    @notes.setter
    def notes(self, val):
        if val != None:
            self.validate('notes', val)
        self._notes = val
    
    @staticmethod
    def get_api_name():
          return "managed-feature-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'feature-name',
            'notes',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'feature_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'notes': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
