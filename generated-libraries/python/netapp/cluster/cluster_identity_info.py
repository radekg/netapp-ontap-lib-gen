from netapp.netapp_object import NetAppObject

class ClusterIdentityInfo(NetAppObject):
    """
    Information that identifies a given cluster.
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
    
    _cluster_serial_number = None
    @property
    def cluster_serial_number(self):
        """
        Serial number of the cluster in the form x-xx-xxxxxx
        Attributes: non-creatable, non-modifiable
        """
        return self._cluster_serial_number
    @cluster_serial_number.setter
    def cluster_serial_number(self, val):
        if val != None:
            self.validate('cluster_serial_number', val)
        self._cluster_serial_number = val
    
    _cluster_name = None
    @property
    def cluster_name(self):
        """
        The textual name of the cluster
        Attributes: non-creatable, modifiable
        """
        return self._cluster_name
    @cluster_name.setter
    def cluster_name(self, val):
        if val != None:
            self.validate('cluster_name', val)
        self._cluster_name = val
    
    _cluster_location = None
    @property
    def cluster_location(self):
        """
        The location of the cluster
        Attributes: non-creatable, modifiable
        """
        return self._cluster_location
    @cluster_location.setter
    def cluster_location(self, val):
        if val != None:
            self.validate('cluster_location', val)
        self._cluster_location = val
    
    _cluster_uuid = None
    @property
    def cluster_uuid(self):
        """
        The 128-bit universally-unique identifier, that
        designates the cluster forever, assigned during cluster
        creation
        Attributes: non-creatable, non-modifiable
        """
        return self._cluster_uuid
    @cluster_uuid.setter
    def cluster_uuid(self, val):
        if val != None:
            self.validate('cluster_uuid', val)
        self._cluster_uuid = val
    
    _cluster_contact = None
    @property
    def cluster_contact(self):
        """
        The contact information for the cluster
        Attributes: non-creatable, modifiable
        """
        return self._cluster_contact
    @cluster_contact.setter
    def cluster_contact(self, val):
        if val != None:
            self.validate('cluster_contact', val)
        self._cluster_contact = val
    
    _rdb_uuid = None
    @property
    def rdb_uuid(self):
        """
        The 128-bit universally-unique identifier for the RDB
        Attributes: non-creatable, non-modifiable
        """
        return self._rdb_uuid
    @rdb_uuid.setter
    def rdb_uuid(self, val):
        if val != None:
            self.validate('rdb_uuid', val)
        self._rdb_uuid = val
    
    @staticmethod
    def get_api_name():
          return "cluster-identity-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cluster-serial-number',
            'cluster-name',
            'cluster-location',
            'cluster-uuid',
            'cluster-contact',
            'rdb-uuid',
        ]
    
    def describe_properties(self):
        return {
            'cluster_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_contact': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rdb_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
