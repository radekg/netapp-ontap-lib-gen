from netapp.netapp_object import NetAppObject

class ClusterApplicationRecordInfo(NetAppObject):
    """
    Information that shows data held by cluster application-record
    table.
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
    
    _record_name = None
    @property
    def record_name(self):
        """
        The name of the record key to set the value.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._record_name
    @record_name.setter
    def record_name(self, val):
        if val != None:
            self.validate('record_name', val)
        self._record_name = val
    
    _modified_from = None
    @property
    def modified_from(self):
        """
        Location from where the value was last modified. If the
        value was modified by an external IP address through a
        zapi api, that IP address will be stored. If the value
        was modified through cli, then console will be stored.
        Attributes: non-creatable, non-modifiable
        """
        return self._modified_from
    @modified_from.setter
    def modified_from(self, val):
        if val != None:
            self.validate('modified_from', val)
        self._modified_from = val
    
    _last_modified_timestamp = None
    @property
    def last_modified_timestamp(self):
        """
        Last time the value was modified.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_modified_timestamp
    @last_modified_timestamp.setter
    def last_modified_timestamp(self, val):
        if val != None:
            self.validate('last_modified_timestamp', val)
        self._last_modified_timestamp = val
    
    _record_value = None
    @property
    def record_value(self):
        """
        The value for the record key.
        Attributes: required-for-create, modifiable
        """
        return self._record_value
    @record_value.setter
    def record_value(self, val):
        if val != None:
            self.validate('record_value', val)
        self._record_value = val
    
    @staticmethod
    def get_api_name():
          return "cluster-application-record-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'record-name',
            'modified-from',
            'last-modified-timestamp',
            'record-value',
        ]
    
    def describe_properties(self):
        return {
            'record_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'modified_from': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_modified_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'record_value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
