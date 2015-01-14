from netapp.connection import NaConnection
from nfsv3_client_stats_info import Nfsv3ClientStatsInfo # 22 properties
from security_rule_info import SecurityRuleInfo # 6 properties
from rpc_data_info import RpcDataInfo # 5 properties
from nfsv2_client_stats_info import Nfsv2ClientStatsInfo # 18 properties
from hostaddr import Hostaddr # 0 properties
from rpc_stats_info import RpcStatsInfo # 2 properties
from nfschownmode import Nfschownmode # 0 properties
from exports_rule_info_2 import ExportsRuleInfo2 # 3 properties
from sec_flavor_info import SecFlavorInfo # 1 properties
from nfs_stats_info import NfsStatsInfo # 5 properties
from nfs_info import NfsInfo # 46 properties
from pathname_info import PathnameInfo # 1 properties
from exports_rule_info import ExportsRuleInfo # 8 properties
from nfs_service_get_iter_key_td import NfsServiceGetIterKeyTd # 1 properties
from owner_info import OwnerInfo # 2 properties
from nfs_top_info import NfsTopInfo # 10 properties
from nfsv4_client_stats_info import Nfsv4ClientStatsInfo # 44 properties
from tcp_flowcontrol_stats_info import TcpFlowcontrolStatsInfo # 4 properties
from exports_hostname_info import ExportsHostnameInfo # 3 properties

class NfsConnection(NaConnection):
    
    def nfs_exportfs_storage_path(self, pathname):
        """
        For the given path, determine the actual storage path.
        Returns an error if the path does not exist.
        
        :param pathname: Virtual pathname which has a rule associated with an actual
                pathname.
        """
        return self.request( "nfs-exportfs-storage-path", {
            'pathname': [ pathname, 'pathname', [ basestring, 'None' ], False ],
        }, {
            'actual-pathname': [ basestring, False ],
        } )
    
    def nfs_stats_top_clients_list_iter_start(self, maxclients=None):
        """
        Starts an iteration through the top NFS clients, ordered
        by total NFS operations.
        
        :param maxclients: Specifies the maximum number of top clients to retrieve
                (the default is 20)
                Range : [1..2^32-1].
        """
        return self.request( "nfs-stats-top-clients-list-iter-start", {
            'maxclients': [ maxclients, 'maxclients', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def nfs_exportfs_fence_enable(self, fenced_hosts, fenced_paths=None, all_pathnames=None, persistent=None):
        """
        Enables fencing to the given exports for the
        given entry. This means that the entry will not have
        write permission to the exports. The rule changes take effect
        immediately. Set the persistent option to true to save the
        rule in the /etc/exports file and keep the option persistent
        upon loading or reboot.
        
        :param fenced_hosts: An array of hostnames which are to be fenced off.
        
        :param fenced_paths: An array of paths which are to be fenced off.
        
        :param all_pathnames: Default value is false. Set to true to fence all rules.
                'fenced-paths' option must be left empty if this option is true.
        
        :param persistent: Default value is false. If true, modifies the etc/exports file
                to append the rule for a permanent change. (The new rule still
                takes effect immediately.)  If false, only change the
                exports in memory.
        """
        return self.request( "nfs-exportfs-fence-enable", {
            'fenced_paths': [ fenced_paths, 'fenced-paths', [ PathnameInfo, 'None' ], True ],
            'all_pathnames': [ all_pathnames, 'all-pathnames', [ bool, 'None' ], False ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'fenced_hosts': [ fenced_hosts, 'fenced-hosts', [ ExportsHostnameInfo, 'None' ], True ],
        }, {
        } )
    
    def nfs_monitor_add(self, hosts):
        """
        starts monitoring the specified hosts for NFS lock recovery
        purposes. The specified hosts are added to the list of
        of clients that will be notified of lock recovery in the
        event of an NFS server crash/reboot. For more information,
        see the sm_mon(1a) manual page.
        
        :param hosts: an array of hosts that are to be monitored.
        """
        return self.request( "nfs-monitor-add", {
            'hosts': [ hosts, 'hosts', [ basestring, 'hostaddr' ], True ],
        }, {
        } )
    
    def nfs_stats_get_client_stats(self, host):
        """
        Collects NFS statistics for a specified client
        
        :param host: Hostname or IP address of client
        """
        return self.request( "nfs-stats-get-client-stats", {
            'host': [ host, 'host', [ basestring, 'None' ], False ],
        }, {
            'nfs-stats': [ NfsStatsInfo, False ],
            'client-info': [ basestring, False ],
            'rpc-stats': [ RpcStatsInfo, False ],
            'tcp-flowcontrol-stats': [ TcpFlowcontrolStatsInfo, False ],
        } )
    
    def nfs_exportfs_check_permission(self, host, pathname, permission):
        """
        Returns true if the host IP has mount permissions for a
        specified path.
        
        :param host: IP address of the host to check in dotted decimal format:
                AAA.BBB.CCC.DDD
        
        :param pathname: Returns the permissions for this path.
        
        :param permission: Possible values: &quot;read-only&quot;, &quot;read-write&quot;, and &quot;root&quot;.
        """
        return self.request( "nfs-exportfs-check-permission", {
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'pathname': [ pathname, 'pathname', [ basestring, 'None' ], False ],
            'permission': [ permission, 'permission', [ basestring, 'None' ], False ],
        }, {
            'is-permissible': [ bool, False ],
        } )
    
    def nfs_status(self):
        """
        Returns the status of the NFS server.
        """
        return self.request( "nfs-status", {
        }, {
            'is-drained': [ bool, False ],
            'is-enabled': [ bool, False ],
        } )
    
    def nfs_exportfs_modify_rule(self, persistent, rule):
        """
        Functionally similar to append with the following caveats.
        Returns an error if the rule does not exist.
        Only works for one rule at a time.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true, modifies
                the etc/exports file to append the rule for a permanent change.
                (The new rule still takes effect immediately.)
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an error will be
                returned.
        
        :param rule: The rule to modify. Returns an error if a previous rule with
                the same pathname is not already loaded into memory.
        """
        return self.request( "nfs-exportfs-modify-rule", {
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'rule': [ rule, 'rule', [ ExportsRuleInfo, 'None' ], False ],
        }, {
        } )
    
    def nfs_stats_top_clients_list_iter_next(self, tag, maximum):
        """
        Continues the nfs-stats-top-clients-list-iter-start iteration
        through the top NFS clients, ordered by total NFS operations.
        
        :param tag: Tag from a previous nfs-stats-top-iter-start
        
        :param maximum: The maximum number of entries to retrieve.
                Range : [0..2^32-1].
        """
        return self.request( "nfs-stats-top-clients-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'nfs-top': [ NfsTopInfo, True ],
        } )
    
    def nfs_service_get(self, desired_attributes=None):
        """
        Get the NFS server configuration.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "nfs-service-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NfsInfo, 'None' ], False ],
        }, {
            'attributes': [ NfsInfo, False ],
        } )
    
    def nfs_monitor_reclaim(self, hosts=None):
        """
        reclaims the NFS locks for the specified client hosts. If
        no hosts are specified, then all the clients locks are
        removed and are notified about lock recovery, as if an
        NFS server crash/reboot had happened. If any hosts are
        specified, then only those client hosts locks are reclaimed
        For more information, see the sm_mon(1a) manual page.
        
        :param hosts: hosts whose locks have to be reclaimed. If no hosts
                are specified, then all the clients locks are reclaimed.
        """
        return self.request( "nfs-monitor-reclaim", {
            'hosts': [ hosts, 'hosts', [ basestring, 'hostaddr' ], True ],
        }, {
        } )
    
    def nfs_exportfs_fence_disable(self, fenced_hosts, fenced_paths=None, remove_locks=None, all_pathnames=None, persistent=None):
        """
        Disables fencing to the given exports for the
        given entry. This means that the entry will have
        write permission to the exports. The rule changes take effect
        immediately. Set the persistent option to true to save the rule
        in the /etc/exports file and keep the option persistent upon
        loading or reboot.
        
        :param fenced_hosts: An array of hostnames which are to be fenced off.
        
        :param fenced_paths: An array of paths which are to be fenced off.
        
        :param remove_locks: Default value is false. Set to true to reclaim locks of the
                specified fenced-hosts.
        
        :param all_pathnames: Default value is false. Set to true to unfence all rules.
                'fenced-paths' option must be left empty if this option is true.
        
        :param persistent: Default value is false. If true, modifies the etc/exports file
                to append the rule for a permanent change. (The new rule still
                takes effect immediately.)  If false, only change the
                exports in memory.
        """
        return self.request( "nfs-exportfs-fence-disable", {
            'fenced_paths': [ fenced_paths, 'fenced-paths', [ PathnameInfo, 'None' ], True ],
            'remove_locks': [ remove_locks, 'remove-locks', [ bool, 'None' ], False ],
            'all_pathnames': [ all_pathnames, 'all-pathnames', [ bool, 'None' ], False ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'fenced_hosts': [ fenced_hosts, 'fenced-hosts', [ ExportsHostnameInfo, 'None' ], True ],
        }, {
        } )
    
    def nfs_exportfs_modify_rule_2(self, persistent, rule):
        """
        Functionally similar to append-2 with the following caveats.
        Returns an error if the rule does not exist.
        Only works for one rule at a time.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true, modifies
                the etc/exports file to append the rule for a permanent change.
                (The new rule still takes effect immediately.)
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an error will be
                returned.
        
        :param rule: The rule to modify. Returns an error if a previous rule with
                the same pathname is not already loaded into memory.
        """
        return self.request( "nfs-exportfs-modify-rule-2", {
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'rule': [ rule, 'rule', [ ExportsRuleInfo2, 'None' ], False ],
        }, {
        } )
    
    def nfs_stats_zero_stats(self):
        """
        Set all NFS statistcs to zero
        """
        return self.request( "nfs-stats-zero-stats", {
        }, {
        } )
    
    def nfs_exportfs_list_rules(self, pathname=None, persistent=None):
        """
        Returns the rules associated with exports.  If a pathname
        is specified, the rules associated with the export matching
        that pathname, are returned; otherwise, rules for all exports
        are returned.
        
        :param pathname: The pathname, for whose matching export, the client wants
                a listing of the associated rules. If this parameter is
                provided, the persistent parameter is ignored.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true,
                the export entries that are present in the /etc/exports file
                are returned; otherwise, those loaded in memory are returned.
                This parameter is ignored, if the pathname parameter is
                provided.
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an empty list
                will be returned.
        """
        return self.request( "nfs-exportfs-list-rules", {
            'pathname': [ pathname, 'pathname', [ basestring, 'None' ], False ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
        }, {
            'rules': [ ExportsRuleInfo, True ],
        } )
    
    def nfs_exportfs_append_rules_2(self, rules, persistent=None, verbose=None):
        """
        Enables pathnames for mounting according to the rules
        specified. New rules for the pathnames take effect immediately,
        ignoring previous rules for specified pathnames.
        In the Data ONTAP 7-Mode, set the persistent option to true to
        save the rule in the etc/exports file and keep the option
        persistent upon loading or reboot whereas it must be true in
        Data ONTAP Cluster-Mode as the export entries are always
        persistent.
        The new security-rule-info structure contains finer grained
        information about security rules than exports-rule-info.
        
        :param rules: List of rules to add to the exports table.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true, modifies
                the etc/exports file to append the rule for a permanent change.
                (The new rule still takes effect immediately.)
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an error will be
                returned.
        
        :param verbose: If true, returns a list of directories which were appended.
                Errors during the append are recorded in the 'results' field
                error and 'loaded-pathnames' will contain which pathnames
                were successfully appended. Default value is false.
        """
        return self.request( "nfs-exportfs-append-rules-2", {
            'rules': [ rules, 'rules', [ ExportsRuleInfo2, 'None' ], True ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'exported-pathnames': [ PathnameInfo, True ],
            'loaded-pathnames': [ PathnameInfo, True ],
        } )
    
    def nfs_monitor_list(self):
        """
        Lists the hosts that are currently being monitored by the
        NFS status monitor.
        """
        return self.request( "nfs-monitor-list", {
        }, {
            'hosts': [ basestring, True ],
        } )
    
    def nfs_monitor_remove(self, hosts):
        """
        Starts unmonitoring the specified hosts for NFS lock
        recovery purposes. The specified hosts are removed
        from the list of clients that will be notified of lock
        recovery in the event of an NFS server crash/reboot. For
        more information, see the sm_mon(1a) manual page.
        
        :param hosts: an array of hosts that are to be unmonitored.
        """
        return self.request( "nfs-monitor-remove", {
            'hosts': [ hosts, 'hosts', [ basestring, 'hostaddr' ], True ],
        }, {
        } )
    
    def nfs_exportfs_load_exports(self, persistent_only=None):
        """
        Loads the etc/exports file into memory. Replaces exports
        rules already residing in memory.
        
        :param persistent_only: Default value is false. If true, atomically reloads each
                rule from the exports file and unloads all other rules.
        """
        return self.request( "nfs-exportfs-load-exports", {
            'persistent_only': [ persistent_only, 'persistent-only', [ bool, 'None' ], False ],
        }, {
        } )
    
    def nfs_disable(self):
        """
        In Data ONTAP 7-Mode, this API will disable NFS server
        access (effectively same as the CLI command "nfs off")
        In Data ONTAP Cluster-Mode, this will stop the Vserver's
        NFS service. If the NFS service was not explicitly created,
        this API does nothing.
        """
        return self.request( "nfs-disable", {
        }, {
        } )
    
    def nfs_get_supported_sec_flavors(self):
        """
        Returns a list of currently supported security flavors.
        Hosts with permmisions and connecting via the proper security
        flavor have access to directories on the filer. Default
        security flavor for all exports is &quot;sys&quot;.
        """
        return self.request( "nfs-get-supported-sec-flavors", {
        }, {
            'sec-flavor': [ SecFlavorInfo, True ],
        } )
    
    def nfs_exportfs_append_rules(self, rules, persistent=None, verbose=None):
        """
        Enables pathnames for mounting according to the rules
        specified. New rules for the pathnames take effect immediately,
        ignoring previous rules for specified pathnames.
        In the Data ONTAP 7-Mode, set the persistent option to true to
        save the rule in the etc/exports file and keep the option
        persistent upon loading or reboot whereas it must be true in
        Data ONTAP Cluster-Mode as the export entries are always
        persistent.
        
        :param rules: List of rules to add to the exports table.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true, modifies
                the etc/exports file to append the rule for a permanent change.
                (The new rule still takes effect immediately.)
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an error will be
                returned.
        
        :param verbose: If true, returns a list of directories which were appended.
                Errors during the append are recorded in the 'results' field
                error and 'loaded-pathnames' will contain which pathnames
                were successfully appended. Default value is false.
        """
        return self.request( "nfs-exportfs-append-rules", {
            'rules': [ rules, 'rules', [ ExportsRuleInfo, 'None' ], True ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'exported-pathnames': [ PathnameInfo, True ],
            'loaded-pathnames': [ PathnameInfo, True ],
        } )
    
    def nfs_service_get_create_defaults(self, attributes=None):
        """
        Obtain the default values for NFS server configuration.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "nfs-service-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ NfsInfo, 'None' ], False ],
        }, {
            'defaults': [ NfsInfo, False ],
        } )
    
    def nfs_service_create(self, is_nfsv3_connection_drop_enabled=None, is_nfsv3_enabled=None, default_windows_user=None, is_nfsv41_acl_preserve_enabled=None, is_nfsv40_referrals_enabled=None, is_nfsv41_pnfs_enabled=None, is_nfsv40_migration_enabled=None, chown_mode=None, is_nfsv41_referrals_enabled=None, nfsv41_implementation_id_domain=None, nfsv41_implementation_id_name=None, is_nfsv4_numeric_ids_enabled=None, is_nfsv40_acl_enabled=None, is_nfs_access_enabled=None, rpcsec_ctx_idle=None, is_nfsv2_enabled=None, nfsv4_acl_max_aces=None, is_nfsv4_fsid_change_enabled=None, is_nfsv40_req_open_confirm_enabled=None, nfsv4_id_domain=None, is_nfsv40_read_delegation_enabled=None, is_nfs_rootonly_enabled=None, is_nfsv41_pnfs_striped_volumes_enabled=None, nfsv41_implementation_id_time=None, is_nfsv41_acl_enabled=None, is_nfsv40_write_delegation_enabled=None, ntfs_unix_security_ops=None, is_mount_rootonly_enabled=None, nfsv4x_session_num_slots=None, enable_ejukebox=None, nfsv4x_session_slot_reply_cache_size=None, rpcsec_ctx_high=None, is_nfsv41_read_delegation_enabled=None, is_vstorage_enabled=None, is_nfsv3_fsid_change_enabled=None, nfsv4_grace_seconds=None, nfsv4_lease_seconds=None, return_record=None, is_nfsv41_write_delegation_enabled=None, is_nfsv41_migration_enabled=None, is_validate_qtree_export_enabled=None, is_nfsv41_enabled=None, is_nfsv40_enabled=None, default_windows_group=None, is_nfsv41_state_protection_enabled=None):
        """
        Create a new NFS configuration.
        
        :param is_nfsv3_connection_drop_enabled: If 'true', then connection is dropped when an NFSv3 request is
                dropped. Default value is 'true'.
        
        :param is_nfsv3_enabled: If 'true', then NFS version 3 is enabled. Default value is
                'true'.
        
        :param default_windows_user: The default windows user for CIFS access.
        
        :param is_nfsv41_acl_preserve_enabled: If 'true', the NFSv4 server will preserve and modify ACL when
                chmod <mode> is done. Default value is 'true'.
        
        :param is_nfsv40_referrals_enabled: If 'true', then NFSv4.0 Referrals feature is enabled. Default
                value is 'false'.
        
        :param is_nfsv41_pnfs_enabled: If 'true', then Parallel NFS support for NFS version 4.1 is
                enabled. Default value is 'true'.
        
        :param is_nfsv40_migration_enabled: If 'true', then NFSv4.0 Migration feature is enabled. Default
                value is 'false'.
        
        :param chown_mode: Vserver Change Ownership Mode. Possible values are 'ignore',
                'fail', 'use_export_policy'. If 'use_export_policy' is set,
                export policy option is used. Default value is
                'use_export_policy'.
                Possible values:
                <ul>
                <li> "restricted"          ,
                <li> "unrestricted"        ,
                <li> "use_export_policy"
                </ul>
        
        :param is_nfsv41_referrals_enabled: If 'true', then NFSv4.1 Referrals feature is enabled. Default
                value is 'false'.
        
        :param nfsv41_implementation_id_domain: NFSv4.1 Implementation id domain. Default value is
                'defaultv41impliddomain.com'.
        
        :param nfsv41_implementation_id_name: NFSv4.1 Implementation id name. Default value is
                'defaultv41implidname'.
        
        :param is_nfsv4_numeric_ids_enabled: If 'true', then NFSv4 support for Numeric Owner IDs is enabled.
                Default value is 'true'.
        
        :param is_nfsv40_acl_enabled: If 'true', then NFSv4.0 ACL feature is enabled. Default value is
                'false'.
        
        :param is_nfs_access_enabled: If 'true',then NFS server access is enabled. Default value is
                'true'.
        
        :param rpcsec_ctx_idle: Time in seconds before an idle entry in RPCSEC_GSS context cache
                is deleted. Default value is 0.
        
        :param is_nfsv2_enabled: Starting Data ONTAP 8.2, NFS v2 is no longer supported. Default
                value is 'false'.
        
        :param nfsv4_acl_max_aces: Maximum Number of ACEs allowed in an ACL. Range is 192 to 1024.
                Default value is 400.
        
        :param is_nfsv4_fsid_change_enabled: If 'true', then clients see change in FSID as NFSv4 clients
                traverse filesystems. Default value is 'true'.
        
        :param is_nfsv40_req_open_confirm_enabled: If 'true', then the server will require an OPEN_CONFIRM operation
                for all NFSv4.0 clients. Default value is 'false'.
        
        :param nfsv4_id_domain: NFSv4 ID mapping domain. Default value is
                'defaultv4iddomain.com'.
        
        :param is_nfsv40_read_delegation_enabled: If 'true', NFSv4.0 read delegation feature is enabled. Default
                value is 'false'.
        
        :param is_nfs_rootonly_enabled: If 'true', then the vserver allows NFS protocol calls only from
                privileged ports (port numbers less than 1024). Default value is
                'false'.
        
        :param is_nfsv41_pnfs_striped_volumes_enabled: If 'true', Striped volume support for Parallel NFS is enabled .
                Default value is 'false'.
        
        :param nfsv41_implementation_id_time: NFSv4.1 Implementation id time.The number of seconds since
                January 1, 1970.
        
        :param is_nfsv41_acl_enabled: If 'true', then NFSv4.1 ACL feature is enabled. Default value is
                'false'.
        
        :param is_nfsv40_write_delegation_enabled: If 'true', NFSv4.0 write delegation feature is enabled. Default
                value is 'false'.
        
        :param ntfs_unix_security_ops: Ignore/Fail unix security operations on NTFS volumes.  Possible
                values are 'ignore', 'fail','use_export_policy'. If
                'use_export_policy' is set, export policy option is used.
                Default value is 'use_export_policy'.
        
        :param is_mount_rootonly_enabled: If 'true', then the vserver allows MOUNT protocol calls only from
                privileged ports (port numbers less than 1024). Default value is
                'true'.
        
        :param nfsv4x_session_num_slots: Number of Slots in the NFSv4.x Session Slot Tables. Default value
                is 180.
        
        :param enable_ejukebox: If 'true', then the NFS server will send EJUKEBOX error on server
                delays.
        
        :param nfsv4x_session_slot_reply_cache_size: Size of the Reply that will be Cached in Each NFSv4.x Session
                Slot (in bytes). Default value is 640.
        
        :param rpcsec_ctx_high: High water mark for the RPCSEC_GSS Context Cache.  Default value
                is 0.
        
        :param is_nfsv41_read_delegation_enabled: If 'true', NFSv4.1 read delegation feature is enabled. Default
                value is 'false'.
        
        :param is_vstorage_enabled: If 'true', then enables the usage of vStorage protocol for server
                side copies, which is mostly used in hypervisors. Default value
                is 'false'.
        
        :param is_nfsv3_fsid_change_enabled: If 'true', then NFSv3 clients see change in FSID as they traverse
                filesystems. Default value is 'true'.
        
        :param nfsv4_grace_seconds: NFSv4 Grace timeout value in seconds. Default value is 45
                seconds.
        
        :param nfsv4_lease_seconds: NFSv4 Lease timeout value in seconds. Default value is 30
                seconds.
        
        :param return_record: If set to true, returns the NFS Server on successful creation.
                Default: false
        
        :param is_nfsv41_write_delegation_enabled: If 'true', NFSv4.1 write delegation feature is enabled. Default
                value is 'false'.
        
        :param is_nfsv41_migration_enabled: If 'true', then NFSv4.1 Migration feature is enabled. Default
                value is 'false'.
        
        :param is_validate_qtree_export_enabled: If 'true', then the Vserver performs additional validation for
                qtree. Default value is 'true'.
        
        :param is_nfsv41_enabled: If 'true', then NFS version 4.1 is enabled. Default value is
                'false'.
        
        :param is_nfsv40_enabled: If 'true', then NFS version 4.0 is enabled. Default value is
                'false'.
        
        :param default_windows_group: The default windows group for CIFS access.
        
        :param is_nfsv41_state_protection_enabled: If 'true', then NFSv4.1 State Protection is enabled. Default
                value is 'true'.
        """
        return self.request( "nfs-service-create", {
            'is_nfsv3_connection_drop_enabled': [ is_nfsv3_connection_drop_enabled, 'is-nfsv3-connection-drop-enabled', [ bool, 'None' ], False ],
            'is_nfsv3_enabled': [ is_nfsv3_enabled, 'is-nfsv3-enabled', [ bool, 'None' ], False ],
            'default_windows_user': [ default_windows_user, 'default-windows-user', [ basestring, 'None' ], False ],
            'is_nfsv41_acl_preserve_enabled': [ is_nfsv41_acl_preserve_enabled, 'is-nfsv41-acl-preserve-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_referrals_enabled': [ is_nfsv40_referrals_enabled, 'is-nfsv40-referrals-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_pnfs_enabled': [ is_nfsv41_pnfs_enabled, 'is-nfsv41-pnfs-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_migration_enabled': [ is_nfsv40_migration_enabled, 'is-nfsv40-migration-enabled', [ bool, 'None' ], False ],
            'chown_mode': [ chown_mode, 'chown-mode', [ basestring, 'nfschownmode' ], False ],
            'is_nfsv41_referrals_enabled': [ is_nfsv41_referrals_enabled, 'is-nfsv41-referrals-enabled', [ bool, 'None' ], False ],
            'nfsv41_implementation_id_domain': [ nfsv41_implementation_id_domain, 'nfsv41-implementation-id-domain', [ basestring, 'None' ], False ],
            'nfsv41_implementation_id_name': [ nfsv41_implementation_id_name, 'nfsv41-implementation-id-name', [ basestring, 'None' ], False ],
            'is_nfsv4_numeric_ids_enabled': [ is_nfsv4_numeric_ids_enabled, 'is-nfsv4-numeric-ids-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_acl_enabled': [ is_nfsv40_acl_enabled, 'is-nfsv40-acl-enabled', [ bool, 'None' ], False ],
            'is_nfs_access_enabled': [ is_nfs_access_enabled, 'is-nfs-access-enabled', [ bool, 'None' ], False ],
            'rpcsec_ctx_idle': [ rpcsec_ctx_idle, 'rpcsec-ctx-idle', [ int, 'None' ], False ],
            'is_nfsv2_enabled': [ is_nfsv2_enabled, 'is-nfsv2-enabled', [ bool, 'None' ], False ],
            'nfsv4_acl_max_aces': [ nfsv4_acl_max_aces, 'nfsv4-acl-max-aces', [ int, 'None' ], False ],
            'is_nfsv4_fsid_change_enabled': [ is_nfsv4_fsid_change_enabled, 'is-nfsv4-fsid-change-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_req_open_confirm_enabled': [ is_nfsv40_req_open_confirm_enabled, 'is-nfsv40-req-open-confirm-enabled', [ bool, 'None' ], False ],
            'nfsv4_id_domain': [ nfsv4_id_domain, 'nfsv4-id-domain', [ basestring, 'None' ], False ],
            'is_nfsv40_read_delegation_enabled': [ is_nfsv40_read_delegation_enabled, 'is-nfsv40-read-delegation-enabled', [ bool, 'None' ], False ],
            'is_nfs_rootonly_enabled': [ is_nfs_rootonly_enabled, 'is-nfs-rootonly-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_pnfs_striped_volumes_enabled': [ is_nfsv41_pnfs_striped_volumes_enabled, 'is-nfsv41-pnfs-striped-volumes-enabled', [ bool, 'None' ], False ],
            'nfsv41_implementation_id_time': [ nfsv41_implementation_id_time, 'nfsv41-implementation-id-time', [ int, 'date' ], False ],
            'is_nfsv41_acl_enabled': [ is_nfsv41_acl_enabled, 'is-nfsv41-acl-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_write_delegation_enabled': [ is_nfsv40_write_delegation_enabled, 'is-nfsv40-write-delegation-enabled', [ bool, 'None' ], False ],
            'ntfs_unix_security_ops': [ ntfs_unix_security_ops, 'ntfs-unix-security-ops', [ basestring, 'None' ], False ],
            'is_mount_rootonly_enabled': [ is_mount_rootonly_enabled, 'is-mount-rootonly-enabled', [ bool, 'None' ], False ],
            'nfsv4x_session_num_slots': [ nfsv4x_session_num_slots, 'nfsv4x-session-num-slots', [ int, 'None' ], False ],
            'enable_ejukebox': [ enable_ejukebox, 'enable-ejukebox', [ bool, 'None' ], False ],
            'nfsv4x_session_slot_reply_cache_size': [ nfsv4x_session_slot_reply_cache_size, 'nfsv4x-session-slot-reply-cache-size', [ int, 'None' ], False ],
            'rpcsec_ctx_high': [ rpcsec_ctx_high, 'rpcsec-ctx-high', [ int, 'None' ], False ],
            'is_nfsv41_read_delegation_enabled': [ is_nfsv41_read_delegation_enabled, 'is-nfsv41-read-delegation-enabled', [ bool, 'None' ], False ],
            'is_vstorage_enabled': [ is_vstorage_enabled, 'is-vstorage-enabled', [ bool, 'None' ], False ],
            'is_nfsv3_fsid_change_enabled': [ is_nfsv3_fsid_change_enabled, 'is-nfsv3-fsid-change-enabled', [ bool, 'None' ], False ],
            'nfsv4_grace_seconds': [ nfsv4_grace_seconds, 'nfsv4-grace-seconds', [ int, 'None' ], False ],
            'nfsv4_lease_seconds': [ nfsv4_lease_seconds, 'nfsv4-lease-seconds', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'is_nfsv41_write_delegation_enabled': [ is_nfsv41_write_delegation_enabled, 'is-nfsv41-write-delegation-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_migration_enabled': [ is_nfsv41_migration_enabled, 'is-nfsv41-migration-enabled', [ bool, 'None' ], False ],
            'is_validate_qtree_export_enabled': [ is_validate_qtree_export_enabled, 'is-validate-qtree-export-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_enabled': [ is_nfsv41_enabled, 'is-nfsv41-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_enabled': [ is_nfsv40_enabled, 'is-nfsv40-enabled', [ bool, 'None' ], False ],
            'default_windows_group': [ default_windows_group, 'default-windows-group', [ basestring, 'None' ], False ],
            'is_nfsv41_state_protection_enabled': [ is_nfsv41_state_protection_enabled, 'is-nfsv41-state-protection-enabled', [ bool, 'None' ], False ],
        }, {
            'result': [ NfsInfo, False ],
        } )
    
    def nfs_service_destroy(self):
        """
        Delete an NFS configuration.
        """
        return self.request( "nfs-service-destroy", {
        }, {
        } )
    
    def nfs_exportfs_flush_cache(self, pathname=None):
        """
        For the given path, renew or flush the access cache.
        
        :param pathname: Pathname to flush. If this input is not provided, all of the
                paths in the exports table are flushed.
        """
        return self.request( "nfs-exportfs-flush-cache", {
            'pathname': [ pathname, 'pathname', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def nfs_exportfs_delete_rules(self, all_pathnames=None, persistent=None, pathnames=None, verbose=None):
        """
        Removes the rules for a set of pathnames. This returns an error
        if any of the pathnames don't have a rule.
        In the Data ONTAP 7-Mode, set the persistent option to modify
        the etc/exports file and keep this change persistent upon
        reboots whereas it must be true in Data ONTAP Cluster-Mode
        as the export entries are always persistent.
        
        :param all_pathnames: Default value is false. Set to true to delete all rules.
                'pathnames' option must be left empty if this option is true.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. Modify
                the etc/exports file to delete the rules permanently.
                CAUTION: If 'all-pathnames' and 'persistent' are both true,
                all exports are removed permanently.
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an error will be
                returned.
        
        :param pathnames: In the Data ONTAP 7-Mode, these must be the pathnames
                to be deleted from the exports table.
                In Data ONTAP Cluster-Mode, the junction paths of the
                volumes to be unexported must be provided.
        
        :param verbose: Return a verbose output of what occurred. If there is
                an error after deleting only a few rules, 'deleted-pathnames'
                will return which rules were deleted. Default value is false.
        """
        return self.request( "nfs-exportfs-delete-rules", {
            'all_pathnames': [ all_pathnames, 'all-pathnames', [ bool, 'None' ], False ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
            'pathnames': [ pathnames, 'pathnames', [ PathnameInfo, 'None' ], True ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'unexported-pathnames': [ PathnameInfo, True ],
            'deleted-pathnames': [ PathnameInfo, True ],
        } )
    
    def nfs_service_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of NFS servers.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the NFS
                Server object.
                All NFS Server objects matching this query up to 'max-records'
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
        return self.request( "nfs-service-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NfsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NfsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NfsInfo, True ],
        } )
    
    def nfs_monitor_remove_locks(self, owners):
        """
        removes the NFS locks of a specfied process of a specified
        client host.
        
        :param owners: List of owners whose locks have to be deleted.
        """
        return self.request( "nfs-monitor-remove-locks", {
            'owners': [ owners, 'owners', [ OwnerInfo, 'None' ], True ],
        }, {
        } )
    
    def nfs_enable(self):
        """
        In Data ONTAP 7-Mode, this API will enable NFS server
        access (effectively same as the CLI command "nfs on")
        In Data ONTAP Cluster-Mode, this will start the Vserver's
        NFS service. If the NFS service was not explicitly created,
        this API will create one with default options.
        """
        return self.request( "nfs-enable", {
        }, {
        } )
    
    def nfs_stats_top_clients_list_iter_end(self, tag):
        """
        Terminate NFS client statistics iteration and cleanup any
        saved info.
        
        :param tag: Tag from a previous nfs-stats-top-clients-list-iter-start
        """
        return self.request( "nfs-stats-top-clients-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def nfs_exportfs_list_rules_2(self, pathname=None, persistent=None):
        """
        Returns the rules associated with exports, using the new
        security info structure.  If a pathname is specified,
        the rules associated with the export matching that
        pathname, are returned; otherwise, rules for all exports
        are returned.
        
        :param pathname: The pathname, for whose matching export, the client wants
                a listing of the associated rules. If this parameter is
                provided, the persistent parameter is ignored.
        
        :param persistent: In Data ONTAP 7-Mode, default value is false. If true,
                the export entries that are present in the /etc/exports file
                are returned; otherwise, those loaded in memory are returned.
                This parameter is ignored, if the pathname parameter is
                provided.
                In Data ONTAP Cluster-Mode, the export entries are always
                persistent. Default value is true. If false, an empty list
                will be returned.
        """
        return self.request( "nfs-exportfs-list-rules-2", {
            'pathname': [ pathname, 'pathname', [ basestring, 'None' ], False ],
            'persistent': [ persistent, 'persistent', [ bool, 'None' ], False ],
        }, {
            'rules': [ ExportsRuleInfo2, True ],
        } )
    
    def nfs_service_modify(self, is_nfsv3_connection_drop_enabled=None, is_nfsv3_enabled=None, default_windows_user=None, is_nfsv41_acl_preserve_enabled=None, is_nfsv40_referrals_enabled=None, is_nfsv41_pnfs_enabled=None, is_nfsv40_migration_enabled=None, chown_mode=None, is_nfsv41_referrals_enabled=None, nfsv41_implementation_id_domain=None, nfsv41_implementation_id_name=None, is_nfsv4_numeric_ids_enabled=None, is_nfsv40_acl_enabled=None, is_nfs_access_enabled=None, rpcsec_ctx_idle=None, is_nfsv2_enabled=None, nfsv4_acl_max_aces=None, is_nfsv4_fsid_change_enabled=None, is_nfsv40_req_open_confirm_enabled=None, nfsv4_id_domain=None, is_nfsv40_read_delegation_enabled=None, is_nfs_rootonly_enabled=None, is_nfsv41_pnfs_striped_volumes_enabled=None, nfsv41_implementation_id_time=None, is_nfsv41_acl_enabled=None, is_nfsv40_write_delegation_enabled=None, ntfs_unix_security_ops=None, is_mount_rootonly_enabled=None, nfsv4x_session_num_slots=None, enable_ejukebox=None, nfsv4x_session_slot_reply_cache_size=None, rpcsec_ctx_high=None, is_nfsv41_read_delegation_enabled=None, is_vstorage_enabled=None, is_nfsv3_fsid_change_enabled=None, nfsv4_grace_seconds=None, nfsv4_lease_seconds=None, is_nfsv41_write_delegation_enabled=None, is_nfsv41_migration_enabled=None, is_validate_qtree_export_enabled=None, is_nfsv41_enabled=None, is_nfsv40_enabled=None, default_windows_group=None, is_nfsv41_state_protection_enabled=None):
        """
        Modify an NFS configuration. If no values are given, the NFS
        configuration is not modified.
        
        :param is_nfsv3_connection_drop_enabled: If 'true', then connection is dropped when an NFSv3 request is
                dropped. Default value is 'true'.
        
        :param is_nfsv3_enabled: If 'true', then NFS version 3 is enabled. Default value is
                'true'.
        
        :param default_windows_user: The default windows user for CIFS access.
        
        :param is_nfsv41_acl_preserve_enabled: If 'true', the NFSv4 server will preserve and modify ACL when
                chmod <mode> is done. Default value is 'true'.
        
        :param is_nfsv40_referrals_enabled: If 'true', then NFSv4.0 Referrals feature is enabled. Default
                value is 'false'.
        
        :param is_nfsv41_pnfs_enabled: If 'true', then Parallel NFS support for NFS version 4.1 is
                enabled. Default value is 'true'.
        
        :param is_nfsv40_migration_enabled: If 'true', then NFSv4.0 Migration feature is enabled. Default
                value is 'false'.
        
        :param chown_mode: Vserver Change Ownership Mode. Possible values are 'ignore',
                'fail', 'use_export_policy'. If 'use_export_policy' is set,
                export policy option is used. Default value is
                'use_export_policy'.
                Possible values:
                <ul>
                <li> "restricted"          ,
                <li> "unrestricted"        ,
                <li> "use_export_policy"
                </ul>
        
        :param is_nfsv41_referrals_enabled: If 'true', then NFSv4.1 Referrals feature is enabled. Default
                value is 'false'.
        
        :param nfsv41_implementation_id_domain: NFSv4.1 Implementation id domain. Default value is
                'defaultv41impliddomain.com'.
        
        :param nfsv41_implementation_id_name: NFSv4.1 Implementation id name. Default value is
                'defaultv41implidname'.
        
        :param is_nfsv4_numeric_ids_enabled: If 'true', then NFSv4 support for Numeric Owner IDs is enabled.
                Default value is 'true'.
        
        :param is_nfsv40_acl_enabled: If 'true', then NFSv4.0 ACL feature is enabled. Default value is
                'false'.
        
        :param is_nfs_access_enabled: If 'true',then NFS server access is enabled. Default value is
                'true'.
        
        :param rpcsec_ctx_idle: Time in seconds before an idle entry in RPCSEC_GSS context cache
                is deleted. Default value is 0.
        
        :param is_nfsv2_enabled: Starting Data ONTAP 8.2, NFS v2 is no longer supported. Default
                value is 'false'.
        
        :param nfsv4_acl_max_aces: Maximum Number of ACEs allowed in an ACL. Range is 192 to 1024.
                Default value is 400.
        
        :param is_nfsv4_fsid_change_enabled: If 'true', then clients see change in FSID as NFSv4 clients
                traverse filesystems. Default value is 'true'.
        
        :param is_nfsv40_req_open_confirm_enabled: If 'true', then the server will require an OPEN_CONFIRM operation
                for all NFSv4.0 clients. Default value is 'false'.
        
        :param nfsv4_id_domain: NFSv4 ID mapping domain. Default value is
                'defaultv4iddomain.com'.
        
        :param is_nfsv40_read_delegation_enabled: If 'true', NFSv4.0 read delegation feature is enabled. Default
                value is 'false'.
        
        :param is_nfs_rootonly_enabled: If 'true', then the vserver allows NFS protocol calls only from
                privileged ports (port numbers less than 1024). Default value is
                'false'.
        
        :param is_nfsv41_pnfs_striped_volumes_enabled: If 'true', Striped volume support for Parallel NFS is enabled .
                Default value is 'false'.
        
        :param nfsv41_implementation_id_time: NFSv4.1 Implementation id time.The number of seconds since
                January 1, 1970.
        
        :param is_nfsv41_acl_enabled: If 'true', then NFSv4.1 ACL feature is enabled. Default value is
                'false'.
        
        :param is_nfsv40_write_delegation_enabled: If 'true', NFSv4.0 write delegation feature is enabled. Default
                value is 'false'.
        
        :param ntfs_unix_security_ops: Ignore/Fail unix security operations on NTFS volumes.  Possible
                values are 'ignore', 'fail','use_export_policy'. If
                'use_export_policy' is set, export policy option is used.
                Default value is 'use_export_policy'.
        
        :param is_mount_rootonly_enabled: If 'true', then the vserver allows MOUNT protocol calls only from
                privileged ports (port numbers less than 1024). Default value is
                'true'.
        
        :param nfsv4x_session_num_slots: Number of Slots in the NFSv4.x Session Slot Tables. Default value
                is 180.
        
        :param enable_ejukebox: If 'true', then the NFS server will send EJUKEBOX error on server
                delays.
        
        :param nfsv4x_session_slot_reply_cache_size: Size of the Reply that will be Cached in Each NFSv4.x Session
                Slot (in bytes). Default value is 640.
        
        :param rpcsec_ctx_high: High water mark for the RPCSEC_GSS Context Cache.  Default value
                is 0.
        
        :param is_nfsv41_read_delegation_enabled: If 'true', NFSv4.1 read delegation feature is enabled. Default
                value is 'false'.
        
        :param is_vstorage_enabled: If 'true', then enables the usage of vStorage protocol for server
                side copies, which is mostly used in hypervisors. Default value
                is 'false'.
        
        :param is_nfsv3_fsid_change_enabled: If 'true', then NFSv3 clients see change in FSID as they traverse
                filesystems. Default value is 'true'.
        
        :param nfsv4_grace_seconds: NFSv4 Grace timeout value in seconds. Default value is 45
                seconds.
        
        :param nfsv4_lease_seconds: NFSv4 Lease timeout value in seconds. Default value is 30
                seconds.
        
        :param is_nfsv41_write_delegation_enabled: If 'true', NFSv4.1 write delegation feature is enabled. Default
                value is 'false'.
        
        :param is_nfsv41_migration_enabled: If 'true', then NFSv4.1 Migration feature is enabled. Default
                value is 'false'.
        
        :param is_validate_qtree_export_enabled: If 'true', then the Vserver performs additional validation for
                qtree. Default value is 'true'.
        
        :param is_nfsv41_enabled: If 'true', then NFS version 4.1 is enabled. Default value is
                'false'.
        
        :param is_nfsv40_enabled: If 'true', then NFS version 4.0 is enabled. Default value is
                'false'.
        
        :param default_windows_group: The default windows group for CIFS access.
        
        :param is_nfsv41_state_protection_enabled: If 'true', then NFSv4.1 State Protection is enabled. Default
                value is 'true'.
        """
        return self.request( "nfs-service-modify", {
            'is_nfsv3_connection_drop_enabled': [ is_nfsv3_connection_drop_enabled, 'is-nfsv3-connection-drop-enabled', [ bool, 'None' ], False ],
            'is_nfsv3_enabled': [ is_nfsv3_enabled, 'is-nfsv3-enabled', [ bool, 'None' ], False ],
            'default_windows_user': [ default_windows_user, 'default-windows-user', [ basestring, 'None' ], False ],
            'is_nfsv41_acl_preserve_enabled': [ is_nfsv41_acl_preserve_enabled, 'is-nfsv41-acl-preserve-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_referrals_enabled': [ is_nfsv40_referrals_enabled, 'is-nfsv40-referrals-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_pnfs_enabled': [ is_nfsv41_pnfs_enabled, 'is-nfsv41-pnfs-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_migration_enabled': [ is_nfsv40_migration_enabled, 'is-nfsv40-migration-enabled', [ bool, 'None' ], False ],
            'chown_mode': [ chown_mode, 'chown-mode', [ basestring, 'nfschownmode' ], False ],
            'is_nfsv41_referrals_enabled': [ is_nfsv41_referrals_enabled, 'is-nfsv41-referrals-enabled', [ bool, 'None' ], False ],
            'nfsv41_implementation_id_domain': [ nfsv41_implementation_id_domain, 'nfsv41-implementation-id-domain', [ basestring, 'None' ], False ],
            'nfsv41_implementation_id_name': [ nfsv41_implementation_id_name, 'nfsv41-implementation-id-name', [ basestring, 'None' ], False ],
            'is_nfsv4_numeric_ids_enabled': [ is_nfsv4_numeric_ids_enabled, 'is-nfsv4-numeric-ids-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_acl_enabled': [ is_nfsv40_acl_enabled, 'is-nfsv40-acl-enabled', [ bool, 'None' ], False ],
            'is_nfs_access_enabled': [ is_nfs_access_enabled, 'is-nfs-access-enabled', [ bool, 'None' ], False ],
            'rpcsec_ctx_idle': [ rpcsec_ctx_idle, 'rpcsec-ctx-idle', [ int, 'None' ], False ],
            'is_nfsv2_enabled': [ is_nfsv2_enabled, 'is-nfsv2-enabled', [ bool, 'None' ], False ],
            'nfsv4_acl_max_aces': [ nfsv4_acl_max_aces, 'nfsv4-acl-max-aces', [ int, 'None' ], False ],
            'is_nfsv4_fsid_change_enabled': [ is_nfsv4_fsid_change_enabled, 'is-nfsv4-fsid-change-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_req_open_confirm_enabled': [ is_nfsv40_req_open_confirm_enabled, 'is-nfsv40-req-open-confirm-enabled', [ bool, 'None' ], False ],
            'nfsv4_id_domain': [ nfsv4_id_domain, 'nfsv4-id-domain', [ basestring, 'None' ], False ],
            'is_nfsv40_read_delegation_enabled': [ is_nfsv40_read_delegation_enabled, 'is-nfsv40-read-delegation-enabled', [ bool, 'None' ], False ],
            'is_nfs_rootonly_enabled': [ is_nfs_rootonly_enabled, 'is-nfs-rootonly-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_pnfs_striped_volumes_enabled': [ is_nfsv41_pnfs_striped_volumes_enabled, 'is-nfsv41-pnfs-striped-volumes-enabled', [ bool, 'None' ], False ],
            'nfsv41_implementation_id_time': [ nfsv41_implementation_id_time, 'nfsv41-implementation-id-time', [ int, 'date' ], False ],
            'is_nfsv41_acl_enabled': [ is_nfsv41_acl_enabled, 'is-nfsv41-acl-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_write_delegation_enabled': [ is_nfsv40_write_delegation_enabled, 'is-nfsv40-write-delegation-enabled', [ bool, 'None' ], False ],
            'ntfs_unix_security_ops': [ ntfs_unix_security_ops, 'ntfs-unix-security-ops', [ basestring, 'None' ], False ],
            'is_mount_rootonly_enabled': [ is_mount_rootonly_enabled, 'is-mount-rootonly-enabled', [ bool, 'None' ], False ],
            'nfsv4x_session_num_slots': [ nfsv4x_session_num_slots, 'nfsv4x-session-num-slots', [ int, 'None' ], False ],
            'enable_ejukebox': [ enable_ejukebox, 'enable-ejukebox', [ bool, 'None' ], False ],
            'nfsv4x_session_slot_reply_cache_size': [ nfsv4x_session_slot_reply_cache_size, 'nfsv4x-session-slot-reply-cache-size', [ int, 'None' ], False ],
            'rpcsec_ctx_high': [ rpcsec_ctx_high, 'rpcsec-ctx-high', [ int, 'None' ], False ],
            'is_nfsv41_read_delegation_enabled': [ is_nfsv41_read_delegation_enabled, 'is-nfsv41-read-delegation-enabled', [ bool, 'None' ], False ],
            'is_vstorage_enabled': [ is_vstorage_enabled, 'is-vstorage-enabled', [ bool, 'None' ], False ],
            'is_nfsv3_fsid_change_enabled': [ is_nfsv3_fsid_change_enabled, 'is-nfsv3-fsid-change-enabled', [ bool, 'None' ], False ],
            'nfsv4_grace_seconds': [ nfsv4_grace_seconds, 'nfsv4-grace-seconds', [ int, 'None' ], False ],
            'nfsv4_lease_seconds': [ nfsv4_lease_seconds, 'nfsv4-lease-seconds', [ int, 'None' ], False ],
            'is_nfsv41_write_delegation_enabled': [ is_nfsv41_write_delegation_enabled, 'is-nfsv41-write-delegation-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_migration_enabled': [ is_nfsv41_migration_enabled, 'is-nfsv41-migration-enabled', [ bool, 'None' ], False ],
            'is_validate_qtree_export_enabled': [ is_validate_qtree_export_enabled, 'is-validate-qtree-export-enabled', [ bool, 'None' ], False ],
            'is_nfsv41_enabled': [ is_nfsv41_enabled, 'is-nfsv41-enabled', [ bool, 'None' ], False ],
            'is_nfsv40_enabled': [ is_nfsv40_enabled, 'is-nfsv40-enabled', [ bool, 'None' ], False ],
            'default_windows_group': [ default_windows_group, 'default-windows-group', [ basestring, 'None' ], False ],
            'is_nfsv41_state_protection_enabled': [ is_nfsv41_state_protection_enabled, 'is-nfsv41-state-protection-enabled', [ bool, 'None' ], False ],
        }, {
        } )
