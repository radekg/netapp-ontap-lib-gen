from netapp.connection import NaConnection
from av_on_demand_command_scan_dir_get_iter_key_td import AvOnDemandCommandScanDirGetIterKeyTd # 2 properties
from av_event_info import AvEventInfo # 3 properties
from av_on_demand_command_scan_cluster_get_iter_key_td import AvOnDemandCommandScanClusterGetIterKeyTd # 2 properties
from av_on_demand_command_scan_dir_info import AvOnDemandCommandScanDirInfo # 9 properties
from job_schedule import JobSchedule # 0 properties
from av_on_access_policy_get_iter_key_td import AvOnAccessPolicyGetIterKeyTd # 2 properties
from av_on_demand_report_get_iter_key_td import AvOnDemandReportGetIterKeyTd # 2 properties
from av_on_demand_job_info import AvOnDemandJobInfo # 6 properties
from av_engine_option import AvEngineOption # 17 properties
from av_log_iter_key_td import AvLogIterKeyTd # 2 properties
from av_on_demand_report_info import AvOnDemandReportInfo # 14 properties
from fileop_profile import FileopProfile # 0 properties
from av_on_demand_command_scan_vserver_info import AvOnDemandCommandScanVserverInfo # 10 properties
from av_on_demand_command_scan_file_info import AvOnDemandCommandScanFileInfo # 5 properties
from av_on_demand_command_scan_cluster_info import AvOnDemandCommandScanClusterInfo # 11 properties
from av_on_demand_command_scan_vserver_get_iter_key_td import AvOnDemandCommandScanVserverGetIterKeyTd # 2 properties
from av_on_demand_command_scan_file_get_iter_key_td import AvOnDemandCommandScanFileGetIterKeyTd # 2 properties
from av_on_access_policy_info import AvOnAccessPolicyInfo # 14 properties
from include_exclude import IncludeExclude # 0 properties
from av_on_demand_job_get_iter_key_td import AvOnDemandJobGetIterKeyTd # 2 properties

class AntivirusConnection(NaConnection):
    
    def av_on_access_policy_modify(self, policy_name, is_scan_enabled=None, is_cifs_execute_access_scan_enabled=None, is_row_volume_scan_enabled=None, include_cifs_share=None, cifs_share_list_pattern=None, include_cifs_file=None, cifs_file_list_pattern=None, fileop_profile=None, is_scan_mandatory=None, protocols=None, is_nfs_execute_permission_scan_enabled=None):
        """
        This API enables you to modify on-access policies for your
        antivirus scan engine.
        
        :param policy_name: Name of the on-access policy.
        
        :param is_scan_enabled: This specifies whether an on-access scan is enabled on the
                virtual server or volume. Default is false.
        
        :param is_cifs_execute_access_scan_enabled: If true, only the files opened with execute access are scanned,
                otherwise all files will be scanned (CIFS only). Default is
                false.
        
        :param is_row_volume_scan_enabled: This specifies whether an on-access scan is enabled on a
                read-only volume. Default is false. Currently not supported.
        
        :param include_cifs_share: This specifies whether the CIFS shares defined in the parameter
                cifs-share-list-pattern will be included in or excluded from the
                antivirus scan.  If true, then cifs-share-list-pattern is an
                inclusive match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param cifs_share_list_pattern: This specifies the regular expression that lists CIFS shares to
                be included in or excluded from an antivirus scan. Uses
                GNU-compatible regular expressions.
        
        :param include_cifs_file: This specifies whether the files defined in the parameter
                cifs-file-list-pattern will be included in or excluded from an
                antivirus scan. If true, then cifs-file-list-pattern is an
                inclusive match, else an exclusive match. Default is true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param cifs_file_list_pattern: This specifies the regular expression that lists files to be
                included in or excluded from an antivirus scan. Uses
                GNU-compatible regular expressions.
        
        :param fileop_profile: This option enables you specify the file profile. This determines
                what scan action should be taken for each incoming file
                operations. Each of this options provide different level or
                priority of scanning for different file operations and some of
                them are very strict in scanning and will have performance impact
                for example  multi-protocols-strict is very safe, does not allow
                any virus to be returned to the clients  but has a performance
                hit when a file is subject to multiple read or write sequences,
                each read of the sequence will launch a scan.
                multi-protocols-standard is  less safe, doesn't protect CIFS or
                NFSv4 in the case a virus is written to the file while it's open
                and has better performance for CIFS.
                Possible values:
                <ul>
                <li> "cifs_nfs4_only"           ,
                <li> "nfs3_only"                ,
                <li> "multi_proto_standard"     ,
                <li> "multi_proto_strict"
                </ul>
        
        :param is_scan_mandatory: This specifies if an access to a file is allowed in the event
                that the system has no antivirus scan servers available to
                perform the scan. Default is true.
        
        :param protocols: This specifies a list of protocols supported for  scanning.
                Default protocols are cifs and nfsv4.
                Possible values:
                <ul>
                <li> "cifs" ,
                <li> "nfs3" ,
                <li> "nfs4"
                </ul>
        
        :param is_nfs_execute_permission_scan_enabled: If true, only the files with execute permission are scanned,
                otherwise files with all permissions are scanned (NFS
                only).Default is false.
        """
        return self.request( "av-on-access-policy-modify", {
            'is_scan_enabled': [ is_scan_enabled, 'is-scan-enabled', [ bool, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'antivirus-policy' ], False ],
            'is_cifs_execute_access_scan_enabled': [ is_cifs_execute_access_scan_enabled, 'is-cifs-execute-access-scan-enabled', [ bool, 'None' ], False ],
            'is_row_volume_scan_enabled': [ is_row_volume_scan_enabled, 'is-row-volume-scan-enabled', [ bool, 'None' ], False ],
            'include_cifs_share': [ include_cifs_share, 'include-cifs-share', [ basestring, 'include-exclude' ], False ],
            'cifs_share_list_pattern': [ cifs_share_list_pattern, 'cifs-share-list-pattern', [ basestring, 'None' ], False ],
            'include_cifs_file': [ include_cifs_file, 'include-cifs-file', [ basestring, 'include-exclude' ], False ],
            'cifs_file_list_pattern': [ cifs_file_list_pattern, 'cifs-file-list-pattern', [ basestring, 'None' ], False ],
            'fileop_profile': [ fileop_profile, 'fileop-profile', [ basestring, 'fileop-profile' ], False ],
            'is_scan_mandatory': [ is_scan_mandatory, 'is-scan-mandatory', [ bool, 'None' ], False ],
            'protocols': [ protocols, 'protocols', [ basestring, 'protocol' ], True ],
            'is_nfs_execute_permission_scan_enabled': [ is_nfs_execute_permission_scan_enabled, 'is-nfs-execute-permission-scan-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_dir_create(self, scan_path, command_name, force=None, enable_subdirectory_recursion=None, return_record=None, file_pattern=None, enable_junction_following=None, include_files=None):
        """
        This API lets you create  an on-demand scan command of scan type
        directory. Use this API when you want the antivirus scan engine
        to scan a set of files within a specified path.
        
        :param scan_path: Full path name of the directory to be scanned.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive scanning is not enabled. To allow recursive
                scanning, set this parameter to false. Default is false.
        
        :param return_record: If set to true, returns the av-on-demand-command-scan-dir on
                successful creation.
                Default: false
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exclude from the antivirus scan. If this parameter
                is used, you must specify whether to include or exclude files
                using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following junctions is not allowed. To allow the scan to follow
                junctions, set this parameter to false. Default is false.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-dir-create", {
            'scan_path': [ scan_path, 'scan-path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
        }, {
            'result': [ AvOnDemandCommandScanDirInfo, False ],
        } )
    
    def av_on_demand_report_upload(self, destination, id):
        """
        This API enables you to upload an on-demand scan report from your
        cluster to a specified location.
        
        :param destination: Destination URL. Can use either FTP, HTTP or TFTP protocol to
                upload the on-demand scan report log file to the chosen server.
        
        :param id: ID
        """
        return self.request( "av-on-demand-report-upload", {
            'destination': [ destination, 'destination', [ basestring, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_dir_modify(self, command_name, scan_path=None, force=None, enable_subdirectory_recursion=None, file_pattern=None, enable_junction_following=None, include_files=None):
        """
        This API lets you modify an on-demand scan command of scan type
        directory. When you modify an existing command, the parameters in
        the modify API replace all parameters specified in the create
        API.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param scan_path: Full path name of the directory to be scanned.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive scanning is not enabled. To allow recursive
                scanning, set this parameter to false. Default is false.
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exclude from the antivirus scan. If this parameter
                is used, you must specify whether to include or exclude files
                using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following junctions is not allowed. To allow the scan to follow
                junctions, set this parameter to false. Default is false.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-dir-modify", {
            'scan_path': [ scan_path, 'scan-path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
        }, {
        } )
    
    def av_on_access_policy_create(self, policy_name, is_scan_enabled=None, is_cifs_execute_access_scan_enabled=None, return_record=None, is_row_volume_scan_enabled=None, include_cifs_share=None, cifs_share_list_pattern=None, include_cifs_file=None, cifs_file_list_pattern=None, fileop_profile=None, is_scan_mandatory=None, protocols=None, is_nfs_execute_permission_scan_enabled=None):
        """
        An antivirus on-access-policy defines the kind of antivirus
        scanning to be done on a file while it is being accessed through
        normal file operations. This API enables you to create on-access
        policies for scanning.
        
        :param policy_name: Name of the on-access policy.
        
        :param is_scan_enabled: This specifies whether an on-access scan is enabled on the
                virtual server or volume. Default is false.
        
        :param is_cifs_execute_access_scan_enabled: If true, only the files opened with execute access are scanned,
                otherwise all files will be scanned (CIFS only). Default is
                false.
        
        :param return_record: If set to true, returns the av-on-access-policy on successful
                creation.
                Default: false
        
        :param is_row_volume_scan_enabled: This specifies whether an on-access scan is enabled on a
                read-only volume. Default is false. Currently not supported.
        
        :param include_cifs_share: This specifies whether the CIFS shares defined in the parameter
                cifs-share-list-pattern will be included in or excluded from the
                antivirus scan.  If true, then cifs-share-list-pattern is an
                inclusive match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param cifs_share_list_pattern: This specifies the regular expression that lists CIFS shares to
                be included in or excluded from an antivirus scan. Uses
                GNU-compatible regular expressions.
        
        :param include_cifs_file: This specifies whether the files defined in the parameter
                cifs-file-list-pattern will be included in or excluded from an
                antivirus scan. If true, then cifs-file-list-pattern is an
                inclusive match, else an exclusive match. Default is true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param cifs_file_list_pattern: This specifies the regular expression that lists files to be
                included in or excluded from an antivirus scan. Uses
                GNU-compatible regular expressions.
        
        :param fileop_profile: This option enables you specify the file profile. This determines
                what scan action should be taken for each incoming file
                operations. Each of this options provide different level or
                priority of scanning for different file operations and some of
                them are very strict in scanning and will have performance impact
                for example  multi-protocols-strict is very safe, does not allow
                any virus to be returned to the clients  but has a performance
                hit when a file is subject to multiple read or write sequences,
                each read of the sequence will launch a scan.
                multi-protocols-standard is  less safe, doesn't protect CIFS or
                NFSv4 in the case a virus is written to the file while it's open
                and has better performance for CIFS.
                Possible values:
                <ul>
                <li> "cifs_nfs4_only"           ,
                <li> "nfs3_only"                ,
                <li> "multi_proto_standard"     ,
                <li> "multi_proto_strict"
                </ul>
        
        :param is_scan_mandatory: This specifies if an access to a file is allowed in the event
                that the system has no antivirus scan servers available to
                perform the scan. Default is true.
        
        :param protocols: This specifies a list of protocols supported for  scanning.
                Default protocols are cifs and nfsv4.
                Possible values:
                <ul>
                <li> "cifs" ,
                <li> "nfs3" ,
                <li> "nfs4"
                </ul>
        
        :param is_nfs_execute_permission_scan_enabled: If true, only the files with execute permission are scanned,
                otherwise files with all permissions are scanned (NFS
                only).Default is false.
        """
        return self.request( "av-on-access-policy-create", {
            'is_scan_enabled': [ is_scan_enabled, 'is-scan-enabled', [ bool, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'antivirus-policy' ], False ],
            'is_cifs_execute_access_scan_enabled': [ is_cifs_execute_access_scan_enabled, 'is-cifs-execute-access-scan-enabled', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'is_row_volume_scan_enabled': [ is_row_volume_scan_enabled, 'is-row-volume-scan-enabled', [ bool, 'None' ], False ],
            'include_cifs_share': [ include_cifs_share, 'include-cifs-share', [ basestring, 'include-exclude' ], False ],
            'cifs_share_list_pattern': [ cifs_share_list_pattern, 'cifs-share-list-pattern', [ basestring, 'None' ], False ],
            'include_cifs_file': [ include_cifs_file, 'include-cifs-file', [ basestring, 'include-exclude' ], False ],
            'cifs_file_list_pattern': [ cifs_file_list_pattern, 'cifs-file-list-pattern', [ basestring, 'None' ], False ],
            'fileop_profile': [ fileop_profile, 'fileop-profile', [ basestring, 'fileop-profile' ], False ],
            'is_scan_mandatory': [ is_scan_mandatory, 'is-scan-mandatory', [ bool, 'None' ], False ],
            'protocols': [ protocols, 'protocols', [ basestring, 'protocol' ], True ],
            'is_nfs_execute_permission_scan_enabled': [ is_nfs_execute_permission_scan_enabled, 'is-nfs-execute-permission-scan-enabled', [ bool, 'None' ], False ],
        }, {
            'result': [ AvOnAccessPolicyInfo, False ],
        } )
    
    def av_on_demand_command_scan_cluster_modify(self, command_name, directory_pattern=None, force=None, enable_subdirectory_recursion=None, file_pattern=None, enable_junction_following=None, vserver_pattern=None, include_files=None, include_directories=None, include_vservers=None):
        """
        This API lets you modify an on-demand scan command of scan type
        cluster. When you modify an existing command, the parameters in
        the modify API replace a          ll parameters specified in the
        create API.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param directory_pattern: This specifies the directories to be scanned. This parameter
                specifies the case-insensitive regular expression that defines
                what directories      to include or exclude from the antivirus
                scan. If this parameter is used, you must specify whether to
                include or exclude directories using the include-directories
                paramete     r.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive s          canning is not enabled. To allow
                recursive scanning, set this parameter to false. Default is
                false.
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exc          lude from the antivirus scan. If this
                parameter is used, you must specify whether to include or exclude
                files using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following ju          nctions is not allowed. To allow the scan
                to follow junctions, set this parameter to false. Default is
                false.
        
        :param vserver_pattern: This parameter specifies the case-insensitive regular expression
                that defines what Vservers to include or exclude from the
                antivirus scan. If this parameter is used, you must specify
                whether to include or exclude Vservers using the include-vservers
                parameter.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_directories: This specifies whether the files defined in the parameter
                directory-pattern will be included in or excluded from the
                antivirus   scan.  If true, then directory-pattern is an
                inclusive match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_vservers: This specifies whether the files defined in the parameter
                vserver-pattern will be included in or excluded from the
                antivirus  scan.  If true, then vserver-pattern is an inclusive
                match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-cluster-modify", {
            'directory_pattern': [ directory_pattern, 'directory-pattern', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'vserver_pattern': [ vserver_pattern, 'vserver-pattern', [ basestring, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
            'include_directories': [ include_directories, 'include-directories', [ basestring, 'include-exclude' ], False ],
            'include_vservers': [ include_vservers, 'include-vservers', [ basestring, 'include-exclude' ], False ],
        }, {
        } )
    
    def av_get_log(self, datetime, vendor_string=None, desired_attributes=None):
        """
        Get the attributes of the antivirus.
        
        :param datetime: When the event is logged. The time value is in seconds since
                January 1, 1970.
        
        :param vendor_string: Vendor String
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-get-log", {
            'vendor_string': [ vendor_string, 'vendor-string', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvEventInfo, 'None' ], False ],
            'datetime': [ datetime, 'datetime', [ int, 'None' ], False ],
        }, {
            'attributes': [ AvEventInfo, False ],
        } )
    
    def av_on_demand_command_scan_file_create(self, scan_path, command_name, force=None, return_record=None):
        """
        This API lets you create an on-demand scan command of scan type
        file. Use this API when you want the antivirus scan engine to
        scan a single file.
        
        :param scan_path: Full path name of the file to be scanned.
        
        :param command_name: The name of the scan command. Can be any valid string.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param return_record: If set to true, returns the av-on-demand-command-scan-file on
                successful creation.
                Default: false
        """
        return self.request( "av-on-demand-command-scan-file-create", {
            'scan_path': [ scan_path, 'scan-path', [ basestring, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ AvOnDemandCommandScanFileInfo, False ],
        } )
    
    def av_on_access_policy_get(self, policy_name, desired_attributes=None):
        """
        Return an on-access policy specified.
        
        :param policy_name: Name of the on-access policy.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-on-access-policy-get", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'antivirus-policy' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnAccessPolicyInfo, 'None' ], False ],
        }, {
            'attributes': [ AvOnAccessPolicyInfo, False ],
        } )
    
    def av_on_demand_command_scan_file_get(self, command_name, desired_attributes=None):
        """
        Return a specified on-demand command of scan-type file.
        
        :param command_name: The name of the scan command. Can be any valid string.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-on-demand-command-scan-file-get", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanFileInfo, 'None' ], False ],
        }, {
            'attributes': [ AvOnDemandCommandScanFileInfo, False ],
        } )
    
    def av_on_access_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of  on-access policies.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-access-policy object.
                All av-on-access-policy objects matching this query up to
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
        return self.request( "av-on-access-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnAccessPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnAccessPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnAccessPolicyInfo, True ],
        } )
    
    def av_on_demand_job_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of av-on-demand-job objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-job object.
                All av-on-demand-job objects matching this query up to
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
        return self.request( "av-on-demand-job-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandJobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandJobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandJobInfo, True ],
        } )
    
    def av_on_demand_command_abort(self, id):
        """
        @desc
        
        :param id: ID
        """
        return self.request( "av-on-demand-command-abort", {
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def av_set_log(self, vendor_string, datetime, return_record=None, vendor_id=None):
        """
        Create a new antivirus.
        
        :param vendor_string: Vendor String
        
        :param datetime: When the event is logged. The time value is in seconds since
                January 1, 1970.
        
        :param return_record: If set to true, returns the antivirus on successful creation.
                Default: false
        
        :param vendor_id: Vendor ID
        """
        return self.request( "av-set-log", {
            'vendor_string': [ vendor_string, 'vendor-string', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vendor_id': [ vendor_id, 'vendor-id', [ int, 'None' ], False ],
            'datetime': [ datetime, 'datetime', [ int, 'None' ], False ],
        }, {
            'result': [ AvEventInfo, False ],
        } )
    
    def av_on_demand_command_scan_dir_get(self, command_name, desired_attributes=None):
        """
        Return a specified on-demand command of scan-type directory.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-on-demand-command-scan-dir-get", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanDirInfo, 'None' ], False ],
        }, {
            'attributes': [ AvOnDemandCommandScanDirInfo, False ],
        } )
    
    def av_on_demand_command_scan_cluster_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of on-demand command of scan-type cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-command-scan-cluster object.
                All av-on-demand-command-scan-cluster objects matching this query
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
        return self.request( "av-on-demand-command-scan-cluster-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandCommandScanClusterInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanClusterInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandCommandScanClusterInfo, True ],
        } )
    
    def av_on_demand_command_scan_cluster_get(self, command_name, desired_attributes=None):
        """
        Return a specified on-demand command of scan-type cluster.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-on-demand-command-scan-cluster-get", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanClusterInfo, 'None' ], False ],
        }, {
            'attributes': [ AvOnDemandCommandScanClusterInfo, False ],
        } )
    
    def av_on_access_policy_delete(self, policy_name):
        """
        This API enables you to delete a specified on-access antivirus
        policy.
        
        :param policy_name: Name of the on-access policy.
        """
        return self.request( "av-on-access-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'antivirus-policy' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_vserver_get(self, command_name, desired_attributes=None):
        """
        Return a specified on-demand command of scan-type vserver
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-on-demand-command-scan-vserver-get", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanVserverInfo, 'None' ], False ],
        }, {
            'attributes': [ AvOnDemandCommandScanVserverInfo, False ],
        } )
    
    def av_get_remedy_info(self):
        """
        This gets the remedy information of the Anti-Virus engine installed.
        i.e. what to do when a virus is found.
        """
        return self.request( "av-get-remedy-info", {
        }, {
            'action': [ basestring, False ],
            'repair': [ basestring, False ],
            'directory': [ basestring, False ],
            'option': [ basestring, False ],
            'extension': [ basestring, False ],
        } )
    
    def av_on_demand_command_scan_vserver_create(self, command_name, directory_pattern=None, force=None, enable_subdirectory_recursion=None, return_record=None, file_pattern=None, enable_junction_following=None, include_files=None, include_directories=None):
        """
        This API lets you create an on-demand scan command of scan type
        vserver. Use this API when you want the antivirus scan engine to
        scan a set of files within a specified Vserver.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param directory_pattern: This specifies the directories to be scanned. This parameter
                specifies the case-insensitive regular expression that defines
                what directories to include or exclude from the antivirus scan.
                If this parameter is used, you must specify whether to include or
                exclude directories using the include-directories parameter.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive s     canning is not enabled. To allow recursive
                scanning, set this parameter to false. Default is false.
        
        :param return_record: If set to true, returns the av-on-demand-command-scan-vserver on
                successful creation.
                Default: false
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exclude from the antivirus scan. If this parameter
                is used, you must specify whether to include or exclude files
                using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following ju     nctions is not allowed. To allow the scan to
                follow junctions, set this parameter to false. Default is false.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_directories: This specifies whether the files defined in the parameter
                directory-pattern will be included in or excluded from the
                antivirus  scan.  If true, then directory-pattern is an inclusive
                match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-vserver-create", {
            'directory_pattern': [ directory_pattern, 'directory-pattern', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
            'include_directories': [ include_directories, 'include-directories', [ basestring, 'include-exclude' ], False ],
        }, {
            'result': [ AvOnDemandCommandScanVserverInfo, False ],
        } )
    
    def av_set_engine_options(self, max_recursion_depth=None, decompressed_file_size_limit=None, decompressed_file_count_limit=None, proxy_password=None, group_archive_unpack=None, decompression_layers_limit=None, proxy_port=None, mark_files_greater_than_2gb_clean=None, cache_size=None, macro_analysis=None, proxy_host=None, mime_lines_to_scan=None, scan_mime=None, heuristic_analysis=None, is_spyware_enabled=None, decompression_size_factor=None, proxy_login=None):
        """
        Modify the attributes of antivirus object.
        
        :param max_recursion_depth: Max recursion depth into archives
        
        :param decompressed_file_size_limit: Max size of files in archive
        
        :param decompressed_file_count_limit: File count to decompress in archive
        
        :param proxy_password: proxy server password
        
        :param group_archive_unpack: Scan archive file formats
        
        :param decompression_layers_limit: Max layers to traverse in archive
        
        :param proxy_port: proxy server port number
        
        :param mark_files_greater_than_2gb_clean: Mark the State of Files Greater Than 2GB Clean
        
        :param cache_size: Max Cache Size for Scanning Files (MB)
        
        :param macro_analysis: Macro Virus Search Analysis
        
        :param proxy_host: proxy server name e.g. http://proxy_server_name
        
        :param mime_lines_to_scan: Max Lines to Scan to Identify MIME file
        
        :param scan_mime: Scan MIME-Encoded Files
        
        :param heuristic_analysis: Heuristic Virus Search Analysis
        
        :param is_spyware_enabled: Spyware enable/disable
        
        :param decompression_size_factor: Max decompression size factor of files in archive
        
        :param proxy_login: proxy server login
        """
        return self.request( "av-set-engine-options", {
            'max_recursion_depth': [ max_recursion_depth, 'max-recursion-depth', [ int, 'None' ], False ],
            'decompressed_file_size_limit': [ decompressed_file_size_limit, 'decompressed-file-size-limit', [ int, 'None' ], False ],
            'decompressed_file_count_limit': [ decompressed_file_count_limit, 'decompressed-file-count-limit', [ int, 'None' ], False ],
            'proxy_password': [ proxy_password, 'proxy-password', [ basestring, 'None' ], False ],
            'group_archive_unpack': [ group_archive_unpack, 'group-archive-unpack', [ bool, 'None' ], False ],
            'decompression_layers_limit': [ decompression_layers_limit, 'decompression-layers-limit', [ int, 'None' ], False ],
            'proxy_port': [ proxy_port, 'proxy-port', [ int, 'None' ], False ],
            'mark_files_greater_than_2gb_clean': [ mark_files_greater_than_2gb_clean, 'mark-files-greater-than-2gb-clean', [ bool, 'None' ], False ],
            'cache_size': [ cache_size, 'cache-size', [ int, 'None' ], False ],
            'macro_analysis': [ macro_analysis, 'macro-analysis', [ bool, 'None' ], False ],
            'proxy_host': [ proxy_host, 'proxy-host', [ basestring, 'None' ], False ],
            'mime_lines_to_scan': [ mime_lines_to_scan, 'mime-lines-to-scan', [ int, 'None' ], False ],
            'scan_mime': [ scan_mime, 'scan-mime', [ bool, 'None' ], False ],
            'heuristic_analysis': [ heuristic_analysis, 'heuristic-analysis', [ bool, 'None' ], False ],
            'is_spyware_enabled': [ is_spyware_enabled, 'is-spyware-enabled', [ bool, 'None' ], False ],
            'decompression_size_factor': [ decompression_size_factor, 'decompression-size-factor', [ int, 'None' ], False ],
            'proxy_login': [ proxy_login, 'proxy-login', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_vserver_modify(self, command_name, directory_pattern=None, force=None, enable_subdirectory_recursion=None, file_pattern=None, enable_junction_following=None, include_files=None, include_directories=None):
        """
        This API lets you modify an on-demand scan command of scan type
        vserver. When you modify an existing command, the parameters in
        the modify API replace a     ll parameters specified in the
        create API.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param directory_pattern: This specifies the directories to be scanned. This parameter
                specifies the case-insensitive regular expression that defines
                what directories to include or exclude from the antivirus scan.
                If this parameter is used, you must specify whether to include or
                exclude directories using the include-directories parameter.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive s     canning is not enabled. To allow recursive
                scanning, set this parameter to false. Default is false.
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exclude from the antivirus scan. If this parameter
                is used, you must specify whether to include or exclude files
                using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following ju     nctions is not allowed. To allow the scan to
                follow junctions, set this parameter to false. Default is false.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_directories: This specifies whether the files defined in the parameter
                directory-pattern will be included in or excluded from the
                antivirus  scan.  If true, then directory-pattern is an inclusive
                match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-vserver-modify", {
            'directory_pattern': [ directory_pattern, 'directory-pattern', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
            'include_directories': [ include_directories, 'include-directories', [ basestring, 'include-exclude' ], False ],
        }, {
        } )
    
    def av_get_engine_info(self):
        """
        This gets the attributes of the Anti-Virus engine installed.
        """
        return self.request( "av-get-engine-info", {
        }, {
            'license-key': [ basestring, False ],
            'license-type': [ basestring, False ],
            'vendor': [ basestring, False ],
            'update-url': [ basestring, False ],
            'desired-activation-code': [ basestring, False ],
            'current-activation-code': [ basestring, False ],
            'is-enabled': [ bool, False ],
            'seats': [ int, False ],
            'license-expiry-time': [ int, False ],
            'prod-info': [ basestring, False ],
        } )
    
    def av_on_demand_command_scan_dir_delete(self, command_name):
        """
        This API enables you to delete a specified on-demand command of
        scan-type directory.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        """
        return self.request( "av-on-demand-command-scan-dir-delete", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_file_modify(self, command_name, scan_path=None, force=None):
        """
        This API lets you modify an on-demand scan command of scan type
        file. When you modify an existing command, the parameters in the
        modify command replace all parameters specified in the create
        command.
        
        :param command_name: The name of the scan command. Can be any valid string.
        
        :param scan_path: Full path name of the file to be scanned.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        """
        return self.request( "av-on-demand-command-scan-file-modify", {
            'scan_path': [ scan_path, 'scan-path', [ basestring, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_schedule(self, command, schedule, vserver=None):
        """
        @desc
        
        :param command: Command Name
        
        :param schedule: Schedule Name
        
        :param vserver: Vserver
        """
        return self.request( "av-on-demand-command-schedule", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'command': [ command, 'command', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_file_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of on-demand command of scan-type file.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-command-scan-file object.
                All av-on-demand-command-scan-file objects matching this query up
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
        return self.request( "av-on-demand-command-scan-file-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandCommandScanFileInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanFileInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandCommandScanFileInfo, True ],
        } )
    
    def av_on_demand_command_unschedule(self, id, vserver=None):
        """
        @desc
        
        :param id: ID
        
        :param vserver: Vserver
        """
        return self.request( "av-on-demand-command-unschedule", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_file_delete(self, command_name):
        """
        This API enables you to delete a specified on-demand command of
        scan-type file.
        
        :param command_name: The name of the scan command. Can be any valid string.
        """
        return self.request( "av-on-demand-command-scan-file-delete", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def antivirus_modify(self, max_recursion_depth=None, group_archive_unpack=None, trend_decompressed_file_count_limit=None, proxy_port=None, proxy_host=None, trend_is_spyware_enabled=None, cache_size=None, trend_decompression_layers_limit=None, macro_analysis=None, trend_decompressed_file_size_limit=None, mime_lines_to_scan=None, scan_mime=None, heuristic_analysis=None, proxy_login=None, trend_decompression_size_factor=None, trend_mark_files_greater_than_2gb_clean=None):
        """
        auto generated : Configures the Antivirus Server Options
        
        :param max_recursion_depth: Max Recursion Depth into Archives
        
        :param group_archive_unpack: Scan Archive File Formats
        
        :param trend_decompressed_file_count_limit: File Count to Decompress in Archive
        
        :param proxy_port: Proxy Server Port Number
        
        :param proxy_host: Proxy Server Name
        
        :param trend_is_spyware_enabled: Spyware enable/disable
        
        :param cache_size: Max Cache Size for Scanning Files (MB)
        
        :param trend_decompression_layers_limit: Max Layers to Traverse in Archive
        
        :param macro_analysis: Macro Virus Search Analysis
        
        :param trend_decompressed_file_size_limit: Max Size of Files in Archive
        
        :param mime_lines_to_scan: Max Lines to Scan to Identify MIME file
        
        :param scan_mime: Scan MIME-Encoded Files
        
        :param heuristic_analysis: Heuristic Virus Search Analysis
        
        :param proxy_login: Proxy Server Login
        
        :param trend_decompression_size_factor: Max Decompression Size Factor of Files in Archive
        
        :param trend_mark_files_greater_than_2gb_clean: Mark the State of Files Greater Than 2GB Clean
        """
        return self.request( "antivirus-modify", {
            'max_recursion_depth': [ max_recursion_depth, 'max-recursion-depth', [ int, 'None' ], False ],
            'group_archive_unpack': [ group_archive_unpack, 'group-archive-unpack', [ bool, 'None' ], False ],
            'trend_decompressed_file_count_limit': [ trend_decompressed_file_count_limit, 'trend-decompressed-file-count-limit', [ int, 'None' ], False ],
            'proxy_port': [ proxy_port, 'proxy-port', [ int, 'None' ], False ],
            'proxy_host': [ proxy_host, 'proxy-host', [ basestring, 'None' ], False ],
            'trend_is_spyware_enabled': [ trend_is_spyware_enabled, 'trend-is-spyware-enabled', [ bool, 'None' ], False ],
            'cache_size': [ cache_size, 'cache-size', [ int, 'None' ], False ],
            'trend_decompression_layers_limit': [ trend_decompression_layers_limit, 'trend-decompression-layers-limit', [ int, 'None' ], False ],
            'macro_analysis': [ macro_analysis, 'macro-analysis', [ bool, 'None' ], False ],
            'trend_decompressed_file_size_limit': [ trend_decompressed_file_size_limit, 'trend-decompressed-file-size-limit', [ int, 'size' ], False ],
            'mime_lines_to_scan': [ mime_lines_to_scan, 'mime-lines-to-scan', [ int, 'None' ], False ],
            'scan_mime': [ scan_mime, 'scan-mime', [ bool, 'None' ], False ],
            'heuristic_analysis': [ heuristic_analysis, 'heuristic-analysis', [ bool, 'None' ], False ],
            'proxy_login': [ proxy_login, 'proxy-login', [ basestring, 'None' ], False ],
            'trend_decompression_size_factor': [ trend_decompression_size_factor, 'trend-decompression-size-factor', [ int, 'None' ], False ],
            'trend_mark_files_greater_than_2gb_clean': [ trend_mark_files_greater_than_2gb_clean, 'trend-mark-files-greater-than-2gb-clean', [ bool, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_run(self, command, vserver=None):
        """
        @desc
        
        :param command: Command Name
        
        :param vserver: Vserver
        """
        return self.request( "av-on-demand-command-run", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'command': [ command, 'command', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_report_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of on-demand report.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-report object.
                All av-on-demand-report objects matching this query up to
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
        return self.request( "av-on-demand-report-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandReportInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandReportInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandReportInfo, True ],
        } )
    
    def av_on_demand_command_scan_vserver_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of on-demand command of scan-type vserver
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-command-scan-vserver object.
                All av-on-demand-command-scan-vserver objects matching this query
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
        return self.request( "av-on-demand-command-scan-vserver-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandCommandScanVserverInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanVserverInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandCommandScanVserverInfo, True ],
        } )
    
    def av_get_version_info(self):
        """
        This gets the version information of the Anti-Virus engine installed.
        """
        return self.request( "av-get-version-info", {
        }, {
            'virus-pattern-version': [ basestring, False ],
            'last-update-time': [ int, False ],
            'vsapi-64-bit-version': [ basestring, False ],
            'spyware-pattern-version': [ basestring, False ],
            'vsapi-32-bit-version': [ basestring, False ],
        } )
    
    def av_get_engine_options(self, desired_attributes=None):
        """
        Get the attributes of the antivirus.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "av-get-engine-options", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvEngineOption, 'None' ], False ],
        }, {
            'attributes': [ AvEngineOption, False ],
        } )
    
    def av_start_update(self, sync):
        """
        Run an Anti-Virus Update job immediately
        
        :param sync: If 'true', an AV Update job should be started immediately
        """
        return self.request( "av-start-update", {
            'sync': [ sync, 'sync', [ bool, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_cluster_create(self, command_name, directory_pattern=None, force=None, enable_subdirectory_recursion=None, return_record=None, file_pattern=None, enable_junction_following=None, vserver_pattern=None, include_files=None, include_directories=None, include_vservers=None):
        """
        This API lets you create an on-demand scan command of scan type
        cluster. Use this command when you want the antivirus scan engine
        to scan a set of files on the cluster.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        
        :param directory_pattern: This specifies the directories to be scanned. This parameter
                specifies the case-insensitive regular expression that defines
                what directories      to include or exclude from the antivirus
                scan. If this parameter is used, you must specify whether to
                include or exclude directories using the include-directories
                paramete     r.
        
        :param force: Force the file to be scanned even if it has already been scanned.
                Default is false.
        
        :param enable_subdirectory_recursion: This parameter specifies whether to enable or disable  recursive
                scanning through sub-directories. If the parameter is set to
                true, recursive s          canning is not enabled. To allow
                recursive scanning, set this parameter to false. Default is
                false.
        
        :param return_record: If set to true, returns the av-on-demand-command-scan-cluster on
                successful creation.
                Default: false
        
        :param file_pattern: This specifies the files to be scanned. This parameter specifies
                the case-insensitive regular expression that defines what files
                to include or exc          lude from the antivirus scan. If this
                parameter is used, you must specify whether to include or exclude
                files using the include-files parameter.
        
        :param enable_junction_following: This parameter specifies whether the antivirus scan is allowed to
                follow volume junctions. If the parameter is set to true,
                following ju          nctions is not allowed. To allow the scan
                to follow junctions, set this parameter to false. Default is
                false.
        
        :param vserver_pattern: This parameter specifies the case-insensitive regular expression
                that defines what Vservers to include or exclude from the
                antivirus scan. If this parameter is used, you must specify
                whether to include or exclude Vservers using the include-vservers
                parameter.
        
        :param include_files: This specifies whether the files defined in the parameter
                file-pattern will be included in or excluded from the antivirus
                scan.  If true, then file-pattern is an inclusive match, else an
                exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_directories: This specifies whether the files defined in the parameter
                directory-pattern will be included in or excluded from the
                antivirus   scan.  If true, then directory-pattern is an
                inclusive match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        
        :param include_vservers: This specifies whether the files defined in the parameter
                vserver-pattern will be included in or excluded from the
                antivirus  scan.  If true, then vserver-pattern is an inclusive
                match, else an exclusive match.  Default it true.
                Possible values:
                <ul>
                <li> "include"   ,
                <li> "exclude"
                </ul>
        """
        return self.request( "av-on-demand-command-scan-cluster-create", {
            'directory_pattern': [ directory_pattern, 'directory-pattern', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'enable_subdirectory_recursion': [ enable_subdirectory_recursion, 'enable-subdirectory-recursion', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
            'file_pattern': [ file_pattern, 'file-pattern', [ basestring, 'None' ], False ],
            'enable_junction_following': [ enable_junction_following, 'enable-junction-following', [ bool, 'None' ], False ],
            'vserver_pattern': [ vserver_pattern, 'vserver-pattern', [ basestring, 'None' ], False ],
            'include_files': [ include_files, 'include-files', [ basestring, 'include-exclude' ], False ],
            'include_directories': [ include_directories, 'include-directories', [ basestring, 'include-exclude' ], False ],
            'include_vservers': [ include_vservers, 'include-vservers', [ basestring, 'include-exclude' ], False ],
        }, {
            'result': [ AvOnDemandCommandScanClusterInfo, False ],
        } )
    
    def av_on_demand_command_scan_cluster_delete(self, command_name):
        """
        This API enables you to delete a specified on-demand command of
        scan-type cluster.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        """
        return self.request( "av-on-demand-command-scan-cluster-delete", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_vserver_delete(self, command_name):
        """
        This API enables you to delete a specified on-demand command of
        scan-type vserver.
        
        :param command_name: Name of the on-demand command. Can be any valid string.
        """
        return self.request( "av-on-demand-command-scan-vserver-delete", {
            'command_name': [ command_name, 'command-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_set_engine_info(self, license_key=None, license_type=None, vendor=None, update_url=None, desired_activation_code=None, current_activation_code=None, is_enabled=None, seats=None, license_expiry_time=None, prod_info=None):
        """
        This sets the attributes of the Anti-Virus engine installed.
        If an optional attribute is not specified, the current value is left unchanged.
        
        :param license_key: Vendor-specific license key for license management, that is
                currently in effect.
        
        :param license_type: Vendor-specific license type. Possible values:
                <ul>
                <li> "full" - full license</li>
                <li> "eval" - evaluation license</li>
                <li> "none" - no license</li>
                </ul>
        
        :param vendor: Descriptive name of AV vendor
        
        :param update_url: HTTP/HTTPS url for downloading updates.
        
        :param desired_activation_code: Vendor-specific desired activation code for license management.
        
        :param current_activation_code: Vendor-specific activation code for license management, that is
                currently in effect.
        
        :param is_enabled: If 'true', the AV feature is to be enabled on the cluster.
        
        :param seats: Number of nodes that can run an instance of the AV software
                Range : [0..2^32-1]
        
        :param license_expiry_time: Expiry date of license in seconds from midnight Jan 1, 1970.
                Range : [0..2^32-1]
        
        :param prod_info: Detailed information of the AV product
        """
        return self.request( "av-set-engine-info", {
            'license_key': [ license_key, 'license-key', [ basestring, 'None' ], False ],
            'license_type': [ license_type, 'license-type', [ basestring, 'None' ], False ],
            'vendor': [ vendor, 'vendor', [ basestring, 'None' ], False ],
            'update_url': [ update_url, 'update-url', [ basestring, 'None' ], False ],
            'desired_activation_code': [ desired_activation_code, 'desired-activation-code', [ basestring, 'None' ], False ],
            'current_activation_code': [ current_activation_code, 'current-activation-code', [ basestring, 'None' ], False ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
            'seats': [ seats, 'seats', [ int, 'None' ], False ],
            'license_expiry_time': [ license_expiry_time, 'license-expiry-time', [ int, 'None' ], False ],
            'prod_info': [ prod_info, 'prod-info', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_command_scan_dir_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return list of on-demand command of scan-type directory.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                av-on-demand-command-scan-dir object.
                All av-on-demand-command-scan-dir objects matching this query up
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
        return self.request( "av-on-demand-command-scan-dir-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvOnDemandCommandScanDirInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvOnDemandCommandScanDirInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvOnDemandCommandScanDirInfo, True ],
        } )
    
    def av_set_version_info(self, cluster_version, virus_pattern_version=None, vsapi_32_bit_version=None, vsapi_64_bit_version=None, spyware_pattern_version=None, component_updated=None):
        """
        This sets the version information of the Anti-Virus engine installed.
        If an optional attribute is not specified, the current value is left unchanged.
        
        :param cluster_version: The current cluster version of the engine. If this does not correspond to
                the current cluster version of the engine, then the ZAPI fails.
        
        :param virus_pattern_version: The version of the virus pattern files
        
        :param vsapi_32_bit_version: The version of the 32-bit VSAPI engine.
        
        :param vsapi_64_bit_version: The version of the 64-bit VSAPI engine.
        
        :param spyware_pattern_version: The version of the spyware pattern files
        
        :param component_updated: The component that was updated. Possible values:
                <ul>
                <li> "engine" - only antivirus engine was updated</li>
                <li> "vde" - only virus definition files were updated</li>
                <li> "both" - both antivirus engine and virus definition files were updated</li>
                </ul>
        """
        return self.request( "av-set-version-info", {
            'virus_pattern_version': [ virus_pattern_version, 'virus-pattern-version', [ basestring, 'None' ], False ],
            'vsapi_32_bit_version': [ vsapi_32_bit_version, 'vsapi-32-bit-version', [ basestring, 'None' ], False ],
            'vsapi_64_bit_version': [ vsapi_64_bit_version, 'vsapi-64-bit-version', [ basestring, 'None' ], False ],
            'cluster_version': [ cluster_version, 'cluster-version', [ basestring, 'None' ], False ],
            'spyware_pattern_version': [ spyware_pattern_version, 'spyware-pattern-version', [ basestring, 'None' ], False ],
            'component_updated': [ component_updated, 'component-updated', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_set_remedy_info(self, action=None, repair=None, directory=None, option=None, extension=None):
        """
        This sets the quarantine information of the Anti-Virus engine installed.
        If an optional attribute is not specified, the current value is left unchanged.
        
        :param action: The remedy action desired. Possible values:
                <ul>
                <li> "none" - no action will be taken</li>
                <li> "repair" - file will be reparied</li>
                <li> "delete" - file will be deleted</li>
                <li> "quarantine" -  file will be quarantined</li>
                </ul>
        
        :param repair: The failed repair option to try. Possible values:
                <ul>
                <li> "none" - no action will be taken</li>
                <li> "delete" - file will be deleted</li>
                <li> "quarantine" - file will be quarantined</li>
                </ul>
        
        :param directory: The pathname of the directory to use for quarantine.
        
        :param option: The option of the remedy action desired. Possible values:
                <ul>
                <li> "move" - file will be moved</li>
                <li> "add_extension" - an extencion will be added to the file</li>
                </ul>
        
        :param extension: The file extension to use for the remedy action.
        """
        return self.request( "av-set-remedy-info", {
            'action': [ action, 'action', [ basestring, 'None' ], False ],
            'repair': [ repair, 'repair', [ basestring, 'None' ], False ],
            'directory': [ directory, 'directory', [ basestring, 'None' ], False ],
            'option': [ option, 'option', [ basestring, 'None' ], False ],
            'extension': [ extension, 'extension', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def av_on_demand_report_print(self, vserver, id):
        """
        This API prints a specific on-demand scan report to the screen.
        
        :param vserver: Vserver Name
        
        :param id: ID
        """
        return self.request( "av-on-demand-report-print", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
            'file-scanned': [ int, False ],
            'remedy-failed': [ int, False ],
            'scan-retry': [ int, False ],
            'file-infected': [ int, False ],
            'scan-failed': [ int, False ],
            'file-quarantined': [ int, False ],
            'scan-success': [ int, False ],
            'file-deleted': [ int, False ],
            'scan-duration': [ basestring, False ],
            'file-repaired': [ int, False ],
        } )
    
    def av_log_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of antivirus objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                antivirus object.
                All antivirus objects matching this query up to 'max-records'
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
        return self.request( "av-log-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AvEventInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AvEventInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AvEventInfo, True ],
        } )
