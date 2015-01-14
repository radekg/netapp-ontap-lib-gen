from netapp.connection import NaConnection
from asup_invoke_style import AsupInvokeStyle # 0 properties
from autosupport_destinations_get_iter_key_td import AutosupportDestinationsGetIterKeyTd # 1 properties
from autosupport_history_info import AutosupportHistoryInfo # 10 properties
from autosupport_destinations_info import AutosupportDestinationsInfo # 2 properties
from compression_format import CompressionFormat # 0 properties
from autosupport_trigger_get_iter_key_td import AutosupportTriggerGetIterKeyTd # 2 properties
from autosupport_manifest_get_iter_key_td import AutosupportManifestGetIterKeyTd # 3 properties
from autosupport_trigger_info import AutosupportTriggerInfo # 10 properties
from autosupport_budget_get_iter_key_td import AutosupportBudgetGetIterKeyTd # 2 properties
from asup_status import AsupStatus # 0 properties
from autosupport_cmd_tgt import AutosupportCmdTgt # 0 properties
from autosupport_history_get_iter_key_td import AutosupportHistoryGetIterKeyTd # 3 properties
from autosupport_compliant_info import AutosupportCompliantInfo # 4 properties
from asup_destination import AsupDestination # 0 properties
from asup_manifest_status import AsupManifestStatus # 0 properties
from autosupport_manifest_info import AutosupportManifestInfo # 13 properties
from asup_transport import AsupTransport # 0 properties
from asup_content_type import AsupContentType # 0 properties
from autosupport_config_get_iter_key_td import AutosupportConfigGetIterKeyTd # 1 properties
from autosupport_compliant_get_iter_key_td import AutosupportCompliantGetIterKeyTd # 2 properties
from asup_subsystems import AsupSubsystems # 0 properties
from autosupport_budget_info import AutosupportBudgetInfo # 4 properties
from autosupport_config_info import AutosupportConfigInfo # 33 properties

class AutosupportConnection(NaConnection):
    
    def autosupport_invoke(self, node_name, type, message=None, force=None, uri=None):
        """
        Generate a new AutoSupport message
        
        :param node_name: The name of the filer on which the AutoSupport message will be
                generated.
        
        :param type: The type of AutoSupport to generate.
                Possible values:
                <ul>
                <li> "test"           - Test AutoSupport send and receive
                only,
                <li> "performance"    - Generate a Performance AutoSupport as
                requested by technical support,
                <li> "all"            - Send all AutoSupport data without time
                or size limit, as requested by technical support
                </ul>
        
        :param message: Text to include as part of the subject of the AutoSupport
                message.
        
        :param force: Force generation, even if AutoSupport is disabled in the system.
                The default value is false.
        
        :param uri: Alternate destination for the AutoSupport.  If this field is
                omitted, the AutoSupport will be delivered to the currently
                configured destinations.
        """
        return self.request( "autosupport-invoke", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'message': [ message, 'message', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'asup-invoke-style' ], False ],
            'uri': [ uri, 'uri', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autosupport_trigger_modify(self, node_name, trigger, to_enabled=None, noteto_enabled=None, time_limit=None, basic_additional=None, troubleshooting_additional=None):
        """
        Modify the AutoSupport trigger data for the given node and EMS
        message.
        
        :param node_name: Node
        
        :param trigger: EMS Message
        
        :param to_enabled: Deliver to AutoSupport -to Addresses. Possible values are:
                enabled or disabled.
        
        :param noteto_enabled: Deliver to AutoSupport -noteto Addresses. Possible values are:
                enabled or disabled.
        
        :param time_limit: The data collection time budget for this trigger (in seconds).
                Content not collected will be marked as
                collection-truncated-time-limit in the manifest.
        
        :param basic_additional: Additional Subsystems Reporting Basic Info
                Possible values:
                <ul>
                <li> "platform"                 - Hardware information about
                the node,
                <li> "mhost"                    - User Space application
                information for a node,
                <li> "log_files"                - Log files for a node,
                <li> "performance"              - This subsystem gathers the
                .cm_stats_hourly_done file and user space counters,
                <li> "performance_asup"         - Performance specific
                information for a node,
                <li> "nht"                      - This subsystem gathers the
                /mroot/etc/log/nht_info content,
                <li> "san"                      - SAN specific information for
                a node,
                <li> "snapvault"                - SNAPVAULT specific
                information for a node,
                <li> "snapmirror"               - Snapmirror specific
                information for a node,
                <li> "dedupe"                   - Dedupe specific information
                for a node,
                <li> "nfs"                      - NFS specific information for
                a node,
                <li> "wafl"                     - WAFL specific information for
                a node,
                <li> "mot"                      - MOT specific information for
                a node,
                <li> "ha"                       - HA specific information for a
                node,
                <li> "networking"               - Networking specific
                information for a node,
                <li> "cifs"                     - CIFS specific information for
                a node,
                <li> "fpolicy"                  - Fpolicy specific information
                for a node,
                <li> "multistore"               - Multistore specific
                information for a node,
                <li> "raid"                     - RAID specific information for
                a node,
                <li> "storage"                  - Storage specific information
                for a node,
                <li> "asup_ems"                 - ASUP EMS specific information
                for a node,
                <li> "tape"                     - Tape specific information for
                a node,
                <li> "kernel"                   - kernel specific information
                for a node,
                <li> "secd"                     - SECD specific information for
                a node,
                <li> "metrocluster"             - Metrocluster specific
                information for a node,
                <li> "mandatory"                - Mandatory Basic information
                for a node,
                <li> "repository"               - Repository specific
                information for a node,
                <li> "splog_downcontroller"     - SPLOG saved when ontap is
                abnormal down,
                <li> "splog_latest"             - Up-to-date SPLOG from Service
                Processor FW  ,
                <li> "splog_before_spreboot"    - Up-to-date SPLOG from Service
                Processor FW before SP reboot,
                <li> "hm"                       - Health Monitor Alerts
                specific information,
                <li> "kcs"                      - Kernel Cluster Services
                information for a node,
                <li> "av"                       - Antivirus specific
                information for a node,
                <li> "san_ffdc"                 - SAN specific trace dumps for
                a node,
                <li> "nwd"                      - Node Watchdog specific
                information for a node,
                <li> "vscan"                    - Vscan specific information
                for a node
                </ul>
        
        :param troubleshooting_additional: Additional Subsystems Reporting Troubleshooting Info
                Possible values:
                <ul>
                <li> "platform"                 - Hardware information about
                the node,
                <li> "mhost"                    - User Space application
                information for a node,
                <li> "log_files"                - Log files for a node,
                <li> "performance"              - This subsystem gathers the
                .cm_stats_hourly_done file and user space counters,
                <li> "performance_asup"         - Performance specific
                information for a node,
                <li> "nht"                      - This subsystem gathers the
                /mroot/etc/log/nht_info content,
                <li> "san"                      - SAN specific information for
                a node,
                <li> "snapvault"                - SNAPVAULT specific
                information for a node,
                <li> "snapmirror"               - Snapmirror specific
                information for a node,
                <li> "dedupe"                   - Dedupe specific information
                for a node,
                <li> "nfs"                      - NFS specific information for
                a node,
                <li> "wafl"                     - WAFL specific information for
                a node,
                <li> "mot"                      - MOT specific information for
                a node,
                <li> "ha"                       - HA specific information for a
                node,
                <li> "networking"               - Networking specific
                information for a node,
                <li> "cifs"                     - CIFS specific information for
                a node,
                <li> "fpolicy"                  - Fpolicy specific information
                for a node,
                <li> "multistore"               - Multistore specific
                information for a node,
                <li> "raid"                     - RAID specific information for
                a node,
                <li> "storage"                  - Storage specific information
                for a node,
                <li> "asup_ems"                 - ASUP EMS specific information
                for a node,
                <li> "tape"                     - Tape specific information for
                a node,
                <li> "kernel"                   - kernel specific information
                for a node,
                <li> "secd"                     - SECD specific information for
                a node,
                <li> "metrocluster"             - Metrocluster specific
                information for a node,
                <li> "mandatory"                - Mandatory Basic information
                for a node,
                <li> "repository"               - Repository specific
                information for a node,
                <li> "splog_downcontroller"     - SPLOG saved when ontap is
                abnormal down,
                <li> "splog_latest"             - Up-to-date SPLOG from Service
                Processor FW  ,
                <li> "splog_before_spreboot"    - Up-to-date SPLOG from Service
                Processor FW before SP reboot,
                <li> "hm"                       - Health Monitor Alerts
                specific information,
                <li> "kcs"                      - Kernel Cluster Services
                information for a node,
                <li> "av"                       - Antivirus specific
                information for a node,
                <li> "san_ffdc"                 - SAN specific trace dumps for
                a node,
                <li> "nwd"                      - Node Watchdog specific
                information for a node,
                <li> "vscan"                    - Vscan specific information
                for a node
                </ul>
        """
        return self.request( "autosupport-trigger-modify", {
            'to_enabled': [ to_enabled, 'to-enabled', [ basestring, 'None' ], False ],
            'noteto_enabled': [ noteto_enabled, 'noteto-enabled', [ basestring, 'None' ], False ],
            'time_limit': [ time_limit, 'time-limit', [ basestring, 'None' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'trigger': [ trigger, 'trigger', [ basestring, 'None' ], False ],
            'basic_additional': [ basic_additional, 'basic-additional', [ basestring, 'asup-subsystems' ], True ],
            'troubleshooting_additional': [ troubleshooting_additional, 'troubleshooting-additional', [ basestring, 'asup-subsystems' ], True ],
        }, {
        } )
    
    def autosupport_budget_get(self, subsystem, node_name, desired_attributes=None):
        """
        Get AutoSupport time and size limits for the given node and
        subsystem.
        
        :param subsystem: The name of a subsystem from which AutoSupport collects data.
                Possible values:
                <ul>
                <li> "platform"                 - Hardware information about
                the node,
                <li> "mhost"                    - User Space application
                information for a node,
                <li> "log_files"                - Log files for a node,
                <li> "performance"              - This subsystem gathers the
                .cm_stats_hourly_done file and user space counters,
                <li> "performance_asup"         - Performance specific
                information for a node,
                <li> "nht"                      - This subsystem gathers the
                /mroot/etc/log/nht_info content,
                <li> "san"                      - SAN specific information for
                a node,
                <li> "snapvault"                - SNAPVAULT specific
                information for a node,
                <li> "snapmirror"               - Snapmirror specific
                information for a node,
                <li> "dedupe"                   - Dedupe specific information
                for a node,
                <li> "nfs"                      - NFS specific information for
                a node,
                <li> "wafl"                     - WAFL specific information for
                a node,
                <li> "mot"                      - MOT specific information for
                a node,
                <li> "ha"                       - HA specific information for a
                node,
                <li> "networking"               - Networking specific
                information for a node,
                <li> "cifs"                     - CIFS specific information for
                a node,
                <li> "fpolicy"                  - Fpolicy specific information
                for a node,
                <li> "multistore"               - Multistore specific
                information for a node,
                <li> "raid"                     - RAID specific information for
                a node,
                <li> "storage"                  - Storage specific information
                for a node,
                <li> "asup_ems"                 - ASUP EMS specific information
                for a node,
                <li> "tape"                     - Tape specific information for
                a node,
                <li> "kernel"                   - kernel specific information
                for a node,
                <li> "secd"                     - SECD specific information for
                a node,
                <li> "metrocluster"             - Metrocluster specific
                information for a node,
                <li> "mandatory"                - Mandatory Basic information
                for a node,
                <li> "repository"               - Repository specific
                information for a node,
                <li> "splog_downcontroller"     - SPLOG saved when ontap is
                abnormal down,
                <li> "splog_latest"             - Up-to-date SPLOG from Service
                Processor FW  ,
                <li> "splog_before_spreboot"    - Up-to-date SPLOG from Service
                Processor FW before SP reboot,
                <li> "hm"                       - Health Monitor Alerts
                specific information,
                <li> "kcs"                      - Kernel Cluster Services
                information for a node,
                <li> "av"                       - Antivirus specific
                information for a node,
                <li> "san_ffdc"                 - SAN specific trace dumps for
                a node,
                <li> "nwd"                      - Node Watchdog specific
                information for a node,
                <li> "vscan"                    - Vscan specific information
                for a node
                </ul>
        
        :param node_name: The name of a filer on which the AutoSupport tool is running.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-budget-get", {
            'subsystem': [ subsystem, 'subsystem', [ basestring, 'asup-subsystems' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportBudgetInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportBudgetInfo, False ],
        } )
    
    def autosupport_trigger_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a list of the AutoSupport trigger data for all nodes.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-trigger object.
                All autosupport-trigger objects matching this query up to
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
        return self.request( "autosupport-trigger-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportTriggerInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportTriggerInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportTriggerInfo, True ],
        } )
    
    def autosupport_budget_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get AutoSupport time and size limits per subsystem for all
        nodes.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-budget object.
                All autosupport-budget objects matching this query up to
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
        return self.request( "autosupport-budget-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportBudgetInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportBudgetInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportBudgetInfo, True ],
        } )
    
    def autosupport_manifest_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-manifest-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_budget_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-budget-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_compliant_get(self, node, plaintext, desired_attributes=None):
        """
        Get AutoSupport compliance hash mapping
        
        :param node: Node
        
        :param plaintext: Plaintext
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-compliant-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'plaintext': [ plaintext, 'plaintext', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportCompliantInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportCompliantInfo, False ],
        } )
    
    def autosupport_config_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-config-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_config_modify(self, node_name, is_throttle_enabled=None, ondemand_polling_interval=None, is_nht_data_enabled=None, max_smtp_size=None, is_perf_data_enabled=None, transport=None, ondemand_server_url=None, post_url=None, from=None, mail_hosts=None, max_http_size=None, is_reminder_enabled=None, to=None, partner_address=None, put_url=None, is_private_data_removed=None, is_ondemand_remote_diag_enabled=None, noteto=None, is_enabled=None, periodic_tx_window=None, proxy_url=None, is_local_collection_enabled=None, payload_format=None, support_address=None, retry_count=None, is_node_in_subject=None, is_support_enabled=None, minimum_private_data_length=None, is_ondemand_enabled=None, retry_interval=None):
        """
        Modify AutoSupport configuration settings for the given node.
        
        :param node_name: The name of the filer that owns the AutoSupport configuration.
        
        :param is_throttle_enabled: Specifies whether to enable / disable throttling to prevent a
                potential avalanche of AutoSupport messages.
        
        :param ondemand_polling_interval: The AutoSupport OnDemand Client polling rate in minutes.
        
        :param is_nht_data_enabled: Used to enable / disable collection of disk health data.
        
        :param max_smtp_size: Delivery size limit for the SMTP transport protocol (in bytes).
        
        :param is_perf_data_enabled: Used to enable / disable collection of Performance AutoSupport
                data.
        
        :param transport: The name of the transport protocol used to deliver AutoSupport
                messages.
                Possible values:
                <ul>
                <li> "smtp"      ,
                <li> "http"      ,
                <li> "https"
                </ul>
        
        :param ondemand_server_url: The AutoSupport OnDemand Server URL.
        
        :param post_url: The URL used to deliver AutoSupport messages via HTTP POST.
        
        :param from: The e-mail address of the local administrator, used as the sender
                of the AutoSupport message.
        
        :param mail_hosts: The name of the mail server(s) used to deliver AutoSupport
                messages via SMTP.  Both host names and IP addresses may be used
                as valid input. One can optionally specify a username/password
                for authentication with the mailserver(rfc4954).
        
        :param max_http_size: Delivery size limit for the HTTP transport protocol (in bytes).
        
        :param is_reminder_enabled: Specifies whether to enable / disable AutoSupport reminders.
        
        :param to: Specifies up to five recipients of full AutoSupport e-mail
                messages.
        
        :param partner_address: Specifies up to five partner vendor recipients of full
                AutoSupport e-mail messages.
        
        :param put_url: The URL used to deliver AutoSupport messages via HTTP PUT.
        
        :param is_private_data_removed: Used to enable / disable removal of customer-supplied data.
        
        :param is_ondemand_remote_diag_enabled: Specifies whether the AutoSupport OnDemand Remote Diagnostics
                feature is enabled. Default is true.
        
        :param noteto: Specifies up to five recipients of short AutoSupport e-mail
                messages.
        
        :param is_enabled: Specifies whether the AutoSupport daemon is enabled.  When this
                setting is disabled, delivery of all AutoSupport messages is
                turned off.
        
        :param periodic_tx_window: The transmission window (seconds).
        
        :param proxy_url: Optional proxy host for AutoSupport message delivery via HTTP.
        
        :param is_local_collection_enabled: Used to enable / disable collection of AutoSupport data when the
                AutoSupport daemon is disabled.  When this setting is true,
                collection of AutoSupport data will still be done if is-enabled
                is false.
        
        :param payload_format: The format used to compress the AutoSupport message payload.
                Possible values:
                <ul>
                <li> "7z"   - 7-Zip Archive,
                <li> "tgz"  - Zipped Tarball
                </ul>
        
        :param support_address: The e-mail address of Support.
        
        :param retry_count: The maximum number of delivery attempts for an AutoSupport
                message.
        
        :param is_node_in_subject: Specifies whether the filer's hostname should be part of an
                AutoSupport message's subject field.
        
        :param is_support_enabled: Specifies whether AutoSupport notification to technical support
                is enabled.
        
        :param minimum_private_data_length: Minimum Length for Sensitive Data
        
        :param is_ondemand_enabled: Specifies whether AutoSupport OnDemand is enabled. Default is
                true.
        
        :param retry_interval: The number of seconds to wait, after a failed delivery attempt,
                prior to re-transmitting an AutoSupport message.
        """
        return self.request( "autosupport-config-modify", {
            'is_throttle_enabled': [ is_throttle_enabled, 'is-throttle-enabled', [ bool, 'None' ], False ],
            'ondemand_polling_interval': [ ondemand_polling_interval, 'ondemand-polling-interval', [ int, 'None' ], False ],
            'is_nht_data_enabled': [ is_nht_data_enabled, 'is-nht-data-enabled', [ bool, 'None' ], False ],
            'max_smtp_size': [ max_smtp_size, 'max-smtp-size', [ int, 'None' ], False ],
            'is_perf_data_enabled': [ is_perf_data_enabled, 'is-perf-data-enabled', [ bool, 'None' ], False ],
            'transport': [ transport, 'transport', [ basestring, 'asup-transport' ], False ],
            'ondemand_server_url': [ ondemand_server_url, 'ondemand-server-url', [ basestring, 'None' ], False ],
            'post_url': [ post_url, 'post-url', [ basestring, 'None' ], False ],
            'from': [ from, 'from', [ basestring, 'mail-address' ], False ],
            'mail_hosts': [ mail_hosts, 'mail-hosts', [ basestring, 'None' ], True ],
            'max_http_size': [ max_http_size, 'max-http-size', [ int, 'None' ], False ],
            'is_reminder_enabled': [ is_reminder_enabled, 'is-reminder-enabled', [ bool, 'None' ], False ],
            'to': [ to, 'to', [ basestring, 'mail-address' ], True ],
            'partner_address': [ partner_address, 'partner-address', [ basestring, 'mail-address' ], True ],
            'put_url': [ put_url, 'put-url', [ basestring, 'None' ], False ],
            'is_private_data_removed': [ is_private_data_removed, 'is-private-data-removed', [ bool, 'None' ], False ],
            'is_ondemand_remote_diag_enabled': [ is_ondemand_remote_diag_enabled, 'is-ondemand-remote-diag-enabled', [ bool, 'None' ], False ],
            'noteto': [ noteto, 'noteto', [ basestring, 'mail-address' ], True ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
            'periodic_tx_window': [ periodic_tx_window, 'periodic-tx-window', [ basestring, 'None' ], False ],
            'proxy_url': [ proxy_url, 'proxy-url', [ basestring, 'None' ], False ],
            'is_local_collection_enabled': [ is_local_collection_enabled, 'is-local-collection-enabled', [ bool, 'None' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'payload_format': [ payload_format, 'payload-format', [ basestring, 'compression-format' ], False ],
            'support_address': [ support_address, 'support-address', [ basestring, 'mail-address' ], True ],
            'retry_count': [ retry_count, 'retry-count', [ int, 'None' ], False ],
            'is_node_in_subject': [ is_node_in_subject, 'is-node-in-subject', [ bool, 'None' ], False ],
            'is_support_enabled': [ is_support_enabled, 'is-support-enabled', [ bool, 'None' ], False ],
            'minimum_private_data_length': [ minimum_private_data_length, 'minimum-private-data-length', [ int, 'None' ], False ],
            'is_ondemand_enabled': [ is_ondemand_enabled, 'is-ondemand-enabled', [ bool, 'None' ], False ],
            'retry_interval': [ retry_interval, 'retry-interval', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autosupport_destinations_get_total_records(self):
        """
        Return the total number of records.  This sould be equal to the
        number of nodes in the cluster.
        """
        return self.request( "autosupport-destinations-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_history_get(self, node_name, destination, seq_num, desired_attributes=None):
        """
        Get a history record for the given AutoSupport.
        
        :param node_name: The name of the filer where the AutoSupport message was
                previously generated.
        
        :param destination: The transport protocol for this AutoSupport message's
                destination.
                Possible values:
                <ul>
                <li> "smtp"           ,
                <li> "http"           ,
                <li> "noteto"         ,
                <li> "retransmit"
                </ul>
        
        :param seq_num: The AutoSupport message sequence number.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-history-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'destination': [ destination, 'destination', [ basestring, 'asup-destination' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportHistoryInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportHistoryInfo, False ],
        } )
    
    def autosupport_manifest_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a detailed manifest for the contents of an AutoSupport.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-manifest object.
                All autosupport-manifest objects matching this query up to
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
        return self.request( "autosupport-manifest-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportManifestInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportManifestInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportManifestInfo, True ],
        } )
    
    def autosupport_history_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the history records for the last 50 AutoSupport messages.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-history object.
                All autosupport-history objects matching this query up to
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
        return self.request( "autosupport-history-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportHistoryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportHistoryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportHistoryInfo, True ],
        } )
    
    def autosupport_config_get(self, node_name, desired_attributes=None):
        """
        Get AutoSupport configuration settings for the given node.
        
        :param node_name: The name of the filer that owns the AutoSupport configuration.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-config-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportConfigInfo, False ],
        } )
    
    def autosupport_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get AutoSupport configuration settings for all nodes.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-config object.
                All autosupport-config objects matching this query up to
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
        return self.request( "autosupport-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportConfigInfo, True ],
        } )
    
    def autosupport_destinations_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the list of AutoSupport destinations for all nodes.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-destinations object.
                All autosupport-destinations objects matching this query up to
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
        return self.request( "autosupport-destinations-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportDestinationsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportDestinationsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportDestinationsInfo, True ],
        } )
    
    def autosupport_trigger_get(self, node_name, trigger, desired_attributes=None):
        """
        Get the AutoSupport trigger data for the given node and EMS
        message.
        
        :param node_name: Node
        
        :param trigger: EMS Message
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-trigger-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'trigger': [ trigger, 'trigger', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportTriggerInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportTriggerInfo, False ],
        } )
    
    def autosupport_budget_modify(self, subsystem, node_name, size_limit=None, time_limit=None):
        """
        Modify AutoSupport time and size limits per subsystem.
        
        :param subsystem: The name of a subsystem from which AutoSupport collects data.
                Possible values:
                <ul>
                <li> "platform"                 - Hardware information about
                the node,
                <li> "mhost"                    - User Space application
                information for a node,
                <li> "log_files"                - Log files for a node,
                <li> "performance"              - This subsystem gathers the
                .cm_stats_hourly_done file and user space counters,
                <li> "performance_asup"         - Performance specific
                information for a node,
                <li> "nht"                      - This subsystem gathers the
                /mroot/etc/log/nht_info content,
                <li> "san"                      - SAN specific information for
                a node,
                <li> "snapvault"                - SNAPVAULT specific
                information for a node,
                <li> "snapmirror"               - Snapmirror specific
                information for a node,
                <li> "dedupe"                   - Dedupe specific information
                for a node,
                <li> "nfs"                      - NFS specific information for
                a node,
                <li> "wafl"                     - WAFL specific information for
                a node,
                <li> "mot"                      - MOT specific information for
                a node,
                <li> "ha"                       - HA specific information for a
                node,
                <li> "networking"               - Networking specific
                information for a node,
                <li> "cifs"                     - CIFS specific information for
                a node,
                <li> "fpolicy"                  - Fpolicy specific information
                for a node,
                <li> "multistore"               - Multistore specific
                information for a node,
                <li> "raid"                     - RAID specific information for
                a node,
                <li> "storage"                  - Storage specific information
                for a node,
                <li> "asup_ems"                 - ASUP EMS specific information
                for a node,
                <li> "tape"                     - Tape specific information for
                a node,
                <li> "kernel"                   - kernel specific information
                for a node,
                <li> "secd"                     - SECD specific information for
                a node,
                <li> "metrocluster"             - Metrocluster specific
                information for a node,
                <li> "mandatory"                - Mandatory Basic information
                for a node,
                <li> "repository"               - Repository specific
                information for a node,
                <li> "splog_downcontroller"     - SPLOG saved when ontap is
                abnormal down,
                <li> "splog_latest"             - Up-to-date SPLOG from Service
                Processor FW  ,
                <li> "splog_before_spreboot"    - Up-to-date SPLOG from Service
                Processor FW before SP reboot,
                <li> "hm"                       - Health Monitor Alerts
                specific information,
                <li> "kcs"                      - Kernel Cluster Services
                information for a node,
                <li> "av"                       - Antivirus specific
                information for a node,
                <li> "san_ffdc"                 - SAN specific trace dumps for
                a node,
                <li> "nwd"                      - Node Watchdog specific
                information for a node,
                <li> "vscan"                    - Vscan specific information
                for a node
                </ul>
        
        :param node_name: The name of a filer on which the AutoSupport tool is running.
        
        :param size_limit: The maximum allowable collection size (in bytes) for the
                subsystem.
        
        :param time_limit: The maximum allowable collection time (in seconds ) for the
                subsystem.
        """
        return self.request( "autosupport-budget-modify", {
            'subsystem': [ subsystem, 'subsystem', [ basestring, 'asup-subsystems' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'size_limit': [ size_limit, 'size-limit', [ int, 'None' ], False ],
            'time_limit': [ time_limit, 'time-limit', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autosupport_compliant_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get AutoSupport compliance hash mapping
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autosupport-compliant object.
                All autosupport-compliant objects matching this query up to
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
        return self.request( "autosupport-compliant-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutosupportCompliantInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportCompliantInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutosupportCompliantInfo, True ],
        } )
    
    def autosupport_history_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-history-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_history_retransmit(self, node_name, seq_num, uri, size_limit=None):
        """
        Selectively retransmit a previously collected AutoSupport
        message.
        
        :param node_name: Node
        
        :param seq_num: AutoSupport Sequence Number
        
        :param uri: Destination to Send this AutoSupport
        
        :param size_limit: Transmit Size Limit for this AutoSupport.
        """
        return self.request( "autosupport-history-retransmit", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'size_limit': [ size_limit, 'size-limit', [ int, 'None' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'None' ], False ],
            'uri': [ uri, 'uri', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autosupport_compliant_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-compliant-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def autosupport_destinations_get(self, node_name, desired_attributes=None):
        """
        Get the list of AutoSupport destinations for the given node.
        
        :param node_name: The name of the filer that owns this destination configuration.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "autosupport-destinations-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutosupportDestinationsInfo, 'None' ], False ],
        }, {
            'attributes': [ AutosupportDestinationsInfo, False ],
        } )
    
    def autosupport_trigger_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "autosupport-trigger-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
