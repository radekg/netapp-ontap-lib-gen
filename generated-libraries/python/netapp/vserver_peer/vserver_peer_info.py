from netapp.netapp_object import NetAppObject

class VserverPeerInfo(NetAppObject):
    """
    Contains information about the Vserver peer relationship(s).
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
        Specifies name of the local Vserver in the relationship
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _peer_vserver = None
    @property
    def peer_vserver(self):
        """
        Specifies name of the peer Vserver in the relationship
        Attributes: key, non-creatable, non-modifiable
        """
        return self._peer_vserver
    @peer_vserver.setter
    def peer_vserver(self, val):
        if val != None:
            self.validate('peer_vserver', val)
        self._peer_vserver = val
    
    _peer_cluster = None
    @property
    def peer_cluster(self):
        """
        Specifies name of the peer Cluster. If peer Cluster is
        not given, it considers local Cluster. This value is not
        shown  and cannot be set in desired-attributes when the
        API is issued on Vserver LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._peer_cluster
    @peer_cluster.setter
    def peer_cluster(self, val):
        if val != None:
            self.validate('peer_cluster', val)
        self._peer_cluster = val
    
    _peer_state = None
    @property
    def peer_state(self):
        """
        State of the Vserver peer relationship
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "peered"         - Vserver peer relationship is
        established and the respective applications can use peer
        relationship,
        <li> "pending"        - Vserver peer relationship is
        initiated in the peer Cluster and local cluster needs to
        accept the request,
        <li> "initializing"   - Communicating to the peer
        cluster for initializing the peering relationship,
        <li> "initiated"      - Relationship initiated in local
        Cluster,
        <li> "rejected"       - Relationship initiated and peer
        Cluster rejected the same,
        <li> "suspended"      - Relationship got suspended,
        should not initiate any data transfers ,
        <li> "deleted"        - Relationship got deleted on
        peer Cluster
        </ul>
        """
        return self._peer_state
    @peer_state.setter
    def peer_state(self, val):
        if val != None:
            self.validate('peer_state', val)
        self._peer_state = val
    
    _applications = None
    @property
    def applications(self):
        """
        Applications which can make use of the peering
        relationship. This value is not shown and cannot be set
        in desired-attributes when the API is issued on Vserver
        LIF.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "snapmirror"
        </ul>
        """
        return self._applications
    @applications.setter
    def applications(self, val):
        if val != None:
            self.validate('applications', val)
        self._applications = val
    
    @staticmethod
    def get_api_name():
          return "vserver-peer-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'peer-vserver',
            'peer-cluster',
            'peer-state',
            'applications',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'peer_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'peer_cluster': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'peer_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'applications': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
