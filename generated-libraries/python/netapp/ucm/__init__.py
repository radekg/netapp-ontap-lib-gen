from netapp.connection import NaConnection
from ucm_adapter_get_iter_key_td import UcmAdapterGetIterKeyTd # 2 properties
from node_name import NodeName # 0 properties
from ucm_mode import UcmMode # 0 properties
from uc_adapter_info import UcAdapterInfo # 10 properties
from ucm_type import UcmType # 0 properties

class UcmConnection(NaConnection):
    
    def ucm_adapter_modify(self, adapter_name, fc4_type=None, node_name=None, mode=None):
        """
        Modify configuration of an adapter under the Unified Connect
        Management (UCM) framework, including the mode and/or the FC-4
        type.
        
        :param adapter_name: Slot name of adapter (e.g 0e)
        
        :param fc4_type: Modify the FC-4 type of the adapter. Possible values:
                <ul>
                <li> "initiator" - change FC-4 type to Initiator
                <li> "target"    - change FC-4 type to Target
                </ul>
        
        :param node_name: The name of the node where the adapter is installed.
                This is only needed in Cluster-Mode.
        
        :param mode: Modify the mode of the adapter. Possible values:
                <ul>
                <li> "fc"     - change mode to "Fibre Channel"
                <li> "cna"    - change mode to "CNA"
                </ul>
        """
        return self.request( "ucm-adapter-modify", {
            'fc4_type': [ fc4_type, 'fc4-type', [ basestring, 'ucm-type' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'node-name' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'ucm-mode' ], False ],
        }, {
        } )
    
    def ucm_adapter_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of UC Adapter objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the UC
                Adapter object.
                All UC Adapter objects matching this query up to 'max-records'
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
        return self.request( "ucm-adapter-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ UcAdapterInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UcAdapterInfo, 'None' ], False ],
        }, {
            'attributes-list': [ UcAdapterInfo, True ],
        } )
    
    def ucm_adapter_get(self, node_name, adapter_name, desired_attributes=None):
        """
        Get the attributes of the UC Adapter.
        
        :param node_name: Node
        
        :param adapter_name: Adapter
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ucm-adapter-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'node-name' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UcAdapterInfo, 'None' ], False ],
        }, {
            'attributes': [ UcAdapterInfo, False ],
        } )
    
    def ucm_adapter_list_info(self, adapter_name=None):
        """
        Report configuration for all available adapters under
        Unified Connect Management (UCM) framework.
        
        :param adapter_name: Slot name of adapter (e.g 0e). If no adapter is specified,
                information is returned for all adapters.
        """
        return self.request( "ucm-adapter-list-info", {
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
            'uc-adapters': [ UcAdapterInfo, True ],
        } )
