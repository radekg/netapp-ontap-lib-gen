from netapp.connection import NaConnection
from dummy_fcp_adapter_initiators_info import DummyFcpAdapterInitiatorsInfo # 2 properties
from dummy_fcp_get_iter_key_td import DummyFcpGetIterKeyTd # 4 properties
from dummy_portname_alias_list_info import DummyPortnameAliasListInfo # 2 properties
from dummy_fcp_connected_initiator_info import DummyFcpConnectedInitiatorInfo # 4 properties

class DummyfcpConnection(NaConnection):
    
    def dummy_fcp_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of dummy-fcp objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                dummy-fcp object.
                All dummy-fcp objects matching this query up to 'max-records'
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
        return self.request( "dummy-fcp-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DummyFcpAdapterInitiatorsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DummyFcpAdapterInitiatorsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DummyFcpAdapterInitiatorsInfo, True ],
        } )
    
    def dummy_fcp_adapter_initiators_list_info(self, dummy_fcp_adapter):
        """
        Get the attributes of the dummy-fcp.
        
        :param dummy_fcp_adapter: Adapter
        """
        return self.request( "dummy-fcp-adapter-initiators-list-info", {
            'dummy_fcp_adapter': [ dummy_fcp_adapter, 'dummy-fcp-adapter', [ basestring, 'None' ], False ],
        }, {
            'fcp-adapters': [ DummyFcpAdapterInitiatorsInfo, True ],
        } )
    
    def dummy_fcp_create(self, port_address, portname_alias_list, adapter, lif, vserver, node_name, port_name, initiator_group_list, return_record=None):
        """
        Create a new dummy-fcp.
        
        :param port_address: Port Address
        
        :param portname_alias_list: WWPN Alias
        
        :param adapter: Adapter
        
        :param lif: LIF
        
        :param vserver: Vserver Name
        
        :param node_name: Initiator WWNN
        
        :param port_name: Initiator WWPN
        
        :param initiator_group_list: Igroup Name
        
        :param return_record: If set to true, returns the dummy-fcp on successful creation.
                Default: false
        """
        return self.request( "dummy-fcp-create", {
            'port_address': [ port_address, 'port-address', [ int, 'None' ], False ],
            'portname_alias_list': [ portname_alias_list, 'portname-alias-list', [ basestring, 'None' ], False ],
            'adapter': [ adapter, 'adapter', [ basestring, 'None' ], False ],
            'lif': [ lif, 'lif', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'port_name': [ port_name, 'port-name', [ basestring, 'None' ], False ],
            'initiator_group_list': [ initiator_group_list, 'initiator-group-list', [ NtdtestInfo, 'None' ], True ],
        }, {
            'result': [ DummyFcpAdapterInitiatorsInfo, False ],
        } )
    
    def dummy_fcp_destroy(self, vserver, adapter, port_address, lif):
        """
        Delete an existing dummy-fcp object.
        
        :param vserver: Vserver Name
        
        :param adapter: Adapter
        
        :param port_address: Port Address
        
        :param lif: LIF
        """
        return self.request( "dummy-fcp-destroy", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'adapter': [ adapter, 'adapter', [ basestring, 'None' ], False ],
            'port_address': [ port_address, 'port-address', [ int, 'None' ], False ],
            'lif': [ lif, 'lif', [ basestring, 'None' ], False ],
        }, {
        } )
