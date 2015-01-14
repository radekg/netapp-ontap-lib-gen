from netapp.netapp_object import NetAppObject

class ClusterPeerInfo(NetAppObject):
    """
    Contains information about the cluster peer.
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
    
    _active_addresses = None
    @property
    def active_addresses(self):
        """
        The Active IP addresses of the peer cluster.
        Attributes: non-creatable, non-modifiable
        """
        return self._active_addresses
    @active_addresses.setter
    def active_addresses(self, val):
        if val != None:
            self.validate('active_addresses', val)
        self._active_addresses = val
    
    _cluster_name = None
    @property
    def cluster_name(self):
        """
        The name of the peer cluster.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._cluster_name
    @cluster_name.setter
    def cluster_name(self, val):
        if val != None:
            self.validate('cluster_name', val)
        self._cluster_name = val
    
    _timeout = None
    @property
    def timeout(self):
        """
        The timeout for operations in the peer cluster in
        seconds.
        Default: 15
        Attributes: non-creatable, modifiable
        """
        return self._timeout
    @timeout.setter
    def timeout(self, val):
        if val != None:
            self.validate('timeout', val)
        self._timeout = val
    
    _cluster_uuid = None
    @property
    def cluster_uuid(self):
        """
        The UUID of the peer cluster.
        Attributes: non-creatable, non-modifiable
        """
        return self._cluster_uuid
    @cluster_uuid.setter
    def cluster_uuid(self, val):
        if val != None:
            self.validate('cluster_uuid', val)
        self._cluster_uuid = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        This is an assigned serial number of peer cluster. It is
        assigned at the time of cluster create.
        Attributes: non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _remote_cluster_name = None
    @property
    def remote_cluster_name(self):
        """
        The current name of the peer cluster.
        Attributes: non-creatable, non-modifiable
        """
        return self._remote_cluster_name
    @remote_cluster_name.setter
    def remote_cluster_name(self, val):
        if val != None:
            self.validate('remote_cluster_name', val)
        self._remote_cluster_name = val
    
    _peer_addresses = None
    @property
    def peer_addresses(self):
        """
        The Remote IP address or host name of the peer cluster.
        Attributes: non-creatable, modifiable
        """
        return self._peer_addresses
    @peer_addresses.setter
    def peer_addresses(self, val):
        if val != None:
            self.validate('peer_addresses', val)
        self._peer_addresses = val
    
    _availability = None
    @property
    def availability(self):
        """
        The status of the peer cluster connection.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "unavailable"    ,
        <li> "available"
        </ul>
        """
        return self._availability
    @availability.setter
    def availability(self, val):
        if val != None:
            self.validate('availability', val)
        self._availability = val
    
    @staticmethod
    def get_api_name():
          return "cluster-peer-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'active-addresses',
            'cluster-name',
            'timeout',
            'cluster-uuid',
            'serial-number',
            'remote-cluster-name',
            'peer-addresses',
            'availability',
        ]
    
    def describe_properties(self):
        return {
            'active_addresses': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'cluster_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cluster_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'remote_cluster_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'peer_addresses': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'availability': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
