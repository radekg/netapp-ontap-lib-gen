from netapp.netapp_object import NetAppObject

class ClusterPeerStableAddress(NetAppObject):
    """
    A list of stable IP addresses configured in a cluster peer
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
    
    _peer_addresses = None
    @property
    def peer_addresses(self):
        """
        The stable addresses of the peer cluster.
        Attributes: non-creatable, non-modifiable
        """
        return self._peer_addresses
    @peer_addresses.setter
    def peer_addresses(self, val):
        if val != None:
            self.validate('peer_addresses', val)
        self._peer_addresses = val
    
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
    
    @staticmethod
    def get_api_name():
          return "cluster-peer-stable-address"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'peer-addresses',
            'cluster-name',
        ]
    
    def describe_properties(self):
        return {
            'peer_addresses': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'cluster_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
