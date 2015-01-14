from netapp.connection import NaConnection
from vserver_peer_info import VserverPeerInfo # 5 properties
from vserver_peer_get_iter_key_td import VserverPeerGetIterKeyTd # 2 properties
from vserver_peer_state import VserverPeerState # 0 properties
from vserver_peer_application import VserverPeerApplication # 0 properties

class VserverPeerConnection(NaConnection):
    
    def vserver_peer_create(self, vserver, peer_vserver, applications, peer_cluster=None):
        """
        Create a new Vserver peer relationship between two existing
        Vservers
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param applications: Applications which can make use of the peering relationship.
                Possible value: 'snapmirror'.
        
        :param peer_cluster: Specifies name of the peer Cluster. If peer Cluster is not given,
                it considers local Cluster.
        """
        return self.request( "vserver-peer-create", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'peer_cluster': [ peer_cluster, 'peer-cluster', [ basestring, 'None' ], False ],
            'applications': [ applications, 'applications', [ basestring, 'vserver-peer-application' ], True ],
        }, {
        } )
    
    def vserver_peer_suspend(self, vserver, peer_vserver, force=None):
        """
        Suspend a Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param force: Force Suspend
        """
        return self.request( "vserver-peer-suspend", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def vserver_peer_accept(self, vserver, peer_vserver):
        """
        Accept a pending Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        """
        return self.request( "vserver-peer-accept", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_peer_resume(self, vserver, peer_vserver, force=None):
        """
        Resume a Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param force: Force Resume
        """
        return self.request( "vserver-peer-resume", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def vserver_peer_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display information about Vserver peer relationships. If the API
        is issued to the Cluster LIF, then information about all Vservers
        is shown. If the request is sent to the Vserver LIF, then
        information about that Vserver is shown.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vserver-peer object.
                All vserver-peer objects matching this query up to 'max-records'
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
        return self.request( "vserver-peer-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VserverPeerInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverPeerInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VserverPeerInfo, True ],
        } )
    
    def vserver_peer_reject(self, vserver, peer_vserver):
        """
        Reject a Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        """
        return self.request( "vserver-peer-reject", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_peer_get(self, peer_vserver, desired_attributes=None):
        """
        Display information about Vserver peer relationships. Displays
        the local Vserver, peer Vserver and the state of the peering
        relationship.
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "vserver-peer-get", {
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverPeerInfo, 'None' ], False ],
        }, {
            'attributes': [ VserverPeerInfo, False ],
        } )
    
    def vserver_peer_modify(self, vserver, peer_vserver, applications):
        """
        Modify a Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param applications: Applications which can make use of the peering relationship.
                Possible value: 'snapmirror'.
        """
        return self.request( "vserver-peer-modify", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'applications': [ applications, 'applications', [ basestring, 'vserver-peer-application' ], True ],
        }, {
        } )
    
    def vserver_peer_delete(self, vserver, peer_vserver, force=None):
        """
        Delete a Vserver peer relationship
        
        :param vserver: Specifies name of the local Vserver in the relationship
        
        :param peer_vserver: Specifies name of the peer Vserver in the relationship
        
        :param force: Force Delete
        """
        return self.request( "vserver-peer-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'peer_vserver': [ peer_vserver, 'peer-vserver', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
