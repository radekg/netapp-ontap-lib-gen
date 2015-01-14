from netapp.connection import NaConnection
from cluster_application_record_info import ClusterApplicationRecordInfo # 4 properties
from cluster_identity_info import ClusterIdentityInfo # 6 properties
from license_code_v2 import LicenseCodeV2 # 0 properties
from cluster_node_info import ClusterNodeInfo # 5 properties
from cluster_node_get_iter_key_td import ClusterNodeGetIterKeyTd # 1 properties
from cluster_application_record_get_iter_key_td import ClusterApplicationRecordGetIterKeyTd # 1 properties
from cluster_ha_info import ClusterHaInfo # 1 properties
from cluster_create_join_progress_info import ClusterCreateJoinProgressInfo # 2 properties

class ClusterConnection(NaConnection):
    
    def cluster_identity_get(self, desired_attributes=None):
        """
        Returns the cluster identity information.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-identity-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterIdentityInfo, 'None' ], False ],
        }, {
            'attributes': [ ClusterIdentityInfo, False ],
        } )
    
    def cluster_application_record_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return rows of the application-record table
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cluster object.
                All cluster objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "cluster-application-record-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ClusterApplicationRecordInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterApplicationRecordInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ClusterApplicationRecordInfo, True ],
        } )
    
    def cluster_ha_get(self, desired_attributes=None):
        """
        Returns cluster HA configuration - For NetApp internal use only
        and is unsupported as this feature and zapi are expected to be
        incompatible with a future release.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-ha-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterHaInfo, 'None' ], False ],
        }, {
            'attributes': [ ClusterHaInfo, False ],
        } )
    
    def cluster_join(self, cluster_ip_address):
        """
        Start the process to join this node to a cluster.  Use
        cluster-create-join-progress-get to track the status of the
        operation.
        
        :param cluster_ip_address: IP Address of a cluster interface from a node in the cluster
        """
        return self.request( "cluster-join", {
            'cluster_ip_address': [ cluster_ip_address, 'cluster-ip-address', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def cluster_node_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about nodes in a cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cluster object.
                All cluster objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "cluster-node-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ClusterNodeInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterNodeInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ClusterNodeInfo, True ],
        } )
    
    def cluster_application_record_delete(self, record_name):
        """
        Deletes a row of the application-record table
        
        :param record_name: The name of the record key to set the value.
        """
        return self.request( "cluster-application-record-delete", {
            'record_name': [ record_name, 'record-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cluster_create_join_progress_get(self, desired_attributes=None):
        """
        Once the cluster-create or cluster-join operation has been
        started on this node, use this ZAPI to get the current status of
        the operation.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-create-join-progress-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterCreateJoinProgressInfo, 'None' ], False ],
        }, {
            'attributes': [ ClusterCreateJoinProgressInfo, False ],
        } )
    
    def cluster_create(self, cluster_name, license):
        """
        Start the process to create a cluster using this node.  Use
        cluster-create-join-progress-get to track the status of the
        operation.
        
        :param cluster_name: Use this parameter to specify the name of the cluster you are
                creating. The cluster name must begin with a letter and cannot be
                more than 44 characters in length.
        
        :param license: The base cluster license obtain with the hardware or from NetApp
                professional services.
        """
        return self.request( "cluster-create", {
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'None' ], False ],
            'license': [ license, 'license', [ basestring, 'license-code-v2' ], False ],
        }, {
        } )
    
    def cluster_identity_modify(self, cluster_location=None, cluster_contact=None, cluster_name=None):
        """
        Modifies the cluster identity information.
        
        :param cluster_location: The location of the cluster
        
        :param cluster_contact: The contact information for the cluster
        
        :param cluster_name: The textual name of the cluster
        """
        return self.request( "cluster-identity-modify", {
            'cluster_location': [ cluster_location, 'cluster-location', [ basestring, 'None' ], False ],
            'cluster_contact': [ cluster_contact, 'cluster-contact', [ basestring, 'None' ], False ],
            'cluster_name': [ cluster_name, 'cluster-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cluster_application_record_create(self, record_name, record_value, return_record=None):
        """
        Creates a row of the application-record table
        
        :param record_name: The name of the record key to set the value.
        
        :param record_value: The value for the record key.
        
        :param return_record: If set to true, returns the cluster on successful creation.
                Default: false
        """
        return self.request( "cluster-application-record-create", {
            'record_name': [ record_name, 'record-name', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'record_value': [ record_value, 'record-value', [ basestring, 'None' ], False ],
        }, {
            'result': [ ClusterApplicationRecordInfo, False ],
        } )
    
    def cluster_application_record_modify(self, record_name, record_value=None):
        """
        Modifies a row of the application-record table
        
        :param record_name: The name of the record key to set the value.
        
        :param record_value: The value for the record key.
        """
        return self.request( "cluster-application-record-modify", {
            'record_name': [ record_name, 'record-name', [ basestring, 'None' ], False ],
            'record_value': [ record_value, 'record-value', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cluster_node_get(self, node_name, desired_attributes=None):
        """
        Returns information about a node in a cluster.
        
        :param node_name: The textual name of a node.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-node-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterNodeInfo, 'None' ], False ],
        }, {
            'attributes': [ ClusterNodeInfo, False ],
        } )
    
    def cluster_node_modify(self, node_name, is_node_eligible=None, is_node_epsilon=None):
        """
        Modifies state of a node in a cluster.
        
        :param node_name: The textual name of a node.
        
        :param is_node_eligible: This parameter states nodes that are eligible to participate in
                the cluster. A boolean value of true means the node is eligible.
        
        :param is_node_epsilon: You can designate a node as epsilon to add weight to its voting
                in a cluster with an even number of nodes. In a cluster, only one
                node can be designated as epsilon at any given time. A boolean
                value of true means the node is epsilon.
        """
        return self.request( "cluster-node-modify", {
            'is_node_eligible': [ is_node_eligible, 'is-node-eligible', [ bool, 'None' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'node-name' ], False ],
            'is_node_epsilon': [ is_node_epsilon, 'is-node-epsilon', [ bool, 'None' ], False ],
        }, {
        } )
