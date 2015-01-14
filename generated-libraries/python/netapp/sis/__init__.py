from netapp.connection import NaConnection
from dense_status import DenseStatus # 32 properties
from sis_checkpoint_op_type import SisCheckpointOpType # 0 properties
from sis_chkpoint_stage import SisChkpointStage # 0 properties
from sis_policy_get_iter_key import SisPolicyGetIterKey # 2 properties
from sis_policy_info import SisPolicyInfo # 8 properties
from sis_checkpoint_stage import SisCheckpointStage # 0 properties
from sis_policy_get_iter_key_td import SisPolicyGetIterKeyTd # 2 properties
from sis_type import SisType # 0 properties
from sis_op_status import SisOpStatus # 0 properties
from volume_path import VolumePath # 0 properties
from sis_checkpoint_substage import SisCheckpointSubstage # 0 properties
from sis_chkpoint_substage import SisChkpointSubstage # 0 properties
from sis_status_info import SisStatusInfo # 36 properties
from sis_chkpoint_op_type import SisChkpointOpType # 0 properties
from sis_get_iter_key_td import SisGetIterKeyTd # 1 properties
from revert_version import RevertVersion # 0 properties
from sis_qos_policy import SisQosPolicy # 0 properties
from undo_selective_enum import UndoSelectiveEnum # 0 properties
from sis_logical_data import SisLogicalData # 2 properties
from sis_state import SisState # 0 properties

class SisConnection(NaConnection):
    
    def sis_enable(self, path):
        """
        Enable sis on a volume.
        <p>
        On a non-SnapVault secondary volume, the sis operation will
        be started periodically according to a per-volume schedule.
        By default, this schedule is sun-sat&#064;0. (Everyday at 0:00 hours)
        On a SnapVault secondary volume, the sis operation will
        be kicked off at the end of the SnapVault transfer.
        This API does not enable compression on the volume. See the
        "sis-set-config" API for options to enable compression and for
        modifying the default schedule set on the volume.
        A sis operation can also be manually started using the sis-start
        API.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
                Only one path can be specified at a time.
                The volume must be online to enable sis on the volume.
        """
        return self.request( "sis-enable", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def sis_set_config(self, path, enable_compression=None, enable_inline_compression=None, schedule=None, policy_name=None, enable_idd=None, quick_check_fsize=None):
        """
        Setup or modify sis policy, schedule or
        options for a volume.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
        
        :param enable_compression: Enable compression on the sis volume.
                If true, compression will be enabled on the
                sis volume. If false, compression
                will be disabled on the volume. If the value is not specified
                compression state will be unchanged.
                <p>
                Enabling compression on a secondary volume is strongly discouraged.
                If compression is enabled on a secondary volume, storage efficiency
                present on the source will not be preserved during replication.
                The destination system needs to run offline storage efficiency
                scanner (compression and dedupe) to achieve storage savings.
                Additional compression savings on the destination comes at a
                cost of extra computation resources. In environments where there
                is a lot of shared data present on the source, (e.g., virtualized
                environments employing file clones), data inflation during transfer
                may lead to failed backups due to lack of space on the secondary
                volume.
        
        :param enable_inline_compression: Enable inline compression on the sis volume. To enable inline
                compression, compression must be enabled either in this API
                call or by a previous call to sis-set-config.
                If true, inline-compression will be enabled on the
                sis volume. If false, inline-compression
                will be disabled on the volume. If the value is not specified,
                inline-compression state will be unchanged.
        
        :param schedule: The schedule string for the sis operation.
                <p>
                The format of the schedule:
                <p>
                day_list[&#064;hour_list]
                or hour_list[&#064;day_list]
                or -
                or auto
                or manual
                <p>
                The day_list specifies which days of the week the
                sis operation should run. It is a comma-separated list
                of the first three letters of the day: sun, mon, tue,
                wed, thu, fri, sat. The names are not case sensitive.
                Day ranges such as mon-fri can also be given.
                The default day_list is sun-sat.
                <p>
                The hour_list specifies which hours of the day the
                sis operation should run on each scheduled day.
                The hour_list is a comma-separated list of the integers from
                0 to 23. Hour ranges such as 8-17 are allowed. Step values
                can be used in conjunction with ranges. For example, 0-23/2
                means "every two hours". The default hour_list is 0, i.e.
                midnight on the morning of each scheduled day.
                <p>
                If "-" is specified, no schedule is set. In Data ONTAP
                Cluster-Mode, policy-name and schedule must not be specified
                together in the same API call. If schedule is passed, any previous
                policy-name set on the volume is automatically reset.
                <p>
                The "auto" schedule string means the sis operation will be
                triggered by the amount of new data written to the volume.
                The criterion is subject to being changed later.
                <p>
                The "manual" schedule string prevents SIS from automatically
                triggering any operations and disables change-logging. This
                schedule string can only be used on SnapVault destination volumes.
                The use of this schedule is mainly desirable when inline
                compression is enabled on a SnapVault destination volume and
                background processing is not necessary.
        
        :param policy_name: The sis policy name to be attached to the volume.
                The policy name will determine which M-Host sis policy
                will trigger the scheduled sis operations. In Data ONTAP
                Cluster-Mode, policy-name and schedule must not be specified
                together in the same API call. If policy-name is passed,
                any previous schedule set on the volume is automatically reset.
        
        :param enable_idd: This enables file level incompressible data detection and
                quick check incompressible data detection for large files.
                This is per volume option. Once this set to true, inline
                compression will do a 4k compression quick check
                for large files before proceeding with full CG compression.
                If quick check finds a 4k within a CG as incompressible,
                inline compression won't attempt to compress the CG. And the
                blocks are written in uncompressed form to disk. Also once
                this is enabled, if inline compression encounters a
                incompressible CG within small files, it will mark the file
                with do not compress flag.
                As long as this flag is set on a small file, inline compression
                won't attempt further compression on the file.
                Default value is 'false'.
        
        :param quick_check_fsize: Quick check file size for Incompressible Data Detection.
                If Incompressible data detection is enabled and if the
                file size is >= quick-check-fsize, inline compression will
                do a 4k quick check before doing full CG compression.
        """
        return self.request( "sis-set-config", {
            'enable_compression': [ enable_compression, 'enable-compression', [ bool, 'None' ], False ],
            'enable_inline_compression': [ enable_inline_compression, 'enable-inline-compression', [ bool, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'enable_idd': [ enable_idd, 'enable-idd', [ bool, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'quick_check_fsize': [ quick_check_fsize, 'quick-check-fsize', [ int, 'None' ], False ],
        }, {
        } )
    
    def sis_stop_async(self, volume_name, all_operations=None):
        """
        Abort currently active sis operation on the Infinite Volume.
        The sis operation will remain paused and the operation
        can be resumed by "sis-start-async" or the
        scheduler.
        <p>
        This API is not supported for Flexible Volumes. This API is not supported
        on Infinite Volume constituents or Infinite Volumes that are
        managed by storage services.
        
        :param volume_name: The name of the Infinite Volume.
        
        :param all_operations: If this is "true", both active and queued sis operation will
                be stopped.
                Default value: "false"
        """
        return self.request( "sis-stop-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'all_operations': [ all_operations, 'all-operations', [ bool, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def sis_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of sis policy objects.
        
        :param max_records: The maximum number of records to return in this call.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in
                the sis policy.
                All sis policy objects matching this query up to 'max-records'
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
        return self.request( "sis-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SisPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SisPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SisPolicyInfo, True ],
        } )
    
    def sis_undo(self, compression=None, volume=None, undo_type=None, path=None, dedupe=None, inode=None, log=None):
        """
        auto generated : Undo efficiency on a volume
        
        :param compression: Decompress The Data In The Volume
        
        :param volume: Volume Name
        
        :param undo_type: Selective Undo
                Possible values:
                <ul>
                <li> "all"       - Undo all shared data,
                <li> "wrong"     - Only undo the incorrectly shared data
                </ul>
        
        :param path: Volume Path
        
        :param dedupe: Undo Block Sharing In The Volume
        
        :param inode: Inode Number To Undo Sharing
        
        :param log: Only Log Incorrect Savings
        """
        return self.request( "sis-undo", {
            'compression': [ compression, 'compression', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'undo_type': [ undo_type, 'undo-type', [ basestring, 'undo-selective-enum' ], False ],
            'path': [ path, 'path', [ basestring, 'volume-path' ], False ],
            'dedupe': [ dedupe, 'dedupe', [ bool, 'None' ], False ],
            'inode': [ inode, 'inode', [ int, 'None' ], False ],
            'log': [ log, 'log', [ bool, 'None' ], False ],
        }, {
        } )
    
    def sis_set_config_async(self, volume_name, enable_compression=None, enable_inline_compression=None, schedule=None, policy_name=None, enable_idd=None, quick_check_fsize=None):
        """
        Setup or modify sis policy, schedule or
        options for an Infinite Volume.
        <p>
        This API is not supported for Flexible Volumes. This API is not supported
        on Infinite Volume constituents or Infinite Volumes that are
        managed by storage services.
        
        :param volume_name: Name of the Infinite Volume.
        
        :param enable_compression: Enable compression on the sis Infinite Volume.
                If true, compression will be enabled on the
                sis Infinite Volume. If false, compression
                will be disabled on the Infinite Volume. If the value is not
                specified
                compression state will be unchanged.
        
        :param enable_inline_compression: Enable inline compression on the sis Infinite Volume. To enable
                inline  compression, compression must be enabled either in
                this API call or by a previous call to sis-set-config.
                If true, inline-compression will be enabled on the
                sis Infinite Volume. If false, inline-compression
                will be disabled on the Infinite Volume. If the value is not
                specified, inline-compression state will be unchanged.
        
        :param schedule: The schedule string for the sis operation.
                <p>
                The format of the schedule:
                <p>
                day_list[&#064;hour_list]
                or hour_list[&#064;day_list]
                or -
                or auto
                or manual
                <p>
                The day_list specifies which days of the week the
                sis operation should run. It is a comma-separated list
                of the first three letters of the day: sun, mon, tue,
                wed, thu, fri, sat. The names are not case sensitive.
                Day ranges such as mon-fri can also be given.
                The default day_list is sun-sat.
                <p>
                The hour_list specifies which hours of the day the
                sis operation should run on each scheduled day.
                The hour_list is a comma-separated list of the integers from
                0 to 23. Hour ranges such as 8-17 are allowed. Step values
                can be used in conjunction with ranges. For example, 0-23/2
                means "every two hours". The default hour_list is 0, i.e.
                midnight on the morning of each scheduled day.
                <p>
                If "-" is specified, no schedule is set. In Data ONTAP
                Cluster-Mode, policy-name and schedule must not be specified
                together in the same API call. If schedule is passed, any
                previous
                policy-name set on the Infinite Volume is automatically reset.
                <p>
                The "auto" schedule string means the sis operation will be
                triggered by the amount of new data written to the Infinite Volume.
                The criterion is subject to being changed later.
                <p>
                If "manual" is specified, sis operation will never be triggered
                automatically. Only the user can manually execute the sis
                operation.
        
        :param policy_name: The sis policy name to be attached to the Infinite Volume.
                The policy name will determine which M-Host sis policy
                will trigger the scheduled sis operations. The policy-name and
                schedule must not be specified
                together in the same API call. If policy-name is passed,
                any previous schedule set on the Infinite Volume is automatically
                reset.
        
        :param enable_idd: This enables file level incompressible data detection and
                quick check incompressible data detection for large files.
                This is per volume option. Once this set to true, inline
                compression will do a 4k compression quick check
                for large files before proceeding with full CG compression.
                If quick check finds a 4k within a CG as incompressible,
                inline compression won't attempt to compress the CG. And the
                blocks are written in uncompressed form to disk. Also once
                this is enabled, if inline compression encounters a
                incompressible CG within small files, it will mark the file
                with do not compress flag.
                As long as this flag is set on a small file, inline compression
                won't attempt further compression on the file.
                Default value is 'false'.
        
        :param quick_check_fsize: Quick check file size for Incompressible Data Detection.
                If Incompressible data detection is enabled and if the
                file size is >= quick-check-fsize, inline compression will
                do a 4k quick check before doing full CG compression.
        """
        return self.request( "sis-set-config-async", {
            'enable_compression': [ enable_compression, 'enable-compression', [ bool, 'None' ], False ],
            'enable_inline_compression': [ enable_inline_compression, 'enable-inline-compression', [ bool, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'enable_idd': [ enable_idd, 'enable-idd', [ bool, 'None' ], False ],
            'quick_check_fsize': [ quick_check_fsize, 'quick-check-fsize', [ int, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def sis_check(self, volume=None, path=None, delete_checkpoint=None):
        """
        auto generated : Scrub efficiency metadata of a volume
        
        :param volume: Volume Name
        
        :param path: Volume Path
        
        :param delete_checkpoint: Delete Checkpoint
        """
        return self.request( "sis-check", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'path': [ path, 'path', [ basestring, 'volume-path' ], False ],
            'delete_checkpoint': [ delete_checkpoint, 'delete-checkpoint', [ bool, 'None' ], False ],
        }, {
        } )
    
    def sis_policy_create(self, policy_name, comment=None, schedule=None, enabled=None, duration=None, qos_policy=None):
        """
        Create a new sis policy.
        
        :param policy_name: sis policy name.
        
        :param comment: A brief description of the policy.
        
        :param schedule: Cron type job schedule name. When the associated policy is set on
                a volume, the sis operation will be triggered for the volume on
                this schedule.
                These schedules can be created using the job-schedule-cron-create
                API.
                Existing schedules can be queried using the job-schedule-cron-get-iter
                API.
        
        :param enabled: If the value is true, the sis policy is active in
                this cluster. If the value is false this policy will not be
                activated by the schedulers and hence will be inactive. A policy
                can be assigned to managed objects although it is disabled.
                Default value: "true"
        
        :param duration: The duration in hours for which the scheduled sis operation
                should run. After this time expires, the sis operation
                will be stopped even if the operation is incomplete. If '-' is
                specified as the duration, the sis operation will
                run till it completes. Otherwise, the duration has to be an
                integer greater than 0.
                By default, the operation runs till it completes.
        
        :param qos_policy: QoS policy for the sis operation. Possible values:
                <ul>
                <li> "background" - sis operation will run in background with
                minimal or no impact on data serving
                client operations,
                <li> "best-effort" - sis operations may have some impact on
                data serving client operations.
                </ul>
                Default value: "best-effort"
        """
        return self.request( "sis-policy-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ bool, 'None' ], False ],
            'duration': [ duration, 'duration', [ basestring, 'None' ], False ],
            'qos_policy': [ qos_policy, 'qos-policy', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def sis_get(self, path, desired_attributes=None):
        """
        Get status of a sis volume.
        <p>
        This API is not supported on Infinite Volumes that are
        managed by storage services.
        
        :param path: Volume for which sis information is returned. Path
                is of the format /vol/&lt;vol_name&gt;.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "sis-get", {
            'path': [ path, 'path', [ basestring, 'volume-path' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SisStatusInfo, 'None' ], False ],
        }, {
            'attributes': [ SisStatusInfo, False ],
        } )
    
    def sis_start_async(self, volume_name, build_metadata=None, scan_all=None, queue_operation=None, scan=None, qos_policy=None, delete_checkpoint=None, restart_checkpoint=None):
        """
        Start a sis operation on an Infinite Volume. The Infinite Volume must have
        sis enabled, before starting a sis operation. If the sis operation
        is already active on the Infinite Volume, this API will fail.
        <p>
        This API is not supported for Flexible Volumes. This API is not supported
        on Infinite Volume constituents or Infinite Volumes that are
        managed by storage services.
        
        :param volume_name: The name of the Infinite Volume.
                The Infinite Volume must be online in order to start the sis
                operation.
        
        :param build_metadata: If this argument is "true", scanner will scan the entire volume
                and generate fingerprint database without attempting the sharing.
                This argument is valid only if scan argument is set to "true".
                Look at the documentation for scan parameter for more details.
                Default Value: "false"
        
        :param scan_all: If this argument is "true", scanner will scan entire volume
                without applying shared block optimization. This argument is
                valid only if scan argument is set to "true". Look at the
                documentation for scan parameter for more details.
                Default Value: "false"
        
        :param queue_operation: If this is "true", the requested sis operation will be queued if
                a sis operation is already running on the Infinite Volume, and the
                running operation is in the fingerprint verification phase.
                Default value: "false"
        
        :param scan: If this is "true", the sis operation will scan the file
                system to process all the existing data.
                <p>
                The scan will include whatever is enabled on the
                Infinite Volume.
                For example: If compression is not enabled on the Infinite Volume,
                the scan will not include compression. This default behavior can
                be
                changed by using the run-dedupe-scan and run-compression-scan
                parameters.
                <p>
                If scan is false only data added since the last sis
                operation will be processed.
                Default value: "false"
        
        :param qos_policy: QoS policy for the sis operation. Possible values:
                <ul>
                <li> "background" - sis operation will run in background with
                minimal or no impact on data serving
                client operations,
                <li> "best-effort" - sis operations may have some impact on
                data serving client operations.
                </ul>
                Default value: "best-effort"
        
        :param delete_checkpoint: If this is "true", the sis operation will delete existing
                checkpoint and start the sis operation from the beginning.
                Default value: "false"
        
        :param restart_checkpoint: If this is "true", the sis operation will restart from
                previous checkpoint without checking for validity. This
                option should be used along with "scan" option.
                Default value: "false"
        """
        return self.request( "sis-start-async", {
            'build_metadata': [ build_metadata, 'build-metadata', [ bool, 'None' ], False ],
            'scan_all': [ scan_all, 'scan-all', [ bool, 'None' ], False ],
            'queue_operation': [ queue_operation, 'queue-operation', [ bool, 'None' ], False ],
            'scan': [ scan, 'scan', [ bool, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'qos_policy': [ qos_policy, 'qos-policy', [ basestring, 'None' ], False ],
            'delete_checkpoint': [ delete_checkpoint, 'delete-checkpoint', [ bool, 'None' ], False ],
            'restart_checkpoint': [ restart_checkpoint, 'restart-checkpoint', [ bool, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def sis_stop(self, path, all_operations=None):
        """
        Abort currently active sis operation on the volume.
        The sis operation will remain paused and the operation
        can be resumed by "sis-start", SnapVault transfer,
        or the scheduler.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
        
        :param all_operations: If this is "true", both active and queued sis operation will
                be stopped.
                Default value: "false"
        """
        return self.request( "sis-stop", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'all_operations': [ all_operations, 'all-operations', [ bool, 'None' ], False ],
        }, {
        } )
    
    def sis_policy_delete(self, policy_name):
        """
        Delete a sis policy.
        
        :param policy_name: sis policy name.
        """
        return self.request( "sis-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def sis_disable_async(self, volume_name):
        """
        Disable sis on an Infinite Volume. If the sis operation is
        active on the Infinite Volume, it needs to be stopped by
        "sis-stop-async" API before disabling.
        <p>
        This API is not supported for Flexible Volumes. This API is not supported
        on Infinite Volume constituents or Infinite Volumes that are
        managed by storage services.
        
        :param volume_name: Name of the Infinite Volume.
        """
        return self.request( "sis-disable-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def sis_status(self, path=None, verbose=None):
        """
        Get Status of a sis volume
        This API is not optimal for use in Data ONTAP Cluster-Mode
        systems, and is deprecated. Use sis-get and sis-get-iter APIs
        for Data ONTAP Cluster Mode systems.
        This API is still supported for Data ONTAP 7-Mode systems.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
                Only one path can be specified at a time.
                The volume must be online if not then an error will be
                returned. If path variable is not used then the status
                for all online sis volumes in the filer
                will be returned.
        
        :param verbose: If set to true the output is detailed.
                Default value: "false"
        """
        return self.request( "sis-status", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'sis-object': [ DenseStatus, True ],
        } )
    
    def sis_revert_to(self, volume=None, path=None, version=None, clean_up=None, delete=None):
        """
        auto generated : Reverts volume efficiency metadata
        
        :param volume: Volume Name
        
        :param path: Volume Path
        
        :param version: Revert to Version
                Possible values:
                <ul>
                <li> "8_1"  - Data ONTAP 8.1
                </ul>
        
        :param clean_up: Delete Previously Downgraded Metafiles
        
        :param delete: Delete Existing Metafile on Revert
        """
        return self.request( "sis-revert-to", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'path': [ path, 'path', [ basestring, 'volume-path' ], False ],
            'version': [ version, 'version', [ basestring, 'revert-version' ], False ],
            'clean_up': [ clean_up, 'clean-up', [ bool, 'None' ], False ],
            'delete': [ delete, 'delete', [ bool, 'None' ], False ],
        }, {
        } )
    
    def sis_disable(self, path):
        """
        Disable sis on a volume. If the sis operation is
        active on the volume, it needs to be stopped by "sis-stop"
        API before disabling.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
                Only one path can be specified at a time.
        """
        return self.request( "sis-disable", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def sis_enable_async(self, volume_name):
        """
        Enable sis on an Infinite Volume.
        <p>
        This is similar to 'sis-enable' API except
        that it operates on an Infinite Volume. Read about
        'sis-enable' API for specific details.
        <p>
        This API is not supported for Flexible Volumes. This API is not supported
        on Infinite Volume constituents or Infinite Volumes that are
        managed by storage services.
        
        :param volume_name: Name of the Infinite Volume.
                The Infinite Volume must be online to enable sis.
        """
        return self.request( "sis-enable-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def sis_policy_modify(self, policy_name, comment=None, schedule=None, enabled=None, duration=None, qos_policy=None):
        """
        Modify the attributes of a sis policy.
        
        :param policy_name: sis policy name.
                Attributes: key, non-modifiable
        
        :param comment: A brief description of the policy. If a value is not provided the
                current settings are retained. An empty string can be used to
                clear the current settings.
        
        :param schedule: Cron type job schedule name. When the associated policy is set on
                a volume, the sis operation will be triggered for the
                volume on this schedule. If this field is not set, the existing
                value is not modified.
        
        :param enabled: If the value is true, the sis policy is active in
                this cluster. If the value is false this policy will not be
                activated by the schedulers and hence will be inactive. A policy
                can be assigned to managed objects although it is disabled. If
                the value is not specified, the current settings are retained.
        
        :param duration: The duration in hours for which the scheduled sis operation
                should run. After this time expires, the sis operation
                will be stopped even if the operation is incomplete. If '-' is
                specified as the duration, the sis operation will
                run till it completes. If duration is not provided the current
                setting is not modified.
        
        :param qos_policy: QoS policy for the sis operation. Possible values:
                <ul>
                <li> "background" - sis operation will run in background with
                minimal or no impact on data serving
                client operations,
                <li> "best-effort" - sis operations may have some impact on
                data serving client operations.
                </ul>
                Default value: "best-effort"
        """
        return self.request( "sis-policy-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ bool, 'None' ], False ],
            'duration': [ duration, 'duration', [ basestring, 'None' ], False ],
            'qos_policy': [ qos_policy, 'qos-policy', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def sis_policy_get(self, policy_name, desired_attributes=None):
        """
        Get attributes of a sis policy.
        
        :param policy_name: sis policy name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "sis-policy-get", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SisPolicyInfo, 'None' ], False ],
        }, {
            'attributes': [ SisPolicyInfo, False ],
        } )
    
    def sis_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of sis volumes.
        <p>
        This API is not supported on Infinite Volumes that are
        managed by storage services.
        
        :param max_records: The maximum number of records to return in this call.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes.
                All sis objects matching this query up to 'max-records' will be
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
        return self.request( "sis-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SisStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SisStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SisStatusInfo, True ],
        } )
    
    def sis_start(self, path, build_metadata=None, scan_all=None, queue_operation=None, scan=None, qos_policy=None, delete_checkpoint=None, restart_checkpoint=None):
        """
        Start a sis operation on a volume. The volume must have sis
        enabled, before starting a sis operation. If the sis operation
        is already active on the volume, this API will fail.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param path: The full path of the sis volume, /vol/&lt;vol_name&gt;.
                The volume must be online in order to start the sis operation.
        
        :param build_metadata: If this argument is "true", scanner will scan the entire volume
                and generate fingerprint database without attempting the sharing.
                This argument is valid only if scan argument is set to "true".
                Look at the documentation for scan parameter for more details.
                Default value: "false"
        
        :param scan_all: If this argument is "true", scanner will scan entire volume
                without applying shared block optimization. This argument is
                valid only if scan argument is set to "true". Look at the
                documentation for scan parameter for more details.
                Default value: "false"
        
        :param queue_operation: If this is "true", the requested sis operation will be queued if
                a sis operation is already running on the volume, and the
                running operation is in the fingerprint verification phase.
                Default value: "false"
        
        :param scan: If this is "true", the sis operation will scan the file
                system to process all the existing data.
                <p>
                The scan will include whatever is enabled on the
                volume.
                For example: If compression is not enabled on the volume,
                the scan will not include compression. This default behavior can be
                changed by using the run-dedupe-scan and run-compression-scan
                parameters.
                <p>
                If scan is false only data added since the last sis
                operation will be processed.
                Default value: "false"
        
        :param qos_policy: QoS policy for the sis operation. Possible values are:
                <ul>
                <li> "background" - sis operation will run in background with
                minimal or no impact on data serving
                client operations,
                <li> "best-effort" - sis operations may have some impact on
                data serving client operations.
                </ul>
                Default value: "best-effort"
        
        :param delete_checkpoint: If this is "true", the sis operation will delete existing
                checkpoint and start the sis operation from the beginning.
                Default value: "false"
        
        :param restart_checkpoint: If this is "true", the sis operation will restart from
                previous checkpoint without checking for validity. This
                option should be used along with "scan" option.
                Default value: "false"
        """
        return self.request( "sis-start", {
            'build_metadata': [ build_metadata, 'build-metadata', [ bool, 'None' ], False ],
            'scan_all': [ scan_all, 'scan-all', [ bool, 'None' ], False ],
            'queue_operation': [ queue_operation, 'queue-operation', [ bool, 'None' ], False ],
            'scan': [ scan, 'scan', [ bool, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'qos_policy': [ qos_policy, 'qos-policy', [ basestring, 'None' ], False ],
            'delete_checkpoint': [ delete_checkpoint, 'delete-checkpoint', [ bool, 'None' ], False ],
            'restart_checkpoint': [ restart_checkpoint, 'restart-checkpoint', [ bool, 'None' ], False ],
        }, {
        } )
