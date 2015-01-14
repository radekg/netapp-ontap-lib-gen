from netapp.connection import NaConnection
from peer_ping_protocol import PeerPingProtocol # 0 properties
from cluster_peer_avail import ClusterPeerAvail # 0 properties
from cluster_peer_active_address import ClusterPeerActiveAddress # 2 properties
from cluster_peer_health_info import ClusterPeerHealthInfo # 10 properties
from peer_ping_status import PeerPingStatus # 0 properties
from cluster_peer_info import ClusterPeerInfo # 8 properties
from cluster_peer_ping_iter_key_td import ClusterPeerPingIterKeyTd # 6 properties
from cluster_peer_ping_info import ClusterPeerPingInfo # 12 properties
from cluster_peer_get_iter_key_td import ClusterPeerGetIterKeyTd # 1 properties
from cluster_peer_stable_address import ClusterPeerStableAddress # 2 properties
from cluster_peer_health_info_get_iter_key_td import ClusterPeerHealthInfoGetIterKeyTd # 3 properties

class ClusterPeerConnection(NaConnection):
    
    def cluster_peer_active_addresses_get(self, cluster_name, desired_attributes=None):
        """
        Get the list of active IP Addresses for the specified peer
        cluster.
        
        :param cluster_name: The name of the peer cluster.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-active-addresses-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerActiveAddress, 'None' ], False ],
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'cluster-name' ], False ],
        }, {
            'attributes': [ ClusterPeerActiveAddress, False ],
        } )
    
    def cluster_peer_create(self, peer_addresses, user_name=None, password=None, timeout=None):
        """
        Create a cluster peer relationship
        
        :param peer_addresses: The remote intercluster addresses and hostnames of the peer
                cluster.
        
        :param user_name: The user name required to authenticate with the peer cluster.
                This value is only used at peer creation time and not stored.
        
        :param password: The password required to authenticate with the peer cluster. This
                value is only used at peer creation time and not stored.
        
        :param timeout: The timeout for operations in the peer cluster in seconds.
                Default: 15
        """
        return self.request( "cluster-peer-create", {
            'peer_addresses': [ peer_addresses, 'peer-addresses', [ basestring, 'remote-inet-address' ], True ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
            'timeout': [ timeout, 'timeout', [ int, 'None' ], False ],
        }, {
        } )
    
    def cluster_peer_ping_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Ping the specified peer nodes.
        Ping operations take place between a node in a cluster and
        a node in a remote cluster.  The originating node is the
        node which initiates the ping operation and the destination
        cluster and node specify the remote node which is the
        target of the ping.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cluster-peer-ping object.
                All cluster-peer-ping objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-ping-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ClusterPeerPingInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerPingInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ClusterPeerPingInfo, True ],
        } )
    
    def cluster_peer_modify(self, cluster_name, peer_addresses=None, timeout=None):
        """
        Modifies a cluster peer relationship
        
        :param cluster_name: The name of the peer cluster to modify.
        
        :param peer_addresses: The Remote IP address or host name of the peer cluster.  If not
                specified, the peer-addresses are not modified.
        
        :param timeout: The timeout for operations in the peer cluster in seconds.  If
                not specified, the timeout is not modified.
        """
        return self.request( "cluster-peer-modify", {
            'peer_addresses': [ peer_addresses, 'peer-addresses', [ basestring, 'remote-inet-address' ], True ],
            'timeout': [ timeout, 'timeout', [ int, 'None' ], False ],
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cluster_peer_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns a list of cluster peer relationships
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cluster-peer object.
                All cluster-peer objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ClusterPeerInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ClusterPeerInfo, True ],
        } )
    
    def cluster_peer_stable_addresses_register(self):
        """
        Register cluster stable IP addresses.
        """
        return self.request( "cluster-peer-stable-addresses-register", {
        }, {
        } )
    
    def cluster_peer_stable_addresses_get(self, cluster_name, desired_attributes=None):
        """
        Get the list of stable IP Addresses for the specified peer
        cluster.
        
        :param cluster_name: The name of the peer cluster.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-stable-addresses-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerStableAddress, 'None' ], False ],
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'cluster-name' ], False ],
        }, {
            'attributes': [ ClusterPeerStableAddress, False ],
        } )
    
    def cluster_peer_active_addresses_register(self):
        """
        Register active IP addresses for the specified cluster.
        Registering addresses forces the local cluster to update its
        internal peer IP address mappings to reflect the current set of
        active addresses.
        """
        return self.request( "cluster-peer-active-addresses-register", {
        }, {
        } )
    
    def cluster_peer_health_info_get(self, originating_node, destination_node, destination_cluster, desired_attributes=None):
        """
        Get the health of the specified peer node
        
        :param originating_node: The name of the local node.
        
        :param destination_node: The name of the node in the peer cluster.
        
        :param destination_cluster: The name of the peer cluster.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-health-info-get", {
            'originating_node': [ originating_node, 'originating-node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerHealthInfo, 'None' ], False ],
            'destination_node': [ destination_node, 'destination-node', [ basestring, 'peer-node-name' ], False ],
            'destination_cluster': [ destination_cluster, 'destination-cluster', [ basestring, 'cluster-name' ], False ],
        }, {
            'attributes': [ ClusterPeerHealthInfo, False ],
        } )
    
    def cluster_peer_active_address_insert(self, cluster_name, active_address):
        """
        Insert an active IP address for the specified cluster
        
        :param cluster_name: The name of the peer cluster.
        
        :param active_address: Active IP Address To Insert
        """
        return self.request( "cluster-peer-active-address-insert", {
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'cluster-name' ], False ],
            'active_address': [ active_address, 'active-address', [ basestring, 'remote-inet-address' ], False ],
        }, {
        } )
    
    def cluster_peer_health_info_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the health of all local and peer nodes sequentially
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cluster-peer object.
                All cluster-peer objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-health-info-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ClusterPeerHealthInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerHealthInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ClusterPeerHealthInfo, True ],
        } )
    
    def cluster_peer_delete(self, cluster_name):
        """
        Delete a cluster peer relationship
        
        :param cluster_name: The name of the peer cluster.
        """
        return self.request( "cluster-peer-delete", {
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cluster_peer_get(self, cluster_name, desired_attributes=None):
        """
        Return the specified peer cluster relationship information
        
        :param cluster_name: The name of the peer cluster.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-peer-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterPeerInfo, 'None' ], False ],
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ ClusterPeerInfo, False ],
        } )
