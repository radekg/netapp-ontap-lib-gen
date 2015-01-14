from netapp.connection import NaConnection
from autosize_info import AutosizeInfo # 7 properties
from volume_snapshot_autodelete_attributes import VolumeSnapshotAutodeleteAttributes # 8 properties
from storage_service_info import StorageServiceInfo # 6 properties
from volume_language_attributes import VolumeLanguageAttributes # 6 properties
from guarantee import Guarantee # 1 properties
from volmovecutoveraction import Volmovecutoveraction # 0 properties
from cache_policy import CachePolicy # 0 properties
from raidtype_info import RaidtypeInfo # 1 properties
from junction_path import JunctionPath # 0 properties
from volume_clone_get_iter_key_td import VolumeCloneGetIterKeyTd # 2 properties
from volume_inode_attributes import VolumeInodeAttributes # 6 properties
from volume_64bit_upgrade_info import Volume64BitUpgradeInfo # 1 properties
from volume_move_target_aggr_info import VolumeMoveTargetAggrInfo # 3 properties
from sis_info import SisInfo # 18 properties
from volume_flexcache_attributes import VolumeFlexcacheAttributes # 4 properties
from scrub_detail_info import ScrubDetailInfo # 4 properties
from vol_footprint_info import VolFootprintInfo # 11 properties
from volume_performance_attributes import VolumePerformanceAttributes # 6 properties
from footprint_info import FootprintInfo # 20 properties
from volume_modify_iter_key_td import VolumeModifyIterKeyTd # 2 properties
from volume_space_attributes import VolumeSpaceAttributes # 22 properties
from volume_mirror_attributes import VolumeMirrorAttributes # 6 properties
from vm_align_info import VmAlignInfo # 2 properties
from volume_modify_iter_info import VolumeModifyIterInfo # 3 properties
from volume_64bit_upgrade_check_attributes import Volume64BitUpgradeCheckAttributes # 6 properties
from clone_parent_info import CloneParentInfo # 2 properties
from volume_snapshot_attributes import VolumeSnapshotAttributes # 5 properties
from volume_vm_align_attributes import VolumeVmAlignAttributes # 2 properties
from volume_infinitevol_attributes import VolumeInfinitevolAttributes # 7 properties
from volume_autosize_attributes import VolumeAutosizeAttributes # 9 properties
from space_info import SpaceInfo # 24 properties
from storage_service_name import StorageServiceName # 0 properties
from storage_service_id import StorageServiceId # 0 properties
from volume_modify_iter_async_info import VolumeModifyIterAsyncInfo # 5 properties
from volume_move_info import VolumeMoveInfo # 35 properties
from volume_get_iter_key_td import VolumeGetIterKeyTd # 2 properties
from raidgroup_size_info import RaidgroupSizeInfo # 4 properties
from volume_sis_attributes import VolumeSisAttributes # 9 properties
from volume_clone_attributes import VolumeCloneAttributes # 2 properties
from volume_transition_attributes import VolumeTransitionAttributes # 3 properties
from volume_antivirus_attributes import VolumeAntivirusAttributes # 1 properties
from volume_space_get_iter_key_td import VolumeSpaceGetIterKeyTd # 2 properties
from volume_move_get_iter_key_td import VolumeMoveGetIterKeyTd # 2 properties
from clone_child_info import CloneChildInfo # 1 properties
from transition_info import TransitionInfo # 2 properties
from volume_security_unix_attributes import VolumeSecurityUnixAttributes # 3 properties
from volume_modify_iter_async_key_td import VolumeModifyIterAsyncKeyTd # 2 properties
from volume_move_target_aggr_get_iter_key_td import VolumeMoveTargetAggrGetIterKeyTd # 3 properties
from volume_directory_attributes import VolumeDirectoryAttributes # 3 properties
from compression_info import CompressionInfo # 1 properties
from vol_move_status_info import VolMoveStatusInfo # 11 properties
from volume_option_info import VolumeOptionInfo # 2 properties
from repos_constituent_role import ReposConstituentRole # 0 properties
from volume_transition_volinfo import VolumeTransitionVolinfo # 2 properties
from mediascrub_detail_info import MediascrubDetailInfo # 3 properties
from space_guarantee_enum import SpaceGuaranteeEnum # 0 properties
from volume_storage_service_get_iter_key_td import VolumeStorageServiceGetIterKeyTd # 3 properties
from volume_transition_log_attrs_info import VolumeTransitionLogAttrsInfo # 2 properties
from volume_security_attributes import VolumeSecurityAttributes # 2 properties
from volume_64bit_upgrade_attributes import Volume64BitUpgradeAttributes # 1 properties
from clone_split_detail_info import CloneSplitDetailInfo # 6 properties
from volume_qos_attributes import VolumeQosAttributes # 1 properties
from snap_autodelete_info import SnapAutodeleteInfo # 8 properties
from vol_space_info import VolSpaceInfo # 12 properties
from clone_split_estimate_info import CloneSplitEstimateInfo # 1 properties
from vbn import Vbn # 0 properties
from volume_clone_parent_attributes import VolumeCloneParentAttributes # 6 properties
from volume_footprint_get_iter_key_td import VolumeFootprintGetIterKeyTd # 2 properties
from volume_export_attributes import VolumeExportAttributes # 1 properties
from volume_hybrid_cache_attributes import VolumeHybridCacheAttributes # 2 properties
from volume_attributes import VolumeAttributes # 23 properties
from volume_64bit_upgrade_check_info import Volume64BitUpgradeCheckInfo # 6 properties
from volume_state_attributes import VolumeStateAttributes # 17 properties
from storage_service_type import StorageServiceType # 0 properties
from volume_id_attributes import VolumeIdAttributes # 18 properties
from errors_warnings_info import ErrorsWarningsInfo # 1 properties
from volume_info import VolumeInfo # 59 properties
from volume_transition_log_record_info import VolumeTransitionLogRecordInfo # 7 properties
from volume_clone_info import VolumeCloneInfo # 22 properties

class VolumeConnection(NaConnection):
    
    def volume_clone_split_stop(self, volume):
        """
        Stop the process of splitting off a clone from its
        parent volume and snapshot.  All of the blocks that
        were formerly shared between the given clone and
        its parent volume that have already been split off
        will remain that way.
        This command fails if applied to a traditional
        volume.  Cloning is a new capability that applies
        exclusively to flexible volumes.
        
        :param volume: The name of the clone for which we want to stop the
                process of being split off from its parent volume and
                snapshot.
        """
        return self.request( "volume-clone-split-stop", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_size_async(self, volume_name, new_size=None):
        """
        Given the name of an Infinite Volume, either return its
        current size or set the Infinite Volume's size to the stated
        amount.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: The name of the Infinite Volume.
        
        :param new_size: Specify the Infinite Volume's new size using the
                following format:
                [+|-]&lt number &gt [k|m|g|t|p]
                If a leading '+' or '-' appears, it indicates that the
                given Infinite Volume's size is to be increased or
                decreased (respectively) by the indicated amount, else
                the amount is the absolute size to set.
                The optional trailing 'k', 'm', 'g', 't', and 'p' indicates
                the desired units, namely 'kilobytes', 'megabytes',
                'gigabytes', 'terabytes', and 'petabytes' (respectively).  If the
                trailing unit character doesn't appear, then &lt number &gt
                is interpreted as the number of kilobytes desired.
                The file system size of a readonly Infinite Volume,
                such as a snapmirror destination, is determined from the
                snapmirror source. In such cases, the value set using
                this API is interpreted as an upper limit on the size.
                An Infinite Volume that's not a snapmirror destination which has
                the "fs_size_fixed" option set may have its size displayed,
                but not changed.  Attempting to set the volume size in this
                case will result in failure and a EINTERNALERROR error code.
                Users must be able to adjust readonly snapmirror destination
                Infinite Volume size in order to maintain enough capacity to
                accommodate transfers from the replica source.  Attempting
                to set a readonly snapmirror destination size to be less than
                that of its source will result in a failure indicated by the
                EONTAPI_ENOSPC error code.
                If this input is specified, the size modification occurs
                asynchronously, and the 'volume-size' output is not
                returned to the caller.
                Infinite Volume creation and expansion operations may involve
                creation and initialization of Namespace Mirrors. The initialization
                is started during the creation or expansion operation, but can
                continue after the Infinite Volume operation has completed. When
                this happens, the Infinite Volume will be in a 'mixed' state, until
                the Namespace Mirror initialization is complete. While in a 'mixed'
                further operations of the Infinite Volume are not possible.
                This parameter is not supported on Infinite Volumes that are managed
                by storage services.
        """
        return self.request( "volume-size-async", {
            'new_size': [ new_size, 'new-size', [ basestring, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-status': [ basestring, False ],
            'result-error-code': [ int, False ],
            'volume-size': [ basestring, False ],
        } )
    
    def volume_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of a volume or a group of volume objects.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param query: If modifying a specific volume, this input element must specify
                all keys.
                If modifying volume objects based on query, this input element
                must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching volume
                even when the modification of a previous matching volume fails,
                and do so until the total number of objects failed to be modified
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of volume objects
                (just keys) that were successfully updated.
                If set to false, the list of volume objects modified will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple volume objects match a
                given query.
                If set to true, the API will continue modifying the next matching
                volume even when modification of a previous volume fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of volume objects
                (just keys) that were not modified due to some error.
                If set to false, the list of volume objects not modified will not
                be returned.
                Default: true
        """
        return self.request( "volume-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ VolumeAttributes, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ VolumeAttributes, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ VolumeModifyIterInfo, True ],
            'failure-list': [ VolumeModifyIterInfo, True ],
        } )
    
    def volume_clone_split_estimate(self, volume):
        """
        Display an estimate of additional storage required in the
        underlying aggregate to perform a volume clone split operation.
        This command fails if applied to a traditional volume.
        Cloning is a new capability that applies exclusively
        to flexible volumes.
        
        :param volume: The name of the clone whose split usage is being
                estimated.
        """
        return self.request( "volume-clone-split-estimate", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'clone-split-estimate': [ CloneSplitEstimateInfo, True ],
        } )
    
    def volume_get_language(self, volume):
        """
        Get the given volume's language mapping.
        
        :param volume: Name of the volume for which we want the language
                mapping.
        """
        return self.request( "volume-get-language", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'language-code': [ basestring, False ],
            'nfs-character-set': [ basestring, False ],
            'oem-character-set': [ basestring, False ],
            'language': [ basestring, False ],
        } )
    
    def volume_transition_check(self, source_node, volumes, operation_type=None, override_warnings=None, destination_vserver_name=None, non_disruptive=None):
        """
        Check to see if a desired volume transition can be performed
        from one volume type to another.
        Only 7-mode flexible volume to cluster-mode flexible volume and vice versa
        with limited options are supported at this time.
        
        :param source_node: The name of the node where the target volumes reside.
        
        :param volumes: Volumes to check for the ability to transition to Cluster-Mode.
        
        :param operation_type: The type of transition operation;
        
        :param override_warnings: A 'true' value indicates that all warnings will be ignored as a part of the transition
        
        :param destination_vserver_name: The name of the vserver into which a volume is being transitioned.
        
        :param non_disruptive: A 'true' value indicates that only a non-disruptive transition will be accepted.
        """
        return self.request( "volume-transition-check", {
            'source_node': [ source_node, 'source-node', [ basestring, 'None' ], False ],
            'operation_type': [ operation_type, 'operation-type', [ basestring, 'None' ], False ],
            'override_warnings': [ override_warnings, 'override-warnings', [ bool, 'None' ], False ],
            'destination_vserver_name': [ destination_vserver_name, 'destination-vserver-name', [ basestring, 'None' ], False ],
            'volumes': [ volumes, 'volumes', [ VolumeTransitionVolinfo, 'None' ], True ],
            'non_disruptive': [ non_disruptive, 'non-disruptive', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_clone_split_status(self, volume=None):
        """
        Display the progress in separating clones from their
        underlying parent volumes and snapshots.  If a clone
        name is specified, then the split status for that
        clone is provided.  If no clone name is provided, then
        status is provided for all clones currently being
        split.
        This command fails if applied to a traditional volume,
        and EONTAPI_EVOLNOTFLEX is thrown.  Cloning is a
        capability that applies exclusively to flexible volumes.
        This command fails if the volume specified is not a
        clone, and EVOLNOTCLONE is thrown.
        This command fails if the volume specified is not being
        split, and EVOLOPNOTUNDERWAY is thrown.
        
        :param volume: The name of the clone being split off from its parent
                volume and snapshot for which we want status.
        """
        return self.request( "volume-clone-split-status", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'clone-split-details': [ CloneSplitDetailInfo, True ],
        } )
    
    def volume_create(self, disk_size=None, is_nvfail_enabled=None, containing_aggr_name=None, volume_raid_type=None, raid_size=None, qos_policy_group_name=None, volume_state=None, unix_permissions=None, junction_path=None, antivirus_on_access_policy=None, size=None, percentage_snapshot_reserve=None, is_snaplock=None, stripe_width=None, stripe_optimize=None, snapshot_policy=None, stripe_constituent_volume_count=None, user_id=None, volume_type=None, max_dir_size=None, disk_size_with_unit=None, language_code=None, storage_service=None, stripe_algorithm=None, flexcache_fill_policy=None, max_write_alloc_blocks=None, snaplock_type=None, constituent_role=None, volume=None, is_junction_active=None, flexcache_cache_policy=None, mirror_disks=None, remote_location=None, stripe_concurrency=None, export_policy=None, group_id=None, volume_comment=None, disks=None, vm_align_suffix=None, flexcache_origin_volume_name=None, is_vserver_root=None, volume_security_style=None, is_mirrored=None, vm_align_sector=None, space_reserve=None, force=None, disk_count=None):
        """
        Create a volume.
        <p>
        The detailed behavior of this API depends on
        where it is received:
        <p>
        1. In Data ONTAP Cluster-Mode, create a new
        flexible volume.
        <p>
        2. In Data ONTAP 7-Mode, create a new flexible,
        traditional, or sparse volume with the given
        name and characteristics. Freshly-created
        traditional volumes may not be operational
        immediately after the API returns.  Use
        'volume-list-info' to obtain information about
        volumes, including the status of the newly-created
        traditional volume in order to determine
        when it is fully operational.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param disk_size: <b>Traditional</b> volumes only.
                Disk size in 4KB blocks.  Disks that are within 20% of the
                specified size will be selected for use	in the
                traditional volume.  If neither "disk-size"
                nor "disk-size-with-unit" is specified, existing
                groups are appended with disks that are the best
                match for the largest disk in the group.  When
                starting new groups, the smallest disks are
                selected first.  This option is ignored if a
                specific list of disks to use is specified through
                the "disks" parameter.
                Range [0..2^31-1].
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear,
                an error message will be returned.
        
        :param is_nvfail_enabled: If true, the controller performs additional work at boot
                and takeover times if it finds that there has been any
                potential data loss in this volume due to an NVRAM
                failure.
                <p>
                For 7-Mode volumes, it causes the invalidation of all NFS
                file handles on all volumes affected by the problem so
                that client-side users are forced to remount the affected
                file system (and thus not continue to use potentially
                incorrect data).
                <p>
                It is also possible to specify a set of files per volume
                that are to be renamed out of the way in these cases.
                The controller sends error messages to the console
                whenever such problems are found.
                <p>
                For Cluster-Mode volumes, the volume would be put in a
                special state called 'in-nvfailed-state' such that
                protocol access is blocked. This will cause the client
                applications to crash and thus prevent access to stale
                data on the volume.
                <p>
                To get out of this situation, the admin needs to manually
                clear the 'in-nvfailed-state' on the volume.
                <p>
                By default, this value is false.
        
        :param containing_aggr_name: <b>Flexible</b> volumes only.
                The name of the aggregate in which to create the new
                flexible volume.  If provided, this argument must be
                accompanied by the "size" parameter described below.
                <p>
                This input is required for creating a Cluster-Mode volume.
        
        :param volume_raid_type: <b>Traditional</b> volumes only.
                Specifies the type of RAID groups to use in the new
                traditional volume.  The default is "raid4" on most
                platforms.   Possible values: raid4, raid_dp.
        
        :param raid_size: <b>Traditional</b> volumes only.
                Specifies the maximum number of disks in each RAID
                group in the traditional volume.  The maximum value
                for this parameter is of raidsize is 28.  The default
                value is platform-dependent.  The valid	range of
                values is also platform-dependent, but never wider
                than [2..28].
        
        :param qos_policy_group_name: The QoS Policy Group Name that is to be associated with this
                volume in order to enforce Service Level Objectives (SLO).
                If you do not assign a QoS policy group to a volume,
                the system will not monitor and control the traffic to it.
                NOTE: "none" is a reserved keyword for deleting the
                association of the volume with a QoS policy group. Specifying
                "none" as a the QoS policy group during volume creation will
                have no effect. This parameter is not supported on Infinite Volumes.
        
        :param volume_state: Desired state of the volume after it is created.
                <p>
                Possible values:
                <ul>
                <li> 'online',
                <li> 'restricted',
                <li> 'offline'
                </ul>
        
        :param unix_permissions: Unix permission bits in octal string format.
                <p>
                It's similar to Unix style permission bits:
                <p>
                In Data ONTAP 7-mode, the default setting of '0755' gives
                read/write/execute permissions to owner and read/execute
                to group and other users.
                <p>
                In Data ONTAP Cluster-Mode, for security style "mixed" or "unix",
                the default setting of '0755' gives read/write/execute permissions
                to owner and read/execute permissions to group and other users. For
                security style "ntfs", the default setting of '0000' gives no permissions
                to owner, group and other users.
                <p>
                It consists of 4 octal digits derived by adding up bits
                4, 2 and 1. Omitted digits are assumed to be zeros. First
                digit selects the set user ID(4), set group ID (2) and
                sticky (1) attributes. The second digit selects
                permission for the owner of the file: read (4), write (2)
                and execute (1); the third selects permissions for other
                users in the same group; the fourth for other users not
                in the group.
        
        :param junction_path: The Junction Path at which this volume is to be mounted.
                <p>
                The fully-qualified pathname in the owning Vserver's namespace at
                which a volume is mounted.  The pathname is case insensitive and
                must be unique within a Vserver's namespace. Note that this pathname
                may itself contain junctions, one for each volume (other than the
                namespace root volume) that provides storage along the pathname's
                length. As with all fully-qualified pathnames , this string must begin
                with '/'.  In addition, it must not end with '/'.
                <p>
                An example of a valid junction path is: '/user/my_volume'.
                <p>
                Only one volume can be mounted at any given junction path.
                If an incorrect junction path is specified,
                EINVALIDINPUTERROR is returned. If another
                volume is mounted at the specified junction path,
                EVOLALREADYMOUNTED is returned.
        
        :param antivirus_on_access_policy: {Deprecated, this field does not have any effect on the operation
                of the volume.} The name of the Anti-Virus On-Access policy.
                The default policy name is 'default'.
                <p>
                If not specified when creating a volume, the Anti-Virus
                On-Access Policy is inherited from the owning Vserver.
                Currently, this policy can only be managed using the
                'antivirus' command line interfaces.
        
        :param size: <b>Flexible</b> volumes only.
                The initial size of the new flexible volume.  The
                format to use is:
                &lt number &gt k|m|g|t
                where "k" means kilobytes, "m" means megabytes,
                "g" means gigabytes, and "t" means terabytes.  If
                the trailing unit character doesn't appear, then
                &lt number &gt is interpreted as the number of bytes
                desired. If provided, this argument must be accompanied
                by the "containing-aggr-name" parameter described above.
        
        :param percentage_snapshot_reserve: The percentage of disk space that has to be set aside as reserve
                for snapshot usage. The default value is 5.
                Range : [0..90]
                <p>
                If this argument is not specified for the creation of
                constituents of an Infinite Volume that does not support
                storage services, the default reserve is the reserve of
                the Infinite Volume.
        
        :param is_snaplock: Specifies the creation of a SnapLock volume.
                By default, is-snaplock is not specified.
                When is-snaplock is "true" the type of snaplock volume is
                determined in the following way -
                1> If snaplock-type is set, create the type specified in
                snaplock-type (see snaplock-type for more details)
                2> Otherwise, create a Snaplock enterprise volume
                if a Snaplock enterprise license has been installed.
                3> Otherwise, create a Snaplock compliance volume.
                ESERVICENOTLICENSED is returned if the required Snaplock
                Compliance or Enterprise license is not installed.
                EONTAPI_EWORMNOCLOCK is returned if SnapLock
                Compliance Clock is not running.
                If you need to create a snaplock volume, the suggested
                method is to specify snaplock-type as "compliance" or
                "enterprise" and not specify is-snaplock at all.
                If you want to create a non-snaplock volume, the
                suggested method is to specify neither snaplock-type nor
                is-snaplock.
        
        :param stripe_width: The size of a stripe in bytes. Increases can be made in
                4KB increments. The default is 64 MBytes.
        
        :param stripe_optimize: Optimization Policy for striped volumes.
                <p>
                Possible values:
                <ul>
                <li> 'max_performance' ... Guarantees best performance
                even if doing so might result
                in less free space being
                available,
                <li> 'performance'     ... Provides best performance
                until free space becomes low;
                then lowers performance in
                order to maximize free space
                (default setting),
                <li> 'space'           ... Balances good performance
                with moderate constraints to
                ensure that free space is
                not wasted,
                <li> 'max_space'       ... Ensures data consumes as
                little space as possible, even
                if doing so slightly
                reduces performance
                </ul>
        
        :param snapshot_policy: The name of the snapshot policy.
                <p>
                The default policy name is 'default'.
                <p>
                This policy can be created using the
                'snapshot-policy-create' API. It can be managed using the
                'snapshot-policy-*' APIs.
        
        :param stripe_constituent_volume_count: The number of constituent volumes in the collective
                striped volume. The default setting is equal to the
                number of striped constituent aggregates.
        
        :param user_id: The UNIX user ID for the volume. The default value
                is 0 ('root').
        
        :param volume_type: The type of the volume to be created.
                Possible values:
                <ul>
                <ul> "rw"   - read-write volume (default setting),
                <ul> "ls"   - load-sharing volume,
                <ul> "dp"   - data-protection volume,
                <ul> "dc"   - data-cache volume (FlexCache)
                </ul>
        
        :param max_dir_size: The maximum size (in bytes) to which any directory in
                this volume can grow.
                <p>
                For 7-Mode volumes, the default setting of 10240 limits
                directory size to 10 MBytes and allows it to hold up to
                approximately 300,000 files. For Cluster-Mode volumes,
                the default setting is 100 MBytes and it allows the
                directory to hold up to approximately 3,000,000 files.
                The number of files that the directory actually can hold
                varies depending on such things as the length of the
                names and whether it needs to use double-byte UNICODE
                characters.
                <p>
                Most users should not need to change this field's default
                setting. It is useful for environments where system users
                may grow a directory to a size that starts impacting
                system performance.  When a user tries to create a file
                in a directory that is at the limit, the system returns a
                ENOSPC error and fails the create.
        
        :param disk_size_with_unit: <b>Traditional</b> volumes only.
                Disk size in the specified unit. It is a positive integer
                number followed by unit of "T", "G", "M" or "K".
                This option is ignored if a
                specific list of disks to use is specified through
                the "disks" parameter.
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear, an error
                message will be returned.
        
        :param language_code: Specifies the language to use for the new volume via
                a language code.   The default language is the one
                used by the filer's root volume.  Available language
                codes are:
                <ul>
                <li> 'C'            ... POSIX,
                <li> 'ar'           ... Arabic,
                <li> 'cs'           ... Czech,
                <li> 'da'           ... Danish,
                <li> 'de'           ... German,
                <li> 'en'           ... English,
                <li> 'en_US'        ... English (US),
                <li> 'es'           ... Spanish,
                <li> 'fi'           ... Finnish,
                <li> 'fr'           ... French,
                <li> 'he'           ... Hebrew,
                <li> 'hr'           ... Croatian,
                <li> 'hu'           ... Hungarian,
                <li> 'it'           ... Italian,
                <li> 'ja'           ... Japanese euc-j*,
                <li> 'ja_v1'        ... Japanese euc-j,
                <li> 'ja_JP.PCK'    ... Japanese PCK (sjis)*,
                <li> 'ja_JP.932'    ... Japanese cp932*,
                <li> 'ja_JP.PCK_v2' ... Japanese PCK (sjis),
                <li> 'ko'           ... Korean,
                <li> 'no'           ... Norwegian,
                <li> 'nl'           ... Dutch,
                <li> 'pl'           ... Polish,
                <li> 'pt'           ... Portuguese,
                <li> 'ro'           ... Romanian,
                <li> 'ru'           ... Russian,
                <li> 'sk'           ... Slovak,
                <li> 'sl'           ... Slovenian,
                <li> 'sv'           ... Swedish,
                <li> 'tr'           ... Turkish,
                <li> 'zh'           ... Simplified Chinese,
                <li> 'zh.GBK'       ... Simplified Chinese (GBK),
                <li> 'zh_TW'        ... Traditional Chinese euc-tw,
                <li> 'zh_TW.BIG5'   ... Traditional Chinese Big 5
                </ul>
                <p>
                To use UTF-8 as the NFS character set, append '.UTF-8' to the
                language code.
        
        :param storage_service: Name of the storage service with which to associate the
                creation of a constituent of an Infinite Volume.
                <p>
                This argument is required for the creation of constituents
                of an Infinite Volume that supports storage services. If
                the storage service does not exist before creating the
                constituent, it will be automatically created. Clients
                can query for the 'is-managed-by-service' field to
                determine if an Infinite Volume supports storage services.
                <p>
                This argument is not supported for Flexible Volumes.
        
        :param stripe_algorithm: Indicates the striping algorithm in force. This is
                applicable only for striped volumes.
                <p>
                Possible values:
                <ul>
                <li> 'roundrobin' ... Original algorithm for
                data-only striping,
                <li> 'data'       ... Data-only striping,
                <li> 'full'       ... Full striping (data and
                metadata). This is the
                default setting.
                </ul>
        
        :param flexcache_fill_policy: The name of the FlexCache prefill policy.
                <p>
                The default policy name is 'default'.
                <p>
                This policy applies only to FlexCache volumes and can be
                created using the 'flexcache-fill-policy-create' API.
        
        :param max_write_alloc_blocks: The maximum number of blocks used for write allocation.
                <p>
                This feature is deprecated.
        
        :param snaplock_type: Specifies the type of Snaplock volume to be
                created.
                Possible values - "compliance" or "enterprise"
                ESERVICENOTLICENSED is returned if the necessary Snaplock
                compliance or enterprise license has not been installed.
                EINVALIDINPUT is returned if snaplock-type has an illegal
                value or if is-snaplock has been set to "false".
                EONTAPI_EWORMNOCLOCK is returned if SnapLock
                Compliance Clock is not running.
        
        :param constituent_role: This field specifies the role of a constituent within an
                Infinite Volume. This field is only supported for Infinite
                Volume constituents and this API will fail if no value is passed
                for an Infinite Volume constituent.
                <p>
                Possible values:
                <ul>
                <li> 'namespace' ... namespace constituent,
                <li> 'data' ... data constituent,
                <li> 'ns_mirror' ... namespace mirror constituent
                </ul>
        
        :param volume: Name of the volume to create.  The volume name can
                contain letters, numbers, and the underscore character
                (_), but the first character must be a letter or an
                underscore. In Data ONTAP Cluster-Mode, the volume names
                must be unique within a Vserver. In Data ONTAP 7-mode,
                the volume names must be unique on a controller. For
                an Infinite Volume constituent, the parameter is optional;
                if a name is not specified, DATA ONTAP will generate the
                correct name based on the constituent type.
        
        :param is_junction_active: This field indicates whether the mounted volume is
                accessible. The default is true. If the mounted junction
                path is not accessible, the volume does not appear in the
                owning Vserver's namespace. This field applies
                only to Cluster-Mode volumes.
        
        :param flexcache_cache_policy: The name of the FlexCache cache policy.
                <p>
                The default policy name is 'default'.
                <p>
                This policy applies only to FlexCache volumes and can be
                created using the 'flexcache-cache-policy-create' API.
        
        :param mirror_disks: <b>Traditional</b> volumes only.
                List of mirror disks to use.  It must contain the
                same number of disks specified in "disks".
        
        :param remote_location: Specifies the remote host and volume name for the origin
                of the FlexCache. A FlexCache license is necessary for
                this option to be utilized. The default action is not to
                create a FlexCache Volume.
                Format: <Remote-Host>:<Remote-Volume>
                Create a sparse volume as a FlexCache for the given
                remote host and remote volume name.
                Remote Host: Should be formatted as either the DNS hostname
                or as an IP address.
                Remote Volume: Should be formatted the same as a volume
                name.
                ESERVICENOTLICENSED is returned if the FlexCache service
                is not licensed.
                EINVALIDINPUT is returned if the host, or source volume
                is found to be invalid.
        
        :param stripe_concurrency: Concurrency level for striped volumes.
                <p>
                Possible values:
                <ul>
                <li> 'low'    ... Maximum compatibility in exchange
                for significant performance loss,
                <li> 'medium' ... Excellent client compatibility, but
                noticeable performance loss,
                <li> 'high'   ... Good level of compatibility with a
                small performance loss (default setting),
                <li> 'peak'   ... Maximum performance; some
                applications may observe file-timestamp
                anomalies
                </ul>
        
        :param export_policy: The name of the Export Policy to be used by NFS/CIFS
                protocols. The default policy name is 'default'.
        
        :param group_id: The UNIX group ID for the volume.  The default value
                is 0 ('root').
        
        :param volume_comment: A description for the volume being created. Range:[0..1023]
        
        :param disks: <b>Traditional</b> volumes only.
                Specific list of disks to use for the new volume.
                If "mirrored" is set to true and a specific list
                of disks is supplied, the "mirror-disks" list with
                the same number of disks must also be supplied.
                Either "disk-count" or "disks" must be supplied
                when creating traditional volumes.
        
        :param vm_align_suffix: The Virtual Machine alignment suffix. The suffix such as
                '.xyz' is used to identify the files which needs to be aligned.
                This element  can only be specified if the vm-align-sector
                input element is also specified. See the description
                for 'vm-align-sector' above for more information on this.
        
        :param flexcache_origin_volume_name: The name of the origin volume that contains the
                authoritative data. This field is valid only for a
                FlexCache volume. The origin volume must belong to the
                same Vserver that owns this volume.
        
        :param is_vserver_root: If true, this volume is the
                namespace root volume of the Vserver which owns this
                volume. The default value is false.
                <p>
                When creating a volume, if this field is set to true, the
                new volume is to become the new namespace root volume of
                the Vserver. This field can be used in a recovery
                scenario in which the namespace root volume of the
                Vserver becomes unrecoverable.
        
        :param volume_security_style: The security style associated with this volume.
                <p>
                Possible values:
                <ul>
                <li> 'mixed' ... Mixed-style security,
                <li> 'ntfs'  ... NTFS/Windows-style security,
                <li> 'unified'  .Unified-style security, Unified UNIX, NFS and CIFS permissions (default for Infinite Volume)
                <li> 'unix'  ... Unix-style security (default for Flexible Volume)
                </ul>
                <p>
                Security styles don't apply to GX-striped data volumes.
                Infinite Volumes can only use the 'unified' security style.
                All other volumes cannot use the 'unified' security style.
        
        :param is_mirrored: <b>Traditional</b> volumes only.
                Specifies that the new traditional volume be
                mirrored (have two plexes).  If set to "true",
                then the indicated disks will be split across the
                two plexes.  By default, the new volume will not
                be mirrored.
        
        :param vm_align_sector: The Virtual Machine alignment 512 byte sector number.
                All files created with the suffix specified in the
                'vm-align-suffix' input parameter will have zero-filled
                <512 * 'vm-align-sector'> bytes data at the beginning so that
                it's actual data starts at a different offset instead of zero.
                This is done so that the read & writes to such files are
                aligned to WAFL's 4k block boundary.
        
        :param space_reserve: Specifies the type of volume guarantee the new volume
                will use.  Possible values: none, file, volume.  If
                this argument is not provided, the default volume guarantee
                type is volume.
                <p>
                If this argument is not specified for the creation of
                constituents of an Infinite Volume that does not support
                storage services, the default guarantee is the guarantee
                of the Infinite Volume.
        
        :param force: <b>Traditional</b> volumes only.
                Disks in a plex are not normally permitted to span
                spare pools.  This behavior is overridden with this
                option when it is set to "true".
        
        :param disk_count: <b>Traditional</b> volumes only.
                Number of disks to place into the new traditional
                volume, including the parity disks.  The disks in
                this newly-created traditional volume come from the
                spare disk pool.  The smallest disks in this pool
                join the traditional volume first, unless the
                "disk-size" argument is specified.  Either
                "disk-count" or "disks" must be supplied for
                traditional volumes.
                Range [0..2^31-1].
        """
        return self.request( "volume-create", {
            'disk_size': [ disk_size, 'disk-size', [ int, 'None' ], False ],
            'is_nvfail_enabled': [ is_nvfail_enabled, 'is-nvfail-enabled', [ basestring, 'None' ], False ],
            'containing_aggr_name': [ containing_aggr_name, 'containing-aggr-name', [ basestring, 'None' ], False ],
            'volume_raid_type': [ volume_raid_type, 'volume-raid-type', [ basestring, 'None' ], False ],
            'raid_size': [ raid_size, 'raid-size', [ int, 'None' ], False ],
            'qos_policy_group_name': [ qos_policy_group_name, 'qos-policy-group-name', [ basestring, 'None' ], False ],
            'volume_state': [ volume_state, 'volume-state', [ basestring, 'None' ], False ],
            'unix_permissions': [ unix_permissions, 'unix-permissions', [ basestring, 'None' ], False ],
            'junction_path': [ junction_path, 'junction-path', [ basestring, 'None' ], False ],
            'antivirus_on_access_policy': [ antivirus_on_access_policy, 'antivirus-on-access-policy', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ basestring, 'None' ], False ],
            'percentage_snapshot_reserve': [ percentage_snapshot_reserve, 'percentage-snapshot-reserve', [ int, 'None' ], False ],
            'is_snaplock': [ is_snaplock, 'is-snaplock', [ bool, 'None' ], False ],
            'stripe_width': [ stripe_width, 'stripe-width', [ int, 'None' ], False ],
            'stripe_optimize': [ stripe_optimize, 'stripe-optimize', [ basestring, 'None' ], False ],
            'snapshot_policy': [ snapshot_policy, 'snapshot-policy', [ basestring, 'None' ], False ],
            'stripe_constituent_volume_count': [ stripe_constituent_volume_count, 'stripe-constituent-volume-count', [ int, 'None' ], False ],
            'user_id': [ user_id, 'user-id', [ int, 'None' ], False ],
            'volume_type': [ volume_type, 'volume-type', [ basestring, 'None' ], False ],
            'max_dir_size': [ max_dir_size, 'max-dir-size', [ int, 'None' ], False ],
            'disk_size_with_unit': [ disk_size_with_unit, 'disk-size-with-unit', [ basestring, 'None' ], False ],
            'language_code': [ language_code, 'language-code', [ basestring, 'None' ], False ],
            'storage_service': [ storage_service, 'storage-service', [ basestring, 'None' ], False ],
            'stripe_algorithm': [ stripe_algorithm, 'stripe-algorithm', [ basestring, 'None' ], False ],
            'flexcache_fill_policy': [ flexcache_fill_policy, 'flexcache-fill-policy', [ basestring, 'None' ], False ],
            'max_write_alloc_blocks': [ max_write_alloc_blocks, 'max-write-alloc-blocks', [ int, 'None' ], False ],
            'snaplock_type': [ snaplock_type, 'snaplock-type', [ basestring, 'None' ], False ],
            'constituent_role': [ constituent_role, 'constituent-role', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'is_junction_active': [ is_junction_active, 'is-junction-active', [ bool, 'None' ], False ],
            'flexcache_cache_policy': [ flexcache_cache_policy, 'flexcache-cache-policy', [ basestring, 'None' ], False ],
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'remote_location': [ remote_location, 'remote-location', [ basestring, 'None' ], False ],
            'stripe_concurrency': [ stripe_concurrency, 'stripe-concurrency', [ basestring, 'None' ], False ],
            'export_policy': [ export_policy, 'export-policy', [ basestring, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
            'volume_comment': [ volume_comment, 'volume-comment', [ basestring, 'None' ], False ],
            'disks': [ disks, 'disks', [ DiskInfo, 'None' ], True ],
            'vm_align_suffix': [ vm_align_suffix, 'vm-align-suffix', [ basestring, 'None' ], False ],
            'flexcache_origin_volume_name': [ flexcache_origin_volume_name, 'flexcache-origin-volume-name', [ basestring, 'None' ], False ],
            'is_vserver_root': [ is_vserver_root, 'is-vserver-root', [ bool, 'None' ], False ],
            'volume_security_style': [ volume_security_style, 'volume-security-style', [ basestring, 'None' ], False ],
            'is_mirrored': [ is_mirrored, 'is-mirrored', [ bool, 'None' ], False ],
            'vm_align_sector': [ vm_align_sector, 'vm-align-sector', [ int, 'None' ], False ],
            'space_reserve': [ space_reserve, 'space-reserve', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'disk_count': [ disk_count, 'disk-count', [ int, 'None' ], False ],
        }, {
            'bad-disks': [ DiskInfo, True ],
        } )
    
    def volume_scrub_resume(self, name=None):
        """
        Resume RAID parity scrubbing on the named traditional
        volume, plex, or RAID group.  If no name is given,
        then resume scrubbing on all RAID groups for which
        it is suspended.
        
        :param name: Name of the existing traditional volume, plex, or
                RAID group for which the scrubbing is to resume.
        """
        return self.request( "volume-scrub-resume", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_options_list_info(self, volume):
        """
        Get the options that have been set for the specified
        volume.
        
        :param volume: Name of the existing volume for which we want option
                information.
        """
        return self.request( "volume-options-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'options': [ VolumeOptionInfo, True ],
        } )
    
    def volume_space_list_info(self, volume=None):
        """
        Return a list of volumes and a breakdown of their space usage.
        This information is only available for online volumes. If no
        volume is specified, status is displayed for all online volumes
        on the filer. Note that if space status information for more
        than 20 volumes is desired, the volume-space-list-info-iter-*
        ZAPIs will be more efficient and should be used instead.
        
        :param volume: The name of the volume for which we want status
                information.  If not supplied, then we want status
                for all volumes on the filer.
        """
        return self.request( "volume-space-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'vol-space-infos': [ VolSpaceInfo, True ],
        } )
    
    def volume_mediascrub_list_info(self, volume=None):
        """
        Get the RAID media scrubbing status on the named
        traditional volume, plex, or RAID group.  If no
        name is given, then status is provided for all
        RAID groups currently undergoing media scrubbing.
        
        :param volume: Name of traditional volume, plex or RAID group for
                which media scrub status is desired.  If no name
                is given, then status is provided for all RAID
                groups currently undergoing media scrubbing.
        """
        return self.request( "volume-mediascrub-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'mediascrub-details': [ MediascrubDetailInfo, True ],
        } )
    
    def volume_restrict_async(self, volume_name):
        """
        Restrict the specified Infinite Volume
        making it unavailable for data access.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: Name of an existing Infinite Volume.
        """
        return self.request( "volume-restrict-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_unmount(self, volume_name, force=None):
        """
        Unmount a volume from its parent volume and delete the junction
        path at which the volume is mounted.  This API is not supported
        on Infinite Volume constituents.
        
        :param volume_name: The name of the volume.
        
        :param force: This specifies whether the volume unmount operation is forced or
                not. The default value is false.
                <p>
                Under certain circumstances, such as an unexpected reboot while
                in the middle of unmounting, the unmount operation might find
                that after the reboot, it is unable to delete the junction path
                at which the volume is mounted in the file system. In this
                situation, if the force option is set to false, the unmount
                operation is failed (EJUNCTIONDELETEFAILED), leaving the junction
                path information intact in the Volume Management Database.
                Instead, if the force option is set to true, the unmount
                operation proceeds to delete the junction path information in the
                Volume Management Database, irrespective of any failure to delete
                the junction path in the file system.
        """
        return self.request( "volume-unmount", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_get_filer_info(self):
        """
        Get information on what possibilities and parameters
        exist for volumes on a given filer.
        """
        return self.request( "volume-get-filer-info", {
        }, {
            'disk-types': [ basestring, False ],
            'default-raidtype': [ basestring, False ],
            'checksum-types': [ basestring, False ],
            'root-volume': [ basestring, False ],
            'raidgroup-size': [ RaidgroupSizeInfo, True ],
            'allowed-raidtypes': [ RaidtypeInfo, True ],
            'snapshots-max': [ int, False ],
        } )
    
    def volume_split(self, new_volume_name, plex):
        """
        Remove the specified plex from a mirrored traditional
        volume and create a new unmirrored traditional volume
        with the specified name that contains the split-off
        plex.  The original mirrored traditional volume becomes
        unmirrored.  The plex to be split from the original
        traditional volume must be functional (not partial),
        but it could be inactive, resyncing, or out-of-date.
        A 'volume-split' operation can therefore be used to
        gain access to a plex that is not up to date with
        respect to its partner plex if its partner plex is
        currently failed.  If the plex is offline at the time
        of the split, the resulting traditional volume will
        also be offline. Otherwise,  the resulting traditional
        volume will be in the same online/offline/restricted
        state as the original traditional volume.  Note that
        a split mirror can be joined back together via the
        "victim-volume" option to "volume-mirror".
        
        :param new_volume_name: Name of the new traditional volume to create from the
                split plex.
        
        :param plex: Name of the plex to split out of its traditional volume.
        """
        return self.request( "volume-split", {
            'new_volume_name': [ new_volume_name, 'new-volume-name', [ basestring, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_create_async(self, volume_name, is_nvfail_enabled=None, max_data_constituent_size=None, volume_state=None, junction_path=None, unix_permissions=None, size=None, snapshot_policy=None, user_id=None, namespace_aggregate=None, max_dir_size=None, storage_service=None, is_managed_by_service=None, max_namespace_constituent_size=None, space_guarantee=None, data_aggr_list=None, export_policy=None, group_id=None, volume_type=None, namespace_mirror_aggr_list=None, volume_security_style=None, enable_snapdiff=None):
        """
        Create an Infinite Volume. This API will select one aggregate from
        the aggregates assigned to the VServer to create the namespace
        constituent. The remaining assigned aggregates will be used
        for data constituents. You must have the
        aggregates and the Vserver with Infinite Volume created, as well as assigned the
        aggregates to the Vserver.
        Infinite Volume creation and expansion operations may involve
        creation and initialization of Namespace Mirrors.  The initialization
        is started during the creation or expansion operation, but can
        continue after the Infinite Volume operation has completed. When
        this happens, the Infinite Volume will be in a 'mixed' state, until
        the Namespace Mirror initialization is complete. While in a 'mixed'
        state, further operations of the Infinite Volume are not possible.
        This API is not supported for Flexible Volumes.
        
        :param volume_name: Name of the Infinite Volume to create.  The name can
                contain letters, numbers, and the underscore character
                (_), but the first character must be a letter or an
                underscore.
        
        :param is_nvfail_enabled: If true, the controller performs additional work at boot
                and takeover times if it finds that there has been any
                potential data loss in the Infinite Volume constituents due to
                an NVRAM  failure.
                <p>
                The Infinite Volume constituents would be put in a
                special state called 'in-nvfailed-state' such that
                protocol access is blocked. This will cause the client
                applications to crash and thus prevent access to stale
                data.
                <p>
                To get out of this situation, the admin needs to manually
                clear the 'in-nvfailed-state' on the Infinite Volume constituents.
                <p>
                By default, this value is true.
        
        :param max_data_constituent_size: The maximum size of each data constituent in bytes.  The default value
                is determined by checking the maximum FlexVol size setting on all nodes
                used by the Infinite Volume. The smallest value found is chosen as
                the default for the max-data-constituent-size for the Infinite Volume.
        
        :param volume_state: Desired state of the Infinite Volume after it is created.
                <p>
                Possible values:
                <ul>
                <li> 'online' (default for Infinite Volumes),
                <li> 'restricted',
                <li> 'offline'
                </ul>
        
        :param junction_path: The Junction Path at which the Infinite Volume is to be mounted.
                <p>
                The fully-qualified pathname in the owning Vserver's namespace
                at which the Infinite Volume is mounted.  The pathname is case
                insensitive. This string must begin with '/'.  In addition, it
                must not end with '/', and may only have one element.
                <p>
                An example of a valid junction path is: '/My_InfiniteVolume'. The
                path '/My_InfiniteVolume/dir' is invalid, as it has two elements.
                <p>
                Only one Infinite Volume can be mounted at any given junction path.
                If an incorrect junction path is specified,
                EINVALIDINPUTERROR is returned. If another
                Infinite Volume is mounted at the specified junction path,
                EVOLALREADYMOUNTED is returned.
                <p>
                If the junction-path is not specified, the Infinite Volume is
                mounted at /NS.
        
        :param unix_permissions: Unix permission bits in octal string format.
                <p>
                It's similar to Unix style permission bits:
                <p>
                The default setting of '0755' gives read/write/execute
                permissions to owner and read/execute permissions to group
                and other users.
                <p>
                It consists of 4 octal digits derived by adding up bits
                4, 2 and 1. Omitted digits are assumed to be zeros. First
                digit selects the set user ID(4), set group ID (2) and
                sticky (1) attributes. The second digit selects
                permission for the owner of the file: read (4), write (2)
                and execute (1); the third selects permissions for other
                users in the same group; the fourth for other users not
                in the group.
        
        :param size: The initial size of the Infinite Volume in bytes. If size is
                not specified, then it will use the system default which
                is the number of constituents times the FlexVol default
                size.
        
        :param snapshot_policy: The name of the snapshot policy.
                <p>
                This policy can be created using the
                'snapshot-policy-create' API. It can be managed using the
                'snapshot-policy-*' APIs.
                <p>
                The default policy name is 'default-1weekly'.
        
        :param user_id: The UNIX user ID for the Infinite Volume. The default value
                is 0.
        
        :param namespace_aggregate: The name of the aggregate in which to create the namespace
                constituent. If not provided, ONTAP will pick the best
                available aggregate assigned to the Vserver.
        
        :param max_dir_size: The maximum size (in bytes) to which any directory in
                the Infinite Volume namespace can grow.
                <p>
                Most users should not need to change this field's default
                setting. It is useful for environments where system users
                may grow a directory to a size that starts impacting
                system performance.  When a user tries to create a file
                in a directory that is at the limit, the system returns a
                ENOSPC error and fails the create.
        
        :param storage_service: Name of the storage service with which to associate the
                creation of an Infinite Volume.
                <p>
                If the client specifies this argument upon Infinite Volume
                creation, the argument will be used as the initial storage
                service for constituents of the Infinite Volume.
                <p>
                If the client does not specify this argument upon Infinite
                Volume creation, the Infinite Volume will be created
                without support for storage services. Support for storage
                services can be enabled at a later time using the
                volume-modify-iter-async API.
        
        :param is_managed_by_service: This argument is used to indicate that the Infinite
                Volume will be managed by storage services. If set
                to 'true', the client must also provide a name for
                the 'storage-service' argument.
        
        :param max_namespace_constituent_size: The maximum size of the namespace constituent.  The default
                value is 10TB.
        
        :param space_guarantee: Specifies the type of space guarantee the new Infinite Volume
                will use.  Possible values: none, file, volume.  If
                this argument is not provided, the default guarantee
                is "volume".
        
        :param data_aggr_list: Specifies an array of names of aggregates to be used for
                Infinite Volume data constituents. If this input is not
                specified all the aggregates assigned to the Vserver are used.
        
        :param export_policy: The name of the Export Policy to be used by the NFS
                protocol. The default policy name for Infinite Volumes is
                'repos_namespace_export_policy'.
        
        :param group_id: The UNIX group ID for the Infinite Volume.  The default value
                for Infinite Volumes is 1.
        
        :param volume_type: The type of the Infinite Volume to be created.
                Possible values:
                <ul>
                <ul> 'rw'   - read-write Infinite Volume (default),
                <ul> 'dp'   - data-protection Infinite Volume
                </ul>
        
        :param namespace_mirror_aggr_list: Specifies an array of names of aggregates to be used for
                Infinite Volume namespace mirror constituents. If this input is not
                specified all the aggregates assigned to the Vserver are used.
                If the arguments 'is-managed-by-service' and 'enable-snapdiff'
                are both set to 'true', a value must be provided.
        
        :param volume_security_style: The security style associated with this volume.
                <p>
                Possible values:
                <ul>
                <li> 'mixed' ... Mixed-style security,
                <li> 'ntfs'  ... NTFS/Windows-style security,
                <li> 'unified'  .Unified-style security, Unified UNIX, NFS and CIFS permissions (default for Infinite Volume)
                <li> 'unix'  ... Unix-style security (default for Flexible Volume)
                </ul>
                <p>
                Security styles don't apply to GX-striped data volumes.
                Infinite Volumes can only use the 'unified' security style.
                FlexVol volumes cannot use the 'unified' security style.
        
        :param enable_snapdiff: Whether to enable Snapdiff. If enabled, the namespace
                mirrors will be created for Snapdiff use. The default value
                is false.
        """
        return self.request( "volume-create-async", {
            'is_nvfail_enabled': [ is_nvfail_enabled, 'is-nvfail-enabled', [ bool, 'None' ], False ],
            'max_data_constituent_size': [ max_data_constituent_size, 'max-data-constituent-size', [ int, 'None' ], False ],
            'volume_state': [ volume_state, 'volume-state', [ basestring, 'None' ], False ],
            'junction_path': [ junction_path, 'junction-path', [ basestring, 'None' ], False ],
            'unix_permissions': [ unix_permissions, 'unix-permissions', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'None' ], False ],
            'snapshot_policy': [ snapshot_policy, 'snapshot-policy', [ basestring, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'user_id': [ user_id, 'user-id', [ int, 'None' ], False ],
            'namespace_aggregate': [ namespace_aggregate, 'namespace-aggregate', [ basestring, 'None' ], False ],
            'max_dir_size': [ max_dir_size, 'max-dir-size', [ int, 'None' ], False ],
            'storage_service': [ storage_service, 'storage-service', [ basestring, 'None' ], False ],
            'is_managed_by_service': [ is_managed_by_service, 'is-managed-by-service', [ bool, 'None' ], False ],
            'max_namespace_constituent_size': [ max_namespace_constituent_size, 'max-namespace-constituent-size', [ int, 'None' ], False ],
            'space_guarantee': [ space_guarantee, 'space-guarantee', [ basestring, 'None' ], False ],
            'data_aggr_list': [ data_aggr_list, 'data-aggr-list', [ basestring, 'aggr-name' ], True ],
            'export_policy': [ export_policy, 'export-policy', [ basestring, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
            'volume_type': [ volume_type, 'volume-type', [ basestring, 'None' ], False ],
            'namespace_mirror_aggr_list': [ namespace_mirror_aggr_list, 'namespace-mirror-aggr-list', [ basestring, 'aggr-name' ], True ],
            'volume_security_style': [ volume_security_style, 'volume-security-style', [ basestring, 'None' ], False ],
            'enable_snapdiff': [ enable_snapdiff, 'enable-snapdiff', [ bool, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_scrub_stop(self, name=None):
        """
        Stop RAID parity scrubbing on the named volume, plex,
        or group; if no name is given, on all RAID groups
        currently undergoing parity scrubbing.
        
        :param name: Name of an existing volume, plex, or raid-group.
        """
        return self.request( "volume-scrub-stop", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_set_msid(self, new_msid, name):
        """
        auto generated : Set MSID of a volume
        
        :param new_msid: New MSID of the Volume
        
        :param name: The name of the volume.
        """
        return self.request( "volume-set-msid", {
            'new_msid': [ new_msid, 'new-msid', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'volume-name' ], False ],
        }, {
        } )
    
    def volume_clone_get(self, volume, desired_attributes=None):
        """
        Display details of a specific FlexClone volume
        
        :param volume: FlexClone Volume
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "volume-clone-get", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VolumeCloneInfo, 'None' ], False ],
        }, {
            'attributes': [ VolumeCloneInfo, False ],
        } )
    
    def volume_space_list_info_iter_start(self, volume=None):
        """
        Starts an iteration through the list of volumes.
        
        :param volume: The name of the volume for which we want space status
                information.  If not supplied, then we display space status
                for all volumes on the filer.
        """
        return self.request( "volume-space-list-info-iter-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def volume_scrub_suspend(self, name=None):
        """
        Suspend RAID parity scrubbing on the named traditional
        volume, plex, or RAID group.  If no name is given,
        suspend scrubbing on all RAID groups currently being
        scrubbed.
        
        :param name: Name of an existing traditional volume, plex, or
                RAID group.
        """
        return self.request( "volume-scrub-suspend", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_get_volume_path(self, volume, is_style_cifs):
        """
        Return the junction-path of the volume.
        
        :param volume: Volume Name
        
        :param is_style_cifs: CIFS-style-flag
        """
        return self.request( "volume-get-volume-path", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'is_style_cifs': [ is_style_cifs, 'is-style-cifs', [ bool, 'None' ], False ],
        }, {
            'junction': [ basestring, False ],
        } )
    
    def volume_rename_async(self, volume_name, new_volume_name):
        """
        Renames the specified Infinite Volume to a new name specified by
        "new-volume-name".
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: Name of an existing Infinite Volume.
        
        :param new_volume_name: New name of the Infinite Volume.
        """
        return self.request( "volume-rename-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'new_volume_name': [ new_volume_name, 'new-volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_verify_stop(self, volume=None):
        """
        Stop RAID mirror verification on the named traditional
        volume.  If no name is given, stop RAID mirror
        verification on all aggregates (including those
        embedded in traditional volumes) currently being
        verified.
        
        :param volume: Name of the traditional volume for which we are to
                stop RAID mirror verification.
        """
        return self.request( "volume-verify-stop", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_move_abort(self, source_volume):
        """
        Aborts the volume move operation of the specified source volume. This is a synchronous API.
        
        :param source_volume: Name of the volume whose move has to be aborted
        """
        return self.request( "volume-move-abort", {
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_container(self, volume):
        """
        Return the name of the containing aggregate for
        the named flexible volume.
        
        :param volume: The name of the flexible volume for which we want the
                containing aggregate.
        """
        return self.request( "volume-container", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'containing-aggregate': [ basestring, False ],
        } )
    
    def volume_copy_start(self, vserver, destination_volume, source_volume, destination_aggregate):
        """
        Copy a volume
        A job will be spawned to operate on the volume and the job id
        will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param vserver: The name of the Vserver which owns the volume.
        
        :param destination_volume: Specify the name of volume on destination aggregate where the
                source-volume should be copied.
        
        :param source_volume: Specifies the name of the volume to be copied.
        
        :param destination_aggregate: Specify the name of aggregate where the source-volume should be
                copied.
        """
        return self.request( "volume-copy-start", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'destination_volume': [ destination_volume, 'destination-volume', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'destination_aggregate': [ destination_aggregate, 'destination-aggregate', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_space_list_info_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous volume-space-list-info-iter-start.
        """
        return self.request( "volume-space-list-info-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def volume_autosize_get(self, volume):
        """
        Given the name of a flexible volume, get the autosize
        settings. This API is not supported for Infinite Volumes.
        
        :param volume: The name of the flexible volume for which we want to
                get autosize.
        """
        return self.request( "volume-autosize-get", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'increment-size': [ basestring, False ],
            'minimum-size': [ basestring, False ],
            'grow-threshold-percent': [ int, False ],
            'maximum-size': [ basestring, False ],
            'shrink-threshold-percent': [ int, False ],
            'is-enabled': [ bool, False ],
            'mode': [ basestring, False ],
        } )
    
    def volume_move_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get status of move operation
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume object.
                All volume objects matching this query up to 'max-records' will
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
        return self.request( "volume-move-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VolumeMoveInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VolumeMoveInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VolumeMoveInfo, True ],
        } )
    
    def volume_online_async(self, volume_name):
        """
        Bring the specified Infinite Volume online.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: Name of an existing Infinite Volume.
        """
        return self.request( "volume-online-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_transition_log_get_iter(self, volume_name, source_node=None, desired_phases=None, operation_type=None, tag=None, destination_vserver_name=None, desired_features=None, desired_levels=None, maximum_records=None):
        """
        Retrieve the logged information about a transition operation.
        
        :param volume_name: Volume to obtain transition log information from.
        
        :param source_node: Node owning the 7-Mode volumes being transitioned.
        
        :param desired_phases: The list of the specific phases whose log
                records are desired by the caller.  To receive all phases,
                "all" can be specified.
                Possible values:
                <dl>
                <dt><dd> all </dd><br></dt>
                <dt><dd> check </dd><br></dt>
                <dt><dd> lock_config </dd><br></dt>
                <dt><dd> prepare </dd><br></dt>
                <dt><dd> pre_commit </dd><br></dt>
                <dt><dd> commit </dd><br></dt>
                <dt><dd> post_commit </dd><br></dt>
                <dt><dd> online </dd><br></dt>
                <dt><dd> rollback </dd><br></dt>
                <dt><dd> cleanup </dd><br></dt>
                <dt><dd> unlock_config </dd><br></dt>
                <dt><dd> complete </dd><br></dt>
                </dl>
                <p>
                If this argument is not provided, the default is 'all'.
        
        :param operation_type: The type of transition operation;
                Possible values are:
                "transition" (default)
                "untransition"
                Transition is currently the only supported mode; "untransition"
                should only be used in testing scenarios.
        
        :param tag: Value to use to get next entry.
        
        :param destination_vserver_name: The name of the containing vserver for the volume,
                if applicable.
        
        :param desired_features: The list of the specific features whose log records
                are desired by the caller. The caller can either specify a list of features or
                "all" to include all phases.
                If this argument is not provided, then it is
                equivalent to setting 'desired-features' to 'all'.
        
        :param desired_levels: The list of the specific level log records which
                are desired by the caller. The caller can either specify a list of levels or
                "all" to include all levels.
                <p>
                Possible values:
                <p>
                <dl>
                <dt><dd> all </dd><br></dt>
                <dt><dd> error </dd><br></dt>
                <dt><dd> warning </dd><br></dt>
                <dt><dd> info </dd><br></dt>
                <dt><dd> debug </dd><br></dt>
                <dt><dd> trace </dd><br></dt>
                </dl>
                <p>
                If this argument is not provided, then it is
                equivalent to setting 'desired-levels' to 'all'.
        
        :param maximum_records: The maximum number of records to return
        """
        return self.request( "volume-transition-log-get-iter", {
            'source_node': [ source_node, 'source-node', [ basestring, 'None' ], False ],
            'desired_phases': [ desired_phases, 'desired-phases', [ basestring, 'None' ], True ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'operation_type': [ operation_type, 'operation-type', [ basestring, 'None' ], False ],
            'tag': tag,
            'destination_vserver_name': [ destination_vserver_name, 'destination-vserver-name', [ basestring, 'None' ], False ],
            'desired_features': [ desired_features, 'desired-features', [ basestring, 'None' ], True ],
            'desired_levels': [ desired_levels, 'desired-levels', [ basestring, 'None' ], True ],
            'maximum_records': [ maximum_records, 'maximum-records', [ int, 'None' ], False ],
        }, {
            'records': [ VolumeTransitionLogRecordInfo, True ],
            'eof': [ bool, False ],
        } )
    
    def volume_move_resume(self, source_volume, cutover_window=None, is_manual_cutover=None, is_override_warnings=None, cutover_attempts=None, is_keep_source=None):
        """
        Resumes a previously paused volume move operation of a specified source volume.
        his is an asynchronous API.
        It will run a series of checks to determine if the volume
        move can be resumed. If there are no errors or warnings, the
        API will return successfully. The move will be resumed. The
        status of the move can be obtained from the
        volume-move-status API. If any of the checks result in an error
        or warning, the API will return with an error. If the
        checks result in no errors but one or more warnings and
        is-override-warnings is set to true, the API will return
        successfully and the move will be resumed.
        
        :param source_volume: Name of the volume whose move must be resumed
        
        :param cutover_window: Time interval to complete cutover in seconds. If not specified,
                then the existing value is maintained.
        
        :param is_manual_cutover: If specified, user has to initiate cutover.
        
        :param is_override_warnings: If warnings are encountered during the resume, the default
                behavior is to pause. If is-override-warnings is true, the move
                will continue and return these warnings in the errors-warnings
                element.
        
        :param cutover_attempts: Number of cutover attempts. If not specified, then the existing
                value is maintained.
        
        :param is_keep_source: If specified, the source volume will not be destroyed after
                the move is complete.
        """
        return self.request( "volume-move-resume", {
            'cutover_window': [ cutover_window, 'cutover-window', [ int, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'is_manual_cutover': [ is_manual_cutover, 'is-manual-cutover', [ bool, 'None' ], False ],
            'is_override_warnings': [ is_override_warnings, 'is-override-warnings', [ bool, 'None' ], False ],
            'cutover_attempts': [ cutover_attempts, 'cutover-attempts', [ int, 'None' ], False ],
            'is_keep_source': [ is_keep_source, 'is-keep-source', [ bool, 'None' ], False ],
        }, {
            'errors-warnings': [ ErrorsWarningsInfo, True ],
        } )
    
    def volume_modify_iter_async(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of an Infinite Volume or a group of
        repositories.
        <p>
        Infinite Volume creation and expansion operations may involve
        creation and initialization of Namespace Mirrors. The
        initialization is started during the creation of expansion
        operation, but can continue after the Infinite Volume operation
        has completed. When this happens, the Infinite Volume will be in
        a 'mixed' state, until the Namespace Mirror initilization is
        complete. While in a 'mixed' state, further operations of the
        Infinite Volume are not possible.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents. This API does not
        require any license when operating on an Infinite Volume.
        
        :param query: If modifying a specific volume, this input element must specify
                all keys.
                If modifying volume objects based on query, this input element
                must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching volume
                even when the modification of a previous matching volume fails,
                and do so until the total number of objects failed to be modified
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of volume objects
                (just keys) that were successfully updated or scheduled for
                update.
                If set to false, the list of volume objects modified will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple volume objects match a
                given query.
                If set to true, the API will continue modifying the next matching
                volume even when modification of a previous volume fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of volume objects
                (just keys) that were not modified due to some error.
                If set to false, the list of volume objects not modified will not
                be returned.
                Default: true
        """
        return self.request( "volume-modify-iter-async", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ VolumeAttributes, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ VolumeAttributes, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ VolumeModifyIterAsyncInfo, True ],
            'failure-list': [ VolumeModifyIterAsyncInfo, True ],
        } )
    
    def volume_scrub_start(self, name=None):
        """
        Start RAID parity scrubbing on the named traditional
        volume, plex, or RAID group.  RAID parity scrubbing
        compares the data disks to the parity disk in a RAID
        group, correcting the parity disk's contents as
        necessary.  If a plex name is given, then scrubbing
        is started on all RAID groups contained in the plex.
        If a RAID group name is given, then scrubbing is
        started only in that RAID group.  If no name is
        given, then scrubbing is started on the RAID groups
        within all online traditional volumes and aggregates.
        Use 'volume-scrub-list-info' to check scrub status.
        
        :param name: Name of an existing traditional volume, plex, or
                RAID group.
        """
        return self.request( "volume-scrub-start", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_mirror(self, volume, mirror_disks=None, force=None, victim_volume=None):
        """
        Turns an unmirrored traditional volume into a mirrored
        traditional volume by adding a plex to it.  The plex
        is either newly formed from disks chosen from a spare
        pool or, if the "victim-volume" option is specified,
        is taken from another existing unmirrored volume.  The
        volume must currently be unmirrored.  Disks may be
        specified explicitly using the "mirror-disks" argument
        list option in the same way as with the 'volume-create'
        and 'volume-add' APIs.  The number of disks specified
        must exactly match the number present in the existing
        traditional volume.  If the disks to use are not
        explicitly specified, then the appropriate disks are
        automatically selected to match those already in the
        traditional volume's existing plex.  It is not possible
        to directly mirror a flexible volume; if that is the
        goal, then consider using 'volume-container' to find
        the flexible volume's containing aggregate, then use
        'aggr-mirror' to mirror that aggregate (which, of
        course, will case all other volumes contained in the
        given aggregate to become mirrored as well).
        
        :param volume: Name of the traditional volume to be mirrored.
        
        :param mirror_disks: Specific list of mirror disks to use.  It must have
                the same number of disks as are present in the given
                traditional volume.  The specified disks are not
                permitted to span disk pools; this behavior can be
                overridden with the "force" argument.
        
        :param force: Force the mirroring operation through, past the normal
                roadblocks that would otherwise cause it to be aborted.
                For example, disks in a plex are not normally permitted
                to span spare pools.  This safety-drive behavior is
                overridden when the 'force' option is provided and set
                to 'true'.
        
        :param victim_volume: The "victim" traditional volume to cannibalize in
                order to mirror the given traditional volume.
                The result is a mirrored traditional volume that is
                otherwise identical to the original volume before
                the operation.  The "victim-volume" is effectively
                destroyed.  "victim-volume" must have been previously
                mirrored with this volume, then separated via the
                "volume-split" command.  "victim-volume" must be
                offline.
        """
        return self.request( "volume-mirror", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'victim_volume': [ victim_volume, 'victim-volume', [ basestring, 'None' ], False ],
        }, {
            'bad-disks': [ DiskInfo, True ],
        } )
    
    def volume_get_supported_guarantees(self, volume):
        """
        Returns the list of guarantee types that are supported on
        this volume. This just does semantic checks and so
        enabling supported guarantees can still fail because of
        space checks.
        
        :param volume: Name of the volume. Ex: flex1, vol0 etc.
        """
        return self.request( "volume-get-supported-guarantees", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'guarantee-types': [ Guarantee, True ],
        } )
    
    def volume_charmap_set(self, volume, charmap=None):
        """
        Associate a charmap description with a specified volume.
        
        :param volume: Name of the volume with which the charmap is to
                be associated.
        
        :param charmap: Description of the character mapping to be done
                for this volume. This mapping is to allow CIFS clients
                to use NFS file names that would otherwise result in
                invalid CIFS names. The values are comma-separated pairs
                of hex character mappings. The A-F hex values can be in
                upper or lower case, and the values do not have to be
                padded. Example: "5c:f2e1,3c:b6,3e:ae,7C:394". If a value
                is not passed, any existing charmap will be removed.
        """
        return self.request( "volume-charmap-set", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'charmap': [ charmap, 'charmap', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_move_trigger_abort(self, vserver, source_volume):
        """
        Stop a running volume move operation.
        <p>
        This is an asynchrous API call and it does not wait for the abort
        to finish before returning. volume-move-get-iter can be used to
        monitor the progress of the abort and get the status. Unlike 'job
        stop', this API makes it possible to stop a move job by the
        vserver and volume name. If the specified volume has completed
        the volume move operation, an error is returned.
        
        :param vserver: Vserver Name
        
        :param source_volume: The volume that is part of a completed or running volume move
                operation.
        """
        return self.request( "volume-move-trigger-abort", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_footprint_list_info_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous volume-footprint-list-info-iter-start.
        """
        return self.request( "volume-footprint-list-info-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def volume_verify_resume(self, volume=None):
        """
        Resume RAID mirror verification on the named
        traditional volume.  If no name is given, then
        resume RAID mirror verification on all aggregates
        (including those embedded in traditional volumes)
        that have been suspended.
        
        :param volume: Name of the existing traditional volume for which
                RAID mirror verification is to resume.
        """
        return self.request( "volume-verify-resume", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_wafl_info(self):
        """
        DEFINED HERE FOR BACKWARDS COMPATIBILITY ONLY.  CHANGE
        OVER TO USING THE NEW 'volume-get-filer-info' AS SOON
        AS POSSIBLE.
        Get WAFL status information.
        """
        return self.request( "volume-wafl-info", {
        }, {
            'root-volume': [ basestring, False ],
            'disk-types': [ basestring, False ],
            'snapshots-max': [ int, False ],
            'checksum-types': [ basestring, False ],
        } )
    
    def volume_move_modify(self, vserver, source_volume, cutover_window=None, cutover_action=None, cutover_attempts=None):
        """
        This is an asynchrous API call. This API allows user to modify
        parameters for running move job by Vserver and volume name. If
        the specified volume has neither started, nor completed the
        volume move operation, an error is returned.
        'volume-move-get-iter' API can be used to verify the modification
        of parameter. These modified parameters will be used when the
        move job will try to cutover next time.
        
        :param vserver: Vserver Name
        
        :param source_volume: The volume that is part of a completed or running volume move
                operation
        
        :param cutover_window: The time window in seconds for the cutover phase of volume move.
        
        :param cutover_action: The action to be taken for cutover or during cutover failure.
                cutover-action can have the following values <ul>
                <li>abort_on_failure
                <li>defer_on_failure
                <li>force
                <li>wait
                </ul>
                This is the input given during the start of volume move.
        
        :param cutover_attempts: The number of attempts to be used by the move operation to
                cutover to the destination volume. If the number of attempts is
                exhausted, the cutover-action input determines the next course of
                action for the move operation.
        """
        return self.request( "volume-move-modify", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'cutover_window': [ cutover_window, 'cutover-window', [ int, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'volume-name' ], False ],
            'cutover_action': [ cutover_action, 'cutover-action', [ basestring, 'None' ], False ],
            'cutover_attempts': [ cutover_attempts, 'cutover-attempts', [ int, 'None' ], False ],
        }, {
        } )
    
    def volume_set_language(self, volume, language_code):
        """
        Set the given volume's language mapping.
        
        :param volume: Name of the volume that is to have its language
                mapping changed.
        
        :param language_code: The new language mapping for the volume.  For a list
                of legal language mapping values, see 'volume-create'.
        """
        return self.request( "volume-set-language", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'language_code': [ language_code, 'language-code', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_list_info_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous volume-list-info-iter-start.
        """
        return self.request( "volume-list-info-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def volume_mount(self, volume_name, junction_path, export_policy_override=None, activate_junction=None):
        """
        Mount a volume on another volume (parent) with a junction-path.
        This API is not supported on Infinite Volume constituents.
        
        :param volume_name: The name of the volume.
        
        :param junction_path: The Junction Path.
                <p>
                The fully-qualified pathname in the owning Vserver's namespace
                at
                which a volume is mounted.  The pathname is case insensitive and
                must
                be unique within a Vserver's context. Note that this pathname may
                itself
                contain junctions, one for each volume (other than the namespace
                root volume) that provides storage along the pathname's length.
                As with all fully-qualified pathnames , this string must begin
                with '/'.  In addition, it must not end with '/'. An Infinite
                Volume
                has the additional restriction of allowing only one element.
                <p>
                An example of a valid FlexVol junction path is:
                '/user/my_volume'.
                An example of a valid Infinite Volume junction path is:
                '/repository'.
                <p>
                Only one volume can be mounted at any given junction path. If an
                incorrect junction path is specified, EINVALIDINPUTERROR is
                returned. If this volume is mounted at a different junction path,
                or if another volume is mounted at the specified junction path,
                EVOLALREADYMOUNTED is returned.
        
        :param export_policy_override: This field optionally specifies whether the parent volume's
                export policy overrides the mounted volume's Export Policy. The
                default is false.
        
        :param activate_junction: This field optionally specifies whether the mounted volume is
                accessible. The default is true. If the mounted path is not
                accessible, it does not appear in the owning Vserver's
                namespace.
        """
        return self.request( "volume-mount", {
            'export_policy_override': [ export_policy_override, 'export-policy-override', [ bool, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'activate_junction': [ activate_junction, 'activate-junction', [ bool, 'None' ], False ],
            'junction_path': [ junction_path, 'junction-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_footprint_list_info(self, volume=None):
        """
        Return a list of volumes and a breakdown of their data and
        metadata footprints in their parent aggregates. The term
        footprint is used to refer to the portion of aggregate used
        space that will be freed when the relevant volume is destroyed.
        This can exceed the size of the volume due to metadata. If no
        volume is specified, footprints are displayed for all online
        volumes on the filer. Note that if space footprint information
        for more than 20 volumes is desired, the
        volume-footprint-list-info-iter-* ZAPIs will be more efficient
        and should be used instead.
        
        :param volume: The name of the volume for which we want status
                information.  If not supplied, then we want status
                for all volumes on the filer.
        """
        return self.request( "volume-footprint-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'vol-footprint-infos': [ VolFootprintInfo, False ],
        } )
    
    def volume_set_total_files(self, volume, requested_total_files, force=None):
        """
        Set a volume's 'files-total' value to the given
        quantity.  This specifies the maximum number of
        user-visible files that the given volume can hold,
        as reported by the 'files-total' value within:
        - the 'volumes' output parameter of the Data ONTAP
        7-Mode 'volume-list-info' API, and
        - the 'attributes-list' output parameter of the Data
        ONTAP Cluster-Mode 'volume-get-iter' API.
        Note that this interface corresponds to the following
        Data ONTAP 7-Mode 'maxfiles' console command and
        Data ONTAP Cluster-Mode 'volume modify' console command:
        'maxfiles &lt;vol-name&gt; &lt;requested_new_max&gt;'
        'volume modify -vserver &lt;vserver-name&gt; -volume
        &lt;volume-name%gt -files &lt;requested_new_max&gt;'
        
        :param volume: The name of the volume whose 'files-total' field we
                wish to set.  The chosen volume must be online and
                not read-only for this operation to succeed.
        
        :param requested_total_files: Specifies the new value for the volume's 'files-total'
                field.  This value must be larger than the volume's
                current 'files-total' value, and can never be larger
                than the number of 4KB blocks in the volume.  The
                filer may actually choose a smaller value so as to
                comply with certain internal accounting and alignment
                requirements.  Once this value has been increased for
                a volume, it cannot be reduced below the value of
                'inodefile-public-capacity' for that volume.
                Range : [0..2^31-1]
        
        :param force: Indicates whether the filer should reject a legal but
                "unreasonable" (seemingly too large) value for
                'requested-total-files', or accept it without question.
                By default, legal but "unreasonable" values are rejected.
        """
        return self.request( "volume-set-total-files", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'requested_total_files': [ requested_total_files, 'requested-total-files', [ int, 'None' ], False ],
        }, {
            'resulting-total-files': [ int, False ],
        } )
    
    def volume_list_info(self, volume=None, verbose=None):
        """
        Get volume status.  Note that all RAID-related status
        items (e.g., 'raid-size', 'raid-status',
        'checksum-style') reported for a flexible volume
        actually describe the state of its containing
        aggregate.
        
        :param volume: The name of the volume for which we want status
                information.  If not supplied, then we want status
                for all volumes on the filer.  Note that if status
                information for more than 20 volumes is desired, the
                volume-list-info-iter-* zapis will be more efficient
                and should be used instead.
        
        :param verbose: If set to "true", more detailed volume information
                is returned.  If not supplied or set to "false",
                this extra information is not returned.
        """
        return self.request( "volume-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'volumes': [ VolumeInfo, True ],
        } )
    
    def volume_list_info_iter_start(self, volume=None, verbose=None):
        """
        Starts an iteration through the list of volumes.
        
        :param volume: The name of the volume for which we want status
                information.  If not supplied, then we want status
                for all volumes on the filer.
        
        :param verbose: If set to "true", more detailed volume information
                is returned.  If not supplied or set to "false",
                this extra information is not returned.
        """
        return self.request( "volume-list-info-iter-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def volume_add(self, volume, disk_size_with_unit=None, mirror_disks=None, disk_size=None, force=None, disks=None, raid_group=None, disk_count=None):
        """
        Adds disks to the given traditional volume.  Specify
        the disks to add in the same way as for 'volume-create'.
        Disks cannot be added to a mirrored traditional volume
        if one of its plexes is offline.  Addition of the
        specified disk(s) may not have completed by the time
        the API returns.  Use 'volume-list-info' to query the
        traditional volume's status, and thus determine when
        the disk addition is complete.  It is not possible to
        add disks directly to a flexible volume; if that is the
        goal, then consider using 'volume-container' to find
        the flexible volume's containing aggregate, then use
        'aggr-add' to add the desired disks there (which, of
        course, will make their storage available to all
        flexible volumes contained in that same aggregate).
        
        :param volume: Name of the traditional volume to which disks are to
                be added.
        
        :param disk_size_with_unit: The disk size in specified unit.
                It is a positive integer number followed by unit of "T", "G",
                "M" or "K".
                This option is ignored if
                a specific list of disks to use is provided via the
                "disks" argument.
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear, an error
                message will be returned.
        
        :param mirror_disks: Specific list of mirror disks needed to accompany
                the list in the "disks" argument.  This list must
                contain the same number of disks specified in "disks".
        
        :param disk_size: The disk size in 4KB blocks.  Disks that are within
                approximately 20% of the specified size are selected
                for use in the traditional volume.  If neither the
                "disk-size" nor the "disk-size-with-unit" is specified,
                the smallest disks in the spare pool join the
                traditional volume first.  This option is ignored if
                a specific list of disks to use is provided via the
                "disks" argument.
                Range : [0..2^31-1].
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear,
                an error message will be returned.
        
        :param force: Disks in a plex are not permitted to span spare
                spare pools. This behavior is overridden with this
                option when it is set to "true".
        
        :param disks: Specific list of disks to add to the traditional volume.
                If the traditional volume is mirrored and a specific
                disk list is supplied, another list ("mirror-disks")
                must also be supplied with the same number of disks.
        
        :param raid_group: Specifies the RAID group (for example, 'rg0') to which
                the indicated disks are to be added.  When a RAID group
                other than the last RAID group is specified, the
                traditional volume can no longer be reverted to a
                version of ONTAP prior to 6.2.  In such a case, the
                "force" option must be specified as well.  By default,
                the filer fills up one RAID group with disks before
                starting another RAID group.  Suppose a traditional
                volume currently has one RAID group of 12 disks and its
                RAID group size is 14.  If you add 5 disks to this
                traditional volume, it will have one RAID group with
                14 disks and another RAID group with 3 disks.  The
                filer does not evenly distribute disks among RAID
                groups.
        
        :param disk_count: Number of disks to add, including parity disks.  The
                disks will come from the spare pool.  The smallest
                disks in the spare pool join the volume first, unless
                "disk-size" is specified as an argument.
                Range : [0..2^31-1].
        """
        return self.request( "volume-add", {
            'disk_size_with_unit': [ disk_size_with_unit, 'disk-size-with-unit', [ basestring, 'None' ], False ],
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'disk_size': [ disk_size, 'disk-size', [ int, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'disks': [ disks, 'disks', [ DiskInfo, 'None' ], True ],
            'raid_group': [ raid_group, 'raid-group', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'disk_count': [ disk_count, 'disk-count', [ int, 'None' ], False ],
        }, {
            'bad-disks': [ DiskInfo, True ],
        } )
    
    def volume_transition(self, source_node, volumes, affinity_node=None, operation_type=None, override_warnings=None, destination_vserver_name=None, non_disruptive=None):
        """
        Transition a volume between 7-Mode and Cluster-Mode.
        Currently the only supported operation type is
        transitioning a 7-Mode Flexible Volume that has been
        copied from a 7-Mode Filer for the purpose of
        transitioning it to a Cluster-Mode Flexible Volume.
        A job-id will be returned that can be used to query
        to progress of the transition job.
        
        :param source_node: The name of the node where the target volumes reside.
        
        :param volumes: Volumes to attempt to transition.
        
        :param affinity_node: The name of the node where the transition job should run.
        
        :param operation_type: The type of transition operation;
                Possible values are:
                "copy_based" (default)
                "in_place"
                "untransition"
                Copy Based Transition is currently the only supported mode
                for transition; "in_place" and "untransition" should only
                be used in testing scenarios.
        
        :param override_warnings: A 'true' value indicates that all warnings will be ignored as a part of the transition
                process.  The system will select default values as appropriate.  If not specified,
                values will not be overridden.
        
        :param destination_vserver_name: The name of the vserver into which a volume is being
                transitioned.
        
        :param non_disruptive: A 'true' value indicates that only a non-disruptive transition will be accepted.
                This is not available for all volume configurations.  If a value
                is not specified, this field will default to true - non-disruptive
                desired.
        """
        return self.request( "volume-transition", {
            'affinity_node': [ affinity_node, 'affinity-node', [ basestring, 'None' ], False ],
            'source_node': [ source_node, 'source-node', [ basestring, 'None' ], False ],
            'operation_type': [ operation_type, 'operation-type', [ basestring, 'None' ], False ],
            'override_warnings': [ override_warnings, 'override-warnings', [ bool, 'None' ], False ],
            'destination_vserver_name': [ destination_vserver_name, 'destination-vserver-name', [ basestring, 'None' ], False ],
            'volumes': [ volumes, 'volumes', [ VolumeTransitionVolinfo, 'None' ], True ],
            'non_disruptive': [ non_disruptive, 'non-disruptive', [ bool, 'None' ], False ],
        }, {
            'job-id': [ int, False ],
        } )
    
    def volume_charmap_get(self, volume):
        """
        Return charmap information for a specified volume.
        
        :param volume: Name of the volume on which to list the charmap
                information.
        """
        return self.request( "volume-charmap-get", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'charmap': [ basestring, False ],
        } )
    
    def volume_vbncheck(self, volume, vbns):
        """
        Look up files by VBNs in a volume.
        It starts a background WAFL scanner to scan the volume.
        The scanner status can be checked by 'wafl scan status'.
        Lookup results are saved to output file
        '/etc/WAFL_vbntoino.VOL.YYYYMMDDHHMMSS'
        Example Output (for VBN 2264 in vol0):
        Checking volume: vol0
        Vbn List:
        2264
        VVBN 2264
        Inode 204 has 1 name.
        pathname = /vol/vol0/etc/passwd
        Scan performed on snapshots created before Fri Jul 18
        19:36:32 GMT 2008
        The following snapshots contain any of the listed blocks:
        hourly.23   Thu Jul 17 00:00:31 GMT 2008
        VBN lookup completed
        
        :param volume: This is the name of the volume where VBNs belong
        
        :param vbns: An array of VBNs, Virtual Block Numbers, to check.
        """
        return self.request( "volume-vbncheck", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'vbns': [ vbns, 'vbns', [ int, 'vbn' ], True ],
        }, {
            'output-file': [ basestring, False ],
        } )
    
    def volume_verify_start(self, volume=None, fix_plex=None, log_only=None):
        """
        Start RAID mirror verification on the named traditional
        volume.  RAID mirror verification compares the data in
        both plexes of a mirrored aggregate (whether it's
        free-standing or embedded in a traditional volume).
        In the default case, any blocks that differ are logged
        and no changes are made. The fix-plex option is used to
        fix any mismatches. It specifies which plex to fix.
        If no name is given, then RAID mirror verification is
        started on all online aggregates (including those
        embedded in traditional volumes).  Use either the
        "aggr-verify-list-info" or "volume-verify-list-info"
        API to check RAID mirror verification status. If the
        fix-plex option is used, then a name must be specified.
        
        :param volume: Name of the mirrored traditional volume to verify.
        
        :param fix_plex: If provided, this specifies the plex to fix in case
                the two plexes do not match. The default is to log
                any discrepancies instead of fixing them.
        
        :param log_only: If provided, and if the value is "true", then simply
                log any discrepancies instead of fixing them.  The
                default value is "true". If log-only is "false", then
                the fix-plex option must also be specified. If log-only
                is "true" and fix-plex is also specified, then the
                log-only option will be ignored.
        """
        return self.request( "volume-verify-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'fix_plex': [ fix_plex, 'fix-plex', [ int, 'None' ], False ],
            'log_only': [ log_only, 'log-only', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_verify_suspend(self, volume=None):
        """
        Suspend RAID mirror verification on the named
        traditional volume.  If no name is given, suspend
        mirror verification on all aggregates (including
        those embedded in traditional volumes) currently
        being verified.
        
        :param volume: Name of the traditional volume for which we are to
                suspend RAID mirror verification.
        """
        return self.request( "volume-verify-suspend", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_storage_service_rename(self, volume, storage_service, new_storage_service):
        """
        Volume Storage Service Rename
        
        :param volume: Volume Name
        
        :param storage_service: Storage Service Name
        
        :param new_storage_service: New Storage Service Name
        """
        return self.request( "volume-storage-service-rename", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'storage_service': [ storage_service, 'storage-service', [ basestring, 'None' ], False ],
            'new_storage_service': [ new_storage_service, 'new-storage-service', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_footprint_list_info_iter_start(self, volume=None):
        """
        Starts an iteration through the list of volumes.
        
        :param volume: The name of the volume for which we want space footprint
                information. If not supplied, then we display space footprint
                for all volumes on the filer.
        """
        return self.request( "volume-footprint-list-info-iter-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def volume_storage_service_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of volume-storage-service objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume-storage-service object.
                All volume-storage-service objects matching this query up to
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
        return self.request( "volume-storage-service-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ StorageServiceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ StorageServiceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ StorageServiceInfo, True ],
        } )
    
    def volume_transition_log_delete(self, volume_name, operation_type=None, destination_vserver_name=None, source_node=None):
        """
        Transition a volume from one type to another.
        Delete the logged information about a transition operation.
        
        :param volume_name: Volumes to delete the transition log from.
        
        :param operation_type: The type of transition operation;
                Possible values are:
                "transition" (default)
                "untransition"
                Transition is currently the only supported mode; "untransition"
                should only be used in testing scenarios.
        
        :param destination_vserver_name: The name of the containing vserver for the volume,
                if applicable.
        
        :param source_node: Node owning the 7-mode volumes being transitioned
        """
        return self.request( "volume-transition-log-delete", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'operation_type': [ operation_type, 'operation-type', [ basestring, 'None' ], False ],
            'destination_vserver_name': [ destination_vserver_name, 'destination-vserver-name', [ basestring, 'None' ], False ],
            'source_node': [ source_node, 'source-node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_verify_list_info(self, volume=None):
        """
        Get the status of RAID mirror verification on the
        named traditional volume.  Status includes percentage
        complete and whether it's currently suspended.
        
        :param volume: Name of an existing mirrored traditional volume.  If
                no name is given, then mirror verification status is
                generated for all aggregates currently being verified
                (including the ones embedded in traditional volumes).
        """
        return self.request( "volume-verify-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'verify-details': [ VerifyDetailInfo, True ],
        } )
    
    def volume_move_status(self, source_volume=None, is_verbose=None):
        """
        Obtains the status of the volume move operation. This is a synchronous API.
        
        :param source_volume: Name of the volume that is being moved. If source-volume is
                not provided, then the status of all active moves is listed.
                If it is provided the status of the move of source-volume is
                returned. Since this version will support only one move at a
                time, this input will not alter the output returned
                by this API.
        
        :param is_verbose: If not supplied or set to "false", output shows source volume, destination aggregate,
                cutover window, cutover attempts and state of move. If set to "true", verbose output containing
                details about last and current snapmirror transfer in addition to above parameters is returned.
        """
        return self.request( "volume-move-status", {
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'is_verbose': [ is_verbose, 'is-verbose', [ bool, 'None' ], False ],
        }, {
            'status': [ VolMoveStatusInfo, True ],
        } )
    
    def volume_list_info_iter_next(self, tag, maximum):
        """
        Continues an iteration through the list of volumes.
        
        :param tag: Tag from a previous volume-list-info-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "volume-list-info-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'volumes': [ VolumeInfo, True ],
        } )
    
    def volume_clone_split_start(self, volume):
        """
        Begin the process by which the given clone is split off
        from its underlying parent volume and snapshot.  New
        storage is allocated for the clone that is distinct
        from its parent.
        This process may take some time and proceeds in the
        background.  Use the 'volume-clone-split-status'
        command to view the operation's progress.
        Both clone and parent volumes remain available during
        the process of splitting them apart.  Upon completion,
        the snapshot on which the clone was based will be
        unlocked in the parent volume.  Any snapshots in the
        clone are removed at the end of processing.  Use the
        'volume-clone-split-stop' command to stop this process.
        This command fails if applied to a traditional volume.
        Cloning is a new capability that applies exclusively
        to flexible volumes.
        <p>
        In Data ONTAP Cluster-Mode, a job is created to perform
        the split operation. The job id of the job is returned
        in the API response. The progress of the job can be tracked
        using the job APIs.
        
        :param volume: Name of the clone that we want split off from its
                parent volume and snapshot.
        """
        return self.request( "volume-clone-split-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_get_root_name(self):
        """
        Return the name of the "root" volume on the filer. If
        this request is executed in the context of a vfiler,
        the "root" volume of the vfiler will be returned.
        If this request is executed in the context of a Vserver
        the "namespace root" volume of the Vserver will be returned.
        If the "namespace root" volume of the Admin Vserver is
        requested, EVSERVER_OP_NOT_ALLOWED will be returned.
        """
        return self.request( "volume-get-root-name", {
        }, {
            'volume': [ basestring, False ],
        } )
    
    def volume_scrub_list_info(self, name=None, verbose=None):
        """
        Get the status of RAID parity scrubbing on the named
        traditional volume, plex, or RAID group.  If no name
        is given, then status is provided for all RAID groups
        currently undergoing scrubbing.  Scrubbing status
        includes a percent-complete value and its suspended
        status (if any).
        
        :param name: Name of an existing traditional volume, plex, or
                RAID group.  If no name is given, then status is
                generated for all RAID groups currently being
                scrubbed.
        
        :param verbose: If set to "true", this operation will be verbose.
                If not supplied or set to 'false', normal output
                levels will be used.
        """
        return self.request( "volume-scrub-list-info", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'scrub-details': [ ScrubDetailInfo, True ],
        } )
    
    def volume_offline(self, name, cifs_delay=None):
        """
        Take the specified volume or plex offline, making
        it unavailable for both user-level data access and
        RAID-level access (unless it's a flexible volume,
        at which time its containing aggregate is not
        affected in any way, and will remain fully online).
        The operation takes effect before the API returns
        except in maintenance mode, when the current root
        volume may not be taken offline.  A volume marked
        to become the root cannot be taken offline.  Taking
        a flexible volume offline does not affect its
        containing aggregate in any way.
        A number of operations being performed on the given
        volume (or its containing aggregate) can prevent this
        operation from succeeding, either at all or for various
        lengths of time.  If such operations are found, the
        system waits up to one second for them to finish.  If
        they don't, the command is aborted.
        A check is also made for files on the volume opened
        by internal ONTAP processes.  The command is aborted
        if any are found.
        Plexes are not supported for Cluster-Mode volumes.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param name: Name of an existing volume or plex.
                If a volume contains CIFS shares, users should be warned
                before taking the volume offline.  Use "cifs-delay"
                to specify number of seconds to wait.
                If a plex is specified, the plex must be part of a
                mirrored volume, and both plexes must be online.  Prior
                to offlining a plex, the system will flush all
                internally-buffered data associated with the plex
                and create a snapshot that is written out to both
                plexes.  The snapshot allows for efficient
                resynchronization when the plex is subsequently
                brought back online.
        
        :param cifs_delay: If a volume contains CIFS shares, users should be
                warned before taking the volume offline.  This argument
                specifies the number of minutes to delay before taking
                the volume offline, during which time CIFS users are
                warned of the pending loss of service.  A 'cifs-delay'
                time of 0 means that the volume is to be taken offline
                immediately without issuing any warnings.  CIFS users
                can lose data if they are not given a chance to
                terminate applications gracefully.  By default, the
                value of 'cifs-delay' is 0.
        """
        return self.request( "volume-offline", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'cifs_delay': [ cifs_delay, 'cifs-delay', [ int, 'None' ], False ],
        }, {
        } )
    
    def volume_check_test(self, name):
        """
        auto generated : Start a volume check unit test
        
        :param name: The name of the volume.
        """
        return self.request( "volume-check-test", {
            'name': [ name, 'name', [ basestring, 'volume-name' ], False ],
        }, {
        } )
    
    def volume_set_option(self, volume, option_value, option_name):
        """
        Set the option named 'option-name' to the value
        specified by 'option-value' in the specified volume.
        The change remains effective even after the filer
        is rebooted.  Some options have values that are
        numbers or strings, and others have values that are 'on'
        (also expressible as 'yes', 'true', or '1' ) or "off" (also
        expressible as 'no', 'false', or '0').  A mixture of
        uppercase and lowercase characters may be used for an
        option's value.  Note that the 'root' option is
        special in that it does not have an associated value.
        Also, note that some of these options can NOT be set
        for a flexible volume, as they relate only to
        aggregates (either free-standing ones or those
        embedded in traditional volumes). Other options may
        only apply for flexible volumes.
        
        :param volume: Name of the volume for which we want to set an option.
        
        :param option_value: The value to set the named option (except for
                option 'root', which has no associated value).
        
        :param option_name: Name of the option to be set.  Possible values:
                <dl>
                <dt>"convert_ucode" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" forces conversion
                of all directories to UNICODE format when
                accessed from both NFS and CIFS.  By default,
                it is set to "off", in which case access from
                CIFS causes conversion of pre-4.0 and 4.0-
                format directories.  Access from NFS causes
                conversion of 4.0 format directories.
                This option cannot be set on a Cluster-Mode
                volume unless it was transitioned from 7-Mode.
                </dd><br>
                <dt>"snapshot_clone_dependency" (value: "on" | "off")</dt>
                <dd>
                Setting this option "on" will unlock all initial and
                intermediate backing snapshots for all inactive LUN
                clones. For active LUN clones, only the backing
                snapshot will be locked. If the option is "off" the
                backing snapshot will remain locked until all
                intermediate backing snapshots are deleted.
                This option is not valid for a Cluster-Mode volume.
                </dd><br>
                <dt>"create_reserved"</dt>
                <dd>
                This option is no longer supported.
                </dd><br>
                <dt>"create_ucode" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" forces UNICODE
                format directories to be created by default,
                both from NFS and CIFS.  The default value is
                "off", in which case all directories are
                created in pre-4.0 format and only converted
                to UNICODE format upon the first CIFS access.
                This option cannot be set on a Cluster-Mode volume.
                </dd><br>
                <dt>"extent" (value: "on" | "space_optimized" | "off")</dt>
                <dd>
                Setting this option to "on" enables extents in the volume.
                This causes application writes to be written in the volume
                as a write of a larger group of related data blocks called
                an extent.  Using extents may help workloads that perform
                many small random writes followed by large sequential
                reads.  However, using extents may increase the amount of
                disk operations performed on the filer, so this option
                should only be used where applicable.  The default value is
                "off", in which case extents are not used.  The value
                "space_optimized" indicates extent updates will not
                duplicate snapshot blocks into the active file system,
                thereby using space conservatively.  The "space_optimized"
                value may result in degraded snapshot read performance;
                and may only be used for <b>flexible</b> volumes.
                </dd><br>
                <dt>"fractional_reserve" (value: &lt number &gt)</dt>
                <dd>
                This option decreases the amount of space reserved
                for overwrites of reserved objects (LUNs, files) in
                a volume. The option is set to 100 by default and
                indicates that 100% of the required reserved space will
                actually be reserved so the objects are fully protected
                for overwrites. The value can vary from 0 to 100.
                Using a value of less than 100 indicates what percentage
                of the required reserved space should actually be
                reserved. This returns the extra space to the available
                space for the volume, decreasing the total amount of
                space used. However, this does leave the protected
                objects in the volume vulnerable to out of space errors
                since less than 100% of the required reserved space is
                actually reserved. If reserved space becomes exhausted
                this will cause disruptions on the hosts using the
                objects. If the percentage is decreased below 100%,
                it is highly recommended that the administrator actively
                monitor the space usage on the volume and take corrective
                action if the reserved space nears exhaustion.
                </dd><br>
                <dt>"fs_size_fixed" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" causes the file
                system to remain the same size (and not grow)
                when a SnapMirror relationship is broken, or
                when a "vol/aggr add" is performed on it.  This
                option is automatically set to be "on" when
                a volume becomes a SnapMirrored.  It remains
                "on" after the "snapmirror break" command is
                issued for the volume.  This option allows
                a volume to be SnapMirrored back to the
                source without needing grow the source
                volume.  If the volume size is larger than
                the file system size, turning off this option
                forces the file system to grow to the size of
                the volume.
                </dd><br>
                <dt>"guarantee" (value: "none" | "file" | "volume")</dt>
                <dd>
                <b>Flexible</b> volumes only.
                Setting this option controls the type of space
                reservation for the named flexible volume.  There
                are three possible settings.  The first, "none",
                provides no guarantee that there will be enough
                blocks in the containing aggregate to meet the
                flexible volume's needs.  The second, "file",
                guarantees there will be enough blocks in the
                containing aggregate to meet the needs of the
                specified files in the flexible volume.  The
                third, "volume", is the default setting and
                guarantees there will be enough blocks available
                in the containing aggregate to meet the entire
                flexible volume's needs.  An error will be
                returned if an attempt is made to set this
                option on a traditional volume.
                </dd><br>
                <dt>"ignore_inconsistent" (value: "on" | "off")</dt>
                <dd>
                This option can only be set in maintenance
                mode.  If set to "on", then the root volume
                may be brought online when booting even if
                it is marked as inconsistent.  The user is
                cautioned that bringing it online prior to
                running WAFL_check or wafliron may result in
                further file system inconsistency.
                </dd><br>
                <dt>"maxdirsize" (value: &lt number &gt)</dt>
                <dd>
                Set the maximum size (in KBytes) to which any
                directory can grow.  The default setting of
                10240 limits directory size to 10 MBytes and
                allows it to hold up to approximately 300,000
                files.  The number of files that the directory
                actually can hold varies depending on such
                things as the length of the names and whether
                it needs to use double-byte UNICODE characters.
                Most users should not need to change this
                option's setting.  This option is useful for
                environments where system users may grow a
                directory to a size that starts impacting
                system performance.  When a user tries to
                create a file in a directory that is at the
                limit, the system returns a ENOSPC error and
                fails the create.
                </dd><br>
                <dt>"max_write_alloc_blocks" (value: &lt number &gt)</dt>
                <dd>
                Set the maximum number of blocks used for
                write allocation.  The default setting, 0,
                uses the system-wide default number of
                blocks, which should be optimal for most
                users.  Some sequential read workloads may
                benefit from increasing this value.  On
                rare occasions, some multi-stream sequential
                write workloads may benefit from decreasing
                this value.  Range: [0..2048].
                </dd><br>
                <dt>"minra" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" causes the filer
                to perform minimal read-ahead on this volume.
                By default, this option is "off", causing the
                filer to perform very aggressive read-ahead
                on the volume.
                </dd><br>
                <dt>"no_atime_update" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" prevents the update
                of inode access times when a file is read.  This
                option is useful for volumes with extremely
                high read traffic, since it prevents writes to
                the inode file for the volume from contending
                with reads from other files.  It should be used
                carefully.  That is, use this option when you
                know in advance that the correct access time for
                inodes will not be needed for files on that
                volume.
                </dd><br>
                <dt>"no_i2p" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" disables inode to parent
                pathname translations on the volume.
                The default setting is off.
                </dd><br>
                <dt>"nosnap" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" disables automatic
                snapshots on the volume.
                This option is not supported for Cluster-Mode volumes.
                </dd><br>
                <dt>"nosnapdir" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" disables the visible
                .snapshot directory that is normally present at
                system internal mount points.  It also turns off
                access to all other .snapshot directories in the
                volume.
                </dd><br>
                <dt>"nvfail" (value : "on" | "off")</dt>
                <dd>
                If this option is on, the filer performs additional
                work at boot time if it finds that there has been
                any potential data loss due to an NVRAM failure.
                In such situations, it causes the invalidation of
                all NFS file handles on all volumes affected by
                the problem so that client-side users are forced
                to remount the affected file system (and thus not
                continue to use potentially incorrect data).  It
                is also possible to specify a set of files per
                volume that are to be renamed out of the way in
                these cases.  The filer sends error messages to
                the console whenever such problems are found.
                </dd><br>
                <dt>"raid_cv" (value: "on" | "off")</dt>
                <dd>
                <b>Traditional</b> volumes only.
                Setting the option to "off" disables block checksum
                protection on the volume.  The default is "on".
                The user is cautioned that turning off the option
                exposes the filesystem to inconsistency that could be
                caused by a misbehaving hardware component in the system.
                </dd><br>
                <dt>"raid_zoned" (value: "on" | "off")</dt>
                <dd>
                <b>Traditional</b> volumes only.
                Setting the option to "off" disables zoned checksum
                protection on the volume.  The default is "on".
                The user is cautioned that turning off the option
                exposes the filesystem to inconsistency that could be
                caused by a misbehaving hardware component in the system.
                </dd><br>
                <dt>"raidsize" (value: &lt number &gt)</dt>
                <dd>
                <b>Traditional</b> volumes only.
                The maximum size of a RAID group within the
                traditional volume.  Changing this option
                doesn't cause existing RAID groups to grow or
                shrink.  Rather, it only affects whether more
                disks will be added to the last existing RAID
                group in the future, and how large new RAID
                groups will be.
                </dd><br>
                <dt>"raidtype" (value: "raid4" | "raid_dp")</dt>
                <dd>
                <b>Traditional</b> volumes only.
                The type of RAID group used for this traditional
                volume.  The "raid4" setting  provides one parity
                disk per RAID group, while "raid_dp" provides two.
                Changing this option immediately changes the RAID
                group type for all RAID groups in the traditional
                volume.  When upgrading RAID groups from "raid4"
                to "raid_dp", each RAID group begins reconstruction
                onto a spare disk allocated for the second "dparity"
                parity disk.
                </dd><br>
                <dt>"read_realloc" (value: "on" | "space_optimized" | "off")</dt>
                <dd>
                Setting this option to "on" enables read-reallocation in
                the volume.  This causes application reads to optimize the
                layout of parts of a file or LUN after the data has been
                read from disk and is in the appliance memory.  The
                default value is "off", in which case read-reallocate is
                not used.  The value "space_optimized" indicates
                read-reallocate updates will not duplicate blocks into
                the active file system, thereby using space conservatively.
                The "space_optimized" value may result in degraded
                snapshot read performance; and may only be used for
                <b>flexible</b> volumes.
                </dd><br>
                <dt>"resyncsnaptime" (value: &lt number &gt)</dt>
                <dd>
                <b>Traditional</b> volumes only.
                Sets the RAID mirror resynchronization snapshot
                frequency to be the given number of minutes.
                The default value is '60' (minutes).
                </dd><br>
                <dt>"root" (value: &lt none &gt)</dt>
                <dd>
                The specified volume is to become the root
                volume for the filer on the next reboot.  This
                option can be used on only one volume at any
                given time.  The existing root volume will
                become a non-root volume after the reboot.
                Until the system is rebooted, the current
                root volume will continue to show 'root' as
                one of its options, and the new root volume
                will show 'diskroot' as an option.  In general,
                the volume that has the 'diskroot' option
                value is the one that becomes the root volume
                following the next reboot.  The only way to
                remove the root status of a volume is to set
                it on another one.
                </dd><br>
                <dt>"schedsnapname" (value: "create_time" | "ordinal")</dt>
                <dd>
                Setting the option to "ordinal" causes scheduled snapshots to
                be named in the hourly.n name format. Setting the value to
                "create_time" causes snapshots to use a hourly.yyyy-mm-dd_hhmm
                name format instead.  The default is "ordinal".
                </dd><br>
                <dt>"snapmirrored" (value : "off")</dt>
                <dd>
                If SnapMirror is enabled, the filer automatically
                sets this option to "on".  Set this option to
                "off" if SnapMirror should no longer be used to
                update the mirror.  After setting this option to
                "off", the mirror becomes a regular writable
                volume.  This option can only be set to "off"
                with this interface.  Only the filer can change
                this option's value from "off" to "on".
                This option is not settable in Data ONTAP Cluster-Mode.
                Use "snapmirror-break" API instead.
                </dd><br>
                <dt>"try_first" (value : "volume_grow" | "snap_delete")</dt>
                <dd>
                If the flexible volume is configured to
                automatically reclaim space if the volume is running
                out of space, then setting this option to
                "volume_grow" will cause the volume to
                increase in size before deleting snapshots.
                If the option was set to "snap_delete",
                snapshots will be deleted before the volume size is
                increased.
                </dd><br>
                <dt>"svo_enable" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" enables SnapValidator
                functionality on this volume.  This option
                only applies to non-root volumes.
                This option is unsupported in Data ONTAP Cluster-Mode.
                </dd><br>
                <dt>"svo_allow_rman" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" enables SnapValidator
                functionality on this volume to allow this
                volume to contain Oracle RMAN backup data.
                This option only applies to non-root volumes.
                This option is unsupported in Data ONTAP Cluster-Mode.
                </dd><br>
                <dt>"svo_checksum" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" enables SnapValidator
                checksumming of all writes to this volume.
                This option only applies to non-root volumes.
                This option is unsupported in Data ONTAP Cluster-Mode.
                </dd><br>
                <dt>"svo_reject_errors" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" enables SnapValidator
                functionality to reject any write to the
                volume which fails the SnapValidator checks.
                This option only applies to non-root volumes.
                This option is unsupported in Data ONTAP Cluster-Mode.
                </dd><br>
                <dt>"thorough_scrub" (value: "on" | "off")</dt>
                <dd>
                <b>Traditional</b> volumes only.
                Setting the option to "on" enables thorough scrub
                on a block checksum volume.
                That means that a scrub will initialize any
                zeroed checksum entries that it finds.
                If there are any checksum entries to be initialized,
                scrub will run slower than normal.
                </dd><br>
                <dt>"snaplock_autocommit_period" (value: "none" | <count>
                h|d|m|y)</dt>
                <dd>
                <b>SnapLock</b> volumes only.
                This option defines the criteria for committing files to
                WORM on a SnapLock volume by the autocommit scanner.
                h, d, m, y denote hours, days, months and years
                respectively. The default value of this option
                is "none" that corresponds to autocommit being disabled in
                the SnapLock volume. The minimum autocommit period on a
                SnapLock volume is 2h. Any valid value other than "none",
                specified in hours (h), days (d), months (m) or years (y)
                would trigger the autocommit scanner on the Snaplock volume.
                </dd><br>
                <dt> "snaplock_default_period" (value : min | max | infinite |
                <count>s|h|d|m|y)</dt>
                <dd>
                This option can be set only for <b>SnapLock</b> volumes and
                specifies the default retention period that will be applied
                to files committed to WORM state without an associated
                retention period.
                If this option value is <b>min</b> then
                snaplock_minimum_period is used as the default retention
                period. If this option value is <b>max</b> then
                snaplock_maximum_period is used as the default retention
                period. If this option value is <b>infinite</b> then
                infinite retention period will be used as the
                default retention period.
                WORM files with infinite retention period are retained
                forever.
                The retention period can also be explicitly specified as a
                number followed by a suffix. The valid suffixes are <b>s</b>
                for seconds, <b>h</b> for hours, <b>d</b>
                for days, <b>m</b> for months and <b>y</b> for years.
                For example, a value of <b>6m</b> represents a retention
                period of 6 months. The maximum valid retention period is
                70 years. This option is not applicable while extending
                retention period of an already committed WORM file
                </dd><br>
                <dt> "snaplock_maximum_period" (value: infinite |
                <count>s|h|d|m|y)</dt>
                </dt>
                <dd>
                This option can be set only for <b>SnapLock</b> volumes
                and specifies the maximum allowed retention period for files
                committed to WORM state on the volume. Any file committed
                with a retention period longer than snaplock_maximum_period
                will be assigned a retention period equal to
                snaplock_maximum_period.
                If this option value is <b>infinite</b> then files can
                be committed for infinite retention period in the volume.
                WORM files with infinite retention period are retained
                forever.
                The retention period can also be explicitly specified as a
                number followed by a suffix.
                The valid suffixes are <b>s</b> for seconds,
                <b>h</b> for hours, <b>d</b>
                for days, <b>m</b> for months and <b>y</b> for years.
                For example, a value of <b>6m</b> represents a retention
                period of 6 months. The maximum valid retention period is
                70 years. This option is not applicable while extending
                retention period of an already committed WORM file
                </dd><br>
                <dt> "snaplock_minimum_period" (value: infinite |
                <count>s|h|d|m|y)</dt>
                </dt>
                <dd>
                This option can only be set for <b>SnapLock</b> volumes
                and specifies the minimum allowed retention period for files
                committed to WORM state on the volume. Any file committed
                with a retention period shorter than snaplock_minimum_period
                will be assigned a retention period equal to
                snaplock_minimum_period.
                If this option value is <b>infinite</b> then every file
                committed to the volume will have a infinite retention
                period.
                WORM files with infinite retention period are retained
                forever.
                The retention period can also be explicitly specified as a
                number followed by a suffix.
                The valid suffixes are <b>s</b> for seconds,
                <b>h</b> for hours, <b>d</b>
                for days, <b>m</b> for months and <b>y</b> for years.
                For example, a value of <b>6m</b> represents a retention
                period of 6 months. The maximum valid retention period is
                70 years. This option is not applicable while extending
                retention period of an already committed WORM file
                </dd><br>
                </dl>
        """
        return self.request( "volume-set-option", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'option_value': [ option_value, 'option-value', [ basestring, 'None' ], False ],
            'option_name': [ option_name, 'option-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_move_cutover(self, source_volume, cutover_window=None):
        """
        Initiates a manual cutover operation on the specified source volume.
        This is a synchronous API. Cutover is the final phase of
        volume move operation after which destination volume takes the
        identity of the source volume. If cutover cannot be
        initiated or completed, the API will return with an
        error. The move will pause and an EMS message will be printed.
        The volume-move-status API will show the state of the move as
        move(paused). The user can resume or abort the move.
        
        :param source_volume: Name of the volume, whose move is waiting for cutover to be initiated.
        
        :param cutover_window: Time interval to complete cutover in seconds. If not specified,
                then the existing value is maintained.
        """
        return self.request( "volume-move-cutover", {
            'cutover_window': [ cutover_window, 'cutover-window', [ int, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of volume objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume object.
                All volume objects matching this query up to 'max-records' will
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
        return self.request( "volume-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VolumeAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VolumeAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ VolumeAttributes, True ],
        } )
    
    def volume_get_limits(self, space_guarantee=None, data_aggr_list=None, enable_snapdiff=None, namespace_mirror_aggr_list=None, max_data_constituent_size=None, max_namespace_constituent_size=None, namespace_aggregate=None):
        """
        Return calculated volume limits, which are based on the current
        configuration of the Vserver.  If an Infinite Volume already
        exists on the Vserver, the values returned are in relation to
        the existing volume.
        <p>
        This API is not supported for Flexible Volumes.
        
        :param space_guarantee: Identifies the guarantee type for which the volume limits are
                calculated. If this argument is not provided, the default space
                guarantee option is 'volume'.
                <p>
                Possible values:
                <ul>
                <li> 'none',
                <li> 'volume' (default)
                </ul>
        
        :param data_aggr_list: Specifies an array of names of aggregates that would be used for
                Infinite Volume data constituents. If this input is not specified all
                the aggregates assigned to the Vserver are used.  This input is
                not supported if an Infinite Volume already exists on the
                Vserver.
        
        :param enable_snapdiff: Whether to enable Snapdiff. If enabled, the namespace mirrors
                will be calculated for Snapdiff use. The default value is false.
        
        :param namespace_mirror_aggr_list: Specifies an array of names of aggregates that would be used for
                Infinite Volume namespace mirror constituents. If this input is not
                specified all the aggregates assigned to the Vserver are used.
        
        :param max_data_constituent_size: The maximum size of each data constituent in bytes.  The default value
                is determined by checking the maximum FlexVol size setting on all nodes
                used by the Infinite Volume. The smallest value found is chosen as
                the default for the max-data-constituent-size for the Infinite Volume.
        
        :param max_namespace_constituent_size: The maximum size of the namespace constituent in bytes.  The
                default value is 10TB.
        
        :param namespace_aggregate: The name of the aggregate in which the namespace constituent
                would be created. If not provided, ONTAP will pick the best
                available aggregate assigned to the Vserver.  This input is
                not supported if an Infinite Volume already exists on the
                Vserver.
        """
        return self.request( "volume-get-limits", {
            'space_guarantee': [ space_guarantee, 'space-guarantee', [ basestring, 'None' ], False ],
            'data_aggr_list': [ data_aggr_list, 'data-aggr-list', [ basestring, 'aggr-name' ], True ],
            'enable_snapdiff': [ enable_snapdiff, 'enable-snapdiff', [ bool, 'None' ], False ],
            'namespace_mirror_aggr_list': [ namespace_mirror_aggr_list, 'namespace-mirror-aggr-list', [ basestring, 'aggr-name' ], True ],
            'max_data_constituent_size': [ max_data_constituent_size, 'max-data-constituent-size', [ int, 'None' ], False ],
            'max_namespace_constituent_size': [ max_namespace_constituent_size, 'max-namespace-constituent-size', [ int, 'None' ], False ],
            'namespace_aggregate': [ namespace_aggregate, 'namespace-aggregate', [ basestring, 'None' ], False ],
        }, {
            'max-infinitevol-size': [ int, False ],
            'min-infinitevol-size': [ int, False ],
        } )
    
    def volume_move_start(self, source_volume, dest_aggr, cutover_window=None, is_manual_cutover=None, is_override_warnings=None, cutover_attempts=None, vserver=None, is_keep_source=None, perform_validation_only=None, cutover_action=None):
        """
        This API is applicable to Data ONTAP 7-Mode as well as
        Data ONTAP Cluster-Mode.
        If the API is sent to a Data ONTAP 7-Mode controller,
        Vol Move will move a single 7-mode
        flexvol between two aggregates on the same controller.
        If the API is sent to the Admin Vserver LIF, the flexvol
        can be moved to any eligible aggregate in the cluster.
        The list of eligible aggregates can be obtained using
        the "volume-move-target-aggr-get-iter" API.
        This API will start the move. It will run a series of checks to
        determine if the volume can be moved. If any of the checks
        results in an error or warning, the API will return with an
        error. The user has to take the necessary corrective action
        before restarting the move. If all the checks pass, the API will
        return a success. If "perform-validation-only" is not true,
        the destination volume will be created and the move
        will start. By default, the move will cutover automatically.
        If "perform-validation-only" is set to true, all the errors and warnings
        encountered from the checks will be returned in the errors-warnings
        output element. The API will return successfully. The move will
        not be initiated.
        When the API is sent to a Data ONTAP 7-Mode controller,
        if "is-override-warnings" is set to true and the checks return no
        errors but one or more warnings, the API will return
        successfully. The warnings will be in the errors-warnings output
        element.
        If the API is sent to a Data ONTAP 7-Mode controller, the status
        of the move can be obtained using the "volume-move-status" API.
        If the move fails an EMS message will be generated. The reason for
        the failure can be obtained from the volume-move-status API.
        After a successful move, the source volume will be destroyed unless
        the user has specified the "is-keep-source" option. If cutover cannot be
        completed in the default or user specified number of attempts, an
        EMS message will be printed and the move will pause. The reason
        for the pause will be available in the "volume-move-status" API.
        The user can either resume or abort the move. This is an
        asynchronous API.
        If the API is sent to the Admin Vserver LIF, a background job will
        be created and the API returns immediately with the job ID
        information. The status of the move job can be obtained by using
        "job-get" or "job-get-iter" API.
        
        :param source_volume: Name of the volume that must be moved
        
        :param dest_aggr: Name of the destination aggregate
        
        :param cutover_window: Time interval to complete cutover in seconds. Default value
                for Data ONTAP Cluster-Mode volume move is 45 seconds. Default
                value for Data ONTAP 7-mode volume move is 60 seconds.
        
        :param is_manual_cutover: If specified, user has to initiate cutover. Default is false.
        
        :param is_override_warnings: If warnings are encountered during the move, the default
                behavior is to stop. If is-override-warnings is true, the move
                will continue and return these warnings in the errors-warnings
                element. Default is false.
        
        :param cutover_attempts: Number of cutover attempts. Default value is 3
        
        :param vserver: Name of the Vserver in which the volume to be moved resides.
                This value is required for C-Mode volumes.
        
        :param is_keep_source: If specified, the source volume will not be destroyed after
                the move is complete. Default is false.
        
        :param perform_validation_only: Run pre-checks for the move, return all the errors and
                warning messages encountered during the checks in the
                errors-warnings element and exit. The move will not be
                triggered. Default is false.
        
        :param cutover_action: Specifies the action to be taken for cutover.
                Possible values are "abort_on_failure", "defer_on_failure",
                "force" and "wait". Default is "defer_on_failure".
                If "abort_on_failure" action is specified, the job will try
                cutover till the cutover-attempts are exhausted, and cleanup
                if it fails to cutover.
                If "defer_on_failure" action is specified, the job will try
                cutover till the cutover-attempts are exhausted and move
                into "cutover deferred" state if it fails to cutover.
                This is the default option. The volume move job waits for
                intervention to restart the cutover process again.
                If "force" action is specified, the job will try cutover
                till the cutover-attempts are exhausted and force
                the cutover at the expense of disrupting the clients.
                If "wait" action is specified, when the job hits the decision
                point, it will not go into cutover automatically, instead it
                will wait for the user to issue a "volume-move-trigger-cutover"
                command as the signal to try the cutover.
        """
        return self.request( "volume-move-start", {
            'cutover_window': [ cutover_window, 'cutover-window', [ int, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'is_manual_cutover': [ is_manual_cutover, 'is-manual-cutover', [ bool, 'None' ], False ],
            'is_override_warnings': [ is_override_warnings, 'is-override-warnings', [ bool, 'None' ], False ],
            'cutover_attempts': [ cutover_attempts, 'cutover-attempts', [ int, 'None' ], False ],
            'dest_aggr': [ dest_aggr, 'dest-aggr', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'is_keep_source': [ is_keep_source, 'is-keep-source', [ bool, 'None' ], False ],
            'perform_validation_only': [ perform_validation_only, 'perform-validation-only', [ bool, 'None' ], False ],
            'cutover_action': [ cutover_action, 'cutover-action', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'errors-warnings': [ ErrorsWarningsInfo, True ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_autosize_set(self, volume, reset=None, increment_size=None, minimum_size=None, grow_threshold_percent=None, maximum_size=None, shrink_threshold_percent=None, is_enabled=None, mode=None):
        """
        Given the name of a flexible volume, set the autosize
        settings. This API is not supported for Infinite Volumes.
        
        :param volume: The name of the flexible volume for which we want to
                set autosize.
        
        :param reset: Sets the values of is-enabled, maximum size, increment-size,
                minimum-size, grow-threshold-percent, shrink-threshold-percent
                and mode to their defaults.
        
        :param increment_size: Specify the flexible volume's increment size using
                the following format
                &lt number &gt [k|m|g|t]
                The amount is the absolute size to set. The optional trailing
                'k', 'm', 'g', and 't' indicates the desired units,
                namely 'kilobytes', 'megabytes', 'gigabytes', and 'terabytes'
                (respectively).  If the trailing unit character doesn't
                appear, then &lt number &gt is interpreted as the number
                of bytes desired. The default value of increment size is 5%.
        
        :param minimum_size: Specify the flexible volume's minimum allowed size using
                the following format
                &lt number &gt [k|m|g|t]
                The amount is the absolute size to set. The optional trailing
                'k', 'm', 'g', and 't' indicates the desired units,
                namely 'kilobytes', 'megabytes', 'gigabytes', and 'terabytes'
                (respectively).  If the trailing unit character doesn't
                appear, then &lt number &gt is interpreted as the number
                of bytes desired. The default value is the size of the volume
                at the time the 'grow_shrink' mode was enabled. It is an error
                for the minimum size to be greater than or equal to the maximum
                size.
        
        :param grow_threshold_percent: Specifies the percentage of the flexible volume's capacity at
                which autogrow is initiated. The default grow threshold varies
                from 85% to 98%, depending on the volume size. It is an error
                for the grow threshold to be less than or equal to the shrink
                threshold.
                Range : [0..100]
        
        :param maximum_size: Specify the flexible volume's maximum allowed size using
                the following format
                &lt number &gt [k|m|g|t]
                The amount is the absolute size to set. The optional trailing
                'k', 'm', 'g', and 't' indicates the desired units,
                namely 'kilobytes', 'megabytes', 'gigabytes', and 'terabytes'
                (respectively).  If the trailing unit character doesn't
                appear, then &lt number &gt is interpreted as the number
                of bytes desired. The default value is 20% greater than the
                volume size at the time autosize was enabled. It is an error
                for the maximum volume size to be less than the current volume
                size. It is also an error for the maximum size to be less than
                or equal to the minimum size.
        
        :param shrink_threshold_percent: Specifies the percentage of the flexible volume's capacity
                at which autoshrink is initiated. The default shrink theshold
                is 50%. It is an error for the shrink threshold to be greater
                than or equal to the grow threshold.
                Range : [0..100]
        
        :param is_enabled: This element is deprecated in Data ONTAP 8.2 and later. Please
                use autosize-mode instead. Setting this parameter to 'true'
                enables the 'grow' mode, while setting it to 'false' disables
                autosize and sets the autosize mode to 'off'. The default value
                is 'false'.
        
        :param mode: Specify the flexible volume's autosize mode of operation.
                Valid values are "grow", "grow_shrink", and "off".
                The default mode is "off".
        """
        return self.request( "volume-autosize-set", {
            'reset': [ reset, 'reset', [ bool, 'None' ], False ],
            'increment_size': [ increment_size, 'increment-size', [ basestring, 'None' ], False ],
            'minimum_size': [ minimum_size, 'minimum-size', [ basestring, 'None' ], False ],
            'grow_threshold_percent': [ grow_threshold_percent, 'grow-threshold-percent', [ int, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'maximum_size': [ maximum_size, 'maximum-size', [ basestring, 'None' ], False ],
            'shrink_threshold_percent': [ shrink_threshold_percent, 'shrink-threshold-percent', [ int, 'None' ], False ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
            'mode': [ mode, 'mode', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_footprint_list_info_iter_next(self, tag, maximum):
        """
        Continues an iteration through the list of volumes.
        
        :param tag: Tag from a previous volume-footprint-list-info-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "volume-footprint-list-info-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'vol-footprint-infos': [ VolFootprintInfo, True ],
        } )
    
    def volume_online(self, name):
        """
        Bring the specified volume or the plex online. This
        command takes effect immediately.  If there are CIFS
        shares associated with the volume, they are enabled.
        Plexes are not supported for Cluster-Mode volumes.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param name: Name of an existing volume or plex.  If a volume is
                specified, it must be currently offline, restricted,
                or foreign.  If the volume is foreign, it will be made
                native before being brought online.  A ``foreign''
                volume is a traditional volume that consists of disks
                moved from another filer and that has never been brought
                online on the current filer.  Traditional volumes that
                are not foreign are considered ``native.''  If the
                volume is inconsistent, but has not lost data, it is
                advisable to run WAFL_check or wafliron (or do a
                'snapmirror initialize' in case of a replica volume)
                prior to bringing an inconsistent volume online.
                Bringing an inconsistent volume online increases the
                risk of further file system corruption.  If the volume
                is inconsistent and has experienced possible loss of
                data, it cannot be brought online unless WAFL_check
                or wafliron (or 'snapmirror initialize') has been run
                on the volume.
                If a plex is specified, the plex must be part of an
                online mirrored traditional volume or aggregate.
                The system will initiate resynchronization of the
                plex as part of online processing.
        """
        return self.request( "volume-online", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_space_list_info_iter_next(self, tag, maximum):
        """
        Continues an iteration through the list of volumes.
        
        :param tag: Tag from a previous volume-space-list-info-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "volume-space-list-info-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'vol-space-infos': [ VolSpaceInfo, True ],
        } )
    
    def volume_footprint_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display a list of volumes and their data and metadata
        footprints in their parent aggregate. The term footprint is used
        to refer to space that is considered used in an aggregate due to
        data in a specific volume.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume-footprint object.
                All volume-footprint objects matching this query up to
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
        return self.request( "volume-footprint-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FootprintInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FootprintInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FootprintInfo, True ],
        } )
    
    def volume_offline_async(self, volume_name):
        """
        Take the specified Infinite Volume offline,
        thereby making it unavailable for data access.
        The Infinite Volume must be unmounted
        before it can be made offline.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: Name of an existing Infinite Volume.
        """
        return self.request( "volume-offline-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_clone_create_async(self, parent_volume, volume, use_snaprestore_license=None, junction_active=None, space_reserve=None, junction_path=None, parent_snapshot=None):
        """
        Create a flexible volume that is a clone of a "backing"
        or "parent" flexible volume by spawning a background job.
        The jobid will be returned. The progress of the job can be
        tracked using the job APIs.
        This command fails if the chosen parent volume is
        currently involved in a split operation.  This
        command also fails if the chosen parent volume is
        a traditional volume.  Cloning is a new capability
        that applies exclusively to flexible volumes.
        
        :param parent_volume: Name of the parent flexible volume for the clone.
        
        :param volume: Desired name of the clone.
        
        :param use_snaprestore_license: If set to 'true', allows vol clone create if the SnapRestore
                license is installed, the FlexClone license is not required.
                If neither license is installed, vol clone create will fail.
                Default value is false.
                Note that FlexClone license is NOT required to use this input.
                THIS INPUT IS CURRENTLY SUPPORTED FOR USE ONLY BY SMVI,
                ANY OTHER USE IS NOT SUPPORTED.
        
        :param junction_active: This field indicates whether the mounted volume is
                accessible. The default is true. If the mounted junction
                path is not accessible, the volume does not appear in the
                owning Vserver's namespace. This field applies
                only to Cluster-Mode volumes.
        
        :param space_reserve: Specifies the type of volume guarantee for the clone.
                Possible values: none, file, volume.  If this argument
                is not provided, then guarantee type is inherited from
                parent volume.
        
        :param junction_path: The Junction Path at which this volume is to be mounted.
                <p>
                The fully-qualified pathname in the owning Vserver's namespace at
                which a volume is mounted.  Note that this pathname may itself
                contain junctions, one for each volume (other than the namespace
                root volume) that provides storage along the pathname's length.
                As with all fully-qualified pathnames , this string must begin
                with '/'.  In addition, it must not end with '/'.
                <p>
                An example of a valid junction path is: '/user/my_volume'.
                <p>
                Only one volume can be mounted at any given junction path.
                If an incorrect junction path is specified,
                EINVALIDINPUTERROR is returned. If another
                volume is mounted at the specified junction path,
                EVOL_ALREADY_MOUNTED is returned.
        
        :param parent_snapshot: Name of the snapshot within 'parent-volume' that is to
                serve as the parent snapshot for the clone.  If not
                provided, the filer will create a new snapshot named
                'clone_parent_<UUID>' (using a freshy-generated UUID)
                in 'parent-volume' for this purpose.
        """
        return self.request( "volume-clone-create-async", {
            'use_snaprestore_license': [ use_snaprestore_license, 'use-snaprestore-license', [ bool, 'None' ], False ],
            'parent_volume': [ parent_volume, 'parent-volume', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'junction_active': [ junction_active, 'junction-active', [ bool, 'None' ], False ],
            'space_reserve': [ space_reserve, 'space-reserve', [ basestring, 'None' ], False ],
            'junction_path': [ junction_path, 'junction-path', [ basestring, 'None' ], False ],
            'parent_snapshot': [ parent_snapshot, 'parent-snapshot', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_move_target_aggr_get_iter(self, vserver, volume_name, max_records=None, desired_attributes=None, tag=None, query=None):
        """
        Scans aggregates and returns a list of compatible target
        aggregates for the given volume move operation.
        
        :param vserver: Vserver Name (Required field)
        
        :param volume_name: Volume Name (Required field)
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume object.
                All volume objects matching this query up to 'max-records' will
                be returned.
        """
        return self.request( "volume-move-target-aggr-get-iter", {
            'max_records': max_records,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VolumeMoveTargetAggrInfo, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'tag': tag,
            'query': [ query, 'query', [ VolumeMoveTargetAggrInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VolumeMoveTargetAggrInfo, True ],
        } )
    
    def volume_size(self, volume, new_size=None):
        """
        Given the name of a flexible volume, either return its
        current size or set the volume's size to the stated
        amount.
        <p>
        This API is not supported for Infinite Volumes.
        Also, this API does not allow to set the volume's size from
        vFiler context.
        
        :param volume: The name of the flexible volume for which we want to
                get or set its size.
        
        :param new_size: Specify the flexible volume's new size using the
                following format:
                [+|-]&lt number &gt k|m|g|t]
                If a leading '+' or '-' appears, it indicates that the
                given flexible volume's size is to be increased or
                decreased (respectively) by the indicated amount, else
                the amount is the absolute size to set.
                The optional trailing 'k', 'm', 'g', and 't' indicates
                the desired units, namely 'kilobytes', 'megabytes',
                'gigabytes', and 'terabytes' (respectively).  If the
                trailing unit character doesn't appear, then &lt number &gt
                is interpreted as the number of bytes desired.
                The file system size of a readonly replica flexible volume,
                such as a snapmirror destination, is determined from the
                replica source. In such cases, the value set using
                "volume-size" is interpreted as an upper limit on the size.
                A flexible volume that's not a readonly replica which has
                the "fs_size_fixed" option set may have its size displayed,
                but not changed.  Attempting to set the volume size in this
                case will result in failure and a EINTERNALERROR error code.
                Users must be able to adjust readonly replica flexible
                volume size in order to maintain enough capacity to
                accommodate transfers from the replica source.  Attempting
                to set a readonly replica destination size to be less than
                that of its source will result in a failure indicated by the
                EONTAPI_ENOSPC error code.
                This option is not applicable from vFiler context. Attempting
                to set volume size from vfiler context will result in failure
                with EINTERNALERROR error code being returned.
        """
        return self.request( "volume-size", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'new_size': [ new_size, 'new-size', [ basestring, 'None' ], False ],
        }, {
            'is-fixed-size-flex-volume': [ bool, False ],
            'is-readonly-flex-volume': [ bool, False ],
            'is-replica-flex-volume': [ bool, False ],
            'volume-size': [ basestring, False ],
        } )
    
    def volume_restrict(self, name, cifs_delay=None):
        """
        Restrict the specified volume, making it unavailable
        for user-level data access but leaving it (or its
        containing aggregate, if it's a flexible volume)
        available to internal OnTAP RAID-level access.
        <p>
        This API is not supported for Infinite Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param name: Name of the volume to restrict.
        
        :param cifs_delay: If a volume contains CIFS shares, users should be warned
                before restricting the volume . This argument specifies
                the number of minutes to delay before restricting the
                volume, during which time CIFS users are warned of the
                pending loss of service.  A 'cifs-delay' time of 0 means
                that the volume is to be restricted immediately without
                issuing any warnings.  CIFS users can lose data if they
                are not given a chance to terminate applications
                gracefully.  By default, the value of 'cifs-delay' is 0.
        """
        return self.request( "volume-restrict", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'cifs_delay': [ cifs_delay, 'cifs-delay', [ int, 'None' ], False ],
        }, {
        } )
    
    def volume_transition_protect(self, vserver, volume, is_enabled):
        """
        Fence access to volume during Transition.
        
        :param vserver: The name of the Vserver which owns the volume.
        
        :param volume: The name of the volume.
        
        :param is_enabled: Protection Enabled
        """
        return self.request( "volume-transition-protect", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_destroy_async(self, volume_name):
        """
        Destroy an Infinite Volume.
        The Infinite Volume must be unmounted and must be offline
        before it can be destroyed.
        <p>
        This API is not supported for Flexible Volumes. This API is not
        supported on Infinite Volume constituents.
        
        :param volume_name: Name of an existing Infinite Volume.
        """
        return self.request( "volume-destroy-async", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def volume_clone_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display a list of FlexClone volumes
        
        :param max_records: The maximum number of records to return in this call.
                Default: 10
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume object.
                All volume objects matching this query up to 'max-records' will
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
        return self.request( "volume-clone-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VolumeCloneInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VolumeCloneInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VolumeCloneInfo, True ],
        } )
    
    def volume_space_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display a list of volumes and a breakup of their
        used space. This information is only available when the volume
        is online
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                volume-space object.
                All volume-space objects matching this query up to 'max-records'
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
        return self.request( "volume-space-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SpaceInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SpaceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SpaceInfo, True ],
        } )
    
    def volume_destroy(self, name, force=None, unmount_and_offline=None):
        """
        Destroy the specified volume or plex.  If a flexible
        volume is specified, all of its blocks are freed and
        returned to its containing aggregate; no other flexible
        volumes in the same containing aggregate (if any) are
        affected.  If a traditional volume is specified, all
        of its plexes are destroyed, and its disks are
        returned to the appropriate spare pool(s).  If a plex
        is specified, it must be for a mirrored aggregate
        (which could potentially be embedded in a traditional
        volume), leaving it unmirrored.  Only offline volumes
        and plexes can be destroyed. Plexes are not supported
        for Cluster-Mode volumes.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param name: Name of an existing volume or plex.
        
        :param force: Force the destruction of the volume even if a
                non-default vfiler has storage on it.  Normally,
                the system will not destroy such a volume and
                will instead return EVOLUME_HAS_VFILER_STORAGE.
        
        :param unmount_and_offline: If set to 'true', then volume will be destroyed by doing the
                following things:
                1). If the volume is in mounted state, then it will be unmounted.
                2). If the volume is not in offline state, then it will be
                offlined.
                Default value is false.
                THIS INPUT IS CURRENTLY SUPPORTED FOR USE ONLY BY MEI,
                ANY OTHER USE IS NOT SUPPORTED.
        """
        return self.request( "volume-destroy", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'unmount_and_offline': [ unmount_and_offline, 'unmount-and-offline', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_move_pause(self, source_volume):
        """
        Pauses the volume move operation of the specified source volume. This is a synchronous API.
        
        :param source_volume: Name of the volume whose move must be paused
        """
        return self.request( "volume-move-pause", {
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_move_trigger_cutover(self, source_volume, vserver=None, force=None):
        """
        Trigger cutover of a move job
        
        :param source_volume: The name of the volume.
        
        :param vserver: Name of the Vserver in which the volume to be moved resides.
                This value is required for C-Mode volumes.
        
        :param force: Force cutover
        """
        return self.request( "volume-move-trigger-cutover", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'source_volume': [ source_volume, 'source-volume', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def volume_rename(self, volume, new_volume_name):
        """
        Renames the specified volume to a new name specified by
        "new-volume-name". If the volume is referenced in the
        /etc/exports file, remember to make the name change in
        /etc/exports also so that the affected file system can
        be exported by the filer after the filer reboots. The
        "volume-rename" command does not automatically update
        the /etc/exports file.
        <p>
        This API is not supported for Infinite Volumes.
        
        :param volume: Name of an existing volume.
        
        :param new_volume_name: New volume name.
        """
        return self.request( "volume-rename", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'new_volume_name': [ new_volume_name, 'new-volume-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def volume_clone_create(self, parent_volume, volume, use_snaprestore_license=None, force_worm_clone=None, junction_active=None, qos_policy_group_name=None, space_reserve=None, junction_path=None, parent_snapshot=None, volume_type=None):
        """
        Create a flexible volume that is a clone of a "backing"
        or "parent" flexible volume.  A clone is a volume that
        is a writable snapshot of another volume.  Initially,
        the clone and its parent share the same storage; more
        storage space is consumed only as one volume or the
        other changes.
        If a specific snapshot name within the parent volume
        is provided, it is chosen as the parent snapshot.
        Otherwise, the filer will create a new, distinctively-
        named snapshot in the parent volume for that purpose.
        The parent snapshot is locked in the parent volume,
        preventing its deletion until the clone is either
        destroyed or split from the parent using the
        'volume-clone-split-start' command (see below).
        This command fails if the chosen parent volume is
        currently involved in a split operation.  This
        command also fails if the chosen parent volume is
        a traditional volume.  Cloning is a new capability
        that applies exclusively to flexible volumes.
        
        :param parent_volume: Name of the parent flexible volume for the clone.
        
        :param volume: Desired name of the clone.
        
        :param use_snaprestore_license: If set to 'true', allows vol clone create if the SnapRestore
                license is installed, the FlexClone license is not required.
                If neither license is installed, vol clone create will fail.
                Default value is false.
                Note that FlexClone license is NOT required to use this input.
                THIS INPUT IS CURRENTLY SUPPORTED FOR USE ONLY BY SMVI,
                ANY OTHER USE IS NOT SUPPORTED.
        
        :param force_worm_clone: If set to 'true', forces the creation of clone on a worm volume.
                If set to 'false', clone creation on any worm volume will
                fail, because clones of worm volumes are not deletable until
                all the inherited worm files on newly created clone have
                expired.  Default value is false.
        
        :param junction_active: This field indicates whether the mounted volume is
                accessible. The default is true. If the mounted junction
                path is not accessible, the volume does not appear in the
                owning Vserver's namespace. This field applies
                only to Cluster-Mode volumes.
        
        :param qos_policy_group_name: The QoS Policy Group Name that is to be associated with this
                FlexClone volume in order to enforce Service Level
                Objectives (SLO). If you do not assign a QoS policy group
                to a volume, the system will not monitor and control the
                traffic to it.
                Note that "none" is a reserved keyword used to remove the
                association of a storage object to a QoS policy group.
                Specifying "none" as a QoS policy group in this command
                would have no effect.
        
        :param space_reserve: Specifies the type of volume guarantee for the clone.
                Possible values: none, file, volume.  If this argument
                is not provided, then guarantee type is inherited from
                parent volume.
        
        :param junction_path: The Junction Path at which this volume is to be mounted.
                <p>
                The fully-qualified pathname in the owning Vserver's namespace at
                which a volume is mounted.  Note that this pathname may itself
                contain junctions, one for each volume (other than the namespace
                root volume) that provides storage along the pathname's length.
                As with all fully-qualified pathnames , this string must begin
                with '/'.  In addition, it must not end with '/'.
                <p>
                An example of a valid junction path is: '/user/my_volume'.
                <p>
                Only one volume can be mounted at any given junction path.
                If an incorrect junction path is specified,
                EINVALIDINPUTERROR is returned. If another
                volume is mounted at the specified junction path,
                EVOLALREADYMOUNTED is returned.
        
        :param parent_snapshot: Name of the snapshot within 'parent-volume' that is to
                serve as the parent snapshot for the clone.  If not
                provided, the filer will create a new snapshot named
                'clone_parent_<UUID>' (using a freshy-generated UUID)
                in 'parent-volume' for this purpose.
        
        :param volume_type: The type of the volume to be created.
                Possible values:
                <ul>
                <ul> "rw"   - read-write volume (default setting),
                <ul> "dp"   - data-protection volume
                </ul>
                If not provided, the filer will assume the default value i.e.
                "rw" volume. Creation of data-protection volume clone is only
                allowed from parent-volume which is paloma logical DP volume.
        """
        return self.request( "volume-clone-create", {
            'use_snaprestore_license': [ use_snaprestore_license, 'use-snaprestore-license', [ bool, 'None' ], False ],
            'parent_volume': [ parent_volume, 'parent-volume', [ basestring, 'None' ], False ],
            'force_worm_clone': [ force_worm_clone, 'force-worm-clone', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'junction_active': [ junction_active, 'junction-active', [ bool, 'None' ], False ],
            'qos_policy_group_name': [ qos_policy_group_name, 'qos-policy-group-name', [ basestring, 'None' ], False ],
            'space_reserve': [ space_reserve, 'space-reserve', [ basestring, 'None' ], False ],
            'junction_path': [ junction_path, 'junction-path', [ basestring, 'None' ], False ],
            'parent_snapshot': [ parent_snapshot, 'parent-snapshot', [ basestring, 'None' ], False ],
            'volume_type': [ volume_type, 'volume-type', [ basestring, 'None' ], False ],
        }, {
        } )
