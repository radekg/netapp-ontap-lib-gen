from netapp.connection import NaConnection
from iscsi_session_type import IscsiSessionType # 0 properties
from iscsi_stats_info import IscsiStatsInfo # 5 properties
from iscsi_initiator_get_iter_key_td import IscsiInitiatorGetIterKeyTd # 3 properties
from iscsi_stats_get_iter_key_td import IscsiStatsGetIterKeyTd # 1 properties
from iscsi_interface_get_iter_key_td import IscsiInterfaceGetIterKeyTd # 2 properties
from interface_list_entry_info import InterfaceListEntryInfo # 1 properties
from vif_id import VifId # 0 properties
from iscsi_iptpgroup_list_entry_info import IscsiIptpgroupListEntryInfo # 3 properties
from iscsi_session_list_entry_info import IscsiSessionListEntryInfo # 22 properties
from iscsi_service_info import IscsiServiceInfo # 4 properties
from iscsi_portal_list_entry_info import IscsiPortalListEntryInfo # 4 properties
from iscsi_received_stats_info import IscsiReceivedStatsInfo # 10 properties
from iscsi_auth_type import IscsiAuthType # 0 properties
from iscsi_interface_accesslist_entry_info import IscsiInterfaceAccesslistEntryInfo # 3 properties
from iscsi_transmitted_stats_info import IscsiTransmittedStatsInfo # 11 properties
from iscsi_sesssion_cmd_list_entry_info import IscsiSesssionCmdListEntryInfo # 3 properties
from iscsi_interface_accesslist_get_iter_key_td import IscsiInterfaceAccesslistGetIterKeyTd # 3 properties
from iscsi_cdb_stats_info import IscsiCdbStatsInfo # 5 properties
from iscsi_tpgroup_list_entry_info import IscsiTpgroupListEntryInfo # 7 properties
from iscsi_config_adapter_info import IscsiConfigAdapterInfo # 4 properties
from iscsi_initiator_list_entry_info import IscsiInitiatorListEntryInfo # 8 properties
from iscsi_adapter_initiators_info import IscsiAdapterInitiatorsInfo # 2 properties
from iscsi_initiator_auth_get_iter_key_td import IscsiInitiatorAuthGetIterKeyTd # 2 properties
from iscsi_auth_chap_policy import IscsiAuthChapPolicy # 0 properties
from iscsi_security_entry_info import IscsiSecurityEntryInfo # 6 properties
from iscsi_connection_get_iter_key_td import IscsiConnectionGetIterKeyTd # 4 properties
from iscsi_connected_initiator_info import IscsiConnectedInitiatorInfo # 3 properties
from iscsi_isns_info import IscsiIsnsInfo # 7 properties
from iscsi_isns_get_iter_key_td import IscsiIsnsGetIterKeyTd # 1 properties
from iscsi_service_get_iter_key_td import IscsiServiceGetIterKeyTd # 1 properties
from iscsi_tpgroup_get_iter_key_td import IscsiTpgroupGetIterKeyTd # 2 properties
from iscsi_interface_list_entry_info import IscsiInterfaceListEntryInfo # 10 properties
from iscsi_connection_list_entry_info import IscsiConnectionListEntryInfo # 12 properties
from iscsi_error_stats_info import IscsiErrorStatsInfo # 10 properties
from iscsi_session_connection_list_entry_info import IscsiSessionConnectionListEntryInfo # 12 properties
from ipaddress_list_entry_info import IpaddressListEntryInfo # 1 properties
from iscsi_session_get_iter_key_td import IscsiSessionGetIterKeyTd # 3 properties
from iscsi_portal_address_info import IscsiPortalAddressInfo # 3 properties

class IscsiConnection(NaConnection):
    
    def iscsi_interface_disable(self, interface_name):
        """
        Disables an interface for use by iSCSI
        
        :param interface_name: Name of interface to disable.
                In Data ONTAP 7-Mode, this is the name of a physical
                ethernet interface, for example: "e0c".
                In Data ONTAP Cluster-Mode, this is the name of an
                iSCSI data LIF in the Vserver.
        """
        return self.request( "iscsi-interface-disable", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_isns_start(self):
        """
        Start iSNS service.  Service will be avaliable once
        the call returns with success.
        """
        return self.request( "iscsi-isns-start", {
        }, {
        } )
    
    def iscsi_auth_generate_chap_password(self):
        """
        Generate a 128 bit random password that can be used as a CHAP secret.
        """
        return self.request( "iscsi-auth-generate-chap-password", {
        }, {
            'secret': [ basestring, False ],
        } )
    
    def iscsi_isns_stop(self):
        """
        Stops iSNS service.  Service will not be available once
        the call returns with success.
        """
        return self.request( "iscsi-isns-stop", {
        }, {
        } )
    
    def iscsi_tpgroup_list_info(self, tpgroup_tag=None):
        """
        List information about target portal groups
        
        :param tpgroup_tag: Portal group being queried; if not supplied,
                information on all portal groups is returned
        """
        return self.request( "iscsi-tpgroup-list-info", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
        }, {
            'iscsi-tpgroup-list-entries': [ IscsiTpgroupListEntryInfo, True ],
        } )
    
    def iscsi_adapter_config_up(self, iscsi_adapter):
        """
        Configures the specified adapter up.
        This API is obsolete beginning with ONTAP 7.1 and
        will always return the error EOPNOTSUPPORTED. There is
        no equivalent API to replace it.
        
        :param iscsi_adapter: iscsi adapter.
        """
        return self.request( "iscsi-adapter-config-up", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_connection_shutdown(self, session_id, connection_id, tpgroup_name):
        """
        auto generated : Shut down a connection on a node
        
        :param session_id: Target Session ID
        
        :param connection_id: Connection ID
        
        :param tpgroup_name: Target Portal Group
        """
        return self.request( "iscsi-connection-shutdown", {
            'session_id': [ session_id, 'session-id', [ int, 'None' ], False ],
            'connection_id': [ connection_id, 'connection-id', [ int, 'None' ], False ],
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_tpgroup_alua_set(self, tpgroup_tag, tpgroup_alua_preferred, tpgroup_alua_state):
        """
        Change the ALUA parameters on a tpgroup
        Asymmetric Logical Unit Access (ALUA) management
        Data ONTAP supports SCSI ALUA functionality for
        managing multi-pathed SCSI devices. ALUA
        provides a standardized mechanism for path
        discovery and prioritization. Devices are
        identified by target port IDs, which are then
        grouped into target port groups. Each group has
        a state which, when configured, enables the host
        multipathing software to select the appropriate
        path priorities when accessing a LUN.
        For iSCSI, ALUA settings are controlled at the
        target portal group level using the
        "iscsi-tpgroup-alua-set" ZAPI. A target portal
        group can be configured to be either "optimized"
        or "non-optimized"; a host typically uses all
        the optimized paths before using any
        non-optimized paths it may find. All target
        portal groups are optimized by default.
        There is also an optional "preferred" setting
        that may be used on a target portal group.
        Check your host's multi-pathing software
        documentation to see if it supports ALUA and
        the preferred setting.
        ALUA is enabled on Initiator Groups using the
        "igroup-set-attribute" ZAPI. All LUNs mapped
        to an ALUA enabled Initiator Group will support
        the ALUA functionality.
        @test
        
        :param tpgroup_tag: portal group
        
        :param tpgroup_alua_preferred: If "true", target portal group will be marked
                as preferred for ALUA enabled Initiator Groups
        
        :param tpgroup_alua_state: Possible values: "optimized", "non-optimized"
        """
        return self.request( "iscsi-tpgroup-alua-set", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
            'tpgroup_alua_preferred': [ tpgroup_alua_preferred, 'tpgroup-alua-preferred', [ bool, 'None' ], False ],
            'tpgroup_alua_state': [ tpgroup_alua_state, 'tpgroup-alua-state', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_reset_stats(self):
        """
        zero filer iscsi counters
        """
        return self.request( "iscsi-reset-stats", {
        }, {
        } )
    
    def iscsi_interface_list_info(self, interface_name=None):
        """
        Gives status of interface for iSCSI
        
        :param interface_name: Name of interface to report; if not supplied,
                all interfaces are listed. For example: "e0c".
        """
        return self.request( "iscsi-interface-list-info", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
            'iscsi-interface-list-entries': [ IscsiInterfaceListEntryInfo, True ],
        } )
    
    def iscsi_isns_update(self):
        """
        Forces iSNS service to update server.
        """
        return self.request( "iscsi-isns-update", {
        }, {
        } )
    
    def iscsi_stats_list_info(self):
        """
        return current filer iscsi statistics
        """
        return self.request( "iscsi-stats-list-info", {
        }, {
            'iscsi-stats': [ IscsiStatsInfo, True ],
        } )
    
    def iscsi_target_alias_get_alias(self):
        """
        Return the current iscsi target alias
        """
        return self.request( "iscsi-target-alias-get-alias", {
        }, {
            'alias-name': [ basestring, False ],
            'is-alias-assigned': [ bool, False ],
        } )
    
    def iscsi_adapter_stats_list_info(self, iscsi_adapter=None):
        """
        This API is obsolete beginning with ONTAP 7.1 and
        will always return the error EOPNOTSUPPORTED. For the
        equivalent functionality use the ZAPI iscsi-stats-list-info
        The fields returned by iscsi-stats-list-info are very slightly
        different from those previously returned by
        iscsi-adapter-stats-list-info
        
        :param iscsi_adapter: Adapter to get statistics for.
        """
        return self.request( "iscsi-adapter-stats-list-info", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_session_list_info(self, tsih=None):
        """
        Gives list of active sessions
        
        :param tsih: target session ID handle for specific session
        """
        return self.request( "iscsi-session-list-info", {
            'tsih': [ tsih, 'tsih', [ int, 'None' ], False ],
        }, {
            'iscsi-session-list-entries': [ IscsiSessionListEntryInfo, True ],
        } )
    
    def iscsi_target_alias_set_alias(self, alias_name):
        """
        Set the current iscsi target alias
        
        :param alias_name: New iscsi target alias to set; must be 128 bytes or less.
                Free form format otherwise, although a string of all
                blanks will be rejected
        """
        return self.request( "iscsi-target-alias-set-alias", {
            'alias_name': [ alias_name, 'alias-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_tpgroup_interface_delete(self, tpgroup_tag, interface_name):
        """
        Remove an interface from a target portal group.
        Interfaces may only be removed from a user defined
        target portal group. Removing an interface will return
        it to the system defined default group for the
        interface.
        
        :param tpgroup_tag: Target portal group tag.
        
        :param interface_name: Name of network interface to remove.
                In Data ONTAP 7-Mode, this is the name of a physical
                or virtual ethernet interface, for example: "e0c"
                or "vif1"
                In Data ONTAP Cluster-Mode, this is the name of an
                iSCSI data LIF in the Vserver.
        """
        return self.request( "iscsi-tpgroup-interface-delete", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_delete(self, tpgroup_name, force=None):
        """
        auto generated : Delete a user-defined target portal group
        
        :param tpgroup_name: The name target portal group
        
        :param force: Force
        """
        return self.request( "iscsi-delete", {
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def iscsi_iptpgroup_destroy(self, iptpgroup_tag):
        """
        Destroy a IP-based tpgroup
        
        :param iptpgroup_tag: tag of portal group to destroy
        """
        return self.request( "iscsi-iptpgroup-destroy", {
            'iptpgroup_tag': [ iptpgroup_tag, 'iptpgroup-tag', [ int, 'None' ], False ],
        }, {
        } )
    
    def iscsi_isns_destroy(self):
        """
        Destroy the iSNS Service in a Vserver.
        """
        return self.request( "iscsi-isns-destroy", {
        }, {
        } )
    
    def iscsi_connection_list_info(self):
        """
        list iscsi connections on filer
        """
        return self.request( "iscsi-connection-list-info", {
        }, {
            'iscsi-connection-list-entries': [ IscsiConnectionListEntryInfo, True ],
        } )
    
    def iscsi_iptpgroup_list_info(self, iptpgroup_tag=None):
        """
        List information about IP-based target portal groups
        
        :param iptpgroup_tag: Portal group being queried; if not supplied,
                information on all portal groups is returned
        """
        return self.request( "iscsi-iptpgroup-list-info", {
            'iptpgroup_tag': [ iptpgroup_tag, 'iptpgroup-tag', [ int, 'None' ], False ],
        }, {
            'iscsi-iptpgroup-list-entries': [ IscsiIptpgroupListEntryInfo, True ],
        } )
    
    def iscsi_adapter_initiators_list_info(self, iscsi_adapter=None):
        """
        Get the list of initiators currently connected to any
        of the portal groups associated with specified adapter.
        Information returned for each initiator includes the
        target portal group number to which the initiator is
        connected, as well as the iSCSI initiator nodename and
        ISID. If no adapter is specified, information is returned
        for all initiators connected through any adapter in the system.
        NOTE: Beginning with ONTAP 7.1 this API is only intended for use by
        legacy applications that are already coded to this API. New applications
        should use iscsi-portal-list-info to get the list of iSCSI portals.
        associated with this filer.
        Complete removal of this ZAPI may occur in any release after 7.1.
        
        :param iscsi_adapter: Adapter to get initiator list for.  If no adapter is
                specified, information is returned for all initiators
                connected through any iscsi adapter in the system.
        """
        return self.request( "iscsi-adapter-initiators-list-info", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
            'iscsi-adapters': [ IscsiAdapterInitiatorsInfo, True ],
        } )
    
    def iscsi_session_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI session objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI session object.
                All iSCSI session objects matching this query up to 'max-records'
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
        return self.request( "iscsi-session-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiSessionListEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiSessionListEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiSessionListEntryInfo, True ],
        } )
    
    def iscsi_portal_list_info(self):
        """
        list iscsi portals
        """
        return self.request( "iscsi-portal-list-info", {
        }, {
            'iscsi-portal-list-entries': [ IscsiPortalListEntryInfo, True ],
        } )
    
    def iscsi_initiator_set_default_auth(self, auth_type, user_name=None, radius=None, outbound_user_name=None, password=None, outbound_password=None):
        """
        Configure the default authentication method.  If an initiator
        is not configured with a specific authentication method
        using iscsi-initiator-add-auth the default authentication
        method will be applied to it.
        
        :param auth_type: Possible values: "CHAP", "none", "deny".
        
        :param user_name: Inbound CHAP user name, required for auth-type equals to CHAP.
        
        :param radius: "true" if RADIUS is the only forced CHAP authentication policy,
                Default is "false".
        
        :param outbound_user_name: Outbound CHAP user name.  Outbound authentication is optional.
                If Outbound authentication is not specified, then the initiator
                can only do inbound traffic.
        
        :param password: Inbound CHAP user password, required for auth-type equals to CHAP.
        
        :param outbound_password: Outbound CHAP user password.  Outbound authentication is optional.
                If Outbound authentication is not specified, then the initiator
                can only do inbound traffic.
        """
        return self.request( "iscsi-initiator-set-default-auth", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'auth_type': [ auth_type, 'auth-type', [ basestring, 'None' ], False ],
            'radius': [ radius, 'radius', [ bool, 'None' ], False ],
            'outbound_user_name': [ outbound_user_name, 'outbound-user-name', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
            'outbound_password': [ outbound_password, 'outbound-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_tpgroup_interface_add(self, tpgroup_tag, interface_name):
        """
        Add an interface to a target portal group.
        Interfaces may only be added to a user defined
        target portal group.
        
        :param tpgroup_tag: Target portal group tag.
        
        :param interface_name: Name of network interface to add.
                In Data ONTAP 7-Mode, this is the name of a physical
                or virtual ethernet interface, for example: "e0c"
                or "vif1".
                In Data ONTAP Cluster-Mode, this is the name of an
                iSCSI data LIF in the Vserver.
        """
        return self.request( "iscsi-tpgroup-interface-add", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_isns_config(self, isns_ip_addr, force=None):
        """
        Configures the iSNS service.
        In Data ONTAP Cluster-Mode, this this API can
        only modify the configuration of a Vserver where
        an iSNS service has already been created. To
        create an iSNS service in a Vserver where one
        does not exist, use the iscsi-isns-create API.
        
        :param isns_ip_addr: The ip address, in dotted-decimal format, of the iSNS
                server with which to register.
                (for example, "192.168.11.12").
        
        :param force: iSNS config fails if vserver management LIF is not
                configured for the vserver. This behavior is overridden
                with this option when it is set to "true".
        """
        return self.request( "iscsi-isns-config", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'isns_ip_addr': [ isns_ip_addr, 'isns-ip-addr', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def iscsi_initiator_modify_chap_params(self, initiator, remove_outbound=None, user_name=None, radius=None, outbound_user_name=None, password=None, outbound_password=None):
        """
        Modify CHAP parameters to an existing per-initiator
        authentication info whose auth-type equals CHAP.
        
        :param initiator: Name of initiator. The initiator name must conform to
                RFC 3720, for example:
                "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
                The per-initiator authentication info must have an auth-type
                equal to CHAP.
        
        :param remove_outbound: Flag which indicates that mutual CHAP authentication is to
                be converted to one-way CHAP authentication.  Outbound
                CHAP parameters must not be specified when remove-outbound
                is true. The default value is false.
        
        :param user_name: Inbound CHAP user name.  If Inbound CHAP parameters are
                specified they will replace the existing Inbound CHAP
                parameters.  If they are not specified, the existing Inbound
                CHAP parameters will continue to be used.
        
        :param radius: "true" if RADIUS is the only forced CHAP authentication policy,
                Default is "false".
        
        :param outbound_user_name: Outbound CHAP user name.  If Outbound CHAP parameters are
                specified they will replace existing Outbound CHAP
                parameters.  If no Outbound CHAP parameters were previously
                specified, then the specified Outbound CHAP parameters will
                enable mutual CHAP authentication.  If no Outbound CHAP
                parameters are specified and no Outbound CHAP parameters
                exist, then one-way Inbound CHAP authentication will be
                continue to be used.
        
        :param password: Inbound CHAP user password.  If Inbound CHAP parameters are
                specified they will replace the existing Inbound CHAP
                parameters.  If they are not specified, the existing Inbound
                CHAP parameters will continue to be used.
        
        :param outbound_password: Outbound CHAP user password.  If Outbound CHAP parameters are
                specified they will replace existing Outbound CHAP
                parameters.  If no Outbound CHAP parameters were previously
                specified, then the specified Outbound CHAP parameters will
                enable mutual CHAP authentication.  If no Outbound CHAP
                parameters are specified and no Outbound CHAP parameters
                exist, then one-way Inbound CHAP authentication will be
                continue to be used.
        """
        return self.request( "iscsi-initiator-modify-chap-params", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'remove_outbound': [ remove_outbound, 'remove-outbound', [ bool, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'radius': [ radius, 'radius', [ bool, 'None' ], False ],
            'outbound_user_name': [ outbound_user_name, 'outbound-user-name', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
            'outbound_password': [ outbound_password, 'outbound-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_service_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of iSCSI Services.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI Service object.
                All iSCSI Service objects matching this query up to 'max-records'
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
        return self.request( "iscsi-service-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiServiceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiServiceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiServiceInfo, True ],
        } )
    
    def iscsi_iptpgroup_create(self, iptpgroup_name, iptpgroup_tag=None):
        """
        Create a new IP-based tpgroup
        
        :param iptpgroup_name: User-defined name of new target portal group; must be <= 60 bytes,
                and cannot end with "default" as this might conflict
                with names of default system portal groups
                (for example, "192.168.11.12_default" is not allowed)
        
        :param iptpgroup_tag: Optional target portal group tag supplied by user; if not
                supplied, system assigns tag.
        """
        return self.request( "iscsi-iptpgroup-create", {
            'iptpgroup_tag': [ iptpgroup_tag, 'iptpgroup-tag', [ int, 'None' ], False ],
            'iptpgroup_name': [ iptpgroup_name, 'iptpgroup-name', [ basestring, 'None' ], False ],
        }, {
            'iptpgroup-tag': [ int, False ],
        } )
    
    def iscsi_tpgroup_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI Target Portal Group objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI Target Portal Group object.
                All iSCSI Target Portal Group objects matching this query up to
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
        return self.request( "iscsi-tpgroup-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiTpgroupListEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiTpgroupListEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiTpgroupListEntryInfo, True ],
        } )
    
    def iscsi_initiator_list_info(self):
        """
        Gives list of initiators logged in
        """
        return self.request( "iscsi-initiator-list-info", {
        }, {
            'iscsi-initiator-list-entries': [ IscsiInitiatorListEntryInfo, True ],
        } )
    
    def iscsi_interface_accesslist_add(self, initiator, interface_name):
        """
        Add the iSCSI LIFs to the accesslist of the specified initiator
        
        :param initiator: Initiator that can access the iSCSI LIFs
        
        :param interface_name: iSCSI LIF Name
        """
        return self.request( "iscsi-interface-accesslist-add", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_isns_create(self, isns_ip_addr, start=None, force=None):
        """
        Create iSNS Service in a Vserver.
        
        :param isns_ip_addr: iSNS server IP address.
        
        :param start: Determine the initial state of the iSNS Client Service. If true,
                the service will be automatically started after creation
                completes. If false, the service will be left in the stopped
                state and the caller must subsequently call iscsi-isns-start to
                start the service. The default is true.
        
        :param force: iSNS create fails if vserver management LIF is not configured for
                the vserver. This behavior is overridden with this option when it
                is set to true.
        """
        return self.request( "iscsi-isns-create", {
            'start': [ start, 'start', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'isns_ip_addr': [ isns_ip_addr, 'isns-ip-addr', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def iscsi_service_create(self, node_name=None, alias_name=None, start=None):
        """
        Create an iSCSI Service in a Vserver. Each Vserver requires an
        online iSCSI Service in order to serve data via the iSCSI
        protocol.
        
        :param node_name: The iSCSI target name for the Vserver. The target-name must
                conform to RFC 3720. If not provided, one will be
                auto-generated.
        
        :param alias_name: The iSCSI target alias for the iSCSI service. If not provided,
                the Vserver name will be used.
        
        :param start: Determine the initial state of the iSCSI Service. If true, the
                service will be automatically started after creation completes.
                If false, the service will be left in the stopped state and the
                caller must subsequently call iscsi-service-start to start the
                service. The default is true.
        """
        return self.request( "iscsi-service-create", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'alias_name': [ alias_name, 'alias-name', [ basestring, 'None' ], False ],
            'start': [ start, 'start', [ bool, 'None' ], False ],
        }, {
            'node-name': [ basestring, False ],
        } )
    
    def iscsi_adapter_config_down(self, iscsi_adapter):
        """
        Configures the specified adapter down.
        This API is obsolete beginning with ONTAP 7.1 and
        will always return the error EOPNOTSUPPORTED. There is
        no equivalent API to replace it.
        
        :param iscsi_adapter: iscsi adapter.
        """
        return self.request( "iscsi-adapter-config-down", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_adapter_reset_stats(self, iscsi_adapter=None):
        """
        This API is obsolete beginning with ONTAP 7.1 and
        will always return the error EOPNOTSUPPORTED. For the
        equivalent functionality use the ZAPI iscsi-reset-stats
        
        :param iscsi_adapter: Adapter to reset statistics for.
        """
        return self.request( "iscsi-adapter-reset-stats", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_remove(self, lif, tpgroup_name, force=None):
        """
        auto generated : Remove LIFs from a user-defined target portal
        group
        
        :param lif: Logical Interface
        
        :param tpgroup_name: The name target portal group
        
        :param force: Force
        """
        return self.request( "iscsi-remove", {
            'lif': [ lif, 'lif', [ basestring, 'vif-id' ], True ],
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def iscsi_service_start(self):
        """
        Start iSCSI service. Service will be avaliable once
        the call returns with success.
        """
        return self.request( "iscsi-service-start", {
        }, {
        } )
    
    def iscsi_target_alias_clear_alias(self):
        """
        Clear the current iscsi target alias
        """
        return self.request( "iscsi-target-alias-clear-alias", {
        }, {
        } )
    
    def iscsi_tpgroup_destroy(self, tpgroup_tag):
        """
        Destroy a tpgroup. Only user defined target
        portal groups may be destroyed.
        
        :param tpgroup_tag: Tag of portal group to destroy.
        """
        return self.request( "iscsi-tpgroup-destroy", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
        }, {
        } )
    
    def iscsi_service_status(self):
        """
        Get status of the iSCSI service, whether or not it is running.
        """
        return self.request( "iscsi-service-status", {
        }, {
            'is-available': [ bool, False ],
        } )
    
    def iscsi_iptpgroup_ipaddr_add(self, ip_addr, iptpgroup_tag):
        """
        Add an IP Address to an IP-based target portal group
        
        :param ip_addr: The ip address, in dotted-decimal format, with which to add.
                (for example, "192.168.11.12").
        
        :param iptpgroup_tag: portal group tag
        """
        return self.request( "iscsi-iptpgroup-ipaddr-add", {
            'ip_addr': [ ip_addr, 'ip-addr', [ basestring, 'ip-address' ], False ],
            'iptpgroup_tag': [ iptpgroup_tag, 'iptpgroup-tag', [ int, 'None' ], False ],
        }, {
        } )
    
    def iscsi_interface_accesslist_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI Interface Accesslist objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI Interface Accesslist object.
                All iSCSI Interface Accesslist objects matching this query up to
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
        return self.request( "iscsi-interface-accesslist-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiInterfaceAccesslistEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiInterfaceAccesslistEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiInterfaceAccesslistEntryInfo, True ],
        } )
    
    def iscsi_service_stop(self):
        """
        Stops iSCSI service. Service will be not be available once
        the call returns with success.
        """
        return self.request( "iscsi-service-stop", {
        }, {
        } )
    
    def iscsi_add(self, lif, tpgroup_name, force=None):
        """
        auto generated : Add LIFs to a user-defined target portal group
        
        :param lif: Logical Interface
        
        :param tpgroup_name: The name target portal group
        
        :param force: Force
        """
        return self.request( "iscsi-add", {
            'lif': [ lif, 'lif', [ basestring, 'vif-id' ], True ],
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def iscsi_disable(self):
        """
        auto generated : Disable isns capability
        """
        return self.request( "iscsi-disable", {
        }, {
        } )
    
    def iscsi_isns_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Gets iSNS service configuration.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI iSNS Service object.
                All iSCSI iSNS Service objects matching this query up to
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
        return self.request( "iscsi-isns-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiIsnsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiIsnsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiIsnsInfo, True ],
        } )
    
    def iscsi_initiator_add_auth(self, initiator, auth_type, user_name=None, radius=None, outbound_user_name=None, password=None, outbound_password=None):
        """
        Add initiator to the authentication list.
        
        :param initiator: Name of initiator. The initiator name must conform to
                RFC 3720, for example:
                "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
        
        :param auth_type: Authentication type. Possible values: "CHAP", "none", "deny".
        
        :param user_name: Inbound CHAP user name, required for auth-type equals to CHAP.
        
        :param radius: "true" if RADIUS is the only forced CHAP authentication policy,
                Default is "false".
        
        :param outbound_user_name: Outbound CHAP user name.  Outbound authentication is optional.
                If Outbound authentication is not specified, then the initiator
                can only do inbound traffic.
        
        :param password: Inbound CHAP user password, required for auth-type equals to CHAP.
        
        :param outbound_password: Outbound CHAP user password.  Outbound authentication is optional.
                If Outbound authentication is not specified, then the initiator
                can only do inbound traffic.
        """
        return self.request( "iscsi-initiator-add-auth", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'auth_type': [ auth_type, 'auth-type', [ basestring, 'None' ], False ],
            'radius': [ radius, 'radius', [ bool, 'None' ], False ],
            'outbound_user_name': [ outbound_user_name, 'outbound-user-name', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
            'outbound_password': [ outbound_password, 'outbound-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_interface_enable(self, interface_name):
        """
        Enables an interface for use by iSCSI
        
        :param interface_name: Name of interface to enable.
                In Data ONTAP 7-Mode, this is the name of a physical
                ethernet interface, for example: "e0c".
                In Data ONTAP Cluster-Mode, this is the name of an
                iSCSI data LIF in the Vserver.
        """
        return self.request( "iscsi-interface-enable", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_interface_accesslist_remove(self, initiator, interface_name):
        """
        Remove the iSCSI LIFs from the accesslist of the specified
        initiator
        
        :param initiator: Initiator that can access the iSCSI LIFs
        
        :param interface_name: iSCSI LIF Name
        """
        return self.request( "iscsi-interface-accesslist-remove", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_initiator_auth_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI initiator authentication
        configuration objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI initiator authentication configuration object.
                All iSCSI initiator authentication configuration objects matching
                this query up to 'max-records' will be returned.
        
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
        return self.request( "iscsi-initiator-auth-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiSecurityEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiSecurityEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiSecurityEntryInfo, True ],
        } )
    
    def iscsi_node_get_name(self):
        """
        Return the current iscsi node name.
        """
        return self.request( "iscsi-node-get-name", {
        }, {
            'node-name': [ basestring, False ],
        } )
    
    def iscsi_isns_get_info(self):
        """
        Gets iSNS service configuration.
        """
        return self.request( "iscsi-isns-get-info", {
        }, {
            'isns-entity-id': [ basestring, False ],
            'isns-ip-addr': [ basestring, False ],
            'last-update-attempt': [ int, False ],
            'last-successful-update': [ int, False ],
            'last-update-result': [ basestring, False ],
            'is-isns-enabled': [ bool, False ],
        } )
    
    def iscsi_adapter_list_info(self, iscsi_adapter=None):
        """
        Display the configuration information for iscsi adaptor(s),
        including the iSCSI portals associated with a virtual adapter.
        NOTE: Beginning with ONTAP 7.1 this API is only intended for use by
        legacy applications that are already coded to this API. New applications
        should use iscsi-portal-list-info to get the list of iSCSI portals.
        associated with this filer.
        Complete removal of this ZAPI may occur in any release after 7.1.
        
        :param iscsi_adapter: Returns configuration information for adapter if specified.
                If not specified, then configuration information for all
                adapters are returned.
        """
        return self.request( "iscsi-adapter-list-info", {
            'iscsi_adapter': [ iscsi_adapter, 'iscsi-adapter', [ basestring, 'None' ], False ],
        }, {
            'iscsi-config-adapters': [ IscsiConfigAdapterInfo, True ],
        } )
    
    def iscsi_initiator_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of remote iSCSI initiator objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                remote iSCSI initiator object.
                All remote iSCSI initiator objects matching this query up to
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
        return self.request( "iscsi-initiator-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiInitiatorListEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiInitiatorListEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiInitiatorListEntryInfo, True ],
        } )
    
    def iscsi_service_destroy(self):
        """
        Destroy the iSCSI Service in a Vserver.
        """
        return self.request( "iscsi-service-destroy", {
        }, {
        } )
    
    def iscsi_initiator_auth_list_info(self, initiator=None):
        """
        Get authentication information for the specified initiator
        If no initiator is specified, get authentication infomation
        for all the known initiators.  Password, if present
        is left out for security purposes.
        
        :param initiator: Name of initiator. The initiator name must conform to
                RFC 3720, for example:
                "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
                If initiator is not supplied, all initiators are returned.
        """
        return self.request( "iscsi-initiator-auth-list-info", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
        }, {
            'iscsi-security-entries': [ IscsiSecurityEntryInfo, True ],
        } )
    
    def iscsi_session_shutdown(self, tpgroup_name, target_session_id):
        """
        auto generated : Shut down a session on a node
        
        :param tpgroup_name: Target Portal Group
        
        :param target_session_id: Target Session ID
        """
        return self.request( "iscsi-session-shutdown", {
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
            'target_session_id': [ target_session_id, 'target-session-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def iscsi_initiator_get_default_auth(self):
        """
        Get the default auth info for iscsi.  If the auth type
        is CHAP, only the username is retuned, and not the password,
        for security purposes.
        """
        return self.request( "iscsi-initiator-get-default-auth", {
        }, {
            'auth-type': [ basestring, False ],
            'auth-chap-policy': [ basestring, False ],
            'user-name': [ basestring, False ],
            'outbound-user-name': [ basestring, False ],
        } )
    
    def iscsi_iptpgroup_ipaddr_delete(self, ip_addr, iptpgroup_tag):
        """
        Delete an IP Address from an IP-based target portal group
        
        :param ip_addr: The ip address, in dotted-decimal format, with which to add.
                (for example, "192.168.11.12").
        
        :param iptpgroup_tag: portal group
        """
        return self.request( "iscsi-iptpgroup-ipaddr-delete", {
            'ip_addr': [ ip_addr, 'ip-addr', [ basestring, 'ip-address' ], False ],
            'iptpgroup_tag': [ iptpgroup_tag, 'iptpgroup-tag', [ int, 'None' ], False ],
        }, {
        } )
    
    def iscsi_query(self):
        """
        auto generated : Force update of registered iSNS information
        """
        return self.request( "iscsi-query", {
        }, {
        } )
    
    def iscsi_connection_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI Connection objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI Connection object.
                All iSCSI Connection objects matching this query up to
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
        return self.request( "iscsi-connection-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiConnectionListEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiConnectionListEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiConnectionListEntryInfo, True ],
        } )
    
    def iscsi_tpgroup_create(self, tpgroup_name, tpgroup_tag=None):
        """
        Create a new user defined target portal group.
        
        :param tpgroup_name: Name of new user defined target portal group.
                Name must be <= 32 characters.
                In Data ONTAP 7-Mode, user defined target portal
                group names cannot end with "default" as this
                would conflict with names of default target
                portal groups.
                In Data ONTAP Cluster-Mode, user defined target
                portal groups cannot use the name of any defined
                logical interfaces (LIFs) in the vserver as this
                would conflict with names of default target portal
                groups.
        
        :param tpgroup_tag: Optional target portal group tag supplied by user.
                Default value is system generated.
        """
        return self.request( "iscsi-tpgroup-create", {
            'tpgroup_tag': [ tpgroup_tag, 'tpgroup-tag', [ int, 'None' ], False ],
            'tpgroup_name': [ tpgroup_name, 'tpgroup-name', [ basestring, 'None' ], False ],
        }, {
            'tpgroup-tag': [ int, False ],
        } )
    
    def iscsi_initiator_get_auth(self, initiator):
        """
        Get the authentication info for an initiator, if auth
        type is CHAP, only the user-name is returned, password
        is not returned for security purposes.
        
        :param initiator: Name of initiator. The initiator name must conform to
                RFC 3720, for example:
                "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
                If initiator is not found, default authentication method is returned
        """
        return self.request( "iscsi-initiator-get-auth", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
        }, {
            'auth-type': [ basestring, False ],
            'auth-chap-policy': [ basestring, False ],
            'user-name': [ basestring, False ],
            'outbound-user-name': [ basestring, False ],
        } )
    
    def iscsi_node_set_name(self, node_name):
        """
        Set the current iscsi node name.
        
        :param node_name: New iscsi node name; must be  <= 128 chars, and conform to iSCSI rules
        """
        return self.request( "iscsi-node-set-name", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_stats_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iscsi objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iscsi object.
                All iscsi objects matching this query up to 'max-records' will be
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
        return self.request( "iscsi-stats-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiStatsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiStatsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiStatsInfo, True ],
        } )
    
    def iscsi_initiator_delete_auth(self, initiator):
        """
        Delete initiator from the authentication list
        
        :param initiator: Name of initiator. The initiator name must conform to
                RFC 3720, for example:
                "iqn.1987-06.com.initvendor1:appsrv.sn.2346".
        """
        return self.request( "iscsi-initiator-delete-auth", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def iscsi_interface_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of iSCSI target interface objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                iSCSI target interface object.
                All iSCSI target interface objects matching this query up to
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
        return self.request( "iscsi-interface-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ IscsiInterfaceListEntryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ IscsiInterfaceListEntryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ IscsiInterfaceListEntryInfo, True ],
        } )
