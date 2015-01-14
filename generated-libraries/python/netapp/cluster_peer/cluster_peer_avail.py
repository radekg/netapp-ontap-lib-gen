class ClusterPeerAvail(basestring):
    """
    The availability of the peer cluster.
    Possible values:
    <ul>
    <li> "unavailable"   ,
    <li> "available"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cluster-peer-avail"
    
