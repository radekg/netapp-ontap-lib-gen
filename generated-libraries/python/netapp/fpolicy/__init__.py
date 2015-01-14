from netapp.connection import NaConnection
from extension_list_info import ExtensionListInfo # 1 properties
from event_name import EventName # 0 properties
from fpolicy_policy_get_iter_key_td import FpolicyPolicyGetIterKeyTd # 2 properties
from monitored_operation_info import MonitoredOperationInfo # 1 properties
from fpolicy_event_options_config import FpolicyEventOptionsConfig # 6 properties
from secondary_server_info import SecondaryServerInfo # 1 properties
from fpolicy_policy_event_get_iter_key_td import FpolicyPolicyEventGetIterKeyTd # 2 properties
from fpolicy_proto import FpolicyProto # 0 properties
from fpolicy_policy_status_info import FpolicyPolicyStatusInfo # 4 properties
from fpolicy_volumes_list_info import FpolicyVolumesListInfo # 1 properties
from fpolicy_filter import FpolicyFilter # 0 properties
from fpolicy_policy_info import FpolicyPolicyInfo # 7 properties
from engine_name import EngineName # 0 properties
from policy_info import PolicyInfo # 10 properties
from fpolicy_policy_external_engine_get_iter_key_td import FpolicyPolicyExternalEngineGetIterKeyTd # 2 properties
from fpolicy_external_engine_info import FpolicyExternalEngineInfo # 17 properties
from fpolicy_server_status_info import FpolicyServerStatusInfo # 9 properties
from fpolicy_operation import FpolicyOperation # 0 properties
from server_info import ServerInfo # 11 properties
from fpolicy_server_type import FpolicyServerType # 0 properties
from fpolicy_policy_status_get_iter_key_td import FpolicyPolicyStatusGetIterKeyTd # 2 properties
from common_name import CommonName # 0 properties
from fpolicy_ssl_opts import FpolicySslOpts # 0 properties
from fpolicy_scope_config import FpolicyScopeConfig # 11 properties
from fpolicy_server_status_get_iter_key_td import FpolicyServerStatusGetIterKeyTd # 4 properties
from monitored_protocol_info import MonitoredProtocolInfo # 1 properties
from fpolicy_policy_scope_get_iter_key_td import FpolicyPolicyScopeGetIterKeyTd # 2 properties
from fpolicy_server_status import FpolicyServerStatus # 0 properties
from external_engine_type import ExternalEngineType # 0 properties

class FpolicyConnection(NaConnection):
    
    def fpolicy_server_disconnect(self, node, policy_name, server):
        """
        Terminate connection to FPolicy server
        
        :param node: Cluster node name.
        
        :param policy_name: Name of the policy.
        
        :param server: FPolicy server.
        """
        return self.request( "fpolicy-server-disconnect", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'server': [ server, 'server', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def fpolicy_volume_list_set(self, policy_name, list_type, volumes):
        """
        Manipulate a list of volumes in an exclude or include set.
        This limits the set of volumes for which client requests
        trigger (include) or suppress (exclude) fpolicy processing
        for the provided policy.
        The list provided will replace the list currently in place,
        if any. Note that if a policy has both an exclude list and
        an include list, the include list is ignored by the filer.
        
        :param policy_name: Name of the policy.
        
        :param list_type: Defines to which set (exclude or include) a list
                will be applied.
                Possible values: "exclude", "include".
        
        :param volumes: List of volume specifications.
        """
        return self.request( "fpolicy-volume-list-set", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'list_type': [ list_type, 'list-type', [ basestring, 'None' ], False ],
            'volumes': [ volumes, 'volumes', [ FpolicyVolumesListInfo, 'None' ], True ],
        }, {
        } )
    
    def fpolicy_set_required(self, policy_name, required):
        """
        Sets policy's "required" option to on/off.
        
        :param policy_name: Name of the policy.
        
        :param required: Indicator if the policy is required. If set to true,
                the request will fail if there is no server to evaluate it.
                If it's false, the request will succeed.
        """
        return self.request( "fpolicy-set-required", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'required': [ required, 'required', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_enable(self):
        """
        Sets options fpolicy enable to on.
        """
        return self.request( "fpolicy-enable", {
        }, {
        } )
    
    def fpolicy_server_stop(self, server_ip, policy_name):
        """
        Stops specific primary server serving the policy.
        Effectively, this will unregister the fpolicy server.
        
        :param server_ip: The ip address, in dotted-decimal format, of the server.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-server-stop", {
            'server_ip': [ server_ip, 'server-ip', [ basestring, 'ip-address' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_server_connect(self, node, policy_name, server):
        """
        Make a connection to FPolicy server
        
        :param node: Cluster node name.
        
        :param policy_name: Name of the policy.
        
        :param server: FPolicy server.
        """
        return self.request( "fpolicy-server-connect", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'server': [ server, 'server', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def fpolicy_get_required_info(self, policy_name):
        """
        Shows current options for the policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-get-required-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'is-required': [ bool, False ],
        } )
    
    def fpolicy_disable_policy(self, policy_name):
        """
        Disables a specific named policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-disable-policy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_enable_policy(self, policy_name, sequence_number):
        """
        Enables a specific named policy. The operation will fail
        if the policy doesn't exist.
        
        :param policy_name: Name of the policy.
        
        :param sequence_number: Policy Sequence Number
        """
        return self.request( "fpolicy-enable-policy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'sequence_number': [ sequence_number, 'sequence-number', [ int, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_policy_modify(self, policy_name, engine_name=None, privileged_user_name=None, events=None, is_mandatory=None, allow_privileged_access=None):
        """
        Modify a policy.
        
        :param policy_name: Name of the policy.
        
        :param engine_name: Name of the Engine. Default Engine is 'native'.
        
        :param privileged_user_name: User name for privileged access. No default value is set for this
                attribute.
        
        :param events: Events for file access monitoring.
        
        :param is_mandatory: Indicator if the screening with this policy is required, i.e. it
                will fail if no servers are able process the notification
                registered as a part of external engine. If set to true, the
                request will fail if there is no  server to evaluate it. If it's
                false, the request will succeed. Default value is true.
        
        :param allow_privileged_access: Indicator if privileged access should be given to FPolicy servers
                registered for the policy. Default Value is no.
        """
        return self.request( "fpolicy-policy-modify", {
            'engine_name': [ engine_name, 'engine-name', [ basestring, 'engine-name' ], False ],
            'privileged_user_name': [ privileged_user_name, 'privileged-user-name', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'events': [ events, 'events', [ basestring, 'event-name' ], True ],
            'is_mandatory': [ is_mandatory, 'is-mandatory', [ bool, 'None' ], False ],
            'allow_privileged_access': [ allow_privileged_access, 'allow-privileged-access', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_policy_create(self, engine_name, policy_name, events, privileged_user_name=None, return_record=None, is_mandatory=None, allow_privileged_access=None):
        """
        Create a policy.
        
        :param engine_name: Name of the Engine. Default Engine is 'native'.
        
        :param policy_name: Name of the policy.
        
        :param events: Events for file access monitoring.
        
        :param privileged_user_name: User name for privileged access. No default value is set for this
                attribute.
        
        :param return_record: If set to true, returns the fpolicy-policy on successful
                creation.
                Default: false
        
        :param is_mandatory: Indicator if the screening with this policy is required, i.e. it
                will fail if no servers are able process the notification
                registered as a part of external engine. If set to true, the
                request will fail if there is no  server to evaluate it. If it's
                false, the request will succeed. Default value is true.
        
        :param allow_privileged_access: Indicator if privileged access should be given to FPolicy servers
                registered for the policy. Default Value is no.
        """
        return self.request( "fpolicy-policy-create", {
            'engine_name': [ engine_name, 'engine-name', [ basestring, 'engine-name' ], False ],
            'privileged_user_name': [ privileged_user_name, 'privileged-user-name', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'events': [ events, 'events', [ basestring, 'event-name' ], True ],
            'is_mandatory': [ is_mandatory, 'is-mandatory', [ bool, 'None' ], False ],
            'allow_privileged_access': [ allow_privileged_access, 'allow-privileged-access', [ bool, 'None' ], False ],
        }, {
            'result': [ FpolicyPolicyInfo, False ],
        } )
    
    def fpolicy_policy_event_modify(self, event_name, volume_operation=None, protocol=None, file_operations=None, filter_string=None):
        """
        Set FPolicy event options. FPolicy event is consist of protocol,
        file operation, volume operation and f
        ilters.
        
        :param event_name: Name of the Event.
        
        :param volume_operation: Indicator if the volume operation required for the event.Default
                Value is false.
        
        :param protocol: Name of protocol for which event is created. By default no
                protocol is selected.
                Possible values:
                <ul>
                <li> "cifs"      - CIFS protocol,
                <li> "nfsv3"     - NFSv3 protocol,
                <li> "nfsv4"     - NFSv4 protocol
                </ul>
        
        :param file_operations: Name of file operations. By default no operations are monitored.
                Possible values:
                <ul>
                <li> "close"          - File close operation,
                <li> "create"         - File create operation,
                <li> "create_dir"     - File create directory operation,
                <li> "delete"         - File delete operation,
                <li> "delete_dir"     - Directory delete operation,
                <li> "getattr"        - Get attribute operation,
                <li> "link"           - Link operation,
                <li> "lookup"         - Lookup operation,
                <li> "open"           - File open operation,
                <li> "read"           - File read operation,
                <li> "write"          - File write operation,
                <li> "rename"         - File rename operation,
                <li> "rename_dir"     - Directory rename operation,
                <li> "setattr"        - Set attribute operation,
                <li> "symlink"        - Symbolic link operation
                </ul>
        
        :param filter_string: Name of filters. It is notification filtering parameters. By
                default no filters are selected.
                Possible values:
                <ul>
                <li> "monitor_ads"                   - Monitor alternate data
                stream,
                <li> "close_with_modification"       - Filter close with
                modification,
                <li> "close_without_modification"    - Filter close without
                modification,
                <li> "first_read"                    - Filter first read,
                <li> "first_write"                   - Filter first write,
                <li> "offline_bit"                   - Filter offline bit set,
                <li> "open_with_delete_intent"       - Filter open with delete
                intent,
                <li> "open_with_write_intent"        - Filter open with write
                intent,
                <li> "write_with_size_change"        - Filter write with size
                change
                </ul>
        """
        return self.request( "fpolicy-policy-event-modify", {
            'volume_operation': [ volume_operation, 'volume-operation', [ bool, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'fpolicy-proto' ], False ],
            'file_operations': [ file_operations, 'file-operations', [ basestring, 'fpolicy-operation' ], True ],
            'event_name': [ event_name, 'event-name', [ basestring, 'event-name' ], False ],
            'filter_string': [ filter_string, 'filter-string', [ basestring, 'fpolicy-filter' ], True ],
        }, {
        } )
    
    def fpolicy_operations_list_set(self, monitored_operations, policy_name, monitored_protocols, force=None, offline_only=None):
        """
        Manipulate a list of operations and network protocols
        for a policy.
        This determines which user requests cause the filer to
        notify fpolicy servers for this policy.
        The list provided will replace the list currently in place,
        if any. Note that this can be confusing to a server which has
        already connected to a policy and provided a list of
        operations. For example, it may have requested notifications
        when users open files, but start receiving notifications
        when users create symlinks.
        This API is provided in support of "native file blocking"
        in which there is no server connected to the filer for a
        policy.
        Note that it is possible to get the list of operations and
        protocols currently set for a policy with the
        fpolicy-list-info API.
        
        :param monitored_operations: List of operations related values.
        
        :param policy_name: Name of the policy.
        
        :param monitored_protocols: List of protocol related values.
        
        :param force: If a server is connected to the filer and has already
                set the list of operations, should this API override
                the server's setting? If "force" is "true", the policy's
                set of operations will be dropped and replaced with the
                values provided by this API.
                Default value is false.
        
        :param offline_only: Sets the state of offline filtering. If offline filtering
                is set, then only user requests for files which are marked
                "offline" cause notifications.
                Default value is false.
        """
        return self.request( "fpolicy-operations-list-set", {
            'monitored_operations': [ monitored_operations, 'monitored-operations', [ MonitoredOperationInfo, 'None' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'offline_only': [ offline_only, 'offline-only', [ bool, 'None' ], False ],
            'monitored_protocols': [ monitored_protocols, 'monitored-protocols', [ MonitoredProtocolInfo, 'None' ], True ],
        }, {
        } )
    
    def fpolicy_volume_list_info(self, policy_name):
        """
        Returns a volume-regular-expression list for an exclude
        or include set.
        The list describes limits to the set of volumes for which
        client requests trigger (include) or suppress (exclude)
        fpolicy processing for the provided policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-volume-list-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'include-volumes': [ FpolicyVolumesListInfo, True ],
            'exclude-volumes': [ FpolicyVolumesListInfo, True ],
        } )
    
    def fpolicy_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information about policies.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-policy object.
                All fpolicy-policy objects matching this query up to
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
        return self.request( "fpolicy-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyPolicyInfo, True ],
        } )
    
    def fpolicy_policy_event_delete(self, event_name):
        """
        Delete FPolicy event.
        
        :param event_name: Name of the Event.
        """
        return self.request( "fpolicy-policy-event-delete", {
            'event_name': [ event_name, 'event-name', [ basestring, 'event-name' ], False ],
        }, {
        } )
    
    def fpolicy_extensions_list_info(self, policy_name):
        """
        Returns information on existing extension sets.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-extensions-list-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'exclude-extensions': [ ExtensionListInfo, True ],
            'include-extensions': [ ExtensionListInfo, True ],
        } )
    
    def fpolicy_policy_external_engine_create(self, engine_name, port_number, primary_servers, ssl_option, certificate_serial=None, server_progress_timeout=None, secondary_servers=None, certificate_ca=None, request_cancel_timeout=None, return_record=None, certificate_common_name=None, keep_alive_interval=None, extern_engine_type=None, max_connection_retries=None, request_abort_timeout=None, max_server_requests=None, status_request_interval=None):
        """
        Create an external engine.
        
        :param engine_name: Name of the external engine.
        
        :param port_number: Port number of the FPolicy server application.
        
        :param primary_servers: Primary FPolicy servers.
        
        :param ssl_option: SSL option for external communication. No default value is set
                for this field.
                Possible values:
                <ul>
                <li> "no_auth"        - Communication over TCP,
                <li> "server_auth"    - Authentication of FPolicy server only,
                <li> "mutual_auth"    - Mutual authentication of storage system
                and FPolicy server
                </ul>
        
        :param certificate_serial: Serial number of certificate. No default value is set for this
                field.
        
        :param server_progress_timeout: Timeout in seconds in which a throttled FPolicy server must
                complete at least one screen request. If no request is processed
                within the timeout, connection to FPolicy server is terminated.
                Default value set for this field is 60 seconds.
        
        :param secondary_servers: Secondary FPolicy servers. No default value is set for this
                field.
        
        :param certificate_ca: Certificate authority name. No default value is set for this
                field.
        
        :param request_cancel_timeout: Timeout in seconds for a screen request to be processed by an
                FPolicy server. Default value set for this field is 20 seconds.
        
        :param return_record: If set to true, returns the fpolicy-policy-external-engine on
                successful creation.
                Default: false
        
        :param certificate_common_name: FQDN or custom common name of certificate. No default value is
                set for this field.
        
        :param keep_alive_interval: Interval time in seconds for storage appliance to send keep-alive
                message to FPolicy server. Default value set for this field is 10
                seconds.
        
        :param extern_engine_type: External engine type. If the engine is asynchronous, no reply is
                sent from FPolicy servers. Default value set for this field is
                synchronous.
                Possible values:
                <ul>
                <li> "synchronous"    - Synchronous External Engine,
                <li> "asynchronous"   - Asynchronous External Engine
                </ul>
        
        :param max_connection_retries: Number of times storage appliance will attempt to establish a
                broken connection to FPolicy server. Default value set for this
                field is 5.
        
        :param request_abort_timeout: Timeout in seconds for a screen request to be aborted by storage
                appliance. Default value set for this field is 40 seconds.
        
        :param max_server_requests: Maximum number of outstanding screen requests that will be queued
                for an FPolicy Server. Default value set for this field is 50.
        
        :param status_request_interval: Interval time in seconds for storage appliance to query status
                request from FPolicy server. Default value set for this field is
                10 seconds.
        """
        return self.request( "fpolicy-policy-external-engine-create", {
            'engine_name': [ engine_name, 'engine-name', [ basestring, 'engine-name' ], False ],
            'certificate_serial': [ certificate_serial, 'certificate-serial', [ basestring, 'None' ], False ],
            'server_progress_timeout': [ server_progress_timeout, 'server-progress-timeout', [ int, 'None' ], False ],
            'secondary_servers': [ secondary_servers, 'secondary-servers', [ basestring, 'ip-address' ], True ],
            'certificate_ca': [ certificate_ca, 'certificate-ca', [ basestring, 'None' ], False ],
            'request_cancel_timeout': [ request_cancel_timeout, 'request-cancel-timeout', [ int, 'None' ], False ],
            'port_number': [ port_number, 'port-number', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'certificate_common_name': [ certificate_common_name, 'certificate-common-name', [ basestring, 'common-name' ], False ],
            'keep_alive_interval': [ keep_alive_interval, 'keep-alive-interval', [ int, 'None' ], False ],
            'primary_servers': [ primary_servers, 'primary-servers', [ basestring, 'ip-address' ], True ],
            'extern_engine_type': [ extern_engine_type, 'extern-engine-type', [ basestring, 'external-engine-type' ], False ],
            'max_connection_retries': [ max_connection_retries, 'max-connection-retries', [ int, 'None' ], False ],
            'request_abort_timeout': [ request_abort_timeout, 'request-abort-timeout', [ int, 'None' ], False ],
            'ssl_option': [ ssl_option, 'ssl-option', [ basestring, 'fpolicy-ssl-opts' ], False ],
            'max_server_requests': [ max_server_requests, 'max-server-requests', [ int, 'None' ], False ],
            'status_request_interval': [ status_request_interval, 'status-request-interval', [ int, 'None' ], False ],
        }, {
            'result': [ FpolicyExternalEngineInfo, False ],
        } )
    
    def fpolicy_policy_status_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns FPolicy policy status information.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-policy-status object.
                All fpolicy-policy-status objects matching this query up to
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
        return self.request( "fpolicy-policy-status-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyPolicyStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyPolicyStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyPolicyStatusInfo, True ],
        } )
    
    def fpolicy_policy_delete(self, policy_name):
        """
        Delete a policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
        }, {
        } )
    
    def fpolicy_set_policy_options(self, policy_name, reqcancel_timeout=None, is_required=None, is_ads_monitored=None, secondary_servers=None, serverprogress_timeout=None, is_cifs_disconnect_check_enabled=None, is_cifs_setattr_enabled=None):
        """
        Sets policy's options to on/off.
        
        :param policy_name: Name of the policy.
        
        :param reqcancel_timeout: Timeout (in secs) for a screen request to be processed by an
                FPolicy server.
                Range : [0..4294967].
        
        :param is_required: Indicator if the screening with this policy is required,
                i.e. will it fail if the server is not registered.
                If set to true, the request will fail if there is no
                server to evaluate it. If it's false, the request will succeed.
                Default is false.
        
        :param is_ads_monitored: Indicates if the policy monitors the cifs operations
                on Alternate Data Streams.
                Default is false.
        
        :param secondary_servers: List of server's IP addresses. Servers registered
                from these IP will be considered as secondary servers.
        
        :param serverprogress_timeout: Timeout (in secs) in which a throttled FPolicy server must
                complete at least one screen request.
                Range : [0..4294967].
        
        :param is_cifs_disconnect_check_enabled: 'true' if requests associated with disconnected CIFS sessions
                must not be screened, 'false' otherwise.
        
        :param is_cifs_setattr_enabled: Indicator whether cifs-setattr support is enabled
                on this policy or not. If set to true, cifs setattr
                operations will be screened.
                Default is false.
        """
        return self.request( "fpolicy-set-policy-options", {
            'reqcancel_timeout': [ reqcancel_timeout, 'reqcancel-timeout', [ int, 'None' ], False ],
            'is_required': [ is_required, 'is-required', [ bool, 'None' ], False ],
            'is_ads_monitored': [ is_ads_monitored, 'is-ads-monitored', [ bool, 'None' ], False ],
            'secondary_servers': [ secondary_servers, 'secondary-servers', [ SecondaryServerInfo, 'None' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'serverprogress_timeout': [ serverprogress_timeout, 'serverprogress-timeout', [ int, 'None' ], False ],
            'is_cifs_disconnect_check_enabled': [ is_cifs_disconnect_check_enabled, 'is-cifs-disconnect-check-enabled', [ bool, 'None' ], False ],
            'is_cifs_setattr_enabled': [ is_cifs_setattr_enabled, 'is-cifs-setattr-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_set_secondary_servers(self, secondary_servers, policy_name):
        """
        Sets secondary servers information in a form of
        a list of ip addresses. These servers will be used
        if all primary servers are not available, thus increasing
        system availabilty.
        
        :param secondary_servers: List of servers' IP addresses.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-set-secondary-servers", {
            'secondary_servers': [ secondary_servers, 'secondary-servers', [ SecondaryServerInfo, 'None' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_server_status_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns FPolicy server status information.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-server-status object.
                All fpolicy-server-status objects matching this query up to
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
        return self.request( "fpolicy-server-status-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyServerStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyServerStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyServerStatusInfo, True ],
        } )
    
    def fpolicy_policy_external_engine_modify(self, engine_name, certificate_serial=None, server_progress_timeout=None, secondary_servers=None, certificate_ca=None, request_cancel_timeout=None, port_number=None, certificate_common_name=None, keep_alive_interval=None, primary_servers=None, extern_engine_type=None, max_connection_retries=None, request_abort_timeout=None, ssl_option=None, max_server_requests=None, status_request_interval=None):
        """
        Modify an external engine. External engine can be modified only
        when none of the enabled policies are using it.
        
        :param engine_name: Name of the external engine.
        
        :param certificate_serial: Serial number of certificate. No default value is set for this
                field.
        
        :param server_progress_timeout: Timeout in seconds in which a throttled FPolicy server must
                complete at least one screen request. If no request is processed
                within the timeout, connection to FPolicy server is terminated.
                Default value set for this field is 60 seconds.
        
        :param secondary_servers: Secondary FPolicy servers. No default value is set for this
                field.
        
        :param certificate_ca: Certificate authority name. No default value is set for this
                field.
        
        :param request_cancel_timeout: Timeout in seconds for a screen request to be processed by an
                FPolicy server. Default value set for this field is 20 seconds.
        
        :param port_number: Port number of the FPolicy server application.
        
        :param certificate_common_name: FQDN or custom common name of certificate. No default value is
                set for this field.
        
        :param keep_alive_interval: Interval time in seconds for storage appliance to send keep-alive
                message to FPolicy server. Default value set for this field is 10
                seconds.
        
        :param primary_servers: Primary FPolicy servers.
        
        :param extern_engine_type: External engine type. If the engine is asynchronous, no reply is
                sent from FPolicy servers. Default value set for this field is
                synchronous.
                Possible values:
                <ul>
                <li> "synchronous"    - Synchronous External Engine,
                <li> "asynchronous"   - Asynchronous External Engine
                </ul>
        
        :param max_connection_retries: Number of times storage appliance will attempt to establish a
                broken connection to FPolicy server. Default value set for this
                field is 5.
        
        :param request_abort_timeout: Timeout in seconds for a screen request to be aborted by storage
                appliance. Default value set for this field is 40 seconds.
        
        :param ssl_option: SSL option for external communication. No default value is set
                for this field.
                Possible values:
                <ul>
                <li> "no_auth"        - Communication over TCP,
                <li> "server_auth"    - Authentication of FPolicy server only,
                <li> "mutual_auth"    - Mutual authentication of storage system
                and FPolicy server
                </ul>
        
        :param max_server_requests: Maximum number of outstanding screen requests that will be queued
                for an FPolicy Server. Default value set for this field is 50.
        
        :param status_request_interval: Interval time in seconds for storage appliance to query status
                request from FPolicy server. Default value set for this field is
                10 seconds.
        """
        return self.request( "fpolicy-policy-external-engine-modify", {
            'engine_name': [ engine_name, 'engine-name', [ basestring, 'engine-name' ], False ],
            'certificate_serial': [ certificate_serial, 'certificate-serial', [ basestring, 'None' ], False ],
            'server_progress_timeout': [ server_progress_timeout, 'server-progress-timeout', [ int, 'None' ], False ],
            'secondary_servers': [ secondary_servers, 'secondary-servers', [ basestring, 'ip-address' ], True ],
            'certificate_ca': [ certificate_ca, 'certificate-ca', [ basestring, 'None' ], False ],
            'request_cancel_timeout': [ request_cancel_timeout, 'request-cancel-timeout', [ int, 'None' ], False ],
            'port_number': [ port_number, 'port-number', [ int, 'None' ], False ],
            'certificate_common_name': [ certificate_common_name, 'certificate-common-name', [ basestring, 'common-name' ], False ],
            'keep_alive_interval': [ keep_alive_interval, 'keep-alive-interval', [ int, 'None' ], False ],
            'primary_servers': [ primary_servers, 'primary-servers', [ basestring, 'ip-address' ], True ],
            'extern_engine_type': [ extern_engine_type, 'extern-engine-type', [ basestring, 'external-engine-type' ], False ],
            'max_connection_retries': [ max_connection_retries, 'max-connection-retries', [ int, 'None' ], False ],
            'request_abort_timeout': [ request_abort_timeout, 'request-abort-timeout', [ int, 'None' ], False ],
            'ssl_option': [ ssl_option, 'ssl-option', [ basestring, 'fpolicy-ssl-opts' ], False ],
            'max_server_requests': [ max_server_requests, 'max-server-requests', [ int, 'None' ], False ],
            'status_request_interval': [ status_request_interval, 'status-request-interval', [ int, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_get_secondary_servers_info(self, policy_name):
        """
        Shows current options for the policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-get-secondary-servers-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'secondary-servers': [ SecondaryServerInfo, True ],
        } )
    
    def fpolicy_disable(self):
        """
        Sets options fpolicy enable to off.
        """
        return self.request( "fpolicy-disable", {
        }, {
        } )
    
    def fpolicy_create_policy(self, policy_name, policy_type):
        """
        Creates a new policy.
        
        :param policy_name: Name of the policy.
        
        :param policy_type: Type of the policy. Possible values: "screen".
        """
        return self.request( "fpolicy-create-policy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'policy_type': [ policy_type, 'policy-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_server_list_info(self, policy_name):
        """
        Shows a list of primary servers serving the policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-server-list-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'servers': [ ServerInfo, True ],
        } )
    
    def fpolicy_policy_event_create(self, event_name, protocol=None, volume_operation=None, return_record=None, filter_string=None, file_operations=None):
        """
        Create FPolicy Event.
        
        :param event_name: Name of the Event.
        
        :param protocol: Name of protocol for which event is created. By default no
                protocol is selected.
                Possible values:
                <ul>
                <li> "cifs"      - CIFS protocol,
                <li> "nfsv3"     - NFSv3 protocol,
                <li> "nfsv4"     - NFSv4 protocol
                </ul>
        
        :param volume_operation: Indicator if the volume operation required for the event.Default
                Value is false.
        
        :param return_record: If set to true, returns the fpolicy-policy-event on successful
                creation.
                Default: false
        
        :param filter_string: Name of filters. It is notification filtering parameters. By
                default no filters are selected.
                Possible values:
                <ul>
                <li> "monitor_ads"                   - Monitor alternate data
                stream,
                <li> "close_with_modification"       - Filter close with
                modification,
                <li> "close_without_modification"    - Filter close without
                modification,
                <li> "first_read"                    - Filter first read,
                <li> "first_write"                   - Filter first write,
                <li> "offline_bit"                   - Filter offline bit set,
                <li> "open_with_delete_intent"       - Filter open with delete
                intent,
                <li> "open_with_write_intent"        - Filter open with write
                intent,
                <li> "write_with_size_change"        - Filter write with size
                change
                </ul>
        
        :param file_operations: Name of file operations. By default no operations are monitored.
                Possible values:
                <ul>
                <li> "close"          - File close operation,
                <li> "create"         - File create operation,
                <li> "create_dir"     - File create directory operation,
                <li> "delete"         - File delete operation,
                <li> "delete_dir"     - Directory delete operation,
                <li> "getattr"        - Get attribute operation,
                <li> "link"           - Link operation,
                <li> "lookup"         - Lookup operation,
                <li> "open"           - File open operation,
                <li> "read"           - File read operation,
                <li> "write"          - File write operation,
                <li> "rename"         - File rename operation,
                <li> "rename_dir"     - Directory rename operation,
                <li> "setattr"        - Set attribute operation,
                <li> "symlink"        - Symbolic link operation
                </ul>
        """
        return self.request( "fpolicy-policy-event-create", {
            'protocol': [ protocol, 'protocol', [ basestring, 'fpolicy-proto' ], False ],
            'volume_operation': [ volume_operation, 'volume-operation', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'event_name': [ event_name, 'event-name', [ basestring, 'event-name' ], False ],
            'filter_string': [ filter_string, 'filter-string', [ basestring, 'fpolicy-filter' ], True ],
            'file_operations': [ file_operations, 'file-operations', [ basestring, 'fpolicy-operation' ], True ],
        }, {
            'result': [ FpolicyEventOptionsConfig, False ],
        } )
    
    def fpolicy_policy_scope_create(self, policy_name, export_policies_to_include=None, volumes_to_exclude=None, file_extensions_to_exclude=None, export_policies_to_exclude=None, check_extensions_on_directories=None, return_record=None, volumes_to_include=None, shares_to_exclude=None, file_extensions_to_include=None, shares_to_include=None):
        """
        Set FPolicy scope options. FPolicy Scope is consist of share,
        volume, export policy, volume, file extention.
        
        :param policy_name: Name of the policy.
        
        :param export_policies_to_include: Export policies to include for file access monitoring. By default
                no export policy is selected.
        
        :param volumes_to_exclude: Volumes that are inactive for the file policy. The list can
                include items which are regular expressions, such as 'vol*' or
                'user?'. Note that if a policy has both an exclude list and an
                include list, the include list is ignored by the filer when
                processing user requests. By default no volume is selected.
        
        :param file_extensions_to_exclude: File extensions excluded for screening. By default no file
                extension is selected.
        
        :param export_policies_to_exclude: Export Policies to exclude for file access monitoring. By default
                no export policy is selected.
        
        :param check_extensions_on_directories: Indicates whether directory names are also subjected to
                extensions check, similar to file names. By default, the value is
                false.
        
        :param return_record: If set to true, returns the fpolicy-policy-scope on successful
                creation.
                Default: false
        
        :param volumes_to_include: Volumes that are active for the file policy. The list can include
                items which are regular expressions, such as 'vol*' or 'user?'.
                By default no volume is selected.
        
        :param shares_to_exclude: Shares to exclude for file access monitoring. By default no share
                is selected.
        
        :param file_extensions_to_include: File extensions included for screening. By default no file
                extension is selected.
        
        :param shares_to_include: Shares to include for file access monitoring. By default no share
                is selected.
        """
        return self.request( "fpolicy-policy-scope-create", {
            'export_policies_to_include': [ export_policies_to_include, 'export-policies-to-include', [ basestring, 'None' ], True ],
            'volumes_to_exclude': [ volumes_to_exclude, 'volumes-to-exclude', [ basestring, 'None' ], True ],
            'file_extensions_to_exclude': [ file_extensions_to_exclude, 'file-extensions-to-exclude', [ basestring, 'None' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'export_policies_to_exclude': [ export_policies_to_exclude, 'export-policies-to-exclude', [ basestring, 'None' ], True ],
            'check_extensions_on_directories': [ check_extensions_on_directories, 'check-extensions-on-directories', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'volumes_to_include': [ volumes_to_include, 'volumes-to-include', [ basestring, 'None' ], True ],
            'shares_to_exclude': [ shares_to_exclude, 'shares-to-exclude', [ basestring, 'None' ], True ],
            'file_extensions_to_include': [ file_extensions_to_include, 'file-extensions-to-include', [ basestring, 'None' ], True ],
            'shares_to_include': [ shares_to_include, 'shares-to-include', [ basestring, 'None' ], True ],
        }, {
            'result': [ FpolicyScopeConfig, False ],
        } )
    
    def fpolicy_policy_scope_modify(self, policy_name, export_policies_to_include=None, volumes_to_exclude=None, file_extensions_to_exclude=None, export_policies_to_exclude=None, check_extensions_on_directories=None, volumes_to_include=None, shares_to_exclude=None, file_extensions_to_include=None, shares_to_include=None):
        """
        Set FPolicy scope options. FPolicy Scope is consist of share,
        volume, export policy, volume, file extention.
        
        :param policy_name: Name of the policy.
        
        :param export_policies_to_include: Export policies to include for file access monitoring. By default
                no export policy is selected.
        
        :param volumes_to_exclude: Volumes that are inactive for the file policy. The list can
                include items which are regular expressions, such as 'vol*' or
                'user?'. Note that if a policy has both an exclude list and an
                include list, the include list is ignored by the filer when
                processing user requests. By default no volume is selected.
        
        :param file_extensions_to_exclude: File extensions excluded for screening. By default no file
                extension is selected.
        
        :param export_policies_to_exclude: Export Policies to exclude for file access monitoring. By default
                no export policy is selected.
        
        :param check_extensions_on_directories: Indicates whether directory names are also subjected to
                extensions check, similar to file names. By default, the value is
                false.
        
        :param volumes_to_include: Volumes that are active for the file policy. The list can include
                items which are regular expressions, such as 'vol*' or 'user?'.
                By default no volume is selected.
        
        :param shares_to_exclude: Shares to exclude for file access monitoring. By default no share
                is selected.
        
        :param file_extensions_to_include: File extensions included for screening. By default no file
                extension is selected.
        
        :param shares_to_include: Shares to include for file access monitoring. By default no share
                is selected.
        """
        return self.request( "fpolicy-policy-scope-modify", {
            'export_policies_to_include': [ export_policies_to_include, 'export-policies-to-include', [ basestring, 'None' ], True ],
            'volumes_to_exclude': [ volumes_to_exclude, 'volumes-to-exclude', [ basestring, 'None' ], True ],
            'file_extensions_to_exclude': [ file_extensions_to_exclude, 'file-extensions-to-exclude', [ basestring, 'None' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'export_policies_to_exclude': [ export_policies_to_exclude, 'export-policies-to-exclude', [ basestring, 'None' ], True ],
            'check_extensions_on_directories': [ check_extensions_on_directories, 'check-extensions-on-directories', [ bool, 'None' ], False ],
            'volumes_to_include': [ volumes_to_include, 'volumes-to-include', [ basestring, 'None' ], True ],
            'shares_to_exclude': [ shares_to_exclude, 'shares-to-exclude', [ basestring, 'None' ], True ],
            'file_extensions_to_include': [ file_extensions_to_include, 'file-extensions-to-include', [ basestring, 'None' ], True ],
            'shares_to_include': [ shares_to_include, 'shares-to-include', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def fpolicy_list_info(self, policy_name=None):
        """
        Returns a list of existing policies.
        
        :param policy_name: Name of the policy. If this parameter is set, policies
                will have information pertaining to the policy named. If
                there is no such a policy, policies will be empty.
        """
        return self.request( "fpolicy-list-info", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'policies': [ PolicyInfo, True ],
        } )
    
    def fpolicy_policy_scope_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a list of rows for FPolicy scope options. FPolicy Scope
        consists of share, volume, export policy, volume, file
        extention.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-policy-scope object.
                All fpolicy-policy-scope objects matching this query up to
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
        return self.request( "fpolicy-policy-scope-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyScopeConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyScopeConfig, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyScopeConfig, True ],
        } )
    
    def fpolicy_destroy_policy(self, policy_name):
        """
        Destroys existing policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-destroy-policy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fpolicy_policy_external_engine_delete(self, engine_name):
        """
        Delete an external engine.
        
        :param engine_name: Name of the external engine.
        """
        return self.request( "fpolicy-policy-external-engine-delete", {
            'engine_name': [ engine_name, 'engine-name', [ basestring, 'engine-name' ], False ],
        }, {
        } )
    
    def fpolicy_status(self):
        """
        Returns status of options fpolicy enable.
        """
        return self.request( "fpolicy-status", {
        }, {
            'is-enabled': [ bool, False ],
        } )
    
    def fpolicy_policy_scope_delete(self, policy_name):
        """
        Delete a scope.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-policy-scope-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
        }, {
        } )
    
    def fpolicy_extensions(self, policy_name, set_name, command, extensions=None):
        """
        Manipulates with list of  extensions in
        exclude or include set. Exlude set defines extension patterns
        that won't trigger fpolicy processing.
        
        :param policy_name: Name of the policy.
        
        :param set_name: Defines to which set (exclude or include) a command
                (add, remove, etc) will be applied to. For instance,
                command = add, set-name = include will add specified
                list of extensions to the include set.
                Possible values: "exclude", "include".
        
        :param command: Command to be applied on the specified set.
                Supported values: "add", "remove", "set", "reset".
        
        :param extensions: List of extensions. This element is required if the
                the command input value is "add", "set" or "remove".
        """
        return self.request( "fpolicy-extensions", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'set_name': [ set_name, 'set-name', [ basestring, 'None' ], False ],
            'command': [ command, 'command', [ basestring, 'None' ], False ],
            'extensions': [ extensions, 'extensions', [ ExtensionListInfo, 'None' ], True ],
        }, {
        } )
    
    def fpolicy_policy_external_engine_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns information on external engines.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-policy-external-engine object.
                All fpolicy-policy-external-engine objects matching this query up
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
        return self.request( "fpolicy-policy-external-engine-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyExternalEngineInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyExternalEngineInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyExternalEngineInfo, True ],
        } )
    
    def fpolicy_get_policy_options(self, policy_name):
        """
        Shows value of policy options.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "fpolicy-get-policy-options", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
            'reqcancel-timeout': [ int, False ],
            'is-required': [ bool, False ],
            'is-ads-monitored': [ bool, False ],
            'secondary-servers': [ SecondaryServerInfo, True ],
            'serverprogress-timeout': [ int, False ],
            'is-cifs-disconnect-check-enabled': [ bool, False ],
            'is-cifs-setattr-enabled': [ bool, False ],
        } )
    
    def fpolicy_policy_event_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a list of rows for FPolicy event options. FPolicy event is
        consist of protocol, file operations, vo
        lume operation and filters.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                fpolicy-policy-event object.
                All fpolicy-policy-event objects matching this query up to
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
        return self.request( "fpolicy-policy-event-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FpolicyEventOptionsConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FpolicyEventOptionsConfig, 'None' ], False ],
        }, {
            'attributes-list': [ FpolicyEventOptionsConfig, True ],
        } )
