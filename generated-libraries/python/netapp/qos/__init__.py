from netapp.connection import NaConnection
from qos_workload_get_iter_key_td import QosWorkloadGetIterKeyTd # 1 properties
from qos_policy_group_get_iter_key_td import QosPolicyGroupGetIterKeyTd # 1 properties
from qos_settings_read_ahead_info import QosSettingsReadAheadInfo # 30 properties
from qos_tput import QosTput # 0 properties
from qos_policy_group_delete_iter_info import QosPolicyGroupDeleteIterInfo # 3 properties
from qos_workload_modify_iter_info import QosWorkloadModifyIterInfo # 3 properties
from qos_workload_delete_iter_key_td import QosWorkloadDeleteIterKeyTd # 1 properties
from qos_workload_modify_iter_key_td import QosWorkloadModifyIterKeyTd # 1 properties
from qos_settings_control_info import QosSettingsControlInfo # 2 properties
from qos_policy_group_delete_iter_key_td import QosPolicyGroupDeleteIterKeyTd # 1 properties
from qos_settings_read_ahead_destroy_iter_info import QosSettingsReadAheadDestroyIterInfo # 3 properties
from qos_settings_read_ahead_get_iter_key_td import QosSettingsReadAheadGetIterKeyTd # 1 properties
from qos_settings_read_ahead_modify_iter_info import QosSettingsReadAheadModifyIterInfo # 3 properties
from qos_workload_delete_iter_info import QosWorkloadDeleteIterInfo # 3 properties
from qos_settings_read_ahead_destroy_iter_key_td import QosSettingsReadAheadDestroyIterKeyTd # 1 properties
from qos_workload_info import QosWorkloadInfo # 12 properties
from qos_settings_read_ahead_modify_iter_key_td import QosSettingsReadAheadModifyIterKeyTd # 1 properties
from qos_settings_archived_workload_info import QosSettingsArchivedWorkloadInfo # 1 properties
from qos_policy_group_info import QosPolicyGroupInfo # 7 properties
from qos_policy_group_modify_iter_info import QosPolicyGroupModifyIterInfo # 3 properties
from qos_class import QosClass # 0 properties
from qos_policy_group_modify_iter_key_td import QosPolicyGroupModifyIterKeyTd # 1 properties

class QosConnection(NaConnection):
    
    def qos_policy_group_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over list of policy groups.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                qos-policy-group object.
                All qos-policy-group objects matching this query up to
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
        return self.request( "qos-policy-group-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QosPolicyGroupInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosPolicyGroupInfo, 'None' ], False ],
        }, {
            'attributes-list': [ QosPolicyGroupInfo, True ],
        } )
    
    def qos_policy_group_delete(self, policy_group):
        """
        Delete single policy group.  The default policy group may not be
        deleted. The policy group may not be attached to any workloads.
        Only user defined policy groups may be deleted.
        
        :param policy_group: Name of the policy group. Policy group names must be unique and
                are restricted to 128 alphanumeric characters, '-', and '_', and
                must start with an alphanumeric character (a-z, A-Z, or 0-9).
        """
        return self.request( "qos-policy-group-delete", {
            'policy_group': [ policy_group, 'policy-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qos_test_smf_zapi_error(self, error_op_code):
        """
        Returns SMF error with ZAPI error codes
        
        :param error_op_code: OP code of code to display
        """
        return self.request( "qos-test-smf-zapi-error", {
            'error_op_code': [ error_op_code, 'error-op-code', [ int, 'None' ], False ],
        }, {
        } )
    
    def qos_workload_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete multiple workloads.  Only user defined workloads may be
        deleted.
        
        :param query: If deleting a specific qos-workload, this input element must
                specify all keys.
                If deleting multiple qos-workload objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                qos-workload even when the deletion of a previous matching
                qos-workload fails, and do so until the total number of objects
                failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of qos-workload objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of qos-workload
                objects (just keys) that were successfully deleted.
                If set to false, the list of qos-workload objects deleted will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple qos-workload objects
                match a given query.
                If set to true, the API will continue deleting the next matching
                qos-workload even when the deletion of a previous qos-workload
                fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of qos-workload
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of qos-workload objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "qos-workload-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosWorkloadInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosWorkloadDeleteIterInfo, True ],
            'failure-list': [ QosWorkloadDeleteIterInfo, True ],
        } )
    
    def qos_workload_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify multiple workloads
        
        :param query: If modifying a specific qos-workload, this input element must
                specify all keys.
                If modifying qos-workload objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                qos-workload even when the modification of a previous matching
                qos-workload fails, and do so until the total number of objects
                failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of qos-workload
                objects (just keys) that were successfully updated.
                If set to false, the list of qos-workload objects modified will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple qos-workload objects
                match a given query.
                If set to true, the API will continue modifying the next matching
                qos-workload even when modification of a previous qos-workload
                fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of qos-workload
                objects (just keys) that were not modified due to some error.
                If set to false, the list of qos-workload objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "qos-workload-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosWorkloadInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ QosWorkloadInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosWorkloadModifyIterInfo, True ],
            'failure-list': [ QosWorkloadModifyIterInfo, True ],
        } )
    
    def qos_policy_group_rename(self, policy_group_name, new_name):
        """
        Rename a QoS Policy Group
        
        :param policy_group_name: Name of the policy group. Policy group names must be unique and
                are restricted to 128 alphanumeric characters, '-', and '_', and
                must start with an alphanumeric character (a-z, A-Z, or 0-9).
        
        :param new_name: New Policy Group Name
        """
        return self.request( "qos-policy-group-rename", {
            'policy_group_name': [ policy_group_name, 'policy-group-name', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qos_settings_archived_workload_get(self, desired_attributes=None):
        """
        Get the cluster-wide QoS workload archival settings.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "qos-settings-archived-workload-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosSettingsArchivedWorkloadInfo, 'None' ], False ],
        }, {
            'attributes': [ QosSettingsArchivedWorkloadInfo, False ],
        } )
    
    def qos_settings_read_ahead_modify(self, read_ahead_setting_name, jitter=None, min_disk_response_time=None, use_feedback=None, overshoot=None, max_range=None, disk_response_weight=None, min_retire_time=None, interarrival_weight=None, use_async=None, smallfile_blocks=None, max_blocks=None, max_retire_time=None, max_disk_response_time=None, force_dump=None, use_timing=None, min_range=None, max_deadline=None, force_none=None, force_full=None, early_count=None, use_histogram=None, min_file_histogram=None, max_gap=None, default=None, align_blocks=None, min_blocks=None, metadata_blocks=None, disk_response_factor=None):
        """
        Modify an existing read-ahead setting.
        
        :param read_ahead_setting_name: Name of QoS Readahead Setting.
        
        :param jitter: Threshold for detecting jitter (%)
        
        :param min_disk_response_time: Minimum disk response time (ms)
        
        :param use_feedback: Provide cache-miss feedback
        
        :param overshoot: Allowable overshoot (%)
        
        :param max_range: Maximum range used when aging streams (Blocks)
        
        :param disk_response_weight: Weight for disk response time aging (%)
        
        :param min_retire_time: Minimum Time Before a Stream is Retired (us)
        
        :param interarrival_weight: Weight for interarrival time aging (%)
        
        :param use_async: Use asynchronous speculation
        
        :param smallfile_blocks: Maximum blocks for small-file handling
        
        :param max_blocks: Maximum blocks to speculate
        
        :param max_retire_time: Maximum Time Before a Stream is Retired (us)
        
        :param max_disk_response_time: Maximum disk response time (ms)
        
        :param force_dump: Force DUMP-style readahead
        
        :param use_timing: Use timing algorithms
        
        :param min_range: Minimum range used when aging streams (Blocks)
        
        :param max_deadline: Maximum deadline Offset (ms)
        
        :param force_none: Disable readahead
        
        :param force_full: Force full-file readahead
        
        :param early_count: Number of IO operations cautiously predicted
        
        :param use_histogram: Use Histogram-based predictions
        
        :param min_file_histogram: Minimum filesize for Histogram-based predictions (blocks)
        
        :param max_gap: Maximum speculative blocks outstanding
        
        :param default: Specifies whether this is the default readahead setting
        
        :param align_blocks: Block alignment
        
        :param min_blocks: Minimum blocks to speculate
        
        :param metadata_blocks: Minimum blocks for which metadata is predicted
        
        :param disk_response_factor: Disk response time factor
        """
        return self.request( "qos-settings-read-ahead-modify", {
            'jitter': [ jitter, 'jitter', [ int, 'None' ], False ],
            'min_disk_response_time': [ min_disk_response_time, 'min-disk-response-time', [ int, 'None' ], False ],
            'use_feedback': [ use_feedback, 'use-feedback', [ bool, 'None' ], False ],
            'overshoot': [ overshoot, 'overshoot', [ int, 'None' ], False ],
            'max_range': [ max_range, 'max-range', [ int, 'None' ], False ],
            'disk_response_weight': [ disk_response_weight, 'disk-response-weight', [ int, 'None' ], False ],
            'min_retire_time': [ min_retire_time, 'min-retire-time', [ int, 'None' ], False ],
            'interarrival_weight': [ interarrival_weight, 'interarrival-weight', [ int, 'None' ], False ],
            'use_async': [ use_async, 'use-async', [ bool, 'None' ], False ],
            'smallfile_blocks': [ smallfile_blocks, 'smallfile-blocks', [ int, 'None' ], False ],
            'max_blocks': [ max_blocks, 'max-blocks', [ int, 'None' ], False ],
            'max_retire_time': [ max_retire_time, 'max-retire-time', [ int, 'None' ], False ],
            'read_ahead_setting_name': [ read_ahead_setting_name, 'read-ahead-setting-name', [ basestring, 'None' ], False ],
            'max_disk_response_time': [ max_disk_response_time, 'max-disk-response-time', [ int, 'None' ], False ],
            'force_dump': [ force_dump, 'force-dump', [ bool, 'None' ], False ],
            'use_timing': [ use_timing, 'use-timing', [ bool, 'None' ], False ],
            'min_range': [ min_range, 'min-range', [ int, 'None' ], False ],
            'max_deadline': [ max_deadline, 'max-deadline', [ int, 'None' ], False ],
            'force_none': [ force_none, 'force-none', [ bool, 'None' ], False ],
            'force_full': [ force_full, 'force-full', [ bool, 'None' ], False ],
            'early_count': [ early_count, 'early-count', [ int, 'None' ], False ],
            'use_histogram': [ use_histogram, 'use-histogram', [ bool, 'None' ], False ],
            'min_file_histogram': [ min_file_histogram, 'min-file-histogram', [ int, 'None' ], False ],
            'max_gap': [ max_gap, 'max-gap', [ int, 'None' ], False ],
            'default': [ default, 'default', [ bool, 'None' ], False ],
            'align_blocks': [ align_blocks, 'align-blocks', [ int, 'None' ], False ],
            'min_blocks': [ min_blocks, 'min-blocks', [ int, 'None' ], False ],
            'metadata_blocks': [ metadata_blocks, 'metadata-blocks', [ int, 'None' ], False ],
            'disk_response_factor': [ disk_response_factor, 'disk-response-factor', [ int, 'None' ], False ],
        }, {
        } )
    
    def qos_workload_modify(self, workload_name, read_ahead=None):
        """
        Modify an existing workload.  This may be used to rename the
        workload, modify the workload's ID, its class, or its category.
        
        :param workload_name: User visible name of QoS workload.
        
        :param read_ahead: Name for a read-ahead tunable policy.
        """
        return self.request( "qos-workload-modify", {
            'workload_name': [ workload_name, 'workload-name', [ basestring, 'None' ], False ],
            'read_ahead': [ read_ahead, 'read-ahead', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qos_workload_delete(self, workload_name):
        """
        Delete a single workload.  Only user defined workloads may be
        deleted.
        
        :param workload_name: User visible name of QoS workload.
        """
        return self.request( "qos-workload-delete", {
            'workload_name': [ workload_name, 'workload-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qos_settings_read_ahead_destroy(self, read_ahead_setting_name):
        """
        Destroy single read-ahead setting.  The default setting may not
        be destroyed. The setting may not be attached to any workloads.
        Only user defined settings may be destroyed.
        
        :param read_ahead_setting_name: Name of QoS Readahead Setting.
        """
        return self.request( "qos-settings-read-ahead-destroy", {
            'read_ahead_setting_name': [ read_ahead_setting_name, 'read-ahead-setting-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def qos_policy_group_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify multiple policy groups
        
        :param query: If modifying a specific qos-policy-group, this input element must
                specify all keys.
                If modifying qos-policy-group objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                qos-policy-group even when the modification of a previous
                matching qos-policy-group fails, and do so until the total number
                of objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of qos-policy-group
                objects (just keys) that were successfully updated.
                If set to false, the list of qos-policy-group objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple qos-policy-group
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                qos-policy-group even when modification of a previous
                qos-policy-group fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of qos-policy-group
                objects (just keys) that were not modified due to some error.
                If set to false, the list of qos-policy-group objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "qos-policy-group-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosPolicyGroupInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ QosPolicyGroupInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosPolicyGroupModifyIterInfo, True ],
            'failure-list': [ QosPolicyGroupModifyIterInfo, True ],
        } )
    
    def qos_settings_read_ahead_create(self, read_ahead_setting_name, jitter=None, min_disk_response_time=None, use_feedback=None, overshoot=None, max_range=None, return_record=None, disk_response_weight=None, min_retire_time=None, read_ahead_class=None, interarrival_weight=None, use_async=None, smallfile_blocks=None, max_blocks=None, max_retire_time=None, max_disk_response_time=None, force_dump=None, use_timing=None, min_range=None, max_deadline=None, force_none=None, force_full=None, early_count=None, use_histogram=None, min_file_histogram=None, max_gap=None, default=None, align_blocks=None, min_blocks=None, metadata_blocks=None, disk_response_factor=None):
        """
        Create a new read-ahead setting.  A unique name must be provided
        for the new read-ahead setting. If the 'default' field is set to
        true, these become the default read-ahead settings for settings
        that don't otherwise name read-ahead settings.  Unless creating a
        new default, creating read-ahead settings should usually be
        assigned to an existing QoS setting.
        
        :param read_ahead_setting_name: Name of QoS Readahead Setting.
        
        :param jitter: Threshold for detecting jitter (%)
        
        :param min_disk_response_time: Minimum disk response time (ms)
        
        :param use_feedback: Provide cache-miss feedback
        
        :param overshoot: Allowable overshoot (%)
        
        :param max_range: Maximum range used when aging streams (Blocks)
        
        :param return_record: If set to true, returns the qos-settings-read-ahead on successful
                creation.
                Default: false
        
        :param disk_response_weight: Weight for disk response time aging (%)
        
        :param min_retire_time: Minimum Time Before a Stream is Retired (us)
        
        :param read_ahead_class: Readahead setting class
                Possible values:
                <ul>
                <li> "preset"         - Preset,
                <li> "user_defined"   - User Defined,
                <li> "system_defined" - System Defined
                </ul>
        
        :param interarrival_weight: Weight for interarrival time aging (%)
        
        :param use_async: Use asynchronous speculation
        
        :param smallfile_blocks: Maximum blocks for small-file handling
        
        :param max_blocks: Maximum blocks to speculate
        
        :param max_retire_time: Maximum Time Before a Stream is Retired (us)
        
        :param max_disk_response_time: Maximum disk response time (ms)
        
        :param force_dump: Force DUMP-style readahead
        
        :param use_timing: Use timing algorithms
        
        :param min_range: Minimum range used when aging streams (Blocks)
        
        :param max_deadline: Maximum deadline Offset (ms)
        
        :param force_none: Disable readahead
        
        :param force_full: Force full-file readahead
        
        :param early_count: Number of IO operations cautiously predicted
        
        :param use_histogram: Use Histogram-based predictions
        
        :param min_file_histogram: Minimum filesize for Histogram-based predictions (blocks)
        
        :param max_gap: Maximum speculative blocks outstanding
        
        :param default: Specifies whether this is the default readahead setting
        
        :param align_blocks: Block alignment
        
        :param min_blocks: Minimum blocks to speculate
        
        :param metadata_blocks: Minimum blocks for which metadata is predicted
        
        :param disk_response_factor: Disk response time factor
        """
        return self.request( "qos-settings-read-ahead-create", {
            'jitter': [ jitter, 'jitter', [ int, 'None' ], False ],
            'min_disk_response_time': [ min_disk_response_time, 'min-disk-response-time', [ int, 'None' ], False ],
            'use_feedback': [ use_feedback, 'use-feedback', [ bool, 'None' ], False ],
            'overshoot': [ overshoot, 'overshoot', [ int, 'None' ], False ],
            'max_range': [ max_range, 'max-range', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'disk_response_weight': [ disk_response_weight, 'disk-response-weight', [ int, 'None' ], False ],
            'min_retire_time': [ min_retire_time, 'min-retire-time', [ int, 'None' ], False ],
            'read_ahead_class': [ read_ahead_class, 'read-ahead-class', [ basestring, 'qos-class' ], False ],
            'interarrival_weight': [ interarrival_weight, 'interarrival-weight', [ int, 'None' ], False ],
            'use_async': [ use_async, 'use-async', [ bool, 'None' ], False ],
            'smallfile_blocks': [ smallfile_blocks, 'smallfile-blocks', [ int, 'None' ], False ],
            'max_blocks': [ max_blocks, 'max-blocks', [ int, 'None' ], False ],
            'max_retire_time': [ max_retire_time, 'max-retire-time', [ int, 'None' ], False ],
            'read_ahead_setting_name': [ read_ahead_setting_name, 'read-ahead-setting-name', [ basestring, 'None' ], False ],
            'max_disk_response_time': [ max_disk_response_time, 'max-disk-response-time', [ int, 'None' ], False ],
            'force_dump': [ force_dump, 'force-dump', [ bool, 'None' ], False ],
            'use_timing': [ use_timing, 'use-timing', [ bool, 'None' ], False ],
            'min_range': [ min_range, 'min-range', [ int, 'None' ], False ],
            'max_deadline': [ max_deadline, 'max-deadline', [ int, 'None' ], False ],
            'force_none': [ force_none, 'force-none', [ bool, 'None' ], False ],
            'force_full': [ force_full, 'force-full', [ bool, 'None' ], False ],
            'early_count': [ early_count, 'early-count', [ int, 'None' ], False ],
            'use_histogram': [ use_histogram, 'use-histogram', [ bool, 'None' ], False ],
            'min_file_histogram': [ min_file_histogram, 'min-file-histogram', [ int, 'None' ], False ],
            'max_gap': [ max_gap, 'max-gap', [ int, 'None' ], False ],
            'default': [ default, 'default', [ bool, 'None' ], False ],
            'align_blocks': [ align_blocks, 'align-blocks', [ int, 'None' ], False ],
            'min_blocks': [ min_blocks, 'min-blocks', [ int, 'None' ], False ],
            'metadata_blocks': [ metadata_blocks, 'metadata-blocks', [ int, 'None' ], False ],
            'disk_response_factor': [ disk_response_factor, 'disk-response-factor', [ int, 'None' ], False ],
        }, {
            'result': [ QosSettingsReadAheadInfo, False ],
        } )
    
    def qos_settings_control_modify(self, enforcement=None, ratebucket_rebalance=None):
        """
        Modify the existing cluster-wide QoS control settings.
        
        :param enforcement: Cluster-wide QoS enforcement
        
        :param ratebucket_rebalance: Manage QoS ratebucket budgets across the cluster
        """
        return self.request( "qos-settings-control-modify", {
            'enforcement': [ enforcement, 'enforcement', [ bool, 'None' ], False ],
            'ratebucket_rebalance': [ ratebucket_rebalance, 'ratebucket-rebalance', [ bool, 'None' ], False ],
        }, {
        } )
    
    def qos_settings_read_ahead_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Destroy multiple read-ahead settings.
        
        :param query: If deleting a specific qos-settings-read-ahead, this input
                element must specify all keys.
                If deleting multiple qos-settings-read-ahead objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                qos-settings-read-ahead even when the deletion of a previous
                matching qos-settings-read-ahead fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of qos-settings-read-ahead objects to delete
                in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                qos-settings-read-ahead objects (just keys) that were
                successfully deleted.
                If set to false, the list of qos-settings-read-ahead objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple
                qos-settings-read-ahead objects match a given query.
                If set to true, the API will continue deleting the next matching
                qos-settings-read-ahead even when the deletion of a previous
                qos-settings-read-ahead fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                qos-settings-read-ahead objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of qos-settings-read-ahead objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "qos-settings-read-ahead-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosSettingsReadAheadInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosSettingsReadAheadDestroyIterInfo, True ],
            'failure-list': [ QosSettingsReadAheadDestroyIterInfo, True ],
        } )
    
    def qos_policy_group_create(self, policy_group, vserver, return_record=None, max_throughput=None):
        """
        Create a policy group.  A unique name must be provided for the
        new policy group. A QoS Policy group defines measurable Service
        Level Objectives (SLOs) that apply to the storage object with
        which the policy group is associated.
        
        :param policy_group: Name of the policy group. Policy group names must be unique and
                are restricted to 128 alphanumeric characters, '-', and '_', and
                must start with an alphanumeric character (a-z, A-Z, or 0-9).
        
        :param vserver: The Data Vserver to which the policy group belongs.
        
        :param return_record: If set to true, returns the qos-policy-group on successful
                creation.
                Default: false
        
        :param max_throughput: Maximum throughput defined by this policy.  It is specified in
                terms of IOPS or MB/s, and the range is zero to infinity. The
                values entered here are case-insensitive, and the units are base
                ten. There should be no space between the number and the units.
                The default value for max-throughput is infinity. The default
                unit is IOPS. Two reserved keywords, 'none' and 'INF', are
                available for the situation that requires removal of a value, and
                the situation that needs to specify the maximum available value.
                Examples of valid specifications are: 100B/s, 10KB/s, 1gb/s,
                500MB/s, 1tb/s, and 100iops.
        """
        return self.request( "qos-policy-group-create", {
            'policy_group': [ policy_group, 'policy-group', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'max_throughput': [ max_throughput, 'max-throughput', [ basestring, 'qos-tput' ], False ],
        }, {
            'result': [ QosPolicyGroupInfo, False ],
        } )
    
    def qos_settings_archived_workload_modify(self, max_workloads=None):
        """
        Modify the cluster-wide QoS workload archival settings.
        
        :param max_workloads: Maximum Number of Workloads to be Archived
        """
        return self.request( "qos-settings-archived-workload-modify", {
            'max_workloads': [ max_workloads, 'max-workloads', [ int, 'None' ], False ],
        }, {
        } )
    
    def qos_policy_group_get(self, policy_group, desired_attributes=None):
        """
        Get the attributes of a policy group.
        
        :param policy_group: Name of the policy group. Policy group names must be unique and
                are restricted to 128 alphanumeric characters, '-', and '_', and
                must start with an alphanumeric character (a-z, A-Z, or 0-9).
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "qos-policy-group-get", {
            'policy_group': [ policy_group, 'policy-group', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosPolicyGroupInfo, 'None' ], False ],
        }, {
            'attributes': [ QosPolicyGroupInfo, False ],
        } )
    
    def qos_settings_control_get(self, desired_attributes=None):
        """
        Get the cluster-wide QoS control settings.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "qos-settings-control-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosSettingsControlInfo, 'None' ], False ],
        }, {
            'attributes': [ QosSettingsControlInfo, False ],
        } )
    
    def qos_policy_group_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete multiple policy groups.
        
        :param query: If deleting a specific qos-policy-group, this input element must
                specify all keys.
                If deleting multiple qos-policy-group objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                qos-policy-group even when the deletion of a previous matching
                qos-policy-group fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of qos-policy-group objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of qos-policy-group
                objects (just keys) that were successfully deleted.
                If set to false, the list of qos-policy-group objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple qos-policy-group
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                qos-policy-group even when the deletion of a previous
                qos-policy-group fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of qos-policy-group
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of qos-policy-group objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "qos-policy-group-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosPolicyGroupInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosPolicyGroupDeleteIterInfo, True ],
            'failure-list': [ QosPolicyGroupDeleteIterInfo, True ],
        } )
    
    def qos_workload_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over list of workloads.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                qos-workload object.
                All qos-workload objects matching this query up to 'max-records'
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
        return self.request( "qos-workload-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QosWorkloadInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosWorkloadInfo, 'None' ], False ],
        }, {
            'attributes-list': [ QosWorkloadInfo, True ],
        } )
    
    def qos_workload_get(self, workload_name, desired_attributes=None):
        """
        Get the attributes of a workload.
        
        :param workload_name: User visible name of QoS workload.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "qos-workload-get", {
            'workload_name': [ workload_name, 'workload-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosWorkloadInfo, 'None' ], False ],
        }, {
            'attributes': [ QosWorkloadInfo, False ],
        } )
    
    def qos_policy_group_modify(self, policy_group, max_throughput=None):
        """
        Modify an existing policy group.
        
        :param policy_group: Name of the policy group. Policy group names must be unique and
                are restricted to 128 alphanumeric characters, '-', and '_', and
                must start with an alphanumeric character (a-z, A-Z, or 0-9).
        
        :param max_throughput: Maximum throughput defined by this policy.  It is specified in
                terms of IOPS or MB/s, and the range is zero to infinity. The
                values entered here are case-insensitive, and the units are base
                ten. There should be no space between the number and the units.
                The default value for max-throughput is infinity. The default
                unit is IOPS. Two reserved keywords, 'none' and 'INF', are
                available for the situation that requires removal of a value, and
                the situation that needs to specify the maximum available value.
                Examples of valid specifications are: 100B/s, 10KB/s, 1gb/s,
                500MB/s, 1tb/s, and 100iops.
        """
        return self.request( "qos-policy-group-modify", {
            'policy_group': [ policy_group, 'policy-group', [ basestring, 'None' ], False ],
            'max_throughput': [ max_throughput, 'max-throughput', [ basestring, 'qos-tput' ], False ],
        }, {
        } )
    
    def qos_settings_read_ahead_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify multiple read-ahead settings
        
        :param query: If modifying a specific qos-settings-read-ahead, this input
                element must specify all keys.
                If modifying qos-settings-read-ahead objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                qos-settings-read-ahead even when the modification of a previous
                matching qos-settings-read-ahead fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                qos-settings-read-ahead objects (just keys) that were
                successfully updated.
                If set to false, the list of qos-settings-read-ahead objects
                modified will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple
                qos-settings-read-ahead objects match a given query.
                If set to true, the API will continue modifying the next matching
                qos-settings-read-ahead even when modification of a previous
                qos-settings-read-ahead fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                qos-settings-read-ahead objects (just keys) that were not
                modified due to some error.
                If set to false, the list of qos-settings-read-ahead objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "qos-settings-read-ahead-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ QosSettingsReadAheadInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ QosSettingsReadAheadInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ QosSettingsReadAheadModifyIterInfo, True ],
            'failure-list': [ QosSettingsReadAheadModifyIterInfo, True ],
        } )
    
    def qos_settings_read_ahead_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over list of read-ahead settings.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                qos-settings-read-ahead object.
                All qos-settings-read-ahead objects matching this query up to
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
        return self.request( "qos-settings-read-ahead-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QosSettingsReadAheadInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosSettingsReadAheadInfo, 'None' ], False ],
        }, {
            'attributes-list': [ QosSettingsReadAheadInfo, True ],
        } )
    
    def qos_settings_read_ahead_get(self, read_ahead_setting_name, desired_attributes=None):
        """
        Get the attributes of a read-ahead setting.
        
        :param read_ahead_setting_name: Name of QoS Readahead Setting.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "qos-settings-read-ahead-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QosSettingsReadAheadInfo, 'None' ], False ],
            'read_ahead_setting_name': [ read_ahead_setting_name, 'read-ahead-setting-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ QosSettingsReadAheadInfo, False ],
        } )
