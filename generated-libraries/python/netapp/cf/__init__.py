from netapp.connection import NaConnection
from mailbox_status_info import MailboxStatusInfo # 1 properties
from cf_takeover_status_key_td import CfTakeoverStatusKeyTd # 2 properties
from cf_modify_iter_info import CfModifyIterInfo # 3 properties
from mailbox_state import MailboxState # 0 properties
from sf_options_info import SfOptionsInfo # 22 properties
from mailbox_io_times_info import MailboxIoTimesInfo # 2 properties
from takeover_status import TakeoverStatus # 4 properties
from cf_aggregate_giveback_info import CfAggregateGivebackInfo # 6 properties
from storage_failover_info import StorageFailoverInfo # 6 properties
from options_related_info_modify import OptionsRelatedInfoModify # 2 properties
from takeover_info import TakeoverInfo # 1 properties
from cf_modify_iter_key_td import CfModifyIterKeyTd # 1 properties
from node_related_info import NodeRelatedInfo # 10 properties
from cf_aggregate_giveback_status_key_td import CfAggregateGivebackStatusKeyTd # 2 properties
from giveback_related_info import GivebackRelatedInfo # 3 properties
from takeover_reason import TakeoverReason # 0 properties
from reason_takeover_not_possible import ReasonTakeoverNotPossible # 0 properties
from cf_get_iter_key_td import CfGetIterKeyTd # 1 properties
from takeover_related_info import TakeoverRelatedInfo # 11 properties
from timeout_info import TimeoutInfo # 11 properties
from sf_disk_info import SfDiskInfo # 2 properties
from interconnect_related_info import InterconnectRelatedInfo # 3 properties
from options_related_info import OptionsRelatedInfo # 1 properties
from storage_related_info import StorageRelatedInfo # 6 properties
from resource_table_info import ResourceTableInfo # 4 properties
from disk_uid import DiskUid # 0 properties

class CfConnection(NaConnection):
    
    def cf_service_enable(self, node):
        """
        Enables the takeover capability of this filer in the cluster.
        This spawns a process to enable the service
        takeover service is not yet initialized
        takeover service is already enabled
        Can't enable while a revert is in progress
        Partner mailbox is unknown so partner is not in HA mode
        
        :param node: This parameter is the name of the node on which service is to be enabled
        """
        return self.request( "cf-service-enable", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cf_takeover(self, node, force=None, version_mismatch_ok=None, immediate=None, bypass_optimization=None, skip_lif_migration=None, allow_disk_inventory_mismatch=None):
        """
        Initiates a takeover of the storage partner. Takeover
        is done asynchronously; status may be monitored by
        calling the cf-status API and examining the state field.
        If automatic giveback is enabled then control will be
        returned to storage partner once it boots up.
        Already doing takeover.
        A giveback operation is in progress.
        Takeover is not possible due to a partner file system
        or other version mismatch.
        Partner mailboxes are degraded.
        One or more of the strings in takeover-options does not
        specify a legal value.
        Waiting for partner recovery.
        Partner is not halted (VERSION_MISMATCH_OK option only).
        Invalid node parameter
        Disk inventory is mismatched.
        Did not receive partner disk inventory information.
        The partner node is taking over the local node.
        Local node is not in SF_UP state.
        Abort of an ongoing aggregate relocation operation failed.
        There are active cifs sessions on some vfilers of the partner.
        
        :param node: This parameter is the name of the node which is doing a
                takeover of its partner.
        
        :param force: In Classic mode:
                This causes takeover to be immediately initiated.  The
                taken over node, if up, does not get to shut things down
                in an orderly manner so the takeover of the resources
                takes longer. This is the type of takeover that is done
                during normal cluster operation when one of the nodes
                goes away (dies).
                In Cluster mode:
                It forces a node to take over its storage partner even
                though the node detects an error that would otherwise
                prevent a takeover. For example, normally, if a detached
                or faulty interconnect cable between the nodes(ha pair)
                causes the nodes NVRAM contents to be unsynchronized,
                takeover is disabled. However, this will allow the node
                to take over its storage partner despite the
                unsynchronized NVRAM contents. cf-force-takeover is
                dangerous and can lead to data corruption; in almost all
                cases, use cf-takeover instead.
        
        :param version_mismatch_ok: This allows takeover if the partner was running an
                incompatible operating system version and was
                cleanly halted.  This option is used for non-disruptive
                upgrade(NDU).
        
        :param immediate: This causes takeover to be initiated immediately.  The
                taken over node, if up, does not get to shut things down
                in an orderly manner so the takeover of the resources
                takes longer.
        
        :param bypass_optimization: The bypass-optimization option determines whether or
                not an optimized negotiated takeover is run.
                Optimized negotiated takeover refers to the
                serial relocation of SFO aggregates to the taking over node,
                prior to a negotiated takeover. This is an optimization
                because it reduces per-aggregate client outage times.
                If the bypass-optimization option is set to true, then
                the takeover optimization is bypassed, and the normal
                takeover code path is executed. The default value for
                this option is false.
        
        :param skip_lif_migration: This option results in migration of LIFs to be skipped prior
                to a takeover. The default value is `false` and hence the
                default behavior is to synchronously migrate data and
                cluster management LIFs away from the node prior to its
                takeover.
        
        :param allow_disk_inventory_mismatch: This allows takeover if disk inventory information is
                mismatched for non root volume disks. If mismatched,
                local node performance could degrade as what appears
                to be missing disks are rebuilt.
                NOTE:: When using this option and if some of partner's
                file system disks are not visible to local node, then
                after giveback those missing disks can create new
                failed aggregate with same name. So, if any aggregate
                is offline after giveback with same name then using
                "zapi_aggr_destroy", you have to destroy that
                offline aggregate.
        """
        return self.request( "cf-takeover", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'version_mismatch_ok': [ version_mismatch_ok, 'version-mismatch-ok', [ bool, 'None' ], False ],
            'immediate': [ immediate, 'immediate', [ bool, 'None' ], False ],
            'bypass_optimization': [ bypass_optimization, 'bypass-optimization', [ bool, 'None' ], False ],
            'skip_lif_migration': [ skip_lif_migration, 'skip-lif-migration', [ bool, 'None' ], False ],
            'allow_disk_inventory_mismatch': [ allow_disk_inventory_mismatch, 'allow-disk-inventory-mismatch', [ bool, 'None' ], False ],
        }, {
        } )
    
    def cf_aggregate_giveback_status(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns giveback status of all the aggregates in the cluster
        which are taken over or were given back.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the cf
                object.
                All cf objects matching this query up to 'max-records' will be
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
        return self.request( "cf-aggregate-giveback-status", {
            'max_records': max_records,
            'query': [ query, 'query', [ CfAggregateGivebackInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CfAggregateGivebackInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CfAggregateGivebackInfo, True ],
        } )
    
    def cf_service_disable(self, node):
        """
        Disables the takeover capability of this filer in the cluster.
        takeover service is not yet initialized
        takeover service is not licensed.
        takeover service is not enabled
        Can't disable while a revert is in progress
        
        :param node: This parameter is the name of the node on which service is to be disabled
        """
        return self.request( "cf-service-disable", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cf_hwassist_stats(self, node):
        """
        Get useful information about statistics of hardware assisted
        takeover functionality.
        
        :param node: Node name of the filer for which the API is requested.
        """
        return self.request( "cf-hwassist-stats", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'hwassist-stats-times-throttled': [ basestring, False ],
            'hwassist-stats-bad-nvram-id': [ basestring, False ],
            'hwassist-stats-power-off-via-sp': [ basestring, False ],
            'hwassist-stats-reset-via-sp': [ basestring, False ],
            'hwassist-stats-loss-of-heartbeat': [ basestring, False ],
            'hwassist-stats-abnormal-reboot': [ basestring, False ],
            'no-stats': [ basestring, False ],
            'hwassist-stats-power-loss': [ basestring, False ],
            'hwassist-stats-unknown-alerts': [ basestring, False ],
            'hwassist-stats-power-cycle-via-sp': [ basestring, False ],
            'hwassist-stats-test': [ basestring, False ],
            'hwassist-stats-ss-mismatch': [ basestring, False ],
            'hwassist-stats-reset-via-rlm': [ basestring, False ],
            'hwassist-stats-keep-alive': [ basestring, False ],
            'hwassist-stats-post-error': [ basestring, False ],
            'hwassist-stats-power-cycle-via-rlm': [ basestring, False ],
            'hwassist-stats-watchdog-reset': [ basestring, False ],
            'hwassist-stats-power-off-via-rlm': [ basestring, False ],
        } )
    
    def cf_negotiated_failover_status(self, module):
        """
        Returns the status of the negotiated failover module.
        Negotiated failover is a general facility which supports
        negotiated failover on the basis of decisions made by
        various modules.
        
        :param module: Module currently supported is 'disk_shelf'
        """
        return self.request( "cf-negotiated-failover-status", {
            'module': [ module, 'module', [ basestring, 'None' ], False ],
        }, {
            'is-enabled': [ bool, False ],
        } )
    
    def cf_get_partner(self, node):
        """
        Get the host name of the partner. If the name is unknown,
        It will return partner-unknown.
        
        :param node: The node name is passed as an argument
        """
        return self.request( "cf-get-partner", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'partner': [ basestring, False ],
        } )
    
    def cf_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of cf or a group of
        cf objects.
        
        :param query: If modifying a specific cf, this input element must specify all
                keys.
                If modifying cf objects based on query, this input element must
                specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching cf even
                when the modification of a previous matching cf fails, and do so
                until the total number of objects failed to be modified reaches
                the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of cf objects (just
                keys) that were successfully updated.
                If set to false, the list of cf objects modified will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple cf objects match a
                given query.
                If set to true, the API will continue modifying the next matching
                cf even when modification of a previous cf fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of cf objects (just
                keys) that were not modified due to some error.
                If set to false, the list of cf objects not modified will not be
                returned.
                Default: true
        """
        return self.request( "cf-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ OptionsRelatedInfoModify, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ OptionsRelatedInfoModify, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ CfModifyIterInfo, True ],
            'failure-list': [ CfModifyIterInfo, True ],
        } )
    
    def cf_hwassist_status(self, node):
        """
        Get useful information about the status of hw_assist
        functionality.
        
        :param node: Node name of the filer for which the API is requested.
        """
        return self.request( "cf-hwassist-status", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'no-status': [ basestring, False ],
            'partner-hwassist-inactive-corrective-action': [ basestring, False ],
            'local-hwassist-inactive-corrective-action': [ basestring, False ],
            'partner-hwassist-port': [ int, False ],
            'local-hwassist-inactive-reason': [ basestring, False ],
            'local-hwassist-ipaddr': [ basestring, False ],
            'local-hwassist-status': [ basestring, False ],
            'partner-hwassist-ipaddr': [ basestring, False ],
            'local-hwassist-port': [ int, False ],
            'partner-hwassist-status': [ basestring, False ],
            'partner-hwassist-inactive-reason': [ basestring, False ],
            'keep-alive-status': [ basestring, False ],
        } )
    
    def cf_negotiated_failover_enable(self, module):
        """
        Enables negotiated failover. disk_shelf
        is the negotiated failover module currently supported.
        
        :param module: Module currently supported is 'disk_shelf'.
        """
        return self.request( "cf-negotiated-failover-enable", {
            'module': [ module, 'module', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cf_hwassist_test(self, node):
        """
        Validates the hardware-assisted takeover configuration.
        functionality.
        
        :param node: Node name of the filer for which the API is requested.
        """
        return self.request( "cf-hwassist-test", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'hwassist-test-result': [ basestring, False ],
        } )
    
    def cf_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of cf objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the cf
                object.
                All cf objects matching this query up to 'max-records' will be
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
        return self.request( "cf-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ StorageFailoverInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ StorageFailoverInfo, 'None' ], False ],
        }, {
            'attributes-list': [ StorageFailoverInfo, True ],
        } )
    
    def cf_status(self, node):
        """
        Get useful information about the status of the high availability
        service. If the monitor is not initialized, this returns
        an error.
        Invalid node parameter
        
        :param node: This parameter is the name of the node for which High Availability service status is being requested
        """
        return self.request( "cf-status", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'local-mailbox-disks': [ SfDiskInfo, True ],
            'time-since-takeover': [ int, False ],
            'current-resource-table-entry': [ basestring, False ],
            'takeover-reason': [ basestring, False ],
            'takeover-by-partner-possible': [ bool, False ],
            'partner-in-headswap': [ bool, False ],
            'transit-event-time': [ int, False ],
            'partner': [ basestring, False ],
            'kill-packets': [ bool, False ],
            'backup-mailbox-status': [ MailboxStatusInfo, True ],
            'current-resource-table-entry-index': [ int, False ],
            'partner-missing-disks': [ SfDiskInfo, True ],
            'giveback-state': [ basestring, False ],
            'control-partner-aggregates': [ bool, False ],
            'partner-firmware-state': [ basestring, False ],
            'time-until-auto-giveback': [ int, False ],
            'current-giveback-module': [ basestring, False ],
            'interconnect-links': [ basestring, False ],
            'partner-name': [ basestring, False ],
            'local-firmware-progress': [ int, False ],
            'state': [ basestring, False ],
            'current-mode': [ basestring, False ],
            'node-state': [ basestring, False ],
            'takeover-possible': [ bool, False ],
            'giveback-failure-reason': [ basestring, False ],
            'time-until-takeover': [ int, False ],
            'sf-options': [ SfOptionsInfo, False ],
            'nvram-id': [ int, False ],
            'current-takeover-module': [ basestring, False ],
            'fanta-reloc-aggr-count': [ int, False ],
            'is-interconnect-up': [ bool, False ],
            'primary-io-times': [ MailboxIoTimesInfo, False ],
            'interconnect-type': [ basestring, False ],
            'takeover-failure-reason': [ basestring, False ],
            'booting-received': [ int, False ],
            'is-enabled': [ bool, False ],
            'current-time': [ int, False ],
            'local-firmware-state': [ basestring, False ],
            'takeover-of-partner-not-possible-reason': [ TakeoverInfo, True ],
            'partner-firmware-progress': [ int, False ],
            'backup-io-times': [ MailboxIoTimesInfo, False ],
            'partner-mailbox-disks': [ SfDiskInfo, True ],
            'firmware-received': [ int, False ],
            'name': [ basestring, False ],
            'local-in-headswap': [ bool, False ],
            'resource-table': [ ResourceTableInfo, True ],
            'timeouts': [ TimeoutInfo, False ],
            'new-partner-sysid': [ int, False ],
            'primary-mailbox-status': [ MailboxStatusInfo, True ],
            'partner-nvram-id': [ int, False ],
            'local-missing-disks': [ SfDiskInfo, True ],
            'max-resource-table-index': [ int, False ],
            'takeover-by-partner-not-possible-reason': [ TakeoverInfo, True ],
            'logs-unsynced-count': [ int, False ],
            'takeover-state': [ basestring, False ],
        } )
    
    def cf_takeover_status(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the takeover status of a node and the takeover status of all
        its partner aggregates, for all nodes in a cluster.
        Migration failed in a core step.
        Aggregate does not have SFO policy.
        Aggregate in failed or limbo state.
        Offline of the aggregate failed.
        Migration was vetoed.
        Migration failed due to HA messaging errors.
        Aggregate did not come online after migration.
        Failed to online the aggregate.
        NETRA check failed.
        Precommit failed.
        Aggregate in restricted state.
        Aggregate in offline state.
        Aggregate in foreign state.
        Mirrored aggregate with both plexes not online.
        Migration failed as background disk firmware update
        could not be disabled on source node.
        Migration failed as background disk firmware update
        could not be disabled on destination node.
        Aggregate does not have any disks.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                aggr object.
                All aggr objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the
                previous call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is
                available will be returned.
                If present, only the desired attributes for which information
                is available will be returned.
        """
        return self.request( "cf-takeover-status", {
            'max_records': max_records,
            'query': [ query, 'query', [ TakeoverStatus, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TakeoverStatus, 'None' ], False ],
        }, {
            'attributes-list': [ TakeoverStatus, True ],
        } )
    
    def cf_negotiated_failover_disable(self, module):
        """
        Disables negotiated failover. disk_shelf
        is the negotiated failover module currently supported.
        
        :param module: Module currently supported is 'disk_shelf'.
        """
        return self.request( "cf-negotiated-failover-disable", {
            'module': [ module, 'module', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cf_hwassist_stats_clear(self, node):
        """
        Get useful information about stats of hw_assist
        functionality.
        
        :param node: Node name of the filer for which the API is requested.
        """
        return self.request( "cf-hwassist-stats-clear", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cf_giveback(self, node, require_partner_waiting=None, override_vetoes=None, force=None, only_cfo_aggregates=None):
        """
        Initiates a giveback of partner resources. Once the giveback
        is complete, the automatic takeover capability is disabled
        until the partner is rebooted. A giveback fails if outstanding
        CIFS sessions, active system dump processes, or other filer
        operations makes a giveback dangerous or disruptive.
        The partner is not waiting to receive the aggregates.
        We will not normally allow the aggregates to be given back
        if the partner is not up and waiting to receive them.
        There are no aggregates whose "home location" is the partner
        filer.
        There's already an "cf-giveback" operation in progress.
        A takeover operation is in progress.
        The dblade is shutting down.
        The partner has not sent its disk inventory information.
        The partner is missing its disks.
        Invalid node parameter
        The partner node is taking over the local node.
        Aggregate Relocation (ARL) is in progress.
        
        :param node: This parameter is the name of the node which performs giveback
                to its partner.
        
        :param require_partner_waiting: When set to true, this ensures that the process of
                giveback of the aggregates is not initiated if the partner is not
                up and waiting to receive them. When set to false, this allows
                the process of giveback of the aggregates to proceed even if the
                partner is not up and waiting to receive them. The default value is true.
        
        :param override_vetoes: Some conditions cause attempts to giveback aggregates
                to be vetoed. When set to true, this allows the
                process of giveback of the aggregates to be initiated even in
                the face of such vetoes. When set to false, this does not allow
                the process of giveback of the aggregates to proceed if there
                are any vetoes. The default value is false.
        
        :param force: When set to true, this allows a giveback to proceed
                even if there are outstanding CIFS sessions, active system
                dump processes, or other filer operations which makes a giveback
                dangerous or disruptive as long as it would not result
                in data corruption or filer error. When set to false, this does
                not allow a giveback to proceed if there are outstanding CIFS
                sessions, active system dump processes, or other filer operations
                which makes a giveback dangerous or disruptive.
                The default value is false.
        
        :param only_cfo_aggregates: When set to true, only the CFO HA-style aggregates
                (which includes the root aggregate) will be given back.
                This may be needed in the case when the partner node's VLDB
                and other such management applications are not properly working
                (they are required to be online for the SFO HA-style aggregates to start
                serving data), so it might not be possible to giveback SFO HA-style
                aggregates. When set to false, all the aggregates
                (CFO HA-style aggregates + SFO HA-style aggregates) will be given back.
                The default value is false.
        """
        return self.request( "cf-giveback", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'require_partner_waiting': [ require_partner_waiting, 'require-partner-waiting', [ bool, 'None' ], False ],
            'override_vetoes': [ override_vetoes, 'override-vetoes', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'only_cfo_aggregates': [ only_cfo_aggregates, 'only-cfo-aggregates', [ bool, 'None' ], False ],
        }, {
        } )
    
    def cf_force_takeover(self, node, disaster=None):
        """
        Forces one filer to take over its partner even though the
        filer detects an error that would otherwise prevent a
        takeover. For example, normally, if a detached or faulty
        interconnect cable between the filers causes the filers'
        NVRAM contents to be unsynchronized, takeover is disabled.
        However, this will allow the filer to take over its partner
        despite the unsynchronized NVRAM contents.
        cf-force-takeover is dangerous and can lead to data
        corruption; in almost all cases, use cf-takeover instead.
        Already doing takeover.
        A giveback operation is in progress.
        Takeover is not possible due to a partner file system
        or other version mismatch.
        Partner mailboxes are degraded.
        One or more of the strings in takeover-options does not
        specify a legal value.
        Waiting for partner recovery.
        Partner is not halted (VERSION_MISMATCH_OK option only).
        Invalid node parameter
        
        :param node: This parameter is the name of the node which is doing a
                takeover of its partner.
        
        :param disaster: When set to true, forces a filer to take over its partner
                in all cases where a force-takeover would. In addition it
                will force a takeover even if some partner mailbox disks
                are inaccessible. It can only be used when remotesyncmirror
                is licensed.  This option is very dangerous. Not only can
                it cause data corruption, if not used carefully, it can
                also lead to a situation where both the filer and it's
                partner are operational (split brain). As such, it should
                only be used as a means of last resort when the takeover and
                force-takeover operations are unsuccessful in achieving a
                takeover. The operator must ensure that the partner filer
                does not become operational at any time while a filer is
                in a takeover mode initiated by the use of this operation.
                In conjunction with RAID mirroring, it can allow recovery
                from a disaster when the two filers are setup in a
                MetroCluster configuration.
        """
        return self.request( "cf-force-takeover", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'disaster': [ disaster, 'disaster', [ bool, 'None' ], False ],
        }, {
        } )
