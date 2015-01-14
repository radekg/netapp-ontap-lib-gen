from netapp.connection import NaConnection
from fc_config import FcConfig # 6 properties
from fc_config_list_info_key_td import FcConfigListInfoKeyTd # 2 properties
from fc_config_info import FcConfigInfo # 5 properties

class FcConnection(NaConnection):
    
    def fc_config_list_iter_end(self, tag):
        """
        Terminate the fc-config-list iteration
        
        :param tag: Tag from a previous fc-config-list-iter-start.
        """
        return self.request( "fc-config-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def fc_config_list_info(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of fc objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the fc
                object.
                All fc objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "fc-config-list-info", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcConfig, 'None' ], False ],
        }, {
            'attributes-list': [ FcConfig, True ],
        } )
    
    def fc_config_adapter_disable(self, node_name, adapter_name):
        """
        Call the corresponding adapter driver disable function to bring
        the adapter offline. Under some circumstances an adapter
        can not be put offline. (e.g. when the adapter is being
        used by the RAID sub-system to provide disks in a volume).
        In some cases, manual intervention is required. When this
        happens, an appropriate error messages is returned.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system
                name the command will be executed on.
        
        :param adapter_name: FC adapter name (e.g. 0a)
        """
        return self.request( "fc-config-adapter-disable", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fc_config_list_iter_start(self):
        """
        Start iteration through the list of adapter configuration information.
        """
        return self.request( "fc-config-list-iter-start", {
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def fc_config_adapter_enable(self, node_name, adapter_name):
        """
        Call the corresponding adapter driver enable function to bring
        the adapter online. Under some circumstances an adapter
        can not be brought online. (e.g. when that adapter is in the UNCONFIGURED
        state, or when there is no cable attached to the adapter port).  When this
        happens, an appropriate error messages is returned.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system
                name the command will be executed on.
        
        :param adapter_name: FC adapter name (e.g 0a)
        """
        return self.request( "fc-config-adapter-enable", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fc_config_list_iter_next(self, tag, maximum):
        """
        Obtain a list of FC adapter configuration information.
        Only provides information for adapters that are configurable.
        
        :param tag: Tag from a previous fc-config-list-iter-start.
        
        :param maximum: Maximum number of entries to retrieve.
        """
        return self.request( "fc-config-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'adapter-info': [ FcConfigInfo, True ],
        } )
    
    def fc_config_set_adapter_fc_type(self, adapter_name, fc_type, node_name=None):
        """
        fc-config-set-adapter-fc-type changes the adapter driver
        and/or configuration state.  Each configurable adapter
        has an adapter-type and adapter-state.  The adapter-type
        indicates which driver is attached to the adapter, the
        adapter-state indicates what the configuration state of
        the adapter is. The fc-type is used to modify both the
        adapter-type and the adapter-state.
        After setting the adapter fc-type a filer reboot is
        sometimes needed to make the change effective.  Use
        fc-config-list-info to determine if a filer reboot is
        needed.
        
        :param adapter_name: FC adapter name (e.g 0a)
        
        :param fc_type: Sets the type and state of the adapter.  Possible inputs:<br>
                &nbsp; "unconfigured" - set adapter-type to "initiator" and adapter-state to UNCONFIGURED<br>
                &nbsp; "initiator"    - set adapter-type to "initiator" and adapter-state to CONFIGURED<br>
                &nbsp; "target"       - set adapter-type to "target" and adapter-state to CONFIGURED<br>
                &nbsp; "vi"           - set adapter-type to "vi" and adapter-state to CONFIGURED<br>
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system name
                the command will be executed on.
        """
        return self.request( "fc-config-set-adapter-fc-type", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
            'fc_type': [ fc_type, 'fc-type', [ basestring, 'None' ], False ],
        }, {
        } )
