from netapp.netapp_object import NetAppObject

class ClusterPeerHealthInfo(NetAppObject):
    """
    Cluster Peer Health Info
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
    
    _is_node_healthy = None
    @property
    def is_node_healthy(self):
        """
        The RDB health of the node. True means the node is in
        quorum.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_node_healthy
    @is_node_healthy.setter
    def is_node_healthy(self, val):
        if val != None:
            self.validate('is_node_healthy', val)
        self._is_node_healthy = val
    
    _destination_cluster_uuid = None
    @property
    def destination_cluster_uuid(self):
        """
        The UUID of the peer cluster.
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_cluster_uuid
    @destination_cluster_uuid.setter
    def destination_cluster_uuid(self, val):
        if val != None:
            self.validate('destination_cluster_uuid', val)
        self._destination_cluster_uuid = val
    
    _originating_node = None
    @property
    def originating_node(self):
        """
        The name of the local node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._originating_node
    @originating_node.setter
    def originating_node(self, val):
        if val != None:
            self.validate('originating_node', val)
        self._originating_node = val
    
    _icmp_ping = None
    @property
    def icmp_ping(self):
        """
        The status of ICMP Ping operation. Possible values are
        (interface-reachable, unreachable).
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "unknown_node"        - Unknown Node,
        <li> "internal_error"      - Internal Error,
        <li> "unreachable"         - Unreachable,
        <li> "session_reachable"   - Session Reachable,
        <li> "interface_reachable" - Interface Reachable
        </ul>
        """
        return self._icmp_ping
    @icmp_ping.setter
    def icmp_ping(self, val):
        if val != None:
            self.validate('icmp_ping', val)
        self._icmp_ping = val
    
    _bypass_cache = None
    @property
    def bypass_cache(self):
        """
        When false, do not use cached results.  Cached results
        may not be current, but may be retrieved quickly.
        Attributes: non-creatable, non-modifiable
        """
        return self._bypass_cache
    @bypass_cache.setter
    def bypass_cache(self, val):
        if val != None:
            self.validate('bypass_cache', val)
        self._bypass_cache = val
    
    _data_ping = None
    @property
    def data_ping(self):
        """
        The status of Data Ping operation. Possible values are
        (interface-reachable, unreachable).
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "unknown_node"        - Unknown Node,
        <li> "internal_error"      - Internal Error,
        <li> "unreachable"         - Unreachable,
        <li> "session_reachable"   - Session Reachable,
        <li> "interface_reachable" - Interface Reachable
        </ul>
        """
        return self._data_ping
    @data_ping.setter
    def data_ping(self, val):
        if val != None:
            self.validate('data_ping', val)
        self._data_ping = val
    
    _is_destination_node_available = None
    @property
    def is_destination_node_available(self):
        """
        True implies that the destination node is available for
        intercluster communication.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_destination_node_available
    @is_destination_node_available.setter
    def is_destination_node_available(self, val):
        if val != None:
            self.validate('is_destination_node_available', val)
        self._is_destination_node_available = val
    
    _destination_node = None
    @property
    def destination_node(self):
        """
        The name of the node in the peer cluster.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_node
    @destination_node.setter
    def destination_node(self, val):
        if val != None:
            self.validate('destination_node', val)
        self._destination_node = val
    
    _destination_cluster = None
    @property
    def destination_cluster(self):
        """
        The name of the peer cluster.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_cluster
    @destination_cluster.setter
    def destination_cluster(self, val):
        if val != None:
            self.validate('destination_cluster', val)
        self._destination_cluster = val
    
    _is_cluster_healthy = None
    @property
    def is_cluster_healthy(self):
        """
        The status of peer cluster health.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_cluster_healthy
    @is_cluster_healthy.setter
    def is_cluster_healthy(self, val):
        if val != None:
            self.validate('is_cluster_healthy', val)
        self._is_cluster_healthy = val
    
    @staticmethod
    def get_api_name():
          return "cluster-peer-health-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-node-healthy',
            'destination-cluster-uuid',
            'originating-node',
            'icmp-ping',
            'bypass-cache',
            'data-ping',
            'is-destination-node-available',
            'destination-node',
            'destination-cluster',
            'is-cluster-healthy',
        ]
    
    def describe_properties(self):
        return {
            'is_node_healthy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'destination_cluster_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'originating_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'icmp_ping': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bypass_cache': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'data_ping': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_destination_node_available': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'destination_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_cluster': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_cluster_healthy': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
