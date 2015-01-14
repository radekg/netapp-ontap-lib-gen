from netapp.connection import NaConnection
from coredump_delete_core_iter_key_td import CoredumpDeleteCoreIterKeyTd # 4 properties
from coredump_config_modify_iter_info import CoredumpConfigModifyIterInfo # 3 properties
from progress_detail_info import ProgressDetailInfo # 3 properties
from coredump_config_get_iter_key_td import CoredumpConfigGetIterKeyTd # 1 properties
from coredump_save_core_iter_key_td import CoredumpSaveCoreIterKeyTd # 3 properties
from core_detail_info import CoreDetailInfo # 10 properties
from coredump_info import CoredumpInfo # 12 properties
from config_detail_info import ConfigDetailInfo # 12 properties
from coredump_config_info import CoredumpConfigInfo # 7 properties
from coredump_delete_core_iter_info import CoredumpDeleteCoreIterInfo # 3 properties
from coredump_config_modify_iter_key_td import CoredumpConfigModifyIterKeyTd # 1 properties
from coredump_save_core_iter_info import CoredumpSaveCoreIterInfo # 3 properties
from coredump_get_iter_key_td import CoredumpGetIterKeyTd # 4 properties

class CoredumpConnection(NaConnection):
    
    def coredump_config_get_total_records(self):
        """
        Obtain the total number of coredump-config objects.
        This is a point in time estimate and may be different on
        subsequent calls.
        """
        return self.request( "coredump-config-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def coredump_get_total_records(self):
        """
        Return the total number of coredumps.
        """
        return self.request( "coredump-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def coredump_list_cores_iter_next(self, tag, maximum):
        """
        Obtain a list of cores on this system
        
        :param tag: Tag from a previous 'coredump-list-cores-iter-start'
                or 'coredump-list-cores-iter-next'.
        
        :param maximum: Maximum number of directory entries to retrieve.
        """
        return self.request( "coredump-list-cores-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'core-details': [ CoreDetailInfo, True ],
            'records': [ int, False ],
        } )
    
    def coredump_list_info(self):
        """
        Gather info about state of coredump
        """
        return self.request( "coredump-list-info", {
        }, {
            'config-details': [ ConfigDetailInfo, False ],
            'progress-details': [ ProgressDetailInfo, False ],
            'fs-minfree-bytes': [ int, False ],
            'state': [ basestring, False ],
            'fs-bytes-needed': [ int, False ],
            'fs-avail-bytes': [ int, False ],
        } )
    
    def coredump_configure(self, minfree, save_attempts, dump_attempts, sparsecore):
        """
        Setup some coredump options.  If not invoked, the default
        settings are:  sparsecore is true, minfree is zero, and
        dump-attempts is two.
        
        :param minfree: The number of bytes that need to be left in the root
                filesystem after coredump has finished saving a core.
                If this amount of space will not be left, save
                attempts will be aborted.  If a core is already being
                saved, this setting will not take affect until
                savecore starts saving another core.
                Range : [0..2^63-1].
        
        :param save_attempts: The number of times coredump should attempt to save a
                core before requiring the force flag to be set to true
                in the coredump-save interface.	 This is a safeguard
                built into coredump to prevent coredump from causing
                a panic loop.  Range : [0..10].
        
        :param dump_attempts: The number of times coredump should attempt to dump a
                core when faced with disk errors that prevent writes
                from completing.  When set to zero, no cores will be
                dumped.  Range : [0..10].
        
        :param sparsecore: Controls whether or not coredump should dump sparse
                cores.  Sparse cores do not include wafl buffers that
                contain only user data.
        """
        return self.request( "coredump-configure", {
            'minfree': [ minfree, 'minfree', [ int, 'None' ], False ],
            'save_attempts': [ save_attempts, 'save-attempts', [ int, 'None' ], False ],
            'dump_attempts': [ dump_attempts, 'dump-attempts', [ int, 'None' ], False ],
            'sparsecore': [ sparsecore, 'sparsecore', [ bool, 'None' ], False ],
        }, {
        } )
    
    def coredump_delete_core_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete multiple coredumps specified.
        
        :param query: If operating on a specific coredump, this input element must
                specify all keys.
                If operating on coredump objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching coredump
                even when the operation on a previous matching coredump fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of coredump objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of coredump objects
                (just keys) that were successfully operated on.
                If set to false, the list of coredump objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple coredump objects match
                a given query.
                If set to true, the API will continue with the next matching
                coredump even when the operation fails for the coredump.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of coredump objects
                (just keys) that were not operated on due to some error.
                If set to false, the list of coredump objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "coredump-delete-core-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ CoredumpInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ CoredumpDeleteCoreIterInfo, True ],
            'failure-list': [ CoredumpDeleteCoreIterInfo, True ],
        } )
    
    def coredump_remove(self, coreid=None, remove_saved=None):
        """
        Removes saved or unsaved cores from this system.
        
        :param coreid: The id of the core that should be deleted.  If not
                provided, all cores will be deleted.
                Range : [0..2^63-1].
        
        :param remove_saved: Set to true if cores that have already been saved should
                be deleted.  Otherwise, only unsaved cores will be
                deleted.  Default: false
        """
        return self.request( "coredump-remove", {
            'coreid': [ coreid, 'coreid', [ int, 'None' ], False ],
            'remove_saved': [ remove_saved, 'remove-saved', [ bool, 'None' ], False ],
        }, {
        } )
    
    def coredump_save_core_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Save unsaved kernel coredumps
        
        :param query: If operating on a specific coredump, this input element must
                specify all keys.
                If operating on coredump objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching coredump
                even when the operation on a previous matching coredump fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of coredump objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of coredump objects
                (just keys) that were successfully operated on.
                If set to false, the list of coredump objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple coredump objects match
                a given query.
                If set to true, the API will continue with the next matching
                coredump even when the operation fails for the coredump.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of coredump objects
                (just keys) that were not operated on due to some error.
                If set to false, the list of coredump objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "coredump-save-core-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ CoredumpInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ CoredumpSaveCoreIterInfo, True ],
            'failure-list': [ CoredumpSaveCoreIterInfo, True ],
        } )
    
    def coredump_delete_all(self, node_name, core_type=None):
        """
        Delete all coredumps owned by a node
        
        :param node_name: The node that owns the core dumps.
        
        :param core_type: Type of core (unsaved-kernel, saved-kernel, kernel, application,
                all) to delete.  Default: unsaved-kernel.
                Possible values:
                <ul>
                <li> "unsaved_kernel" - Unsaved Coredumps,
                <li> "saved_kernel"   - Saved Coredumps,
                <li> "kernel"         - All Kernel Coredumps,
                <li> "application"    - Application Coredumps,
                <li> "all"            - All Coredumps
                </ul>
        """
        return self.request( "coredump-delete-all", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'core_type': [ core_type, 'core-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def coredump_save_all(self, node_name):
        """
        Save all unsaved kernel coredumps owned by a node to the
        filesystem.
        
        :param node_name: The node that owns the unsaved kernel coredumps.
        """
        return self.request( "coredump-save-all", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def coredump_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of coredump-config objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                coredump-config object.
                All coredump-config objects matching this query up to
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
        return self.request( "coredump-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CoredumpConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoredumpConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CoredumpConfigInfo, True ],
        } )
    
    def coredump_config_get(self, node_name, desired_attributes=None):
        """
        Get the attributes of the coredump-config.
        
        :param node_name: The node to which this coredump configuration belongs.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "coredump-config-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoredumpConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ CoredumpConfigInfo, False ],
        } )
    
    def coredump_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return a list of coredumps available on the node.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                coredump object.
                All coredump objects matching this query up to 'max-records' will
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
        return self.request( "coredump-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CoredumpInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoredumpInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CoredumpInfo, True ],
        } )
    
    def coredump_config_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of coredump-config or a group of
        coredump-config objects.
        
        :param query: If modifying a specific coredump-config, this input element must
                specify all keys.
                If modifying coredump-config objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                coredump-config even when the modification of a previous matching
                coredump-config fails, and do so until the total number of
                objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of coredump-config
                objects (just keys) that were successfully updated.
                If set to false, the list of coredump-config objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple coredump-config
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                coredump-config even when modification of a previous
                coredump-config fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of coredump-config
                objects (just keys) that were not modified due to some error.
                If set to false, the list of coredump-config objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "coredump-config-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ CoredumpConfigInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ CoredumpConfigInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ CoredumpConfigModifyIterInfo, True ],
            'failure-list': [ CoredumpConfigModifyIterInfo, True ],
        } )
    
    def coredump_get(self, node_name, core_name, desired_attributes=None, core_id=None):
        """
        Return information about a specified coredump.
        
        :param node_name: The node that owns the coredump.
        
        :param core_name: The name of the coredump file. The corename has the following
                formats: Kernel: <app name>.<pid>.<sysid>.<date>.<time>.nz,
                Application: <app name>.<pid>.<sysid>.<date>.<time>.ucore.bz2.
                Application cores that are not compressed won't have the .bz2
                extension.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param core_id: A unique Id of the core used for operations like show, delete,
                upload and save.
        """
        return self.request( "coredump-get", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoredumpInfo, 'None' ], False ],
            'core_name': [ core_name, 'core-name', [ basestring, 'None' ], False ],
            'core_id': [ core_id, 'core-id', [ int, 'None' ], False ],
        }, {
            'attributes': [ CoredumpInfo, False ],
        } )
    
    def coredump_upload_core(self, node_name, core_name, upload_location=None, core_id=None, case_number=None):
        """
        Uploads a specified coredump.
        
        :param node_name: The node that owns the coredump.
        
        :param core_name: The name of the coredump file. The corename has the following
                formats: Kernel: <app name>.<pid>.<sysid>.<date>.<time>.nz,
                Application: <app name>.<pid>.<sysid>.<date>.<time>.ucore.bz2.
                Application cores that are not compressed won't have the .bz2
                extension.
        
        :param upload_location: URL for Coredump Upload Directory
        
        :param core_id: A unique Id of the core used for operations like show, delete,
                upload and save.
        
        :param case_number: Case Number
        """
        return self.request( "coredump-upload-core", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'upload_location': [ upload_location, 'upload-location', [ basestring, 'None' ], False ],
            'core_name': [ core_name, 'core-name', [ basestring, 'None' ], False ],
            'core_id': [ core_id, 'core-id', [ int, 'None' ], False ],
            'case_number': [ case_number, 'case-number', [ int, 'None' ], False ],
        }, {
        } )
    
    def coredump_delete_core(self, node_name, core_name, core_id=None):
        """
        Deletes a specified coredump.
        
        :param node_name: The node that owns the coredump.
        
        :param core_name: The name of the coredump file. The corename has the following
                formats: Kernel: <app name>.<pid>.<sysid>.<date>.<time>.nz,
                Application: <app name>.<pid>.<sysid>.<date>.<time>.ucore.bz2.
                Application cores that are not compressed won't have the .bz2
                extension.
        
        :param core_id: A unique Id of the core used for operations like show, delete,
                upload and save.
        """
        return self.request( "coredump-delete-core", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'core_name': [ core_name, 'core-name', [ basestring, 'None' ], False ],
            'core_id': [ core_id, 'core-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def coredump_save(self, coreid=None, force=None):
        """
        Start saving any unsaved cores
        
        :param coreid: The id of the core that should be saved.  If not provided,
                all cores will be saved.  Range : [0..2^63-1].
        
        :param force: Set to true to allow savecore to save cores that have
                had too many failed save attempts in the past.
                Default: false
        """
        return self.request( "coredump-save", {
            'coreid': [ coreid, 'coreid', [ int, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def coredump_save_core(self, node_name, core_name, core_id=None):
        """
        Saves an unsaved kernel coredump on a node.
        
        :param node_name: The node on which the coredump is to be saved.
        
        :param core_name: The name of the coredump file. The corename has the following
                format: <app name>.<pid>.<sysid>.<date>.<time>.nz
        
        :param core_id: A unique Id of the core used for operations like show, delete,
                upload and save.
        """
        return self.request( "coredump-save-core", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'core_name': [ core_name, 'core-name', [ basestring, 'None' ], False ],
            'core_id': [ core_id, 'core-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def coredump_config_modify(self, node_name, save_onstartup=None, save_attempts=None, is_sparsecore_enabled=None, upload_location=None, coredump_attempts=None, min_free=None):
        """
        Modify the attributes of coredump-config object.
        
        :param node_name: The node to which this coredump configuration belongs.
        
        :param save_onstartup: Enable auto-save of coredumps on startup.
        
        :param save_attempts: Maximum number of attempts to save core.
        
        :param is_sparsecore_enabled: Enable sparse cores.
        
        :param upload_location: URL for the coredump upload directory
        
        :param coredump_attempts: Maximum number of attempts to dump core.
        
        :param min_free: Minimum free bytes on root filesystem needed for a core dump.
        """
        return self.request( "coredump-config-modify", {
            'save_onstartup': [ save_onstartup, 'save-onstartup', [ bool, 'None' ], False ],
            'save_attempts': [ save_attempts, 'save-attempts', [ int, 'None' ], False ],
            'is_sparsecore_enabled': [ is_sparsecore_enabled, 'is-sparsecore-enabled', [ bool, 'None' ], False ],
            'upload_location': [ upload_location, 'upload-location', [ basestring, 'None' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'coredump_attempts': [ coredump_attempts, 'coredump-attempts', [ int, 'None' ], False ],
            'min_free': [ min_free, 'min-free', [ int, 'None' ], False ],
        }, {
        } )
    
    def coredump_list_cores_iter_start(self):
        """
        Start an iteration through the core files on this system.
        This interface will return an error unless the state
        returned by coredump-list-info is idle, nocore, or
        waitdump.
        """
        return self.request( "coredump-list-cores-iter-start", {
        }, {
        } )
