from netapp.connection import NaConnection
from system_api_element_info import SystemApiElementInfo # 7 properties
from system_version_tuple import SystemVersionTuple # 3 properties
from system_api_type_entry_info import SystemApiTypeEntryInfo # 2 properties
from node_version_detail_info import NodeVersionDetailInfo # 4 properties
from system_path_version import SystemPathVersion # 2 properties
from system_node_get_iter_key_td import SystemNodeGetIterKeyTd # 1 properties
from system_image_package_get_iter_key_td import SystemImagePackageGetIterKeyTd # 3 properties
from operation_info import OperationInfo # 3 properties
from system_info import SystemInfo # 33 properties
from system_api_info import SystemApiInfo # 3 properties
from capability_info import CapabilityInfo # 2 properties
from replication_transfer_info import ReplicationTransferInfo # 3 properties
from node_details_info import NodeDetailsInfo # 28 properties
from privilege_level import PrivilegeLevel # 0 properties
from node_ontapi_detail_info import NodeOntapiDetailInfo # 4 properties
from vmhost_info import VmhostInfo # 12 properties
from system_get_node_info_iter_key_td import SystemGetNodeInfoIterKeyTd # 1 properties
from vm_system_disks import VmSystemDisks # 6 properties
from system_image_package_attributes import SystemImagePackageAttributes # 2 properties
from arg import Arg # 0 properties
from system_image_attributes import SystemImageAttributes # 8 properties
from system_api_entry_info import SystemApiEntryInfo # 2 properties
from system_user_capability_get_iter_key_td import SystemUserCapabilityGetIterKeyTd # 2 properties
from nvram_battery_status_enum import NvramBatteryStatusEnum # 0 properties
from system_node_kernel_info import SystemNodeKernelInfo # 4 properties
from api_list_info import ApiListInfo # 0 properties
from system_image_get_iter_key_td import SystemImageGetIterKeyTd # 2 properties

class SystemConnection(NaConnection):
    
    def system_ontapi_limits_get(self):
        """
        Get the ONTAPI monitoring limits such as the mode, maximum
        allowed size of any API reply, and/or the maximum allowed runtime
        for any API.
        """
        return self.request( "system-ontapi-limits-get", {
        }, {
            'max-run-time': [ int, False ],
            'monitor-mode': [ basestring, False ],
            'max-reply-size': [ int, False ],
        } )
    
    def system_ontapi_limits_set(self, max_run_time=None, monitor_mode=None, max_reply_size=None):
        """
        Set the maximum allowed size of the API reply, and/or the maximum
        allowed runtime for the API before the API is treated
        noncompliant. At least one of the allowed inputs must be
        specified.
        
        :param max_run_time: Maximum Compliant Run Time
        
        :param monitor_mode: Monitor Mode.
                <p>
                Possible values:
                <ul>
                <li> 'off'       - No monitoring of iter or non-iter APIs,
                <li> 'silent'    - Iter-APIs are silently soft limited,
                <li> 'log'       - Log the detected API
                </ul>
                <p>
        
        :param max_reply_size: Maximum Compliant Reply Size
        """
        return self.request( "system-ontapi-limits-set", {
            'max_run_time': [ max_run_time, 'max-run-time', [ int, 'None' ], False ],
            'monitor_mode': [ monitor_mode, 'monitor-mode', [ basestring, 'None' ], False ],
            'max_reply_size': [ max_reply_size, 'max-reply-size', [ int, 'None' ], False ],
        }, {
        } )
    
    def system_time_change_notify(self, change_type):
        """
        Notify the D-blade about a change in Timekeeping parameters.
        
        :param change_type: The type of Timekeeping parameter that has changed.
                Currently supported values are: ntpd, timezone and zoneinfo.
        """
        return self.request( "system-time-change-notify", {
            'change_type': [ change_type, 'change-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_node_rename(self, node, new_name):
        """
        Rename the specified node to a new name specified by 'new-name'
        
        :param node: The textual name of a node.
        
        :param new_name: New Name
        """
        return self.request( "system-node-rename", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_set_new_ontap_version_downloaded(self):
        """
        Called when a new version of Data ONTAP is downloaded
        making a non-disruptive upgrade possible.
        """
        return self.request( "system-set-new-ontap-version-downloaded", {
        }, {
        } )
    
    def system_image_fetch_package(self, node, package, replace_package=None, rename_package=None):
        """
        Fetch a file from a URL.  This API will return immediately.  The
        progress can be monitored using the
        'system-image-update-progress-get' API.
        
        :param node: Node
        
        :param package: Package URL
        
        :param replace_package: Replace the Local File
        
        :param rename_package: Rename the File
        """
        return self.request( "system-image-fetch-package", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'replace_package': [ replace_package, 'replace-package', [ bool, 'None' ], False ],
            'rename_package': [ rename_package, 'rename-package', [ basestring, 'None' ], False ],
            'package': [ package, 'package', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_node_revert_to(self, node, version, check_only=None, skip_lun_config_check=None, skip_vol_aggr_check=None):
        """
        auto generated : Revert a node to a previous release of Data
        ONTAP
        
        :param node: The textual name of a node.
        
        :param version: Data ONTAP Version
                Possible values:
                <ul>
                <li> "8_1"  - Data ONTAP 8.1
                </ul>
        
        :param check_only: Capability Check
        
        :param skip_lun_config_check: Skip Array LUN Config Check
        
        :param skip_vol_aggr_check: Skip Offline Volume/Aggregate Check
        """
        return self.request( "system-node-revert-to", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'check_only': [ check_only, 'check-only', [ bool, 'None' ], False ],
            'version': [ version, 'version', [ basestring, 'revert-version' ], False ],
            'skip_lun_config_check': [ skip_lun_config_check, 'skip-lun-config-check', [ bool, 'None' ], False ],
            'skip_vol_aggr_check': [ skip_vol_aggr_check, 'skip-vol-aggr-check', [ bool, 'None' ], False ],
        }, {
        } )
    
    def system_cli(self, args, priv=None):
        """
        An interface to the CLI.
        If the request goes to the node LIF, ONTAP 7G CLI will be executed.
        If the request goes to the Admin Vserver LIF, Cluster-Mode CLI will be executed.
        
        :param args: The arguments of the command line.
        
        :param priv: Possible values are: "admin" or "advanced".
        """
        return self.request( "system-cli", {
            'args': [ args, 'args', [ basestring, 'arg' ], True ],
            'priv': [ priv, 'priv', [ basestring, 'None' ], False ],
        }, {
            'cli-result-value': [ int, False ],
            'cli-output': [ basestring, False ],
        } )
    
    def system_image_package_delete(self, node, package):
        """
        Delete a software package
        
        :param node: Node
        
        :param package: Package File Name
        """
        return self.request( "system-image-package-delete", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'package': [ package, 'package', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_available_replication_transfers(self):
        """
        Provide a mechanism to calculate the number of replication
        operations that could be started.
        Returns the number of replication operations that could be
        started for each replication type. Another output is the maximum
        number of transfers for each replication type.
        """
        return self.request( "system-available-replication-transfers", {
        }, {
            'replication-transfer-table': [ ReplicationTransferInfo, True ],
        } )
    
    def system_get_vendor_info(self):
        """
        Obtain the Data ONTAP vendor information.
        """
        return self.request( "system-get-vendor-info", {
        }, {
            'short-name': [ basestring, False ],
            'information-url': [ basestring, False ],
            'ontap-oid-prefix': [ basestring, False ],
            'product-url': [ basestring, False ],
            'customer-support-name': [ basestring, False ],
            'complete-name': [ basestring, False ],
            'autosupport-email': [ basestring, False ],
            'customer-support-contact': [ basestring, False ],
            'autosupport-url': [ basestring, False ],
        } )
    
    def system_user_capability_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns the objects and their operations which are permitted to
        user who called this API.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security login role object.
                All security login role objects matching this query up to
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
        return self.request( "system-user-capability-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CapabilityInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CapabilityInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CapabilityInfo, True ],
        } )
    
    def system_api_list_types(self):
        """
        get list and description of typedefs
        """
        return self.request( "system-api-list-types", {
        }, {
            'type-entries': [ SystemApiTypeEntryInfo, True ],
        } )
    
    def system_image_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display software image information
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                system object.
                All system objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "system-image-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SystemImageAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SystemImageAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ SystemImageAttributes, True ],
        } )
    
    def system_node_shutdown(self, node):
        """
        Shut down a node. Only an admin can initiate a node shutdown.
        If attempted by a user with insufficient privileges EAPIPRIVILEGE
        is returned.
        
        :param node: The textual name of a node.
        """
        return self.request( "system-node-shutdown", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_get_node_info_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Obtain appliance information which includes cpu and backplane
        information. The output contains the head information in a
        sysconfig -a command. I/O information is not included. System
        refers to a node in a cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                system-info object.
                All system-info objects matching this query up to 'max-records'
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
        return self.request( "system-get-node-info-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SystemInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SystemInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SystemInfo, True ],
        } )
    
    def system_image_update_progress_get(self, node):
        """
        Show progress information for current or previous update
        
        :param node: Node
        """
        return self.request( "system-image-update-progress-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
        }, {
            'exit-status': [ basestring, False ],
            'phase': [ basestring, False ],
            'run-status': [ basestring, False ],
            'exit-message': [ basestring, False ],
            'last-message': [ basestring, False ],
        } )
    
    def system_node_reboot(self, node):
        """
        Reboot the specified node. Only an admin can reboot the node.
        If attempted by a user with insufficient privileges EAPIPRIVILEGE
        is returned.
        
        :param node: The textual name of a node.
        """
        return self.request( "system-node-reboot", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def system_get_version(self):
        """
        Obtain the Data ONTAP version.
        """
        return self.request( "system-get-version", {
        }, {
            'node-kernel-info-details': [ SystemNodeKernelInfo, True ],
            'is-clustered': [ bool, False ],
            'version': [ basestring, False ],
            'node-version-details': [ NodeVersionDetailInfo, True ],
            'build-timestamp': [ int, False ],
            'version-tuple': [ SystemVersionTuple, False ],
        } )
    
    def system_get_ontapi_version(self):
        """
        Obtain the current ONTAPI major and minor versions.
        """
        return self.request( "system-get-ontapi-version", {
        }, {
            'major-version': [ int, False ],
            'node-ontapi-details': [ NodeOntapiDetailInfo, True ],
            'minor-version': [ int, False ],
        } )
    
    def system_node_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Obtain the node information when the node is a part of the
        cluster in an iteration.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                system-node object.
                All system-node objects matching this query up to 'max-records'
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
        return self.request( "system-node-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NodeDetailsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NodeDetailsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NodeDetailsInfo, True ],
        } )
    
    def system_set_node_stable_after_startup(self):
        """
        This function is called by the GX management layer once a
        node has booted up to the point where it is operational.
        This "notification" allows the dblade to signal its partner
        that it is ready to receive additional aggregates to complete
        a send-home.
        """
        return self.request( "system-set-node-stable-after-startup", {
        }, {
        } )
    
    def system_node_get(self, node, desired_attributes=None):
        """
        Obtain the node information when the node is part of a cluster.
        Information returned includes details like location,
        serial-number, asset tag, uptime, vendor name etc.
        
        :param node: The textual name of a node.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "system-node-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NodeDetailsInfo, 'None' ], False ],
        }, {
            'attributes': [ NodeDetailsInfo, False ],
        } )
    
    def system_image_package_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display software information for all packages
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                system object.
                All system objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "system-image-package-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SystemImagePackageAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SystemImagePackageAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ SystemImagePackageAttributes, True ],
        } )
    
    def system_image_update(self, node, package, setdefault=None, replace_package=None, replace=None, rename_package=None, ignore_compatibility=None):
        """
        Perform software image upgrade/downgrade.  This API will return
        immediately.  The progress can be monitored using the
        'system-image-update-progress-get' API.
        
        :param node: Node
        
        :param package: Package URL
        
        :param setdefault: Set Newly Updated Image as Default
        
        :param replace_package: Replace the Local File
        
        :param replace: Image to Replace
        
        :param rename_package: Rename the File
        
        :param ignore_compatibility: Ignore Version Compatibility Checking
        """
        return self.request( "system-image-update", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'setdefault': [ setdefault, 'setdefault', [ bool, 'None' ], False ],
            'package': [ package, 'package', [ basestring, 'None' ], False ],
            'replace_package': [ replace_package, 'replace-package', [ bool, 'None' ], False ],
            'replace': [ replace, 'replace', [ basestring, 'None' ], False ],
            'rename_package': [ rename_package, 'rename-package', [ basestring, 'None' ], False ],
            'ignore_compatibility': [ ignore_compatibility, 'ignore-compatibility', [ bool, 'None' ], False ],
        }, {
        } )
    
    def system_get_info(self):
        """
        Obtain appliance information which includes
        cpu and backplane information.  The output
        contains the head information in a sysconfig -a command.
        I/O information is not included.
        """
        return self.request( "system-get-info", {
        }, {
            'system-info': [ SystemInfo, False ],
        } )
    
    def system_api_list(self):
        """
        get list of apis. This returns the names only - to get the
        parameter info, use system-api-get-elements
        """
        return self.request( "system-api-list", {
        }, {
            'apis': [ SystemApiInfo, True ],
        } )
    
    def system_api_get_elements(self, api_list):
        """
        get elements for specified apis
        
        :param api_list: list of apis to retrieve
        """
        return self.request( "system-api-get-elements", {
            'api_list': [ api_list, 'api-list', [ basestring, 'api-list-info' ], True ],
        }, {
            'api-entries': [ SystemApiEntryInfo, True ],
        } )
    
    def system_image_modify(self, node, image, is_default=None):
        """
        Modify software image configuration
        
        :param node: Node
        
        :param image: Image Name
        
        :param is_default: Is Default Image
        """
        return self.request( "system-image-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'image': [ image, 'image', [ basestring, 'None' ], False ],
            'is_default': [ is_default, 'is-default', [ bool, 'None' ], False ],
        }, {
        } )
