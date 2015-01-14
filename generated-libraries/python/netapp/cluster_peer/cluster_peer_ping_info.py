from netapp.netapp_object import NetAppObject

class ClusterPeerPingInfo(NetAppObject):
    """
    Cluster Peer Ping Configuration
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
    
    _count = None
    @property
    def count(self):
        """
        The total number of times to ping.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._count
    @count.setter
    def count(self, val):
        if val != None:
            self.validate('count', val)
        self._count = val
    
    _current_count = None
    @property
    def current_count(self):
        """
        The current ping count.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._current_count
    @current_count.setter
    def current_count(self, val):
        if val != None:
            self.validate('current_count', val)
        self._current_count = val
    
    _destination_cluster_uuid = None
    @property
    def destination_cluster_uuid(self):
        """
        The UUID of the destination cluster.
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
        The name of the originating node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._originating_node
    @originating_node.setter
    def originating_node(self, val):
        if val != None:
            self.validate('originating_node', val)
        self._originating_node = val
    
    _time_to_live = None
    @property
    def time_to_live(self):
        """
        The Time to Live (remaining hops).
        Attributes: non-creatable, non-modifiable
        """
        return self._time_to_live
    @time_to_live.setter
    def time_to_live(self, val):
        if val != None:
            self.validate('time_to_live', val)
        self._time_to_live = val
    
    _destination_address = None
    @property
    def destination_address(self):
        """
        The active IP address of the node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_address
    @destination_address.setter
    def destination_address(self, val):
        if val != None:
            self.validate('destination_address', val)
        self._destination_address = val
    
    _timeout = None
    @property
    def timeout(self):
        """
        The timeout to use when pinging the peer cluster in
        seconds.
        Default: 15
        Attributes: non-creatable, non-modifiable
        """
        return self._timeout
    @timeout.setter
    def timeout(self, val):
        if val != None:
            self.validate('timeout', val)
        self._timeout = val
    
    _ping_status = None
    @property
    def ping_status(self):
        """
        The status of the ping operation.
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
        return self._ping_status
    @ping_status.setter
    def ping_status(self, val):
        if val != None:
            self.validate('ping_status', val)
        self._ping_status = val
    
    _round_trip = None
    @property
    def round_trip(self):
        """
        The roundtrip response time of ping operation in
        microseconds.
        Attributes: non-creatable, non-modifiable
        """
        return self._round_trip
    @round_trip.setter
    def round_trip(self, val):
        if val != None:
            self.validate('round_trip', val)
        self._round_trip = val
    
    _type = None
    @property
    def type(self):
        """
        The network protocol to use when performing the ping
        operation.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "data" - Data Ping,
        <li> "icmp" - ICMP Ping
        </ul>
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _destination_node = None
    @property
    def destination_node(self):
        """
        The name of the destination node.
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
        The name of the destination cluster.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_cluster
    @destination_cluster.setter
    def destination_cluster(self, val):
        if val != None:
            self.validate('destination_cluster', val)
        self._destination_cluster = val
    
    @staticmethod
    def get_api_name():
          return "cluster-peer-ping-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'count',
            'current-count',
            'destination-cluster-uuid',
            'originating-node',
            'time-to-live',
            'destination-address',
            'timeout',
            'ping-status',
            'round-trip',
            'type',
            'destination-node',
            'destination-cluster',
        ]
    
    def describe_properties(self):
        return {
            'count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'current_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_cluster_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'originating_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_to_live': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ping_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'round_trip': { 'class': int, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_cluster': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
