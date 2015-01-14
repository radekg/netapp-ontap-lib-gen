from netapp.connection import NaConnection
from block_range import BlockRange # 3 properties
from clone_id_info import CloneIdInfo # 2 properties
from ops_info import OpsInfo # 11 properties

class CloneConnection(NaConnection):
    
    def clone_list_status(self, clone_id=None):
        """
        Gets the information of a clone operations identified by
        clone-id. If clone-id is not specified, then it will get the
        status of all running and failed clone operation on the filer.
        It will get the status as 'running', 'failed' or 'completed'.
        User may see some other transient status for the clone
        operation, but any other status should be considered for polling
        clone-list-status again.
        User should keep polling clone-list-status till status returned
        is 'failed' or 'completed'. If status is 'completed', the clone
        operation has been completed successfully. If status is
        'failed', then user is responsible for doing clone-clear to
        clean the status of the clone information.
        When a clone operation is aborted using clone-stop, it may
        take some time to stop the clone operation. User should poll
        clone-list-status till status returned is 'completed'.
        When status returned is 'completed' after clone-stop, the clone
        operation has been stopped successfully.
        This API is deprecated in Data ONTAP 8.1 and later. If a clone-id from a
        previous successful call to clone-start is provided, the operation will always
        be in the "completed" state.
        
        :param clone_id: ID information of the clone operation. If not specified, it will
                get the status of all running and failed clone operations on the
                filer.
        """
        return self.request( "clone-list-status", {
            'clone_id': [ clone_id, 'clone-id', [ CloneIdInfo, 'None' ], False ],
        }, {
            'status': [ OpsInfo, True ],
        } )
    
    def clone_autodelete(self, enable, clone_path, volume=None):
        """
        Set autodelete on a lun clone.
        
        :param enable: If this field is true, autodelete will be allowed to delete
                the clone in try/disrupt mode. and if it is false, autodelete
                will not be allowed to delete the clone in try/disrupt mode.
        
        :param clone_path: Path of the file or the LUN inside the volume. It's relative
                if the volume name is specified otherwise it's absolute.
        
        :param volume: Name of the volume where the clone file or LUN reside.
        """
        return self.request( "clone-autodelete", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'enable': [ enable, 'enable', [ bool, 'None' ], False ],
            'clone_path': [ clone_path, 'clone-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def clone_stop(self, clone_id):
        """
        Stops a running clone operation. If not successful, the error
        code will be returned as API error.
        This API is deprecated in Data ONTAP 8.1 and later,
        and will always fail with EDENSE_CLONE_NOT_RUNNING.
        
        :param clone_id: ID information of the clone operation.
        """
        return self.request( "clone-stop", {
            'clone_id': [ clone_id, 'clone-id', [ CloneIdInfo, 'None' ], False ],
        }, {
        } )
    
    def clone_clear(self, clone_id):
        """
        Clears information of a failed clone operation. If not
        successful, the error code will be returned as API error.
        This API is deprecated in Data ONTAP 8.1 and later,
        and will always fail with EDENSE_CLONE_NOT_RUNNING.
        
        :param clone_id: ID information of the clone operation.
        """
        return self.request( "clone-clear", {
            'clone_id': [ clone_id, 'clone-id', [ CloneIdInfo, 'None' ], False ],
        }, {
        } )
    
    def clone_create(self, volume, source_path, ignore_streams=None, destination_path=None, ignore_locks=None, bypass_license_check=None, qos_policy_group_name=None, block_ranges=None, space_reserve=None, snapshot_name=None, destination_exists=None):
        """
        Create a file/sub file or LUN/sub LUN clone.
        
        :param volume: Name of the volume where the source and destination files or LUNs reside.
        
        :param source_path: Relative path of the source file or the source LUN inside the volume.
        
        :param ignore_streams: Clone only the base file and ignore streams on source or destination.
                By default value is false so streams are also cloned from source and
                existing destination streams are deleted.
        
        :param destination_path: Full path of the Destination file or destination LUN relative to the volume.
                The destination file must be in same volume as "source-path".
                If not specified, a sub-range clone of the source file or LUN
                will be performed onto itself.
                Either "destination-path" or "block-ranges" must be specified.
        
        :param ignore_locks: Clone even if (advisory/mandatory) byte_range locks or share_mode
                locks exist on the source or destination.
                By default value is false.
        
        :param bypass_license_check: If set to 'true', allows clone create without FlexClone
                license. Default value is false.
                THIS INPUT IS CURRENTLY SUPPORTED FOR USE ONLY BY SNAPDRIVE TEAM,
                ANY OTHER USE IS NOT SUPPORTED.
        
        :param qos_policy_group_name: QoS policy group defines measurable Service Level Objectives (SLOs)
                that apply to the storage objects with which the policy group is
                associated. If you do not assign a policy group to a flexclone file,
                the system will not monitor and control the traffic to it.
                This field is available in Data ONTAP 8.2 and later
        
        :param block_ranges: List of block ranges for sub-file/sub-LUN cloning. For sub-LUN
                cloning the block range specified will be considered as SCSI LBA
                range.
                If only one block range is supplied, the source and destination range must not overlap
                and both ranges must not extend past the end of the file
                If multiple block ranges are specified in one operation, the user must ensure all
                source and destination ranges do not overlap, otherwise the result is undefined.
                In case of sub-LUN cloning,
                the API will copy data in case the LBAs are not block
                aligned. If the user provides LBAs such that actual number
                of blocks to be cloned is zero, then API
                will return error.
                The API will fail if the source range overlaps with the
                destination range or if the source and the destination ranges overlap amongst themselves.
                If block range is not provided then the file/LUN cloning is fully cloned.
        
        :param space_reserve: Set the space reservation of the destination clone.
                By default space reservation is inherited from source.
                The API errors out if used in conjunction with block
                range arguments, since space reservations cannot be set
                for a block range.
        
        :param snapshot_name: Snapshot name from which to clone the source file or LUN. If not
                specified, the contents of  the active filesystem will be used.
        
        :param destination_exists: Allow clone creation if the destination exists.
                This will be test only option and hidden.
        """
        return self.request( "clone-create", {
            'ignore_streams': [ ignore_streams, 'ignore-streams', [ bool, 'None' ], False ],
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'ignore_locks': [ ignore_locks, 'ignore-locks', [ bool, 'None' ], False ],
            'bypass_license_check': [ bypass_license_check, 'bypass-license-check', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'qos_policy_group_name': [ qos_policy_group_name, 'qos-policy-group-name', [ basestring, 'None' ], False ],
            'block_ranges': [ block_ranges, 'block-ranges', [ BlockRange, 'None' ], True ],
            'space_reserve': [ space_reserve, 'space-reserve', [ bool, 'None' ], False ],
            'snapshot_name': [ snapshot_name, 'snapshot-name', [ basestring, 'None' ], False ],
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
            'destination_exists': [ destination_exists, 'destination-exists', [ bool, 'None' ], False ],
        }, {
        } )
    
    def clone_start(self, source_path, ignore_streams=None, no_snap=None, ignore_locks=None, destination_path=None, block_ranges=None, space_reserve=None, destination_exists=None, snapshot_name=None, change_log=None):
        """
        In Data ONTAP 8.0 and earlier this API starts a file/LUN or sub-file/sub-LUN clone operation
        asynchronously. If clone operation starts successfully, a
        unique
        clone-id is returned.
        User is supposed to poll clone-list-status specifying clone-id
        to get the status of the clone operation. When
        clone-list-status
        returns status as completed, user can consider that the clone
        operation has been completed successfully. If user gets status
        as failed, user is responsible for doing clone-clear which
        will
        clean the status of the clone operation.
        In Data ONTAP 8.1 and later, this API performs a file/LUN or sub-file/sub-LUN
        clone operation synchronously.  When
        this API returns successfully, the destination file is ready for use.
        
        :param source_path: Full path of the source file or LUN in
                /<volume-name>/file-path format.
        
        :param ignore_streams: Clone only the base file and ignore streams on source or destination.
                By default value is false so streams are also cloned from source and
                existing destination streams are deleted.
        
        :param no_snap: If no-snap is FALSE or unspecified, then a temporary snapshot
                will be taken and source file locked in snapshot will be
                considered for cloning. So that the clone operation does not
                get affected by writes to the source file in parallel to the
                clone operation. User will get atomic point in time copy of
                the source. Irrespective of  clone operation completes
                successfully or unsuccessfully, any temporary snapshot taken
                for cloning will be deleted automatically.
                If no-snap is "true", then the source file in AFS will be
                used for cloning. In this case user may get random data in
                clone if source file is modified while clone operation is in
                progress. This option should only be used when user is assured
                that the source file will remain consistent during the clone
                operation.
                Destination file is not protected against any modification
                while clone operation is in progress. User should use the
                destination file or destination block ranges after clone
                operation is finished.
                In Data ONTAP 8.1 and later, this field is accepted for
                backwards compatibility and is ignored.
        
        :param ignore_locks: Clone even if (advisory/mandatory) byte_range locks or share_mode
                locks exist on the source or destination.
                By default value is false.
        
        :param destination_path: Full path of the Destination file or LUN in
                /<volume-name>/file-path format. Destination
                path should be in same flexible volume as "source-path".
                If not specified, a sub-range clone of the source file or LUN will be performed onto itself.
                Either "destination-path" or "block-ranges" must be specified.
        
        :param block_ranges: List of block ranges for sub-file/sub-LUN cloning. The number of
                block ranges is limited to 32. For sub-LUN cloning the block
                range specified will be considered as SCSI LBA
                range.
                If only one block range is supplied, the source and
                destination range must not overlap
                and both ranges must not extend past the end of the file
                If multiple block ranges are specified in one operation,
                the user must ensure all
                source and destination ranges do not overlap, otherwise the
                result is undefined.
                In case of sub-LUN cloning,
                the API will copy data in case the LBAs are not block
                aligned. If the user provides LBAs such that actual number
                of blocks to be cloned is zero, then API
                will return error.
                The API will fail if the source range overlaps with the
                destination range or if the source and the destination ranges
                overlap amongst themselves.
                If block range is not provided then the file/LUN cloning is fully cloned.
        
        :param space_reserve: Set the space reservation of the destination clone.
                By default space reservation is inherited from source.
                The API errors out if used in conjunction with block
                range arguments, since space reservations cannot be set
                for a block range.
        
        :param destination_exists: Allow clone creation if the destination exists.
                This will be test only option and hidden.
        
        :param snapshot_name: Snapshot name from which to clone the source file or LUN. If not
                specified, the contents of in the active filesystem will be used.
                This field is available in Data ONTAP 8.1 or later
        
        :param change_log: If this option is "true", fingerprints of data blocks of the
                destination file/block ranges created will be change logged to
                the change log file if A-SIS is enabled on the volume.
                With change logging clone operation will be slow, as to get
                fingerprints all the data blocks will be read.
                Without change logging clone operation deals with only indirect
                blocks without reading data blocks. Without change logging,
                fingerprints of the clone blocks are not recorded. The clone
                blocks are shared with the source blocks, but as later the
                source blocks are modified, corresponding clone blocks will no
                longer be shared. If change logging option is not used,
                clone blocks, which could be involved in sharing with rest of
                the file system, can not be shared in next sis operation. The
                only option, in case user had not used change logging while
                creating clone, will be to start sis from beginning using
                "sis start -s" to gather fingerprints of clone blocks.
                In Data ONTAP 8.1 and later, this field is accepted for
                backwards compatibility and is ignored.
        """
        return self.request( "clone-start", {
            'ignore_streams': [ ignore_streams, 'ignore-streams', [ bool, 'None' ], False ],
            'no_snap': [ no_snap, 'no-snap', [ bool, 'None' ], False ],
            'ignore_locks': [ ignore_locks, 'ignore-locks', [ bool, 'None' ], False ],
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'block_ranges': [ block_ranges, 'block-ranges', [ BlockRange, 'None' ], True ],
            'space_reserve': [ space_reserve, 'space-reserve', [ bool, 'None' ], False ],
            'destination_exists': [ destination_exists, 'destination-exists', [ bool, 'None' ], False ],
            'snapshot_name': [ snapshot_name, 'snapshot-name', [ basestring, 'None' ], False ],
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
            'change_log': [ change_log, 'change-log', [ bool, 'None' ], False ],
        }, {
            'clone-id': [ CloneIdInfo, False ],
        } )
