from netapp.connection import NaConnection
from fcp_adapter_nameserver_object_info import FcpAdapterNameserverObjectInfo # 10 properties
from fcp_service_get_iter_key_td import FcpServiceGetIterKeyTd # 1 properties
from fcp_connected_initiator_info import FcpConnectedInitiatorInfo # 5 properties
from fcp_adapter_topology_switch_info import FcpAdapterTopologySwitchInfo # 8 properties
from fcp_adapter_zone_member_info import FcpAdapterZoneMemberInfo # 8 properties
from fcp_service_info import FcpServiceInfo # 3 properties
from fcp_adapter_zone_info import FcpAdapterZoneInfo # 4 properties
from fcp_interface_get_iter_key_td import FcpInterfaceGetIterKeyTd # 2 properties
from fcp_port_name_info import FcpPortNameInfo # 4 properties
from fcp_initiator_get_iter_key_td import FcpInitiatorGetIterKeyTd # 3 properties
from aliases_info import AliasesInfo # 3 properties
from fcp_config_adapter_info import FcpConfigAdapterInfo # 36 properties
from fcp_wwpnalias_get_iter_key_td import FcpWwpnaliasGetIterKeyTd # 2 properties
from fcp_connection import FcpConnection # 0 properties
from fcp_adapter_get_iter_key_td import FcpAdapterGetIterKeyTd # 2 properties
from fcp_adapter_topology_attached_port_info import FcpAdapterTopologyAttachedPortInfo # 3 properties
from fcp_adapter_topology_switch_port_info import FcpAdapterTopologySwitchPortInfo # 5 properties
from fcp_interface_info import FcpInterfaceInfo # 8 properties
from fcp_adapter_stats_get_iter_key_td import FcpAdapterStatsGetIterKeyTd # 2 properties
from fcp_adapter_stats_info import FcpAdapterStatsInfo # 37 properties
from fcp_adapter_initiators_info import FcpAdapterInitiatorsInfo # 3 properties
from fcp_adapter_speed import FcpAdapterSpeed # 0 properties
from portname_alias_name import PortnameAliasName # 1 properties
from fcp_port_name_get_iter_key_td import FcpPortNameGetIterKeyTd # 2 properties

class FcpConnection(NaConnection):
    
    def fcp_wwpnalias_remove(self, wwpn=None, alias=None):
        """
        Remove an alias for a World Wide Port Name of an
        initiator. Either the alias or the wwpn argument must
        be provided.
        
        :param wwpn: WWPN for which all aliases are to be removed. Either
                the wwpn or the alias argument must be provided.
        
        :param alias: WWPN Alias to be removed. Either the alias or the wwpn
                argument must be provided.
        """
        return self.request( "fcp-wwpnalias-remove", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'alias': [ alias, 'alias', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_service_start(self):
        """
        Starts FCP service. When FCP service is started, the
        adapters are brought online.  Service will be avaliable once
        the call returns with success.  The adapters however, may
        not be available immediately after the call, it may take
        up to a few seconds for the adapters to initialize.
        """
        return self.request( "fcp-service-start", {
        }, {
        } )
    
    def fcp_get_cfmode(self):
        """
        Get the current cfmode setting for the system.
        """
        return self.request( "fcp-get-cfmode", {
        }, {
            'fcp-cfmode': [ basestring, False ],
        } )
    
    def fcp_wwpnalias_get_alias_info(self, wwpn=None, alias=None):
        """
        Get the list of WWPN for a given alias or an alias for
        for a given WWPN or complete list of all current alias-
        WWPN mappings.
        
        :param wwpn: WWPN for which all aliases will be returned. When
                supplied all aliases for that WWPN will be returned.
                Otherwise, all aliases with their WWPNs present in the
                system will be returned.
        
        :param alias: Alias for a WWPN is the 32-character alias that may
                contain A-Z, a-z, 0-9, _,-,.,{,} and no spaces. When
                supplied, the alias with the corresponding WWPN will be
                returned. Otherwise, all aliases with their WWPNs
                present in the system will be returned.
        """
        return self.request( "fcp-wwpnalias-get-alias-info", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'alias': [ alias, 'alias', [ basestring, 'None' ], False ],
        }, {
            'aliases': [ AliasesInfo, True ],
        } )
    
    def fcp_adapter_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of physical FC adapters.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the FC
                Adapter object.
                All FC Adapter objects matching this query up to 'max-records'
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
        return self.request( "fcp-adapter-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpConfigAdapterInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpConfigAdapterInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpConfigAdapterInfo, True ],
        } )
    
    def fcp_adapter_nameserver_list_iter_start(self, fcp_adapter=None, zoned=None):
        """
        Get the fabric nameserver objects the results of which are
        retreived by using fcp-adapter-nameserver-list-iter-next.
        Connectivity of adapters running on behalf of partners
        are not included in the list when requesting for
        all adapters.  If listing for all adapters and an
        error occurs while retrieving connection status
        for an adapter, status for that adapter will not be
        returned and the API will continue on with the rest
        of the adapters without erroring out.  You can get the
        error msg for that adapter, by specifically specifying
        that adapter.
        
        :param fcp_adapter: Adapter to get nameserver objects for.  If no adapter is
                specified, information is returned for all fcp adapter.
        
        :param zoned: If true, returns only devices that are zoned to the target
                adapter. Otherwise, all devices in the fabric are returned.
                Default is false.
        """
        return self.request( "fcp-adapter-nameserver-list-iter-start", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'zoned': [ zoned, 'zoned', [ bool, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def fcp_adapter_nameserver_list_iter_next(self, tag, maximum):
        """
        Return items from a previous call to
        fcp-adapter-nameserver-list-iter-start
        Information returned for each nameserver entry include the
        port identifier, port type, port name, node name, symbolic
        port name, symbolic node name, fabric port name, class of
        service, and registered FC4 types.
        
        :param tag: Tag from a previous fcp-adapter-nameserver-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "fcp-adapter-nameserver-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'fcp-adapter-nameserver-objects': [ FcpAdapterNameserverObjectInfo, True ],
        } )
    
    def fcp_port_name_set(self, fcp_adapter, port_name):
        """
        Set a valid but unused port name on a Fibre Channel
        target interface.
        
        :param fcp_adapter: FCP target interface to set the WWPN on.
                In Data ONTAP 7-Mode, the name of a local adapter in standby
                single_image cfmode.
                In Data ONTAP Cluster-Mode, the name of an FCP data LIF in
                the vserver.
        
        :param port_name: WWPN to be set on the interface. It has to be a valid
                and unused one.
        """
        return self.request( "fcp-port-name-set", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'port_name': [ port_name, 'port-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_stats_list_info(self, fcp_adapter=None):
        """
        Get statistics about the Fibre Channel target adapters.
        Statistics of adapters running on behalf of partners
        are not included in the list when requesting stats for
        all adapters.  If listing stats for all adapters and an
        error occurred for while retrieving stats for an adapter,
        stats for that adapter will not be returned, and
        the API will continue on with the rest of the adapters
        without erroring out.  You can get the error msg for that
        adapter, by specifically specifying that adapter.
        
        :param fcp_adapter: FC target Adapter.  If no adapter is specified, stats for
                all adapters are retruned.
        """
        return self.request( "fcp-adapter-stats-list-info", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
            'fcp-adapter-stats': [ FcpAdapterStatsInfo, True ],
        } )
    
    def fcp_adapter_config_up(self, node, fcp_adapter):
        """
        Bring a Fibre Channel target adapter online.
        The adapter may not be online immediately after the
        call returns, it may take up to a few seconds for the
        adapter to initialize.
        In Data ONTAP 7-Mode, if the FCP service is not running
        then all adapters are automatically offlined. They cannot
        be brought online again until FCP service is started.
        In Data ONTAP Cluster-Mode, offlining an adapter will
        operationally disable all FCP logical interfaces (LIFs)
        hosted by the adapter.
        
        :param node: The name of the storage system node where the adapter is installed.
        
        :param fcp_adapter: FC adapter to bring online.
        """
        return self.request( "fcp-adapter-config-up", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_clear_partner(self, fcp_adapter):
        """
        Removes the name of the partner adapter which the local
        adapter should takeover. Partner adapter setting is obsolete
        and this operation is no longer supported.
        
        :param fcp_adapter: Local FC adapter.
        """
        return self.request( "fcp-adapter-clear-partner", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_nameserver_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous fcp-adapter-nameserver-list-iter-start.
        """
        return self.request( "fcp-adapter-nameserver-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def fcp_adapter_zone_list_iter_start(self, fcp_adapter=None):
        """
        Get the active zone set information from the zone server.
        The results can then be retreived by using
        fcp-adapter-zone-list-iter-next.
        Connectivity of adapters running on behalf of partners
        is not included in the list when requesting for
        all adapters.  If listing for all adapters and an
        error occurs while retrieving connection status
        for an adapter, status for that adapter will not be
        returned and the API will continue on with the rest
        of the adapters without erroring out.  You can get the
        error msg for that adapter, by specifically specifying
        that adapter.
        
        :param fcp_adapter: Adapter to get zone information for.  If no adapter is
                specified, information is returned for all fcp adapter.
        """
        return self.request( "fcp-adapter-zone-list-iter-start", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def fcp_port_name_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of valid Fibre Channel target port names on
        a Vserver's FCP LIFs.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Fibre Channel target port name object.
                All Fibre Channel target port name objects matching this query up
                to 'max-records' will be returned.
        
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
        return self.request( "fcp-port-name-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpPortNameInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpPortNameInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpPortNameInfo, True ],
        } )
    
    def fcp_adapter_zone_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous fcp-adapter-zone-list-iter-start.
        """
        return self.request( "fcp-adapter-zone-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def fcp_adapter_topology_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous fcp-adapter-topology-list-iter-start.
        """
        return self.request( "fcp-adapter-topology-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def fcp_adapter_topology_list_iter_next(self, tag, maximum):
        """
        Return items from a previous call to
        fcp-adapter-topology-list-iter-start
        Information returned for each switch includes the nodename,
        logical name, domain identifier, vendor, release version, and
        port information. If a port has devices attached to it, then
        information about each attached device is included as well.
        
        :param tag: Tag from a previous fcp-adapter-topology-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "fcp-adapter-topology-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'fcp-adapter-topology-switches': [ FcpAdapterTopologySwitchInfo, True ],
        } )
    
    def fcp_wwpnalias_set(self, wwpn, alias, force=None):
        """
        Set an alias for a World Wide Port Name of an initiator
        that might login to the target.
        
        :param wwpn: WWPN for which alias is being set
        
        :param alias: Alias to be set for the given WWPN ("wwpn");
                The alias can be 32-characters long and may contain:
                A-Z, a-z, 0-9, _,-,.,{,} and no spaces
        
        :param force: When set to true, the WWPN associated with the alias
                will be over-written. Default value is false.
        """
        return self.request( "fcp-wwpnalias-set", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'alias': [ alias, 'alias', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fcp_ping_info(self, port_id_or_wwpn, fcp_adapter, ping_count=None, payload=None):
        """
        Send an ELS ECHO frame to a Fibre Channel address or WWPN. The
        API pings the address or WWPN count times and returns the
        number of successful pings and times. EHOSTNOTFOUND is returned
        if the WWPN cannot be resolved. EONTAPI_EHOSTDOWN is returned if
        the address cannot be pinged. The interval between ping attempts
        is 1 second.
        
        :param port_id_or_wwpn: The Fibre Channel address or the WWPN to ping. The format of
                a Fibre channel address is a hexadecimal or numeric value with
                the range [0..2^24-1]. The format of a WWPN is
                XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal digit.
        
        :param fcp_adapter: Adapter to send the ping request from.
        
        :param ping_count: The number of pings.  Default is 3.
                Range: [1..16]
        
        :param payload: Additional data to send in the payload of the ELS ECHO frame.
                The payload can be up to 248 characters long.
        """
        return self.request( "fcp-ping-info", {
            'ping_count': [ ping_count, 'ping-count', [ int, 'None' ], False ],
            'port_id_or_wwpn': [ port_id_or_wwpn, 'port-id-or-wwpn', [ basestring, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'payload': [ payload, 'payload', [ basestring, 'None' ], False ],
        }, {
            'frames-transmitted': [ int, False ],
            'frames-received': [ int, False ],
            'round-trip-maximum-time': [ int, False ],
            'round-trip-mean-time': [ int, False ],
            'round-trip-minimum-time': [ int, False ],
        } )
    
    def fcp_adapter_set_speed(self, node, fcp_adapter, speed):
        """
        Sets the speed on the Fibre Channel target adapter.
        It can be configured to run at 1Gb, 2Gb, 4Gb, 8Gb, 10Gb,
        16Gb or to auto negotiate. The 10Gb adapter only supports the
        10Gb speed. The 16Gb adapter only supports speeds of 16Gb, 8Gb,
        and 4Gb. The 8Gb adapter only supports speeds of 8Gb, 4Gb, and
        2Gb. The 4Gb adapter only supports speeds of 4Gb, 2Gb, and 1Gb.
        If the adapter is online it must be brought offline
        before setting the speed, and then online in order
        for a new speed to take effect.
        This may temporarily disrupt fcp service on the target
        adapter.
        @test
        
        :param node: The name of the storage system node where the adapter is installed.
        
        :param fcp_adapter: FC Target adapter
        
        :param speed: Link speed (in Gb).  Possible values: "1", "2", "4", "8", "10",
                "16" or "auto" (auto negotiate speed).
        """
        return self.request( "fcp-adapter-set-speed", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'speed': [ speed, 'speed', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_config_down(self, node, fcp_adapter):
        """
        Bring a Fibre Channel target adapter offline.
        The adapter may not be offline immediately after the
        call returns, it may take up to a few seconds for the
        adapter to change state.
        In Data ONTAP 7-Mode, if the FCP service is not running
        then all adapters are automatically offlined. They cannot
        be brought online again until FCP service is started.
        adapter to change state.
        In Data ONTAP Cluster-Mode, offlining an adapter will
        operationally disable all FCP logical interfaces (LIFs)
        hosted by the adapter.
        
        :param node: The name of the storage system node where the adapter is installed.
        
        :param fcp_adapter: FC adapter to bring offline.
        """
        return self.request( "fcp-adapter-config-down", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_list_info(self, partner_only=None, fcp_adapter=None, verbose=None):
        """
        Gets information such as nodename/portname and link state
        about the specified Fibre Channel target adapter, or if
        no adapter is specified, about all the FC target adapters.
        
        :param partner_only: This field is obsolete and no longer used beginning with Data
                ONTAP 8.0.
        
        :param fcp_adapter: FC target Adapter to get config information for.  If no
                adapter is specified, information is returned for all
                FC target Adapters.
        
        :param verbose: If specified with "true", additional adapter info
                is returned.  Look at description of output for
                what additions.
        """
        return self.request( "fcp-adapter-list-info", {
            'partner_only': [ partner_only, 'partner-only', [ bool, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'fcp-config-adapters': [ FcpConfigAdapterInfo, True ],
        } )
    
    def fcp_interface_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of FCP Target Logical Interfaces (LIF).
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the FCP
                data LIF object.
                All FCP data LIF objects matching this query up to 'max-records'
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
        return self.request( "fcp-interface-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpInterfaceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpInterfaceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpInterfaceInfo, True ],
        } )
    
    def fcp_ping(self, port_id_or_wwpn, fcp_adapter, payload=None):
        """
        Send an ELS ECHO frame to a Fibre Channel address or WWPN.
        EHOSTNOTFOUND is returned if the WWPN cannot be resolved.
        EONTAPI_EHOSTDOWN is returned if the address cannot be pinged.
        
        :param port_id_or_wwpn: The Fibre Channel address or the WWPN to ping. The format of
                a Fibre channel address is a hexadecimal or numeric value with
                the range [0..2^24-1]. The format of a WWPN is
                XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal digit.
        
        :param fcp_adapter: Adapter to send the ping request from.
        
        :param payload: Additional data to send in the payload of the ELS ECHO frame.
                The payload can be up to 248 characters long.
        """
        return self.request( "fcp-ping", {
            'port_id_or_wwpn': [ port_id_or_wwpn, 'port-id-or-wwpn', [ basestring, 'None' ], False ],
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'payload': [ payload, 'payload', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_port_name_swap(self, fcp_adapter_2, fcp_adapter_1):
        """
        Swap port names of two local Fibre Channel target adapters.
        
        :param fcp_adapter_2: One of the adapters to swap their port names. It has to be a
                local adapter in standby or single_image cfmode.
        
        :param fcp_adapter_1: One of the adapters to swap their port names. It has to be a
                local adapter in standby or single_image cfmode.
        """
        return self.request( "fcp-port-name-swap", {
            'fcp_adapter_2': [ fcp_adapter_2, 'fcp-adapter-2', [ basestring, 'None' ], False ],
            'fcp_adapter_1': [ fcp_adapter_1, 'fcp-adapter-1', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_set_partner(self, fcp_adapter, partner_adapter):
        """
        Sets the name of the partner adapter which the local
        adapter should takeover. Partner adapter setting is obsolete
        and this operation is no longer supported.
        
        :param fcp_adapter: Local FC adapter.
        
        :param partner_adapter: Partner FC adapter to takeover.
        """
        return self.request( "fcp-adapter-set-partner", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'partner_adapter': [ partner_adapter, 'partner-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_node_set_name(self, node_name, force=None):
        """
        Set the current FCP World Wide Node Name (WWNN). This
        WWNN is in the form XX:XX:XX:XX:XX:XX:XX:XX where X is a
        hexadecimal digit. The supplied WWNN must also match the
        vendor's registered namespace unless the force argument
        is also supplied.
        In Data ONTAP 7-Mode, the registered namespace is
        "50:0a:80:8X:XX:XX:XX" and all Fibre Channel adapters
        must be offline. Changes will take place when the adapters
        are brought online.
        In Data ONTAP Cluster-Mode, the registered namespace is
        "2X:XX:00:a0:98:XX:XX:XX" and the FCP service must be offline.
        Changes will take place when the service is brought online.
        
        :param node_name: FCP World Wide Node Name.
        
        :param force: If true, allow setting the WWNN to a value outside the vendor's
                registered namespace for the current mode. If false or
                not present, the request will fail unless the supplied WWNN
                is inside the correct namespace.
        """
        return self.request( "fcp-node-set-name", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fcp_service_status(self):
        """
        Get status of the FCP service, whether or not it is running.
        """
        return self.request( "fcp-service-status", {
        }, {
            'is-available': [ bool, False ],
        } )
    
    def fcp_port_name_list_info(self, verbose=None):
        """
        Get the list of valid Fibre Channel target port names on a
        filer's local adapters. The filer needs to be in standby or
        single_image cfmode.
        
        :param verbose: If specified with "true", unused port names are also reported.
                Default value is "false".
        """
        return self.request( "fcp-port-name-list-info", {
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'fcp-port-names': [ FcpPortNameInfo, True ],
        } )
    
    def fcp_adapter_stats_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of fcp objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the fcp
                object.
                All fcp objects matching this query up to 'max-records' will be
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
        return self.request( "fcp-adapter-stats-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpAdapterStatsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpAdapterStatsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpAdapterStatsInfo, True ],
        } )
    
    def fcp_service_create(self, node_name=None, start=None, force_node_name=None):
        """
        Create an FCP Service in a Vserver. Each Vserver requires an
        online FCP Service in order to serve data via the Fibre Channel
        protocol.
        
        :param node_name: The FCP World Wide Node Name (WWNN) for the FCP service. If not
                provided, one will be auto-generated.
        
        :param start: Determine the initial state of the FCP Service. If true, the
                service will be automatically started after creation completes.
                If false, the service will be left in the stopped state and the
                caller must subsequently call fcp-service-start to start the
                service. The default is true.
        
        :param force_node_name: If true, allow setting the WWNN to a value outside the vendor's
                registered namespace. If false, the node-name must match the
                namespace 2X:XX:00:a0:98:XX:XX:XX. The default is false.
        """
        return self.request( "fcp-service-create", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'start': [ start, 'start', [ bool, 'None' ], False ],
            'force_node_name': [ force_node_name, 'force-node-name', [ bool, 'None' ], False ],
        }, {
            'node-name': [ basestring, False ],
        } )
    
    def fcp_service_stop(self):
        """
        Stops FCP service. When FCP service is stopped, the
        adapters are brought offline.  Service will be unavaliable
        once the call returns with success.
        """
        return self.request( "fcp-service-stop", {
        }, {
        } )
    
    def fcp_adapter_topology_list_iter_start(self, fcp_adapter=None, verbose=None, zoned=None):
        """
        Get the fabric topology for one or more switches the results of
        which are retreived by using fcp-adapter-topology-list-iter-next.
        Connectivity of adapters running on behalf of partners
        are not included in the list when requesting for
        all adapters.  If listing for all adapters and an
        error occurrs while retrieving connection status
        for an adapter, information for that adapter will not be
        returned and the API will continue on with the rest
        of the adapters without erroring out.  You can get the
        error msg for that adapter, by specifically specifying
        that adapter.
        
        :param fcp_adapter: Adapter to get topology information for.  If no adapter is
                specified, information is returned for all fcp adapter.
        
        :param verbose: If true, returns verbose information including port information
                about each switch in the fabric. Default is true.
        
        :param zoned: If true, returns only devices in the fabric that are zoned to
                the target adapter. Default is false.
        """
        return self.request( "fcp-adapter-topology-list-iter-start", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
            'zoned': [ zoned, 'zoned', [ bool, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def fcp_node_get_name(self):
        """
        Get the current FCP World Wide Node Name (WWNN). This
        WWNN name is in the form XX:XX:XX:XX:XX:XX:XX:XX where
        X is a hexadecimal digit.
        In Data ONTAP 7-Mode, this is the WWNN of the individual
        storage system. In "single_image" cfmode, the WWNN of the
        system and its high availability partner will be the same.
        In Data ONTAP Cluster-Mode, this is the WWNN of the
        Vserver FCP Service.
        """
        return self.request( "fcp-node-get-name", {
        }, {
            'node-name': [ basestring, False ],
        } )
    
    def fcp_set_cfmode(self, fcp_cfmode, force=None):
        """
        Set the current cfmode setting for the system.
        This setting controls how the cluster behaves
        during a takeover/giveback. It also controls
        if the filer should use multiple virtual target
        adapters per physical target adapter. fcp service
        must be stopped before executing this API.
        The only valid value for cfmode is 'single_image'
        If cfmode is set to 'single_image' the filer connects
        to the FC fabric in ptp mode by default but is configurable,
        and all luns in the cluster are visible on all FC target
        ports. In this mode all hosts require multipathing
        software.
        When setting the cfmode to 'single_image' configuration
        checks	are performed.  If these checks fail an EPERM error
        will be returned.  See the lun-config-check-single-image-info
        API for more information.
        
        :param fcp_cfmode: Set current cfmode setting.
                Possible values: single_image
        
        :param force: Forcibly change the cfmode, overriding cluster partner checks.
                Obsolete.
        """
        return self.request( "fcp-set-cfmode", {
            'fcp_cfmode': [ fcp_cfmode, 'fcp-cfmode', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_config_media_type(self, fcp_adapter, media_type):
        """
        Sets the link type on the Fibre Channel target adapter.
        It can be configured to establish a point-to-point link,
        a loop configuration or to automatically sense whether
        the connection type is a point-to-point or loop link.
        Setting the link to point-to-point in a loop configuration
        can prevent the loop from coming up properly.
        If the adapter is online, it must be brought offline and
        then online in order for a new mediatype to take effect.
        This may temporarily disrupt fcp service on the target
        adapter.
        
        :param fcp_adapter: FC adapter to bring offline.
        
        :param media_type: Media type to set.  Valid values are point-to-point ("ptp"),
                loop configuration ("loop"), or automatic ("auto").
        """
        return self.request( "fcp-adapter-config-media-type", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
            'media_type': [ media_type, 'media-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_wwpnalias_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of assigned World Wide Port Name (WWPN)
        aliases.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                WWPN aliases object.
                All WWPN aliases objects matching this query up to 'max-records'
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
        return self.request( "fcp-wwpnalias-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AliasesInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AliasesInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AliasesInfo, True ],
        } )
    
    def fcp_adapter_reset_stats(self, fcp_adapter=None):
        """
        Resets the stats for the specified Fibre Channel Target
        Adapter.  If none specified, reset stats for all FC adapters.
        
        :param fcp_adapter: FC Target adapter.
        """
        return self.request( "fcp-adapter-reset-stats", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcp_adapter_zone_list_iter_next(self, tag, maximum):
        """
        Return items from a previous call to
        fcp-adapter-zone-list-iter-start
        Information returned for each zone entry include the
        active zone set name, the zone name, and the zone members.
        
        :param tag: Tag from a previous fcp-adapter-zone-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
                Range: [0..2^32-1]
        """
        return self.request( "fcp-adapter-zone-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'fcp-adapter-zones': [ FcpAdapterZoneInfo, True ],
        } )
    
    def fcp_adapter_initiators_list_info(self, fcp_adapter=None):
        """
        Get the list of initiators currently connected to the
        specified Fibre Channel target adapter, or if none specified,
        a list of initiators connected to any FC target adapter.
        Information returned for each initiator includes the
        portname of initiators that are currently logged in with
        the the FC target adapters. If the portname is in an initiator
        group, then the group name is also included.  Also the
        Fibre Channel host address and the nodename/portname
        of the initiators are included as well.
        Connectivity of adapters running on behalf of partners
        are not included in the list when requesting for
        all adapters.  If listing for all adapters and an
        error occurred for while retrieving connection status
        for an adapter, status for that adapter will not be
        returned, and the API will continue on with the rest
        of the adapters without erroring out.  You can get the
        error msg for that adapter, by specifically specifying
        that adapter.
        
        :param fcp_adapter: Adapter to get initiator list for.  If no adapter is
                specified, information is returned for all initiators
                connected through any fcp adapter in the system.
        """
        return self.request( "fcp-adapter-initiators-list-info", {
            'fcp_adapter': [ fcp_adapter, 'fcp-adapter', [ basestring, 'None' ], False ],
        }, {
            'fcp-adapters': [ FcpAdapterInitiatorsInfo, True ],
        } )
    
    def fcp_service_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of FCP Services.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the FCP
                Service object.
                All FCP Service objects matching this query up to 'max-records'
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
        return self.request( "fcp-service-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpServiceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpServiceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpServiceInfo, True ],
        } )
    
    def fcp_initiator_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        List all initiators connected to FCP target LIFs.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                connected FCP initiator object.
                All connected FCP initiator objects matching this query up to
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
        return self.request( "fcp-initiator-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FcpAdapterInitiatorsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FcpAdapterInitiatorsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FcpAdapterInitiatorsInfo, True ],
        } )
    
    def fcp_service_destroy(self):
        """
        Destroy the FCP Service in a Vserver.
        """
        return self.request( "fcp-service-destroy", {
        }, {
        } )
