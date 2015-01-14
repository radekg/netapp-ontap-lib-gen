from netapp.connection import NaConnection
from vserver_peer_transition_destroy_iter_key_td import VserverPeerTransitionDestroyIterKeyTd # 2 properties
from vserver_peer_transition_get_iter_key_td import VserverPeerTransitionGetIterKeyTd # 2 properties
from vserver_peer_transition_destroy_iter_info import VserverPeerTransitionDestroyIterInfo # 3 properties
from vserver_name import VserverName # 0 properties
from vserver_peer_transition_info import VserverPeerTransitionInfo # 3 properties

class VserverPeerTransitionConnection(NaConnection):
    
    def vserver_peer_transition_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Gets list of transition peer relationship.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vserver-peer-transition object.
                All vserver-peer-transition objects matching this query up to
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
        return self.request( "vserver-peer-transition-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VserverPeerTransitionInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverPeerTransitionInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VserverPeerTransitionInfo, True ],
        } )
    
    def vserver_peer_transition_get(self, local_vserver, src_filer_name, desired_attributes=None):
        """
        Gets a transition peer relationship.
        
        :param local_vserver: Local Vserver name
        
        :param src_filer_name: Source 7-Mode system
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "vserver-peer-transition-get", {
            'local_vserver': [ local_vserver, 'local-vserver', [ basestring, 'vserver-name' ], False ],
            'src_filer_name': [ src_filer_name, 'src-filer-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverPeerTransitionInfo, 'None' ], False ],
        }, {
            'attributes': [ VserverPeerTransitionInfo, False ],
        } )
    
    def vserver_peer_transition_modify(self, local_vserver, src_filer_name, multi_path_address=None):
        """
        Modifies a transition peer relationship
        
        :param local_vserver: Local Vserver name
        
        :param src_filer_name: Source 7-Mode system
        
        :param multi_path_address: Additional address for source 7-Mode system
        """
        return self.request( "vserver-peer-transition-modify", {
            'local_vserver': [ local_vserver, 'local-vserver', [ basestring, 'vserver-name' ], False ],
            'src_filer_name': [ src_filer_name, 'src-filer-name', [ basestring, 'None' ], False ],
            'multi_path_address': [ multi_path_address, 'multi-path-address', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_peer_transition_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Deletes multiple transition peer relationship
        
        :param query: If deleting a specific vserver-peer-transition, this input
                element must specify all keys.
                If deleting multiple vserver-peer-transition objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                vserver-peer-transition even when the deletion of a previous
                matching vserver-peer-transition fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of vserver-peer-transition objects to delete
                in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                vserver-peer-transition objects (just keys) that were
                successfully deleted.
                If set to false, the list of vserver-peer-transition objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple
                vserver-peer-transition objects match a given query.
                If set to true, the API will continue deleting the next matching
                vserver-peer-transition even when the deletion of a previous
                vserver-peer-transition fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                vserver-peer-transition objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of vserver-peer-transition objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "vserver-peer-transition-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ VserverPeerTransitionInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ VserverPeerTransitionDestroyIterInfo, True ],
            'failure-list': [ VserverPeerTransitionDestroyIterInfo, True ],
        } )
    
    def vserver_peer_transition_create(self, local_vserver, src_filer_name, multi_path_address=None, return_record=None):
        """
        Create a new transition peer relationship between	a Data ONTAP
        7-Mode system and a Data ONTAP Cluster-Mode Vserver
        
        :param local_vserver: Local Vserver name
        
        :param src_filer_name: Source 7-Mode system
        
        :param multi_path_address: Additional address for source 7-Mode system
        
        :param return_record: If set to true, returns the vserver-peer-transition on successful
                creation.
                Default: false
        """
        return self.request( "vserver-peer-transition-create", {
            'local_vserver': [ local_vserver, 'local-vserver', [ basestring, 'vserver-name' ], False ],
            'src_filer_name': [ src_filer_name, 'src-filer-name', [ basestring, 'None' ], False ],
            'multi_path_address': [ multi_path_address, 'multi-path-address', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ VserverPeerTransitionInfo, False ],
        } )
    
    def vserver_peer_transition_destroy(self, local_vserver, src_filer_name):
        """
        Deletes a transition peer relationship
        
        :param local_vserver: Local Vserver name
        
        :param src_filer_name: Source 7-Mode system
        """
        return self.request( "vserver-peer-transition-destroy", {
            'local_vserver': [ local_vserver, 'local-vserver', [ basestring, 'vserver-name' ], False ],
            'src_filer_name': [ src_filer_name, 'src-filer-name', [ basestring, 'None' ], False ],
        }, {
        } )
