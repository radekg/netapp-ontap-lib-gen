from netapp.connection import NaConnection
from snapshotstate_enum import SnapshotstateEnum # 0 properties
from snapshot_id import SnapshotId # 0 properties
from snapshot_info import SnapshotInfo # 22 properties
from snapshot_multirename_error import SnapshotMultirenameError # 3 properties
from snapshot_get_iter_key_td import SnapshotGetIterKeyTd # 4 properties
from snapshot_policy_info import SnapshotPolicyInfo # 7 properties
from UUID import Uuid # 0 properties
from snapshot_policy_get_iter_key_td import SnapshotPolicyGetIterKeyTd # 2 properties
from snapshot_reserve_detail_info import SnapshotReserveDetailInfo # 4 properties
from volume_is_snapcreated import VolumeIsSnapcreated # 2 properties
from volume_error import VolumeError # 4 properties
from snapshot_schedule_info import SnapshotScheduleInfo # 4 properties
from snapshot_modify_iter_key_td import SnapshotModifyIterKeyTd # 4 properties
from snapshot_autodelete_info import SnapshotAutodeleteInfo # 2 properties
from snapshot_owner import SnapshotOwner # 1 properties
from snapshot_modify_iter_info import SnapshotModifyIterInfo # 3 properties

class SnapshotConnection(NaConnection):
    
    def snapshot_rename(self, volume, current_name, new_name):
        """
        Rename a specified snapshot to a new name on a specified volume.
        This API is not supported on Infinite Volume constituents.
        
        :param volume: Name of the volume where the current snapshot and the
                new snapshot are located.
        
        :param current_name: Name of snapshot to be renamed.
        
        :param new_name: New name of snapshot as a result of the rename.
        """
        return self.request( "snapshot-rename", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'current_name': [ current_name, 'current-name', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_partial_restore_file(self, byte_count, start_byte, snapshot, path, force=None, volume=None, snapshot_instance_uuid=None, volume_dsid=None):
        """
        Restores a particular range of bytes in a file from a
        specified snapshot.
        <p>
        Partial file restores are used to restore particular pieces of
        LUNs and NFS or CIFS container files that are used by a host to
        store multiple sources of data. For example, a host may be
        storing multiple user databases in the same LUN. A partial file
        restore can be used to restore one of those databases in the
        LUN while not touching the other databases that are also stored
        in the LUN. Compressed files will not be restored, thought
        compression may be enabled on the volume.
        <p>
        Partial file restores require significant management by the
        caller.  The caller must understand the metadata of the host
        LUN or container file so that they can know which bytes belong
        to the object being restored.
        <p>
        Before the restore operation beings, the caller must quiesce
        the object being restored. It must remain quiesced for the
        duration of the restore operation. No host I/O should be issued
        for the object while it is being restored because the
        snapshot-partial-restore-file commands will be incrementally
        restoring the LUN or file and the host will therefore see
        inconsistent content for the object until the restore operation
        is completed.  Host I/O is permitted for the other objects
        stored in the LUN or container file because the partial file
        restore will not touch the bytes belonging to those other
        objects.
        <p>
        During the restore the caller must issue a
        snapshot-partial-restore-file command for each of the byte
        ranges that belong to the object being restored, based on the
        metadata of the LUN or container file.  Once each command
        returns, that byte range is restored and the changes are
        persistent.  If the filer should halt while processing a
        command, that byte range of the LUN or container file is
        inconsistent.  Some of the bytes at the beginning of the range
        may have been restored while bytes at the end of the range
        have not been restored.  Once the filer is rebooted the caller
        should re-issue the command to restore that byte range to
        complete the restore.
        <p>
        Once the restore is completed, the caller must purge any host
        operating system or application buffers that may hold data for
        the LUN or file that is now stale.  For NFS or CIFS mounted
        volumes the easiest way to purge any host buffers is to unmount
        and remount the volume.  Applications holding buffered data
        may need to be shut down and restarted.
        <p>
        Multiple partial file restore requests may be issued to the
        same LUN or file simultaneously. There is no requirement that
        the requests are all restoring from the same snapshot so that
        multiple restore operations for different objects may be
        concurrent on the same file.  There is no checking to prevent
        overlapping byte ranges between requests. Preventing this
        condition is the responsibility of the caller.
        <p>
        Partial file restores are not intended for restoring parts of
        normal user-level files that are stored in an NFS or CIFS
        exported volume. Use snapshot-restore-file to restore normal
        files like these.
        <p>
        The volume where the LUN or container file to restore and where
        the snapshot to restore from live must be online and must not
        be a mirror volume.
        <p>
        The partial file restore request may fail if there is not
        sufficient free space to overwrite all of the blocks in the
        byte range to be restored.
        <p>
        The partial file restore request may fail if the LUN being
        restored is a read-only LUN unless the force option is used.
        <p>
        The partial file restore request is synchronous, meaning that
        the command will not return until the entire byte range is
        restored.  The snapshot being restored from cannot be deleted
        while a request is being executed, but it can be deleted
        between requests.  If this happens the next request will
        notice that the snapshot has been deleted and will return an
        error.
        <p>
        The maximum number of bytes of data that can be restored in a
        single request is given by the max-byte-count value returned by
        the snapshot-partial-restore-file-list-info command.  This
        limit ensures that requests are periodically interruptible and
        avoids overloading the filer.
        <p>
        If the system halts while a partial file restore request is
        being executed, the request will not be restarted upon reboot.
        Some of the bytes at the beginning of the range may have been
        restored while bytes at the end of the range have not been
        restored.  The caller should reissue the partial file restore
        request for that byte range to complete the restore.
        
        :param byte_count: The number of bytes to restore, beginning at start-byte. The
                byte count must be a multiple of 4096. Use
                snapshot-partial-restore-file-list-info to determine the
                maximum number of bytes that can be restored in a single
                request.
                Range : [0 - 2^64-1]
        
        :param start_byte: The starting byte offset in the file to partially restore. The
                first byte of the file is byte zero. The start byte must be a
                multiple of 4096.
                Range : [0 - 2^64-1]
        
        :param snapshot: The simple name of the snapshot to restore from.  The snapshot
                must be from same volume as the file to partially restore.
        
        :param path: Path of the file to restore. Path syntax has two forms:
                /vol/<volumename>/<rest of path>
                /<rest of path>
                In the latter case (relative path), if volume was not
                specified, the root volume will be used.
        
        :param force: If this field is set to "true", restore operation will
                proceed even if LUN being restored is read-only.
                The default value is false.
        
        :param volume: Volume to restore to/from. If this is passed in, the path
                argument should be relative to the volume.
        
        :param snapshot_instance_uuid: A unique physical version identifier for a given snapshot
                within a volume or an aggregate. A typical snapshot instance
                UUID will look like:
                c0335624-21f3-450c-aea1-55884d0218b9
        
        :param volume_dsid: The volume's ONTAP Data Set ID. DSIDs are formatted as
                18-character strings composed of 16 hex characters
                prefixed with '0x'.
        """
        return self.request( "snapshot-partial-restore-file", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'byte_count': [ byte_count, 'byte-count', [ int, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'start_byte': [ start_byte, 'start-byte', [ int, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'None' ], False ],
            'volume_dsid': [ volume_dsid, 'volume-dsid', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_remove_owner(self, volume, owner, name):
        """
        auto generated : Remove owner from the ownership list
        
        :param volume: Volume
        
        :param owner: Snapshot Owner
        
        :param name: Snapshot
        """
        return self.request( "snapshot-remove-owner", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'snapshot-id' ], False ],
        }, {
        } )
    
    def snapshot_set_schedule(self, volume, hours=None, days=None, which_minutes=None, weeks=None, minutes=None, which_hours=None):
        """
        Set the snapshot schedule on a specified volume.
        If number of snapshots requested is greater than ONTAP
        allows, then ESNAPTOOMANY will be returned with the
        maximum allow snapshots in the reason.
        
        :param volume: Name of the volume name where the snapshots are located.
        
        :param hours: Number of snapshots taken hourly to keep on line.  If not
                provided, the number of weekly snapshots is left at the
                previous value.
        
        :param days: Number of snapshots taken daily to keep on line.  If not
                provided, the number of daily snapshots is left at the
                previous value.
        
        :param which_minutes: Comma-separated list of the minutes at which the minutely
                snapshots are created.  If minutes is 0, which-minutes is
                ignored and cleared.
        
        :param weeks: Number of snapshots taken weekly to keep on line.  If not
                provided, the number of weekly snapshots is left at the
                previous value.
        
        :param minutes: Number of snapshots taken minutely to keep on line.  If not
                provided, the number of minutely snapshots is left at the
                previous value.
        
        :param which_hours: Comma-separated list of the hours at which the hourly
                snapshots are created.  If hours is 0, which-hours is
                ignored and cleared.
        """
        return self.request( "snapshot-set-schedule", {
            'hours': [ hours, 'hours', [ int, 'None' ], False ],
            'days': [ days, 'days', [ int, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'which_minutes': [ which_minutes, 'which-minutes', [ basestring, 'None' ], False ],
            'weeks': [ weeks, 'weeks', [ int, 'None' ], False ],
            'minutes': [ minutes, 'minutes', [ int, 'None' ], False ],
            'which_hours': [ which_hours, 'which-hours', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_hammer_ownership(self, volume, owner, name):
        """
        auto generated : Add and remove ownership to a given snapshot 100
        times
        
        :param volume: Volume
        
        :param owner: Snapshot Name
        
        :param name: Snapshot
        """
        return self.request( "snapshot-hammer-ownership", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'snapshot-id' ], False ],
        }, {
        } )
    
    def snapshot_list_info(self, target_name=None, target_type=None, terse=None, volume=None, lun_clone_snapshot=None, snapowners=None, is_7_mode_snapshot=None):
        """
        Return snapshot information for a specified volume.  A list
        of snapshots and information about each snapshot is returned.
        In Data ONTAP Cluster-Mode, 'snapshot-get-iter' API is the
        preferred way of retrieving snapshot information.
        
        :param target_name: Name of the object on which to list the snaplist information.
                Arguments "target-name" and "target-type" should be used
                together.
                Arguments "volume" and ("target-name", "target-type") pair
                are mutually exclusive. One and only one of them should
                be specified.
        
        :param target_type: Type of the object on which to list the snaplist information.
                Possible values: volume, aggregate.
        
        :param terse: If set to true, the snapshot block ownership values, namely the
                "total" and "cumulative-total" outputs, will be omitted.
                If set to false, the block ownership calculation will be
                included in the output.
                The default value is false.
        
        :param volume: Name of the volume on which to list the snaplist information.
                It is for backward compatibility.
                The recommended usage is to use arguments
                ("target-name", "target-type") pair.
        
        :param lun_clone_snapshot: If set to true, check if snapshot contains any lun clones.
                The default value is false.
        
        :param snapowners: If set to true, owners of the busy snapshot are returned. If false,
                or if the option is omitted, the list of owners is not returned.
        
        :param is_7_mode_snapshot: If set to true, check if snapshot is a 7-mode snapshot.
                A 7-mode snapshot can appear in a cluster-mode volume as
                a result of the volume being transitioned from 7-mode to
                cluster-mode.  A 7-mode snapshot cannot be used in a volume
                snapshot restore.
                The default value is false.
        """
        return self.request( "snapshot-list-info", {
            'target_name': [ target_name, 'target-name', [ basestring, 'None' ], False ],
            'target_type': [ target_type, 'target-type', [ basestring, 'None' ], False ],
            'terse': [ terse, 'terse', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'lun_clone_snapshot': [ lun_clone_snapshot, 'lun-clone-snapshot', [ bool, 'None' ], False ],
            'snapowners': [ snapowners, 'snapowners', [ bool, 'None' ], False ],
            'is_7_mode_snapshot': [ is_7_mode_snapshot, 'is-7-mode-snapshot', [ bool, 'None' ], False ],
        }, {
            'snapshots': [ SnapshotInfo, True ],
        } )
    
    def snapshot_restore_volume_async(self, volume, snapshot, snapshot_instance_uuid=None):
        """
        Reverts an Infinite Volume to a specified snapshot. The Infinite
        Volume must be online and unmounted and must not be a mirror.
        After the reversion, the Infinite Volume is in the same state
        as it was when the snapshot was taken.
        <p>
        This API is not supported on flexible volumes and
        Infinite Volume constituents.
        
        :param volume: Name of Infinite Volume to restore.
        
        :param snapshot: Name of snapshot to restore from.
        
        :param snapshot_instance_uuid: The 128 bit unique snapshot identifier expressed in the form
                of UUID.  This field is optional and can appear together with
                'snapshot' to uniquely identify a snapshot to restore.  If
                this field is provided, 'snapshot' is a required parameter.
                An example of an actual UUID is:
                84a010ec-3d28-11df-84e8-123478653412
        """
        return self.request( "snapshot-restore-volume-async", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'UUID' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapshot_policy_delete(self, policy):
        """
        Delete the specified Snapshot Scheduling Policy
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        """
        return self.request( "snapshot-policy-delete", {
            'policy': [ policy, 'policy', [ basestring, 'snapshot-policy' ], False ],
        }, {
        } )
    
    def snapshot_get_reserve(self, volume):
        """
        Obtain the current snapshot reserve on a specified volume.
        Error Returns: Invalid volume name.
        
        :param volume: Name of the volume that contains the snapshot reserve.
        """
        return self.request( "snapshot-get-reserve", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'percent-reserved': [ int, False ],
            'blocks-reserved': [ int, False ],
        } )
    
    def snapshot_reclaimable_info(self, volume, snapshots):
        """
        Returns the amount of space that would be freed when a set
        of snapshots are deleted from a specified volume.
        
        :param volume: Name of the volume on which the snapshot reclaimable space
                info is to be collected.
        
        :param snapshots: List of snapshots. A maximum of 255 snapshots can be listed.
        """
        return self.request( "snapshot-reclaimable-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshots': [ snapshots, 'snapshots', [ basestring, 'snapshot-name' ], True ],
        }, {
            'reclaimable-size': [ int, False ],
        } )
    
    def snapshot_restore_file(self, snapshot, path, force=None, space_efficient_split_disabled=None, volume=None, restore_path=None, snapshot_instance_uuid=None, volume_dsid=None):
        """
        Reverts a single file to a revision from a specified snapshot.
        The volume used for restoring the file must be online and must
        not be a mirror.  Files other than normal files and LUNs are
        not restored. This includes directories (and their contents),
        and files with NT streams.  Compressed files will not be
        restored in Data ONTAP 7-mode, though compression may
        be enabled on the volume.
        <p>
        If there is not enough space in the volume, the single file
        snap restore will not start.  If the file already exists (in
        the active filesystem), it will be overwritten with the version
        in the snapshot.  Exclusive oplocks and hard exclusive locks
        like the DOS compatibility lock will be invalidated.
        <p>
        Other single file snap restores can be executed concurrently.
        Also it is possible for the single file snap restore to be
        aborted if we run out of disk space during the operation. When
        this happens the timestamp of the file being restored will be
        updated. Thus it will not be the same as the timestamp of the
        file in the snapshot.
        <p>
        For normal files, an in-progress restore can be aborted by
        removing the file. For NFS users, the last link to the file
        must be removed.
        <p>
        For all restored files, the snapshot used for the restore
        cannot be deleted. New snapshots cannot be created while a
        single-file snaprestore is in progress. Scheduled snapshots on
        the volume will be suspended for the duration of the restore.
        Tree, user and group quota limits are not enforced for the
        owner, group and tree in which the file is being restored. Thus
        if the user, group or tree quotas are exceeded, /etc/quotas
        will need to be altered after the single file snap restore
        operation has completed. Then quota resize will need to be run.
        When the restore completes, the file's attributes (size,
        permissions, ownership, etc.) should be identical as those in
        the snapshot.
        <p>
        If the system is halted or crashes while a single file snap
        restore is in progress then the operation will be restarted on
        reboot.  A volume cannot have both a volume snaprestore and a
        single-file snaprestore executing simultaneously. Multiple
        single-file snaprestores can be in progress simultaneously.
        <p>
        <b>The following applies to Data ONTAP 7-mode only:</b>
        <p>
        For normal files while the restore is proceeding, any operation
        which tries to change the file will be suspended until the
        restore is done.  It could take up to several minutes for
        before the API invocation returns.  Once the invocation
        returns, the file restore will proceed in the background.
        The restore may take a long time to complete depending
        on the size of the file being restored.  The file is
        unavailable for use during this time.
        <p>
        For LUNs that are restored over top of their existing LUN, a
        LUN clone can be created that is backed by the snapshot being
        restored from and then the clone is split.  For LUNs that are
        restored over top of their existing LUN, an
        in-progress restore can be aborted by using lun-clone-stop
        when in Data ONTAP 7-mode. The restored LUN will still be a
        clone in this case and it will still be partially backed by
        the snapshot it was restored from. Snapshots are disabled
        during restore due to space efficient LUN clone split.
        In order to disable space efficient split during restore
        set the optional parameter space-efficient-split-disabled.
        While the restore is proceeding the LUN is available and I/O
        (both reads and writes) is permitted. Data that is modified in
        the LUN while the restore is proceeding will not be overwritten
        by the restore process.  The restore may take a long time
        to complete depending on the size of the LUN being restored.
        Use lun-clone-status-list-info to see the progress of the LUN
        restore.
        <p>
        This operation will fail if the LUN being restored is a read-only
        LUN unless the force option is used.
        
        :param snapshot: Name of snapshot to restore from.  Snapshot must be from
                same volume as the file to restore.
        
        :param path: Path of the file to restore. Path syntax has two forms:
                /vol/<volumename>/<rest of path>
                /<rest of path>
                In the latter case (relative path), if volume was not
                specified, the root volume will be used.
        
        :param force: If this field is set to "true", restore operation will
                proceed even if LUN being restored is read-only.
                The default value is false.
        
        :param space_efficient_split_disabled: By default 'false', space-efficient LUN clone split
                is allowed during restore. This parameter, if set to
                'true', disables space-efficient splitting for this
                specific operation.
        
        :param volume: Volume to restore to/from. If this is passed in, the path
                argument should be relative to the volume.
        
        :param restore_path: Path to restore to.  The path must be a full path to a
                filename, and must be in the same volume as the volume
                used for the restore.  If not specified, restore-path
                is defaulted to the original path.
        
        :param snapshot_instance_uuid: A unique physical version identifier for a given snapshot
                within a volume or an aggregate. A typical snapshot instance
                UUID will look like:
                c0335624-21f3-450c-aea1-55884d0218b9
        
        :param volume_dsid: The volume's ONTAP Data Set ID. DSIDs are formatted as
                18-character strings composed of 16 hex characters
                prefixed with '0x'.
        """
        return self.request( "snapshot-restore-file", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'space_efficient_split_disabled': [ space_efficient_split_disabled, 'space-efficient-split-disabled', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'restore_path': [ restore_path, 'restore-path', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'None' ], False ],
            'volume_dsid': [ volume_dsid, 'volume-dsid', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_add_test_owners(self, volume, name):
        """
        auto generated : Add test owners to a snapshot
        
        :param volume: Volume
        
        :param name: Snapshot
        """
        return self.request( "snapshot-add-test-owners", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'name': [ name, 'name', [ basestring, 'snapshot-id' ], False ],
        }, {
        } )
    
    def snapshot_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get Information about multiple Snapshot Policies
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                snapshot object.
                All snapshot objects matching this query up to 'max-records' will
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
        return self.request( "snapshot-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SnapshotPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapshotPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SnapshotPolicyInfo, True ],
        } )
    
    def snapshot_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of snapshot or a group of
        snapshot objects.
        
        :param query: If modifying a specific snapshot, this input element must specify
                all keys.
                If modifying snapshot objects based on query, this input element
                must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                snapshot even when the modification of a previous matching
                snapshot fails, and do so until the total number of objects
                failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of snapshot objects
                (just keys) that were successfully updated.
                If set to false, the list of snapshot objects modified will not
                be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple snapshot objects match
                a given query.
                If set to true, the API will continue modifying the next matching
                snapshot even when modification of a previous snapshot fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of snapshot objects
                (just keys) that were not modified due to some error.
                If set to false, the list of snapshot objects not modified will
                not be returned.
                Default: true
        """
        return self.request( "snapshot-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SnapshotInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ SnapshotInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SnapshotModifyIterInfo, True ],
            'failure-list': [ SnapshotModifyIterInfo, True ],
        } )
    
    def snapshot_autodelete_list_info(self, volume):
        """
        Returns the current snapshot autodelete settings.
        
        :param volume: Name of the existing volume for which we want snapshot
                autodelete settings
        """
        return self.request( "snapshot-autodelete-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'options': [ SnapshotAutodeleteInfo, True ],
        } )
    
    def snapshot_partial_restore_file_list_info(self):
        """
        Returns partial file restore settings of the vserver.
        <p>
        This API is not supported on Infinite Volume.
        """
        return self.request( "snapshot-partial-restore-file-list-info", {
        }, {
            'max-byte-count': [ int, False ],
        } )
    
    def snapshot_policy_get(self, policy, desired_attributes=None):
        """
        Get Information about a single Snapshot Policy
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "snapshot-policy-get", {
            'policy': [ policy, 'policy', [ basestring, 'snapshot-policy' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapshotPolicyInfo, 'None' ], False ],
        }, {
            'attributes': [ SnapshotPolicyInfo, False ],
        } )
    
    def snapshot_policy_add_schedule(self, policy, count, schedule, prefix=None, snapmirror_label=None):
        """
        Add a new schedule to the Snapshot Policy. A schedule can be
        created by using 'job-schedule-cron-create' or
        'job-schedule-interval-create' APIs.
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        
        :param count: The maximum number of snapshots to be retained for the schedule.
                The count of all the snapshots for to be retained for this policy
                cannot be more than 255.
        
        :param schedule: A human readable string describing the name of a new schedule to
                be added inside the snapshot policy. Maximum length of this field
                can be 255 characters. The schedule name can be any one of the
                reserved schedules like 'hourly', 'weekly' or 'daily' or it can
                be a user created schedule.
        
        :param prefix: The snapshot name prefix for the schedule. This field should be
                unique within the policy.
        
        :param snapmirror_label: The SnapMirror Label for the schedule. This label will be used to
                define vaulting policies at a vault destination. Maximum length
                of this field is 31 characters
        """
        return self.request( "snapshot-policy-add-schedule", {
            'policy': [ policy, 'policy', [ basestring, 'snapshot-policy' ], False ],
            'count': [ count, 'count', [ int, 'None' ], False ],
            'prefix': [ prefix, 'prefix', [ basestring, 'None' ], False ],
            'snapmirror_label': [ snapmirror_label, 'snapmirror-label', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_set_reserve(self, volume, percentage):
        """
        Sets the size of the indicated volume's snapshot reserve
        to the specified percentage.  Reserve space can be used
        only by snapshots and not by the active file system.
        
        :param volume: Name of volume on which to set the snapshot space reserve.
        
        :param percentage: Percentage to set.  Range [0-100].
        """
        return self.request( "snapshot-set-reserve", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'percentage': [ percentage, 'percentage', [ int, 'None' ], False ],
        }, {
        } )
    
    def snapshot_policy_modify_schedule(self, policy, schedule, new_count=None, new_snapmirror_label=None):
        """
        Modify a snapshot policy
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        
        :param schedule: A human readable string describing the name of a schedule whose
                retention count will be modified. Maximum length of this field
                can be 255 characters. The schedule name can be any one of the
                reserved schedules like 'hourly','weekly' or 'daily' or it can be
                user created schedule.
        
        :param new_count: The new retention count for the schedule.
        
        :param new_snapmirror_label: The new SnapMirror Label for the schedule. This label will be
                used to define vaulting policies at a vault destination. If an
                empty label is specified, the existing label will be deleted. The
                maximum length of this field is 31 characters
        """
        return self.request( "snapshot-policy-modify-schedule", {
            'policy': [ policy, 'policy', [ basestring, 'snapshot-policy' ], False ],
            'new_count': [ new_count, 'new-count', [ int, 'None' ], False ],
            'new_snapmirror_label': [ new_snapmirror_label, 'new-snapmirror-label', [ basestring, 'None' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_volume_info(self, volume):
        """
        Returns snapshot related volume information. The information
        returned is valid at the time the API call reached the filer
        and maybe outdated soon after.
        
        :param volume: Name of the volume on which the space needs to be checked.
        """
        return self.request( "snapshot-volume-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'size-available': [ int, False ],
        } )
    
    def snapshot_reserve_list_info(self, volume=None):
        """
        Gets the percentage of disk space that is reserved for
        snapshots in the indicated volume.  If no volume is
        specified, this will return the percentage of disk space
        reserved for snapshots for each of the volumes in the
        system. Reserve space can be used only by snapshots
        and not by the active file system.
        This API is deprecated in Data ONTAP Cluster-Mode 8.2 and later.
        Use volume-get-iter instead.
        
        :param volume: Volume to get percentage of space reserved for snapshots.
        """
        return self.request( "snapshot-reserve-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'snapshot-reserve-details': [ SnapshotReserveDetailInfo, True ],
        } )
    
    def snapshot_multirename(self, volume_names, new_snapshot_name, snapshot_name):
        """
        Rename Snapshot copies with a specific name to a new name across
        multiple volumes. The API processes all the specified volumes
        even if rename fails on one or more volumes. The
        snapshot-multirename-errors field should be inspected for
        failures even if the API is successful.This API is not supported
        on Infinite Volume.
        
        :param volume_names: Names of the volumes across which the snapshot is to be renamed.
        
        :param new_snapshot_name: The new snapshot name.
        
        :param snapshot_name: The current snapshot name.
        """
        return self.request( "snapshot-multirename", {
            'volume_names': [ volume_names, 'volume-names', [ basestring, 'volume-name' ], True ],
            'new_snapshot_name': [ new_snapshot_name, 'new-snapshot-name', [ basestring, 'snapshot-id' ], False ],
            'snapshot_name': [ snapshot_name, 'snapshot-name', [ basestring, 'snapshot-id' ], False ],
        }, {
            'snapshot-multirename-errors': [ SnapshotMultirenameError, True ],
        } )
    
    def snapshot_autodelete_set_option(self, volume, option_value, option_name):
        """
        Set the option named 'option-name' to the value
        specified by 'option-value' in the autodelete settings
        of the specified volume.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume: Name of the volume for which we want to change autodelete
                settings.
        
        :param option_value: The value to set the named option
        
        :param option_name: Name of the option to be set. Possible values:
                <dl>
                <dt>"state" (value: "on" | "off")</dt>
                <dd>
                This option determines if the snapshot autodelete is
                currently enabled for the volume.
                Setting the option to "on" switches on the snapshot
                autodelete for the volume.
                Setting the option to "off" switches off the snapshot
                autodelete for the volume.
                </dd><br>
                <dt>"commitment" (value: "try" | "disrupt" | "destroy" )</dt>
                <dd>
                This option determines the snapshots which snapshot
                autodelete is allowed to delete to get back space.
                Setting this option to "try" only permits the snapshots
                which are not locked by data protection utilities
                (dump, mirroring, NDMPcopy) and data backing functionalities
                (volume, LUN and File clones) to be deleted.
                Setting this option to "disrupt" only permits the snapshots
                which are not locked by data backing functionalities
                (volume, LUN and File clones) to be deleted.
                Setting this option to "destroy", will destroy the
                data backing functionality (volume, LUN and File clones)
                if the backing snapshot is deleted.
                </dd><br>
                <dt>"trigger" (value: "volume" | "snap_reserve" | "space_reserve") </dt>
                <dd>
                This option determines the condition which starts
                the automatic deletion of snapshots.
                Setting this option to "volume" triggers automatic
                deletion of snapshots when the volume reaches threshold
                capacity and the volume's snap reserve has been exceeded.
                Setting the option to "snap_reserve" triggers automatic
                deletion of snapshots when the snap reserve of the volume
                reaches threshold capacity.
                Setting the option to "space_reserve" triggers automatic
                deletion of snapshots when the space reserved the volume
                reaches threshold capacity and the volume's snap reserve
                has been exceeded.
                The threshold capacity is determined by the size of the
                volume as given below:
                <ul>
                <li>If the volume size is less than 20 GB,
                the autodelete threshold is 85%.</li>
                <li>If the volume size is equal to or greater than
                20 GB and less than 100 GB, the autodelete threshold
                is 90%.</li>
                <li>If the volume size is equal to or greater than
                100 GB and less than 500 GB, the autodelete threshold
                is 92%.</li>
                <li>If the volume size is equal to or greater than
                500 GB and less than 1 TB, the autodelete threshold
                is 95%.</li>
                <li>If the volume size is equal to or greater than
                1 TB, the autodelete threshold is 98%.</li>
                </ul></dd><br>
                <dt>"target_free_space" (value: &lt; number &gt;)</dt>
                <dd>
                This option determines when snapshot autodelete should stop
                deleting snapshot. Depending on the trigger, snapshots
                are deleted till we reach the target free space
                percentage.
                </dd><br>
                <dt>"delete_order" (value: newest_first | oldest_first)</dt>
                <dd>
                This option determines if the oldest or newest snapshot
                is deleted first.
                </dd><br>
                <dt>"defer_delete" (value: scheduled | user_created | prefix | none) </dt>
                <dd>
                This option determines which kind of snapshots to delete in
                the end.
                Setting this option value to "scheduled" will delete
                the snapshots created by the snapshot scheduler last.
                Setting this option value to "user_created" will delete
                the snapshots not created by the snapshot scheduler last.
                Setting this option value to "prefix" will delete
                the snapshots matching the prefix string to be deleted last.
                Setting this option value to "none" will disable the above
                choices.
                </dd><br>
                <dt>"prefix" (value: &lt; string &gt;)</dt>
                <dd>
                This option can be set to provide the prefix string for
                the "prefix" value of the "defer_delete" option. The
                prefix string length can be 15 char long.
                </dd><br>
                <dt>"destroy_list" (value: &lt; string &gt;)</dt>
                <dd>
                A comma seperated list of services which can be
                destroyed if the snapshot backing that service is deleted.
                For 7-mode, the possible values for this option are a combination
                of "lun_clone", "vol_clone", "cifs_share", "file_clone" or
                "none".
                For cluster-mode, the possible values for this option are a
                combination of "lun_clone,file_clone" (for LUN clone and/or file
                clone), "lun_clone,sfsr" (for LUN clone and/or sfsr), "vol_clone",
                "cifs_share",  or "none". Please note that "lun_clone",
                "file_clone" and "sfsr" individually are not valid values. Only pairs
                "lun_clone,file_clone" and "lun_clone,sfsr" are supported.
                The option "sfsr" is not supported for 7-mode.
                The default value is "none" for 7-mode and cluster-mode.
                </dd><br>
                </dl>
        """
        return self.request( "snapshot-autodelete-set-option", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'option_value': [ option_value, 'option-value', [ basestring, 'None' ], False ],
            'option_name': [ option_name, 'option-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_delete_async(self, volume, snapshot, snapshot_instance_uuid=None, ignore_owners=None):
        """
        Delete a snapshot on a specified Infinite Volume.
        EBUSY is returned when the snapshot is in use.
        EROFS is returned when the Infinite Volume is read-only.
        EAGAIN is returned when splitting a blockmap or reverting.
        <p>
        This API is not supported on flexible volumes and
        Infinite Volume constituents.
        
        :param volume: Name of the Infinite Volume on which the snapshot is to
                be deleted.
        
        :param snapshot: Name of snapshot to be deleted on the specified Infinite Volume.
        
        :param snapshot_instance_uuid: The 128 bit unique snapshot identifier expressed in the form
                of UUID.  This field is optional and can appear together with
                'snapshot' to uniquely identify a snapshot for deletion.  If
                this field is provided, 'snapshot' is a required parameter.
                An example of an actual UUID is:
                73a010ec-3d28-11df-84e8-123478563412
        
        :param ignore_owners: If this field is true, snapshot will be deleted even if
                some other processes are accessing it.
                The default value is false.
        """
        return self.request( "snapshot-delete-async", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'UUID' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'ignore_owners': [ ignore_owners, 'ignore-owners', [ bool, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapshot_delete(self, volume, snapshot, snapshot_instance_uuid=None, ignore_owners=None):
        """
        Delete a snapshot on a specified volume.
        EBUSY is returned when the snapshot is in use.
        EROFS is returned when the volume is read-only.
        EAGAIN is returned when splitting a blockmap or reverting.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume: Name of the volume on which the snapshot is to
                be deleted.
        
        :param snapshot: Name of snapshot to be deleted on the specified volume.
        
        :param snapshot_instance_uuid: The 128 bit unique snapshot identifier expressed in the form
                of UUID.  This field is optional and can appear together with
                'snapshot' to uniquely identify a snapshot for deletion.  If
                this field is provided, 'snapshot' is a required parameter.
                <p>
                An example of an actual UUID is:
                <p>
                73a010ec-3d28-11df-84e8-123478563412
        
        :param ignore_owners: If this field is true, snapshot will be deleted even if
                some other processes are accessing it.
                <p>
                The default value is false.
        """
        return self.request( "snapshot-delete", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'UUID' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'ignore_owners': [ ignore_owners, 'ignore-owners', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapshot_create(self, volume, snapshot, comment=None, is_valid_lun_clone_snapshot=None, async=None, snapmirror_label=None):
        """
        Create a new snapshot on a specified volume.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume: Name of the volume on which the snapshot is to
                be created. The volume name can contain letters,
                numbers, and the underscore character (_), but the
                first character must be a letter or an underscore.
        
        :param snapshot: Name of the snapshot to be created.
                The maximum string length is 256 characters.
        
        :param comment: A human readable comment attached with the snapshot. The
                size of the comment can be at most 255 characters.
        
        :param is_valid_lun_clone_snapshot: If true, the snapshot create has been requested by
                snapvault hence all backing snapshots for all the lun
                clones in this snapshot will be locked. This ensures
                the consistency of this snapshot.
                The default value is false.
        
        :param async: If true, the snapshot is to be created asynchronously.
                The default value is false.
        
        :param snapmirror_label: A human readable SnapMirror Label attached with the
                snapshot. Size of the label can be at most 31 characters.
                This label will be applied as an attribute to the
                snapshot that is created and will be used by the vaulting
                system to identify a vaulting scheme.
        """
        return self.request( "snapshot-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'is_valid_lun_clone_snapshot': [ is_valid_lun_clone_snapshot, 'is-valid-lun-clone-snapshot', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'async': [ async, 'async', [ bool, 'None' ], False ],
            'snapmirror_label': [ snapmirror_label, 'snapmirror-label', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_policy_modify(self, policy, enabled):
        """
        Enable or Disable the specified Snapshot Scheduling Policy
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        
        :param enabled: The state of the snapshot policy. If true, the snapshot policy is
                enabled and scheduled snapshots will be created on the volume
                associated with this policy.
        """
        return self.request( "snapshot-policy-modify", {
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapshot_policy_remove_schedule(self, policy, schedule):
        """
        Remove a snapshot schedule from policy
        
        :param policy: A human readable string describing the name of the snapshot
                scheduling policy.
        
        :param schedule: A human readable string describing the name of a schedule which
                will be removed from the snapshot policy. Maximum length of this
                field can be 255 characters. The schedule name can be any one of
                the reserved schedules like 'hourly','weekly' or 'daily' or it
                can be a user created schedule.
        """
        return self.request( "snapshot-policy-remove-schedule", {
            'policy': [ policy, 'policy', [ basestring, 'snapshot-policy' ], False ],
            'schedule': [ schedule, 'schedule', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapshot_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of snapshot objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                snapshot object.
                All snapshot objects matching this query up to 'max-records' will
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
        return self.request( "snapshot-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SnapshotInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapshotInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SnapshotInfo, True ],
            'volume-errors': [ VolumeError, True ],
        } )
    
    def snapshot_policy_create(self, schedule1, policy, count1, enabled, comment=None, prefix3=None, prefix2=None, prefix1=None, prefix5=None, prefix4=None, schedule4=None, schedule5=None, schedule2=None, schedule3=None, snapmirror_label5=None, snapmirror_label4=None, snapmirror_label1=None, snapmirror_label3=None, snapmirror_label2=None, count3=None, count2=None, count5=None, count4=None):
        """
        Create a new Snapshot Scheduling Policy
        
        :param schedule1: First schedule to be added inside the policy. Atleast one
                schedule has to be added to create a policy.
        
        :param policy: The name of the snapshot scheduling policy which has to be
                created. This API creates a snapshot policy and adds the
                schedules to it. At the most 5 schedules can be added to the
                snapshot policy. Maximum length of this string can be 256
                characters.
        
        :param count1: Retention count for the snapshots created by the first schedule.
                The count of all the snapshots to be retained for this policy
                cannot be more than 255.
        
        :param enabled: Status of the snapshot policy indicating whether the policy will
                be enabled or disabled. If set to true, the policy will be
                enabled.
        
        :param comment: A human readable description associated with the snapshot policy.
                The maximum length of this field can be 255 characters.
        
        :param prefix3: Snapshot name prefix for the third schedule. Prefix name should
                be unique within the policy.
        
        :param prefix2: Snapshot name prefix for the second schedule. Prefix name should
                be unique within the policy.
        
        :param prefix1: Snapshot name prefix for the first schedule. Prefix name should
                be unique within the policy.
        
        :param prefix5: Snapshot name prefix for the fifth schedule. Prefix name should
                be unique within the policy.
        
        :param prefix4: Snapshot name prefix for the fourth schedule. Prefix name should
                be unique within the policy.
        
        :param schedule4: Fourth schedule to be added inside the policy.
        
        :param schedule5: Fifth schedule to be added inside the policy.
        
        :param schedule2: Second schedule to be added inside the policy.
        
        :param schedule3: Third schedule to be added inside the policy.
        
        :param snapmirror_label5: Label for SnapMirror Operations for fifth schedule. Maximum
                length of this field is 31 characters.
        
        :param snapmirror_label4: Label for SnapMirror Operations for fourth schedule. Maximum
                length of this field is 31 characters.
        
        :param snapmirror_label1: Label for SnapMirror Operations for first schedule. Maximum
                length of this field is 31 characters.
        
        :param snapmirror_label3: Label for SnapMirror Operations for third schedule. Maximum
                length of this field is 31 characters.
        
        :param snapmirror_label2: Label for SnapMirror Operations for second schedule. Maximum
                length of this field is 31 characters.
        
        :param count3: Retention count for the snapshots created by the third schedule.
                The count of all the snapshots to be retained for this policy
                cannot be more than 255.
        
        :param count2: Retention count for the snapshots created by the second schedule.
                The count of all the snapshots to be retained for this policy
                cannot be more than 255.
        
        :param count5: Retention count for the snapshots created by the fifth schedule.
                The count of all the snapshots to be retained for this policy
                cannot be more than 255.
        
        :param count4: Retention count for the snapshots created by the fourth schedule.
                The count of all the snapshots to be retained for this policy
                cannot be more than 255.
        """
        return self.request( "snapshot-policy-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'prefix3': [ prefix3, 'prefix3', [ basestring, 'None' ], False ],
            'prefix2': [ prefix2, 'prefix2', [ basestring, 'None' ], False ],
            'prefix1': [ prefix1, 'prefix1', [ basestring, 'None' ], False ],
            'prefix5': [ prefix5, 'prefix5', [ basestring, 'None' ], False ],
            'prefix4': [ prefix4, 'prefix4', [ basestring, 'None' ], False ],
            'schedule4': [ schedule4, 'schedule4', [ basestring, 'None' ], False ],
            'schedule5': [ schedule5, 'schedule5', [ basestring, 'None' ], False ],
            'schedule1': [ schedule1, 'schedule1', [ basestring, 'None' ], False ],
            'schedule2': [ schedule2, 'schedule2', [ basestring, 'None' ], False ],
            'schedule3': [ schedule3, 'schedule3', [ basestring, 'None' ], False ],
            'snapmirror_label5': [ snapmirror_label5, 'snapmirror-label5', [ basestring, 'None' ], False ],
            'snapmirror_label4': [ snapmirror_label4, 'snapmirror-label4', [ basestring, 'None' ], False ],
            'snapmirror_label1': [ snapmirror_label1, 'snapmirror-label1', [ basestring, 'None' ], False ],
            'snapmirror_label3': [ snapmirror_label3, 'snapmirror-label3', [ basestring, 'None' ], False ],
            'snapmirror_label2': [ snapmirror_label2, 'snapmirror-label2', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'count1': [ count1, 'count1', [ int, 'None' ], False ],
            'count3': [ count3, 'count3', [ int, 'None' ], False ],
            'count2': [ count2, 'count2', [ int, 'None' ], False ],
            'count5': [ count5, 'count5', [ int, 'None' ], False ],
            'count4': [ count4, 'count4', [ int, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapshot_create_async(self, volume, snapshot, comment=None):
        """
        Create a new snapshot on a specified Infinite Volume.
        <p>
        This API is not supported on flexible volumes and
        Infinite Volume constituents.
        
        :param volume: Name of the Infinite Volume on which the snapshot is to
                be created. The Infinite Volume name can contain letters,
                numbers, and the underscore character (_), but the
                first character must be a letter or an underscore.
        
        :param snapshot: Name of the snapshot to be created.
                The maximum string length is 256 characters.
        
        :param comment: A human readable comment attached with the snapshot. The
                size of the comment can be at most 255 characters.
        """
        return self.request( "snapshot-create-async", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def snapshot_restore_file_info(self):
        """
        Get information about snapshot file restores on a given
        vserver. Returns maximum snapshot file restores limit and
        snapshot file restores in progress numbers.
        """
        return self.request( "snapshot-restore-file-info", {
        }, {
            'max-sfsr-limit': [ int, False ],
            'sfsr-in-progress': [ int, False ],
        } )
    
    def snapshot_multidelete(self, volume_names, snapshot, volume_uuids):
        """
        Delete the snapshot from the given flexible volumes.
        This API will return failure if the volume could not be
        found or it is busy. All the volumes should be
        online when this API is invoked. It will only delete snapshots
        on Read-Write volumes. Once all the necessary information
        to delete snapshots is available, this API will start deleting
        snapshots on the volumes. If any of the snapshot delete failed,
        the API will remember the failed volume and continue deleting
        snapshot on the remaining volumes. In case of failure to
        delete the snapshots from all the given volumes, the API will
        return a SUCCESS and also return information about the failed
        snapshot deletes via the 'volume-errors' output. If the API
        returns SUCCESS, the applications should check if the
        'volume-errors' output is returned or not to check for failed
        snapshot deletions.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume_names: Names of the volumes across which the snapshot is to be deleted.
        
        :param snapshot: Name of the snapshot to be deleted.
                The maximum string length is 256 characters.
        
        :param volume_uuids: The identities of the volumes from which the snapshot will
                be deleted.
                <p>
                The volume identity string is its 128-bit universally-unique
                identifier (UUID) or its DSID.
                <p>
                UUIDs are formatted as 36-character strings.  These
                strings are composed of 32 hexadecimal characters
                broken up into five groupings separated by '-'s.  The
                first grouping has 8 hex characters, the second through
                fourth groupings have four hex characters each, and the
                fifth and final grouping has 12 hex characters.  Note
                that a leading '0x' is not used.
                <p>
                Here is an example of an actual UUID:
                <p>
                <dl>
                <dt><dd> 49e370d6-5b5a-11d9-9eb5-000100000529 </dd><br></dt>
                </dl>
        """
        return self.request( "snapshot-multidelete", {
            'volume_names': [ volume_names, 'volume-names', [ basestring, 'volume-name' ], True ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'volume_uuids': [ volume_uuids, 'volume-uuids', [ basestring, 'UUID' ], True ],
        }, {
            'volume-errors': [ VolumeError, True ],
        } )
    
    def snapshot_multicreate_validate(self, volume_names, snapshot):
        """
        This is a companion API of snapshot-multicreate.
        It validates the snapshot creation operation on the specified
        volumes. But it does not actually create any snapshot. This API
        only does validations on all volumes and report all errors
        in the output array.
        This API is intended to be issued before the
        snapshot-multicreate API to find out all the errors that may be
        found during the snapshot create. Its main purpose is to enable
        snapshot-multicreate's caller to reduce the likelihood of
        snapshot-multicreate's failure, thereby attempting to avoid
        the cleanup overhead (of deleting any newly created snapshots)
        during failure processing.
        However, this validation API does not guarantee that
        snapshot-multicreate API will actually work. Something could
        change between the two calls to cause the actual snapshot
        creations to fail.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume_names: Names of the volumes across which the snapshot creation is to
                be validated.
        
        :param snapshot: Name of the snapshot to be created.
                The maximum string length is 256 characters.
        """
        return self.request( "snapshot-multicreate-validate", {
            'volume_names': [ volume_names, 'volume-names', [ basestring, 'volume-name' ], True ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'volume-errors': [ VolumeError, True ],
        } )
    
    def snapshot_multicreate(self, volume_names, snapshot, cleanup=None):
        """
        Create a snapshot with the specific name, on each of the
        specified volumes. It is the caller's responsibility to ensure
        that the data in the snapshots across all volumes is
        consistent, by quiescing I/O to these volumes (or the LUNs of
        interest in these volumes), across the call to this API.
        The API returns SUCCESS when a snapshot is successfully created
        on each of the specified volumes. This API bails out and
        reports FAILURE when an error is found at creating a snapshot
        on a volume. It does not continue on to create snapshots on
        the remaining volumes.
        When the API fails, the returned error code is for the failed
        volume. For clustered systems, the output 'status' will be
        set to FALSE in case of failure. In such case the caller
        should look at the output 'volume-errors' to find out in
        which volume snapshot creation failed.
        hen an error occurs, it is possible that some
        snapshots may have been created. If the option cleanup is set to
        TRUE (default), API will attempt to delete these snapshots (but
        snapshot deletion may fail). When set to FALSE, it is users'
        responsibility to delete them. The output array
        volume-snapcreated-list records for each volume, if a snapshot
        has been created or not.
        There are at least two expected use cases for this API.
        The first one is to call this API with the cleanup option set
        to TRUE (default). If the call fails, any successfully created
        snapshots will be deleted before the function returns.
        This is a simple use case, but has the downside that in case
        of a failure, the call may take a long time to return due to
        snapshot cleanup.
        Another use case would be to call this API in a time critical
        environment. In such a scenario, it would be good to reduce
        the impact due to a failure. Hence, it would be better to first
        call the snapshot-multicreate-validate ZAPI, which would reduce
        the likelihood of failure of the snapshot-multicreate API.
        In case a failure does occur, the caller could avoid the cleanup
        delay by setting the cleanup option to FALSE, and performing
        snapshot cleanup later, outside the time-critical window.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume_names: Names of the volumes across which the snapshot is to be created.
                The maximum number of volumes on a cluster system is 1200 (100
                for traditional volumes and 500 for flexible volumes. The number
                is then doubled for a cluster system).
        
        :param snapshot: Name of the snapshot to be created.
                The maximum string length is 256 characters.
        
        :param cleanup: When the API fails, some snapshots may have been created for
                some volumes. When set to TRUE, the API will attempt to delete
                these snapshots.
                Note that newly created snapshots cannot be deleted right away
                until the snapshots are on-disk, which may take up to 10 secs.
                When set to FALSE, newly created snapshots are not deleted.
                Users can delete them later as needed.
                Default is TRUE.
        """
        return self.request( "snapshot-multicreate", {
            'volume_names': [ volume_names, 'volume-names', [ basestring, 'volume-name' ], True ],
            'cleanup': [ cleanup, 'cleanup', [ bool, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'status': [ bool, False ],
            'volume-is-snapcreated-list': [ VolumeIsSnapcreated, True ],
            'volume-errors': [ VolumeError, True ],
        } )
    
    def snapshot_restore_volume(self, volume, snapshot, force=None, snapshot_instance_uuid=None, preserve_lun_ids=None):
        """
        Reverts a volume to a specified snapshot.  The volume
        must be online and must not be a mirror.  If reverting
        the root volume, the filer will be rebooted. Non-root
        volumes do not require a reboot.  A volume cannot have
        both a volume snaprestore and a single-file snaprestore
        executing simultaneously. Multiple single-file snaprestores
        can be in progress simultaneously.  After the reversion,
        the volume is in the same state as it was when the snapshot
        was taken. This operation will fail if the volume being
        restored contains a read-only LUN unless the force option
        is used.
        <p>
        This API is not supported on Infinite Volume.
        
        :param volume: Name of volume to restore.
        
        :param snapshot: Name of snapshot to restore from.
        
        :param force: If this field is set to "true", restore operation will proceed
                even if the volume being restored has a read-only LUN.
                This operation will restore the read-only LUN as well.
                The default value is false.
        
        :param snapshot_instance_uuid: The 128 bit unique snapshot identifier expressed in the form
                of UUID.  This field is optional and can appear together with
                'snapshot' to uniquely identify a snapshot to restore.  If this
                field is provided, 'snapshot' is a required parameter.
                <p>
                An example of an actual UUID is:
                <p>
                84a010ec-3d28-11df-84e8-123478653412
        
        :param preserve_lun_ids: When this field is specified, LUNs in the volume being restored
                will remain mapped and their identities preserved such that
                host connectivity will not be disrupted during the restore
                operation. I/O's to the LUN will be fenced during the restore
                operation by placing the LUNs in an unavailable state.
                Once the restore operation has completed, hosts will be
                able to resume I/O access to the LUNs.
                <p>
                The default value is false.
        """
        return self.request( "snapshot-restore-volume", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'snapshot_instance_uuid': [ snapshot_instance_uuid, 'snapshot-instance-uuid', [ basestring, 'UUID' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
            'preserve_lun_ids': [ preserve_lun_ids, 'preserve-lun-ids', [ bool, 'None' ], False ],
        }, {
        } )
    
    def snapshot_delta_info(self, volume, snapshot1, snapshot2=None):
        """
        Returns the amount of space consumed between two snapshots
        or a snapshot and active filesystem.
        
        :param volume: Name of the volume on which the snapshot delta is to be
                calculated.
        
        :param snapshot1: Name of snapshot to be compared with snapshot2 for space
                consumption calculations.
        
        :param snapshot2: Name of snapshot to be compared with snapshot1 for space
                consumption calculations. If the snapshot is not specified,
                it is assumed to be Active File System.
        """
        return self.request( "snapshot-delta-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot1': [ snapshot1, 'snapshot1', [ basestring, 'None' ], False ],
            'snapshot2': [ snapshot2, 'snapshot2', [ basestring, 'None' ], False ],
        }, {
            'consumed-size': [ int, False ],
            'elapsed-time': [ int, False ],
        } )
    
    def snapshot_exercise_query(self, volume, name):
        """
        auto generated : Exercise the snapshot query (for performance)
        
        :param volume: Volume
        
        :param name: Snapshot
        """
        return self.request( "snapshot-exercise-query", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'name': [ name, 'name', [ basestring, 'snapshot-id' ], False ],
        }, {
        } )
    
    def snapshot_get_schedule(self, volume):
        """
        Obtain the current snapshot schedule on a specified volume.
        Error Returns: Invalid volume name.
        
        :param volume: This the volume name where the snapshots are located.
        """
        return self.request( "snapshot-get-schedule", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'days': [ int, False ],
            'hours': [ int, False ],
            'which-minutes': [ basestring, False ],
            'weeks': [ int, False ],
            'minutes': [ int, False ],
            'which-hours': [ basestring, False ],
        } )
