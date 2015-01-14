class VserverPeerState(basestring):
    """
    peered|pending|initializing|initiated|rejected|suspended|deleted
    Possible values:
    <ul>
    <li> "peered"        - Vserver peer relationship is
    established and the respective applications can use peer
    relationship,
    <li> "pending"       - Vserver peer relationship is initiated
    in the peer Cluster and local cluster needs to accept the
    request,
    <li> "initializing"  - Communicating to the peer cluster for
    initializing the peering relationship,
    <li> "initiated"     - Relationship initiated in local
    Cluster,
    <li> "rejected"      - Relationship initiated and peer Cluster
    rejected the same,
    <li> "suspended"     - Relationship got suspended, should not
    initiate any data transfers ,
    <li> "deleted"       - Relationship got deleted on peer
    Cluster
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vserver-peer-state"
    
