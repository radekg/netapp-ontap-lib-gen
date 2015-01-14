from netapp.netapp_object import NetAppObject

class SnapshotMultirenameError(NetAppObject):
    """
    Information of the error details for snapshot multirename
    operation
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
    
    _error_number = None
    @property
    def error_number(self):
        """
        Error code due to which snapshot rename failed on a
        volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._error_number
    @error_number.setter
    def error_number(self, val):
        if val != None:
            self.validate('error_number', val)
        self._error_number = val
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        Volume name on which snapshot rename failed.
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _error_reason = None
    @property
    def error_reason(self):
        """
        Error reason due to which snapshot rename failed on a
        volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._error_reason
    @error_reason.setter
    def error_reason(self, val):
        if val != None:
            self.validate('error_reason', val)
        self._error_reason = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-multirename-error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-number',
            'volume-name',
            'error-reason',
        ]
    
    def describe_properties(self):
        return {
            'error_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
