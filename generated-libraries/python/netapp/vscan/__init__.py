from netapp.connection import NaConnection
from vscan_server_status import VscanServerStatus # 0 properties
from vscan_status_info import VscanStatusInfo # 2 properties
from policy_name import PolicyName # 0 properties
from privileged_user import PrivilegedUser # 0 properties
from scanner_pool import ScannerPool # 0 properties
from vscan_on_access_policy_info import VscanOnAccessPolicyInfo # 9 properties
from vscan_on_access_policy_get_iter_key_td import VscanOnAccessPolicyGetIterKeyTd # 2 properties
from vscan_disconnect_reason import VscanDisconnectReason # 0 properties
from vscan_scanner_pool_get_iter_key_td import VscanScannerPoolGetIterKeyTd # 2 properties
from vscan_config_owner import VscanConfigOwner # 0 properties
from vscan_connection_extended_stats_info import VscanConnectionExtendedStatsInfo # 8 properties
from vscan_scanner_type import VscanScannerType # 0 properties
from vscan_on_access_policy_filter import VscanOnAccessPolicyFilter # 0 properties
from vscan_active_scanner_pool_info import VscanActiveScannerPoolInfo # 9 properties
from vscan_protocol import VscanProtocol # 0 properties
from vscan_connection_extended_stats_get_iter_key_td import VscanConnectionExtendedStatsGetIterKeyTd # 3 properties
from vscan_active_scanner_pool_get_iter_key_td import VscanActiveScannerPoolGetIterKeyTd # 1 properties
from file_extension import FileExtension # 0 properties
from file_path import FilePath # 0 properties
from vscan_connection_status_all_get_iter_key_td import VscanConnectionStatusAllGetIterKeyTd # 3 properties
from vscan_connection_status_all_info import VscanConnectionStatusAllInfo # 11 properties
from vscan_status_get_iter_key_td import VscanStatusGetIterKeyTd # 1 properties
from scanner_policy import ScannerPolicy # 0 properties
from vscan_scanner_pool_info import VscanScannerPoolInfo # 12 properties

class VscanConnection(NaConnection):
    
    def vscan_connection_status_all_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns connection status.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-connection-status-all object.
                All vscan-connection-status-all objects matching this query up to
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
        return self.request( "vscan-connection-status-all-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanConnectionStatusAllInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanConnectionStatusAllInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanConnectionStatusAllInfo, True ],
        } )
    
    def vscan_on_access_policy_create(self, protocol, policy_name, file_ext_to_exclude=None, return_record=None, paths_to_exclude=None, max_file_size=None, filters=None):
        """
        Create an On-Access policy.
        
        :param protocol: File-Access protocol to monitor for On-Access scanning.
                Possible values:
                <ul>
                <li> "cifs" - CIFS Protocol
                </ul>
        
        :param policy_name: Name of the policy.
        
        :param file_ext_to_exclude: File-Extensions for which On-Access scanning must not be
                performed.
        
        :param return_record: If set to true, returns the vscan-on-access-policy on successful
                creation.
                Default: false
        
        :param paths_to_exclude: File-paths for which On-Access scanning must not be performed.
        
        :param max_file_size: Max file-size (in bytes) allowed for scanning. The default value
                of 2147483648 (2GB) is taken if not provided at the time of
                creating a policy.
        
        :param filters: Filters.
                Possible values:
                <ul>
                <li> "scan_mandatory"      - Enable mandatory scan,
                <li> "scan_ro_volume"      - Enable scans for read-only
                volume,
                <li> "scan_execute_access" - Scan only files opened with
                execute-access (CIFS only)
                </ul>
        """
        return self.request( "vscan-on-access-policy-create", {
            'file_ext_to_exclude': [ file_ext_to_exclude, 'file-ext-to-exclude', [ basestring, 'file-extension' ], True ],
            'protocol': [ protocol, 'protocol', [ basestring, 'vscan-protocol' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'paths_to_exclude': [ paths_to_exclude, 'paths-to-exclude', [ basestring, 'file-path' ], True ],
            'max_file_size': [ max_file_size, 'max-file-size', [ int, 'size' ], False ],
            'filters': [ filters, 'filters', [ basestring, 'vscan-on-access-policy-filter' ], True ],
        }, {
            'result': [ VscanOnAccessPolicyInfo, False ],
        } )
    
    def vscan_reset(self):
        """
        Discard cached information of files that have been successfully
        scanned.
        """
        return self.request( "vscan-reset", {
        }, {
        } )
    
    def vscan_connection_extended_stats_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns connection status.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-connection-extended-stats object.
                All vscan-connection-extended-stats objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "vscan-connection-extended-stats-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanConnectionExtendedStatsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanConnectionExtendedStatsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanConnectionExtendedStatsInfo, True ],
        } )
    
    def vscan_on_access_policy_modify(self, policy_name, max_file_size=None, file_ext_to_exclude=None, filters=None, paths_to_exclude=None):
        """
        Modify an On-Access policy.
        
        :param policy_name: Name of the policy.
        
        :param max_file_size: Max file-size (in bytes) allowed for scanning. The default value
                of 2147483648 (2GB) is taken if not provided at the time of
                creating a policy.
        
        :param file_ext_to_exclude: File-Extensions for which On-Access scanning must not be
                performed.
        
        :param filters: Filters.
                Possible values:
                <ul>
                <li> "scan_mandatory"      - Enable mandatory scan,
                <li> "scan_ro_volume"      - Enable scans for read-only
                volume,
                <li> "scan_execute_access" - Scan only files opened with
                execute-access (CIFS only)
                </ul>
        
        :param paths_to_exclude: File-paths for which On-Access scanning must not be performed.
        """
        return self.request( "vscan-on-access-policy-modify", {
            'max_file_size': [ max_file_size, 'max-file-size', [ int, 'size' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
            'file_ext_to_exclude': [ file_ext_to_exclude, 'file-ext-to-exclude', [ basestring, 'file-extension' ], True ],
            'filters': [ filters, 'filters', [ basestring, 'vscan-on-access-policy-filter' ], True ],
            'paths_to_exclude': [ paths_to_exclude, 'paths-to-exclude', [ basestring, 'file-path' ], True ],
        }, {
        } )
    
    def vscan_status_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns Vscan status information.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-status object.
                All vscan-status objects matching this query up to 'max-records'
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
        return self.request( "vscan-status-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanStatusInfo, True ],
        } )
    
    def vscan_scanner_pool_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns list of scanner pools. Scanner pool is a set of
        attributes which are used to validate and manage connections
        between clustered Data ONTAP and Vscan servers (virus scanners).
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-scanner-pool object.
                All vscan-scanner-pool objects matching this query up to
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
        return self.request( "vscan-scanner-pool-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanScannerPoolInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanScannerPoolInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanScannerPoolInfo, True ],
        } )
    
    def vscan_active_scanner_pool_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns active scanner pool configuration of a vserver.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-active-scanner-pool object.
                All vscan-active-scanner-pool objects matching this query up to
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
        return self.request( "vscan-active-scanner-pool-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanActiveScannerPoolInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanActiveScannerPoolInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanActiveScannerPoolInfo, True ],
        } )
    
    def vscan_on_access_policy_status_modify(self, policy_status, policy_name):
        """
        Modify On-Access policy status.
        
        :param policy_status: Policy Status
        
        :param policy_name: Name of the policy.
        """
        return self.request( "vscan-on-access-policy-status-modify", {
            'policy_status': [ policy_status, 'policy-status', [ bool, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
        }, {
        } )
    
    def vscan_scanner_pool_apply_policy(self, scanner_pool, scanner_policy):
        """
        Apply scanner-policy to a scanner pool.
        
        :param scanner_pool: Name of the virus scanner pool.
        
        :param scanner_policy: Scanner Policy
        """
        return self.request( "vscan-scanner-pool-apply-policy", {
            'scanner_pool': [ scanner_pool, 'scanner-pool', [ basestring, 'scanner-pool' ], False ],
            'scanner_policy': [ scanner_policy, 'scanner-policy', [ basestring, 'scanner-policy' ], False ],
        }, {
        } )
    
    def vscan_on_access_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns list of On-Access policies.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vscan-on-access-policy object.
                All vscan-on-access-policy objects matching this query up to
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
        return self.request( "vscan-on-access-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VscanOnAccessPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VscanOnAccessPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VscanOnAccessPolicyInfo, True ],
        } )
    
    def vscan_status_modify(self, is_vscan_enabled):
        """
        Modify Vscan status.
        
        :param is_vscan_enabled: Vscan status. When true, Vscan feature is enabled for the
                Vserver.
        """
        return self.request( "vscan-status-modify", {
            'is_vscan_enabled': [ is_vscan_enabled, 'is-vscan-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def vscan_scanner_pool_modify(self, scanner_pool, max_session_setup_retries=None, session_teardown_timeout=None, privileged_users=None, servers=None, session_setup_timeout=None, request_timeout=None, scan_queue_timeout=None):
        """
        Modify a scanner pool.
        
        :param scanner_pool: Name of the virus scanner pool.
        
        :param max_session_setup_retries: Maximum number of consecutive session-setup attempts. The default
                value of 5 is taken if not provided while creating a scanner
                pool.
        
        :param session_teardown_timeout: Total session-teardown time-limit in seconds. The default value
                of 10 is taken if not provided while creating a scanner pool.
        
        :param privileged_users: List of privileged users.
        
        :param servers: List of IP addresses of Vscan servers which are allowed to
                connect to clustered Data ONTAP.
        
        :param session_setup_timeout: Total session-setup time-limit in seconds. The default value of
                10 is taken if not provided while creating a scanner pool.
        
        :param request_timeout: Total request-service time-limit in seconds. The default value of
                30 is taken if not provided while creating a scanner pool.
        
        :param scan_queue_timeout: Scan-queue wait-time-limit in seconds. The default value of 20 is
                taken if not provided while creating a scanner pool.
        """
        return self.request( "vscan-scanner-pool-modify", {
            'max_session_setup_retries': [ max_session_setup_retries, 'max-session-setup-retries', [ int, 'None' ], False ],
            'session_teardown_timeout': [ session_teardown_timeout, 'session-teardown-timeout', [ int, 'None' ], False ],
            'privileged_users': [ privileged_users, 'privileged-users', [ basestring, 'privileged-user' ], True ],
            'servers': [ servers, 'servers', [ basestring, 'ip-address' ], True ],
            'scanner_pool': [ scanner_pool, 'scanner-pool', [ basestring, 'scanner-pool' ], False ],
            'session_setup_timeout': [ session_setup_timeout, 'session-setup-timeout', [ int, 'None' ], False ],
            'request_timeout': [ request_timeout, 'request-timeout', [ int, 'None' ], False ],
            'scan_queue_timeout': [ scan_queue_timeout, 'scan-queue-timeout', [ int, 'None' ], False ],
        }, {
        } )
    
    def vscan_scanner_pool_create(self, privileged_users, servers, scanner_pool, max_session_setup_retries=None, session_teardown_timeout=None, return_record=None, session_setup_timeout=None, request_timeout=None, scan_queue_timeout=None):
        """
        Create a virus scanner pool, which is used for validating and
        managing connections between clustered Data ONTAP and Vscan
        servers.
        
        :param privileged_users: List of privileged users.
        
        :param servers: List of IP addresses of Vscan servers which are allowed to
                connect to clustered Data ONTAP.
        
        :param scanner_pool: Name of the virus scanner pool.
        
        :param max_session_setup_retries: Maximum number of consecutive session-setup attempts. The default
                value of 5 is taken if not provided while creating a scanner
                pool.
        
        :param session_teardown_timeout: Total session-teardown time-limit in seconds. The default value
                of 10 is taken if not provided while creating a scanner pool.
        
        :param return_record: If set to true, returns the vscan-scanner-pool on successful
                creation.
                Default: false
        
        :param session_setup_timeout: Total session-setup time-limit in seconds. The default value of
                10 is taken if not provided while creating a scanner pool.
        
        :param request_timeout: Total request-service time-limit in seconds. The default value of
                30 is taken if not provided while creating a scanner pool.
        
        :param scan_queue_timeout: Scan-queue wait-time-limit in seconds. The default value of 20 is
                taken if not provided while creating a scanner pool.
        """
        return self.request( "vscan-scanner-pool-create", {
            'max_session_setup_retries': [ max_session_setup_retries, 'max-session-setup-retries', [ int, 'None' ], False ],
            'session_teardown_timeout': [ session_teardown_timeout, 'session-teardown-timeout', [ int, 'None' ], False ],
            'privileged_users': [ privileged_users, 'privileged-users', [ basestring, 'privileged-user' ], True ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'servers': [ servers, 'servers', [ basestring, 'ip-address' ], True ],
            'scanner_pool': [ scanner_pool, 'scanner-pool', [ basestring, 'scanner-pool' ], False ],
            'session_setup_timeout': [ session_setup_timeout, 'session-setup-timeout', [ int, 'None' ], False ],
            'request_timeout': [ request_timeout, 'request-timeout', [ int, 'None' ], False ],
            'scan_queue_timeout': [ scan_queue_timeout, 'scan-queue-timeout', [ int, 'None' ], False ],
        }, {
            'result': [ VscanScannerPoolInfo, False ],
        } )
    
    def vscan_on_access_policy_delete(self, policy_name):
        """
        Delete an On-Access policy.
        
        :param policy_name: Name of the policy.
        """
        return self.request( "vscan-on-access-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'policy-name' ], False ],
        }, {
        } )
    
    def vscan_scanner_pool_delete(self, scanner_pool):
        """
        Delete a scanner pool.
        
        :param scanner_pool: Name of the virus scanner pool.
        """
        return self.request( "vscan-scanner-pool-delete", {
            'scanner_pool': [ scanner_pool, 'scanner-pool', [ basestring, 'scanner-pool' ], False ],
        }, {
        } )
