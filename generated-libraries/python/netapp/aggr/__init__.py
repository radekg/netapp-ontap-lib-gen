from netapp.connection import NaConnection
from aggr_status_attributes import AggrStatusAttributes # 1 properties
from raidgroup_get_iter_key_td import RaidgroupGetIterKeyTd # 3 properties
from aggr_relocation_info import AggrRelocationInfo # 4 properties
from aggr_start_attributes import AggrStartAttributes # 2 properties
from aggrstate import Aggrstate # 0 properties
from aggr_64bit_upgrade_check_info import Aggr64BitUpgradeCheckInfo # 4 properties
from aggr_volume_count_attributes import AggrVolumeCountAttributes # 5 properties
from aggr_check_attributes import AggrCheckAttributes # 4 properties
from volume_space_info import VolumeSpaceInfo # 4 properties
from aggr_performance_attributes import AggrPerformanceAttributes # 2 properties
from aggr_fs_attributes import AggrFsAttributes # 3 properties
from aggr_inode_attributes import AggrInodeAttributes # 9 properties
from ha_policy_type import HaPolicyType # 0 properties
from raidgroup_info import RaidgroupInfo # 9 properties
from aggr_attributes import AggrAttributes # 17 properties
from aggr_option_info import AggrOptionInfo # 2 properties
from striping_type import StripingType # 0 properties
from raidgroup_attributes import RaidgroupAttributes # 7 properties
from aggr_64bit_upgrade_info import Aggr64BitUpgradeInfo # 3 properties
from aggr_snaplock_attributes import AggrSnaplockAttributes # 2 properties
from aggr_get_iter_key_td import AggrGetIterKeyTd # 3 properties
from plex_attributes import PlexAttributes # 8 properties
from aggrchecksumstyle import Aggrchecksumstyle # 0 properties
from snapshot_space_info import SnapshotSpaceInfo # 13 properties
from aggr_64bit_upgrade_attributes import Aggr64BitUpgradeAttributes # 3 properties
from aggregate_space_info import AggregateSpaceInfo # 2 properties
from aggr_snapmirror_attributes import AggrSnapmirrorAttributes # 3 properties
from aggr_ownership_attributes import AggrOwnershipAttributes # 4 properties
from aggr_64bit_upgrade_start_info import Aggr64BitUpgradeStartInfo # 2 properties
from aggr_info import AggrInfo # 55 properties
from aggrraidtype import Aggrraidtype # 0 properties
from fs_space_info import FsSpaceInfo # 21 properties
from blocktype import Blocktype # 0 properties
from verify_detail_info import VerifyDetailInfo # 3 properties
from prev_cp_inofile_info import PrevCpInofileInfo # 2 properties
from warning_code import WarningCode # 1 properties
from aggr_raid_attributes import AggrRaidAttributes # 20 properties
from aggr_space_attributes import AggrSpaceAttributes # 9 properties
from aggrverifyactiontype import Aggrverifyactiontype # 0 properties
from disk_info import DiskInfo # 1 properties
from aggr_relocation_status_key_td import AggrRelocationStatusKeyTd # 2 properties
from aggrhapolicy import Aggrhapolicy # 0 properties
from aggr_wafliron_attributes import AggrWaflironAttributes # 5 properties
from aggr_64bit_upgrade_status_info import Aggr64BitUpgradeStatusInfo # 8 properties
from plex_info import PlexInfo # 8 properties
from aggr_wafliron_info import AggrWaflironInfo # 5 properties
from aggrfreespacerealloc import Aggrfreespacerealloc # 0 properties
from aggr_space_info import AggrSpaceInfo # 13 properties
from filter_attrs_info import FilterAttrsInfo # 7 properties
from contained_volume_info import ContainedVolumeInfo # 2 properties
from mirror_count_info import MirrorCountInfo # 4 properties
from raid_group_info import RaidGroupInfo # 11 properties
from aggr_striping_attributes import AggrStripingAttributes # 1 properties
from aggr_snapshot_attributes import AggrSnapshotAttributes # 13 properties

class AggrConnection(NaConnection):
    
    def aggr_set_option(self, aggregate, option_value, option_name):
        """
        Set the specified option for the given aggregate
        to "option-value".  The change remains effective
        even if the filer is rebooted.   Some options have
        values that are numbers, and some have values that
        are "on" (also expressible as "yes", "true", or "1" )
        or "off" (also expressible as "no", "false", or "0").
        A mixture of uppercase and lowercase characters may
        be used when typing an option's value.  Note that
        the "root" option is special in that it doesn't have
        a corresponding value.
        This API does not support modifying options of striped aggregate.
        
        :param aggregate: Name or UUID of the aggregate whose option to be set.
                See the synopsis for name/UUID format and restrictions.
        
        :param option_value: The value to set the named option.  It may be the
                NULL/empty value only in the case of the "root"
                option.
        
        :param option_name: Option name.  Possible values:
                <dl>
                <dt>"free_space_realloc" (value: "on" | "off" | "no_redirect")</dt>
                <dd>
                Setting this option to "on" enables free space
                reallocation (continuous segment cleaning)
                on a block checksum aggregate.
                Possible values : on, off, no_redirect
                "on" : Free space reallocation enabled
                with automatically starting the
                redirect scanner
                "off": Free space reallocate disabled
                "no_redirect": Free space reallocation enabled
                without running the redirect scanner
                The default value for this option is "off"
                </dd><br>
                <dt>"fs_size_fixed" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" causes the file
                system to remain the same size (and not grow)
                when the mirror is broken on a SnapMirrored
                aggregate (which MUST be embedded in a
                traditional volume), or when an "aggr add" is
                performed on it.  This option is automatically
                set to be "on" when an aggregate becomes
                SnapMirrored.  It remains "on" after the
                "snapmirror break" command is issued for an
                aggregate embedded in a traditional volume.
                This option allows an embedded aggregate to be
                SnapMirrored back to the source without needing
                to add disks to the source aggregate.  If the
                aggregate size is larger than the file system
                size, turning off this option forces the file
                system to grow to the size of the aggregate.
                This option is not supported when the request is
                sent to the Admin Vserver LIF.
                </dd><br>
                <dt>"ha_policy" (value: "cfo" | "sfo")</dt>
                <dd>
                This option is used to change the HA policy
                of given aggregate and restricted to clustered
                environments. It is not allowed in unclustered
                environments. Also this option does not apply to
                traditional volume. Changing the HA policy of an
                aggregate from SFO to CFO is allowed only in
                Maintenance mode. HA policy can not be changed if:
                1. aggregate is striped.
                2. aggregate contains node volumes.
                3. aggregate is root.
                4. aggregate is partner aggregate during takeover i.e.
                when it is not home to local node.
                EOP_CLUSTER_ATTR_DISALLOWED is returned if this option
                is used in unclustered environments.
                EOP_DISALLOWED_ON_STRIPED_AGGR is returned if this option
                is used with striped aggregate.
                EOP_DISALLOWED_ON_AGGR_WITH_NODE_VOLS is returned if this
                option is used on aggregate which contains node volumes.
                EOP_DISALLOWED_ON_ROOT_AGGR is returned if this option
                is used on root aggregate.
                EOP_DISALLOWED_ON_NOT_HOME_AGGR is returned if this
                option is used on partner aggregate during takeover.
                </dd><br>
                <dt>"ignore_inconsistent" (value: "on" | "off")</dt>
                <dd>
                This command can only be used in maintenance
                mode.  If this option is set to "on", then the
                root aggregate may be brought online when
                booting even if it is marked as inconsistent.
                The user is cautioned that bringing it online
                prior to running WAFL_check or wafliron may
                result in further file system inconsistency.
                This option is not supported when the request is
                sent to the Admin Vserver LIF.
                </dd><br>
                <dt>"lost_write_protect" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "off" disables lost write
                protection on the aggregate. The default is "on".
                The user is cautioned that turning off this option
                may expose the filesystem(s) contained in the aggregate
                to data loss and data corruption. This option should
                not be disabled, unless directed to do so by support
                personnel.
                </dd><br>
                <dt>"max_write_alloc_blocks" (value: value: &lt number &gt)</dt>
                <dd>
                The maximum number of blocks used for write allocation.
                Some sequential read workloads may benefit from increasing
                this value. Default value is 0 which uses the
                controller-wide default value of 64. The default is optimal
                for most users. The controller-wide default can be adjusted
                with the bootarg "wafl-max-write-alloc-blocks"
                </dd><br>
                <dt>"striping" (value: "striped" | "not_striped")</dt>
                <dd>
                This option sets the striping information of
                given aggregate. It is restricted to clustered
                environments and not allowed in unclustered environments.
                When set to true, it marks given aggregate as
                member of stripe. This option is not allowed
                if given aggregate is of 'cfo' HA policy. Also
                this option does not apply to traditional volume.
                EOP_CLUSTER_ATTR_DISALLOWED is returned if this option
                is used in unclustered environments.
                EOP_DISALLOWED_ON_CFO_AGGR is returned if given
                aggregate is of 'cfo' HA policy.
                This option is not supported when the request is
                sent to the Admin Vserver LIF.
                </dd><br>
                <dt>"nosnap" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" disables automatic
                snapshots on the aggregate.
                </dd><br>
                <dt>"raid_cv" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "off" disables block or advanced_zoned checksum (azcs)
                protection on the aggregate.  The default is "on".
                The user is cautioned that turning off this option
                exposes the filesystems contained in the aggregate to
                inconsistency that could be caused by a misbehaving
                hardware component in the system.
                </dd><br>
                <dt>"raid_lost_write" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "off" disables RAID Lost Write
                protection on the aggregate. The default is "on".
                The user is cautioned that turning off this option
                may expose the filesystem(s) contained in the aggregate
                to data loss and data corruption. The option should
                not be disabled, unless directed to do so by support
                personnel.
                </dd><br>
                <dt>"raid_zoned" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "off" disables zoned checksum
                protection on the aggregate.  The default is "on".
                The user is cautioned that turning off this option
                exposes the filesystems contained in the aggregate to
                inconsistency that could be caused by a misbehaving
                hardware component in the system.
                </dd><br>
                <dt>"raidsize" (value: &lt number &gt>)</dt>
                <dd>
                The maximum size of a RAID group within the
                aggregate.  Changing this option doesn't cause
                existing RAID groups to grow or shrink.
                Rather, it only affects whether more disks
                will be added to the last existing RAID group
                in the future, and how large new RAID groups
                will be.
                </dd><br>
                <dt>"cache_raid_group_size" (value: &lt number &gt>)</dt>
                <dd>
                The current maximum size of a SSD RAID group within the
                hybrid aggregate. This option can only be modified for hybrid
                aggregate. Changing this option doesn't cause
                existing RAID groups to grow or shrink.
                Rather, it only affects whether more disks
                will be added to the existing SSD RAID group
                in the future, and how large new SSD RAID groups
                will be.
                </dd><br>
                <dt>"raidtype" (value: "raid4" | "raid_dp" | "raid0")</dt>
                <dd>
                The type of RAID group used for this aggregate.
                The "raid4" setting  provides one parity disk per
                RAID group, while "raid_dp" provides two.
                Changing this option immediately changes the RAID
                group type for all RAID groups in the aggregate.
                When upgrading RAID groups from "raid4" to
                "raid_dp", each RAID group begins a reconstruction
                onto a spare disk allocated for the second
                "dparity" parity disk.
                </dd><br>
                <dt>"resyncsnaptime" (value: &lt number &gt)</dt>
                <dd>
                Sets the mirror resynchronization snapshot
                frequency to be the given number of minutes.
                The default value is 60 (minutes).
                </dd><br>
                <dt>"root" (value: &lt none &gt)</dt>
                <dd>
                The specified aggregate is to become the root
                aggregate for the filer on the next reboot.
                This option can be used only in maintenance mode
                and on only one aggregate at any given time.
                The existing root aggregate will become a
                non-root aggregate after the reboot. Until the
                system is rebooted, the original aggregate
                will continue to show root as an option, and
                the new root aggregate will show diskroot as
                an option.  In general, the aggregate that has
                the diskroot option is the one that becomes
                the root aggregate following the next reboot.
                The only way to remove the root status of an
                aggregate is to set it on another aggregate.
                In clustered environments, this option is not
                allowed with aggregates with 'sfo' HA policy as
                root has to be an aggregate with 'cfo' HA policy.
                EOP_DISALLOWED_ON_SFO_AGGR is returned if given
                aggregate is of 'sfo' HA policy.
                </dd><br>
                <dt>"snapmirrored" (value : "off")</dt>
                <dd>
                If SnapMirror is enabled, the filer auto-
                matically sets this option to "on".  Set this
                option to "off"  with the "snapmirror" command
                if SnapMirror should no longer be used to update
                the mirror.  After setting this option to "off",
                the mirror becomes a regular writable aggregate,
                and all its volumes are restored to whatever
                state they were last in.  Note that it is not
                possible to set this option directly through
                this interface.  Rather, it is automatically
                changed as a side effect of running the
                appropriate "snapmirror" commands.
                This option is not supported when the request is
                sent to the Admin Vserver LIF.
                </dd><br>
                <dt>"snapshot_autodelete" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "off" disables automatic
                snapshot deletion on the aggregate.
                </dd><br>
                <dt>"thorough_scrub" (value: "on" | "off")</dt>
                <dd>
                Setting this option to "on" enables thorough scrub
                on a block checksum aggregate.
                That means that a scrub will initialize any
                zeroed checksum entries that it finds.
                If there are any checksum entries to be initialized,
                scrub will run slower than normal.
                </dd><br>
                <dt>"percent_snapshot_space" (value: &lt number &gt)</dt>
                <dd>
                Percentage of total blocks in the aggregate reserved
                for snapshots.
                </dd><br>
                <dt>"hybrid_enabled" (value: "true" | "false")</dt>
                <dd>
                Setting this option to "true" would mark the aggregate as
                hybrid_enabled. That means the aggregate can contain a mix of SSDs
                and HDDs(Hard Disk Drives, e.g., SAS, SATA, and/or FC).
                The operation can be forced by using the hybrid_enabled_force option
                for the aggregates having flexvols which cannot be write cached.
                EAGGR_CANT_UNDO_HYBRID is returned when we are trying to
                set the option hybrid_enabled to false on an aggregate that
                already contains a mix of HDDs and SSDs.
                EAGGR_HYBRID is returned when we are trying to set option
                hybrid_enabled to true on an aggregate which is already hybrid.
                EOP_DISALLOWED_WORM_HYBRID_AGGR is returned when we are trying to
                set option hybrid_enabled to true on an snaplock aggregate.
                ERAID_HYA_SUPPORT_DISABLED is returned when the partner node in
                HA pair is running a version of Data ONTAP which does not support
                hybrid aggregates.
                EOP_DISALLOWED_ON_SSD_AGGR is returned if this option is
                used on aggregates created out of SSD disks.
                EOP_DISALLOWED_HYA_ON_RAID0_AGGR is returned if this option is
                used on raid0 aggregates.
                EOP_DISALLOWED_HYA_ON_ZONED_AGGR is returned if this option is
                used on aggregates with zoned checksums.
                EOP_DISALLOWED_HYA_ON_LUNS_AGGR is returned if this option
                used on aggregates created out of LUNs.
                </dd><br>
                <dt>"hybrid_enabled_force" (value: "true" | "false")</dt>
                <dd>
                Setting this option to "true" would mark the aggregate as
                hybrid_enabled. That means the aggregate can contain a mix of SSDs
                and HDDs(Hard Disk Drives, e.g., SAS, SATA, and/or FC).
                This option is used for force marking of aggregates having flexvols
                which cannot be write cached as hybrid enabled. FlexVols in the
                aggregate marked as hybrid enabled using this option which cannot
                participate in write-caching only have read-caching enabled.
                All other flexvols in the aggregate can participate in both read and
                write caching.
                EAGGR_CANT_UNDO_HYBRID is returned when we are trying to
                set the option hybrid_enabled_force to false on an aggregate that
                already contains a mix of HDDs and SSDs.
                EAGGR_HYBRID is returned when we are trying to set option
                hybrid_enabled_force to true on an aggregate which is already hybrid.
                EOP_DISALLOWED_WORM_HYBRID_AGGR is returned when we are trying to
                set option hybrid_enabled_force to true on an snaplock aggregate.
                ERAID_HYA_SUPPORT_DISABLED is returned when the partner node in
                HA pair is running a version of Data ONTAP which does not support
                hybrid aggregates.
                EOP_DISALLOWED_ON_SSD_AGGR is returned if this option is
                used on aggregates created out of SSD disks.
                EOP_DISALLOWED_HYA_ON_RAID0_AGGR is returned if this option is
                used on raid0 aggregates.
                EOP_DISALLOWED_HYA_ON_ZONED_AGGR is returned if this option is
                used on aggregates with zoned checksums.
                </dd><br>
                </dl>
        """
        return self.request( "aggr-set-option", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'option_value': [ option_value, 'option-value', [ basestring, 'None' ], False ],
            'option_name': [ option_name, 'option-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_wafliron_reject(self, aggregate_uuid):
        """
        Invoke "IOC reject", to discard the IOC to-be-made changes.
        IOC, or Wafliron Optional Commit, is a special mode of
        Wafliron, in which users will be able to choose to accept
        or reject Wafliron changes.
        <p>
        This interface returns as soon as possible after it sends
        the request for IOC reject operation.  There will be a
        time window before the reject request starts being processed.
        <p>
        Because the ZAPI returns immediately after sending the
        reject, the final result of the reject operation will not
        be known until it is finished.  If any early checks of this
        operation fail, an appropriate error code is returned.
        Otherwise, user must check the success of the reject
        operation by checking the EMS messages, or by checking the
        status of the aggregate or traditional volume by calling
        'aggr-list-info' ZAPI.
        <p>
        IOC reject operation is an advanced operation.  It must
        be run only by the technical support of the vendor.
        <p>
        USAGE:
        <p>
        IOC is invoked on aggregates or traditional volumes.
        It stores the changes that will be made to file system
        somewhere out of the file system.  Users can accept or
        reject the changes after reviewing the changes.  If user
        does not accept the changes that IOC will do, IOC reject
        operation can be used to discard the to-be-made changes.
        That is, the file system state will not change at all.
        <p>
        WHAT IT DOES:
        <p>
        IOC reject operation discards the to-be-made changes without
        writing them to the aggregate or traditional volume.
        <p>
        CAVEAT:
        <p>
        After the IOC reject operation returns, there will no
        way to abort it.
        <p>
        AFTER IT COMPLETES:
        <p>
        At the end of reject operation, an asynchronous offline
        request is issued to offline the aggregate or traditional
        volume.  There might be delay before the offline request
        starts being processed.  It might also take some time to
        finish offlining all the volumes inside an aggregate and
        eventually the aggregate itself.
        <p>
        LOGGING and EMS:
        All the messages related to the IOC reject operation are
        logged by issuing WAFL EMS messages.
        
        :param aggregate_uuid: UUID of the aggregate or traditional volume on which
                IOC reject will be started.
                <p>
                For more information about UUID, please refer to
                the description of the 'aggregate' input of the
                'aggr-wafliron-start' ZAPI.
        """
        return self.request( "aggr-wafliron-reject", {
            'aggregate_uuid': [ aggregate_uuid, 'aggregate-uuid', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_64bit_upgrade_scan_stop(self, aggregate):
        """
        Stop the 64-bit upgrade scanner on the specified
        aggregate. Use the 'aggr-list-info' API to query the
        status of the 64-bit upgrade scanner. The status is
        made available in the 'status' element that is part of
        the 'aggr-64bit-upgrade-info' typedef. Similarly, use
        the 'd-volume-list-info' API to query the status of
        the 64-bit upgrade scanner running on each contained
        flexible volume.
        
        :param aggregate: Name or UUID of the aggregate for which to stop
                the 64-bit upgrade scanner.
        """
        return self.request( "aggr-64bit-upgrade-scan-stop", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_scrub_suspend(self, aggregate=None, raidgroup=None, plex=None):
        """
        Suspend parity scrubbing on the named aggregate, plex,
        or RAID group.  If no name is given, suspend scrubbing
        on all RAID groups currently being scrubbed.
        Use "aggr-scrub-list-info" to check scrubbing status.
        
        :param aggregate: Name or UUID of the entity for which scrubbing is to suspend.
                See the synopsis for name/UUID format and restrictions.
        
        :param raidgroup: If provided, this specifies the RAID group. ex. rg2
                Must be used in conjunction with aggregate and plex inputs.
        
        :param plex: If provided, this specifies the plex name. ex. plex0
                Must be used in conjunction with aggregate input.
        """
        return self.request( "aggr-scrub-suspend", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'raidgroup': [ raidgroup, 'raidgroup', [ basestring, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_plex_delete(self, aggregate, plex):
        """
        auto generated : Delete a plex
        
        :param aggregate: Aggregate
        
        :param plex: Plex
        """
        return self.request( "aggr-plex-delete", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'aggr-name' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_scrub_list_info(self, aggregate=None, verbose=None):
        """
        Get the status of parity scrubbing on the named
        aggregate. Status includes percentage complete
        and the scrub's suspended status (if appropriate).
        If no name is given, then status is generated for
        all RAID groups.
        
        :param aggregate: Name or UUID of the entity to show scrubbing status for.
                See the synopsis for name/UUID format and restrictions.
        
        :param verbose: If set to "true", this operation will be verbose.
                If not supplied or set to false, normal output
                levels will be used.
        """
        return self.request( "aggr-scrub-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'scrub-details': [ ScrubDetailInfo, True ],
        } )
    
    def aggr_mediascrub_list_info(self, aggregate=None):
        """
        Get the status of media scrubbing on the named
        aggregate, plex, or RAID group.  Status includes
        percentage complete and the media scrub's status.
        
        :param aggregate: Name of an existing aggregate, plex, or RAID group,
                using the following format:
                [/vol/]<aggrname>[<plexinfo>][<groupinfo>]
                If no name is given, then status is generated for
                all RAID groups currently being media-scrubbed.
        """
        return self.request( "aggr-mediascrub-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
            'mediascrub-details': [ MediascrubDetailInfo, True ],
        } )
    
    def aggr_modify_raid_type(self, aggregate, raid_type, disk_type=None):
        """
        Modify the RAID type for the given aggregate
        to the specified "raid-type". This API can also selectively
        change the RAID type of specific raid groups in the aggregate
        based on the specified "disk-type". The change remains effective
        even if the filer is rebooted.
        This API does not support modifying options of a striped aggregate.
        
        :param aggregate: Name or UUID of the aggregate whose option is to be set.
                See the synopsis for name/UUID format and restrictions.
        
        :param raid_type: possible values: "raid4","raid_dp"
                The type of RAID group used for this aggregate.
                The "raid4" setting  provides one parity disk per
                RAID group, while "raid_dp" provides two.
                Changing this option immediately changes the RAID
                group type for the RAID groups in the aggregate.
                When upgrading RAID groups from "raid4" to
                "raid_dp", each RAID group begins a reconstruction
                onto a spare disk allocated for the second
                "dparity" parity disk.
        
        :param disk_type: Type of disks to use : ATA, BSAS, FCAL, FSAS, LUN, SAS, SATA, or SSD.
                This option is required if we want to change the raid type
                of raid groups created out of the specified disks only.
                Otherwise, if this is not specified then the raid type for all
                raid groups in the aggregate would change.
        """
        return self.request( "aggr-modify-raid-type", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'disk_type': [ disk_type, 'disk-type', [ basestring, 'None' ], False ],
            'raid_type': [ raid_type, 'raid-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_relocation(self, aggregate_list, destination_node_name, source_node_name, is_relocate_to_higher_version=None, is_override_vetoes=None, is_override_destination_checks=None, is_ndo_controller_upgrade=None):
        """
        Aggregate Relocation
        
        :param aggregate_list: List of aggregate names.
        
        :param destination_node_name: Name of destination node where aggregates are to be relocated.
        
        :param source_node_name: Name of the source node in which aggregate resides.
        
        :param is_relocate_to_higher_version: Relocate to a node running higher major Data ONTAP version.
                If an aggregate is relocated to this destination then that
                aggregate cannot be relocated back to the source node
                till the source is also upgraded to the same or higher
                Data ONTAP version. This option is not required if the
                destination is running on higher minor version but the
                same major version. Default: false
        
        :param is_override_vetoes: Override veto checks for relocating an aggregate.
                Initiating aggregate relocation with vetoes overridden will
                result in relocation proceeding even if the node detects
                outstanding issues that would make aggregate relocation
                dangerous or disruptive. Default: false
        
        :param is_override_destination_checks: Override checks done on destination node.
                This option could be used to force a relocation of
                aggregates even if the destination has outstanding
                issues. Note that this could make the relocation
                dangerous or disruptive. Default: false
        
        :param is_ndo_controller_upgrade: Relocation of aggregates as part of node upgrade.
                Aggregate relocation will not change home ownership of the
                aggregates while relocating as part of controller upgrade.
                Default: false
        """
        return self.request( "aggr-relocation", {
            'is_relocate_to_higher_version': [ is_relocate_to_higher_version, 'is-relocate-to-higher-version', [ bool, 'None' ], False ],
            'aggregate_list': [ aggregate_list, 'aggregate-list', [ basestring, 'None' ], True ],
            'destination_node_name': [ destination_node_name, 'destination-node-name', [ basestring, 'None' ], False ],
            'is_override_vetoes': [ is_override_vetoes, 'is-override-vetoes', [ bool, 'None' ], False ],
            'source_node_name': [ source_node_name, 'source-node-name', [ basestring, 'None' ], False ],
            'is_override_destination_checks': [ is_override_destination_checks, 'is-override-destination-checks', [ bool, 'None' ], False ],
            'is_ndo_controller_upgrade': [ is_ndo_controller_upgrade, 'is-ndo-controller-upgrade', [ bool, 'None' ], False ],
        }, {
        } )
    
    def aggr_get_root_name(self):
        """
        Return the name of the "root" volume on the filer.
        """
        return self.request( "aggr-get-root-name", {
        }, {
            'root-volume': [ basestring, False ],
        } )
    
    def aggr_space_list_info(self, aggregate=None):
        """
        Show the space usage of the aggregate on a per flexible volume
        basis.
        This API is deprecated in Data ONTAP 8.2 and later. Use the
        aggr-space-info attributes in the aggr-list-info API for details
        related to aggregate space usage. Use volume-space-list-info
        and volume-footprint-list-info APIs for details related to
        volume space usage.
        
        :param aggregate: The aggregate to get the space information for. If not
                specified the space information for all aggregates is obtained.
        """
        return self.request( "aggr-space-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
            'aggregates': [ AggrSpaceInfo, True ],
        } )
    
    def aggr_relocation_status(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of aggregate relocation status
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                aggr object.
                All aggr objects matching this query up to 'max-records' will be
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
        return self.request( "aggr-relocation-status", {
            'max_records': max_records,
            'query': [ query, 'query', [ AggrRelocationInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AggrRelocationInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AggrRelocationInfo, True ],
        } )
    
    def aggr_plex_online(self, aggregate, plex):
        """
        auto generated : Online a plex
        
        :param aggregate: Aggregate
        
        :param plex: Plex
        """
        return self.request( "aggr-plex-online", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'aggr-name' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_options_list_info(self, aggregate):
        """
        Get the options that have been set for the specified
        aggregate.
        This API does not support listing options of striped aggregate.
        
        :param aggregate: Name or UUID of the aggregate whose options to retrieve.
                See the synopsis for name/UUID format and restrictions.
        """
        return self.request( "aggr-options-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
            'options': [ AggrOptionInfo, True ],
        } )
    
    def aggr_64bit_upgrade_scan_start(self, aggregate):
        """
        Start the 64-bit upgrade scanner on the specified
        aggregate.  Use the 'aggr-list-info' API to query the
        status of the 64-bit upgrade scanner. The status is
        made available in the 'status' element that is part of
        the 'aggr-64bit-upgrade-info' typedef. Similarly, use
        the 'd-volume-list-info' API to query the status of
        the 64-bit upgrade scanner running on each contained
        flexible volume.
        
        :param aggregate: Name or UUID of the aggregate for which to start
                the 64-bit upgrade scanner.
        """
        return self.request( "aggr-64bit-upgrade-scan-start", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_offline(self, aggregate, unmount_volumes=None, cifs_delay_seconds=None, plex=None):
        """
        Take the specified aggregate or plex offline.  The
        operation takes effect before the API returns.  Except
        in maintenance mode, the current root aggregate may
        not be taken offline.  An aggregate marked to become
        the root aggregate cannot be taken offline.  An
        aggregate containing one or more flexible volumes
        cannot be taken offline; its contained volumes must
        first be destroyed.
        A number of operations being performed on the given
        aggregate can prevent this operation from succeeding,
        either at all or for various lengths of time.  If such
        operations are found, the system waits up to one
        second for them to finish.  If they don't, the command
        is aborted.
        A check is also made for files in the aggregate opened
        by internal Data ONTAP processes.  The command is aborted if
        any are found.
        
        :param aggregate: Name of the existing aggregate or plex to offline,
                using the following format:
                [[/vol]/]<aggrname>[<plexinfo>]
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
                If the aggregate hosts any online volumes, then the
                offline request will fail unless the optional
                "unmount-volumes" argument (see below) appears and
                is set to TRUE.  If we've been cleared to unmount
                any such online volumes hosted by the aggregate, the
                caller may also specify the number of seconds to wait
                should any of those volumes have active CIFS shares
                through the optional "cifs-delay-seconds" argument
                (see below).
                If a plex name is specified, the plex must be part of
                a mirrored aggregate, and both plexes must be online.
                Prior to offlining a plex, the system will flush all
                internally-buffered data associated with the plex and
                create a snapshot that is written out to both plexes.
                The snapshot allows for efficient resynchronization
                when the plex is subsequently brought back online.
                For ontap-cluster, plexinfo is being deprecated
                in lieu of the plex parameter.
        
        :param unmount_volumes: If set to "TRUE", this option specifies that all of
                the volumes hosted by the given aggregate are to be
                unmounted before the offline operation is executed.
                By default, the system will reject any attempt to
                offline an aggregate that hosts one or more online
                volumes.
        
        :param cifs_delay_seconds: The number of seconds to wait before offlining any
                volumes that are hosted in the given aggregate that
                have active CIFS shares (if any).  A value of 0 means
                that all such volumes are to be offlined immediately
                with no warning.  CIFS users can lose data if they
                aren't given a chance to terminate applications
                gracefully.  By default, "cifs-delay-seconds" is 0.
                NOTE: This argument may ONLY appear if the
                "unmount-volumes" argument (see above) also appears
                and is set to "TRUE".
        
        :param plex: Name of a particular plex to offline.  If no plex
                is specified, then the aggregate will be taken offline.
                If a plex is specified, the plex must be part of
                a mirrored aggregate, and both plexes must be online.
                Prior to offlining a plex, the system will flush all
                internally-buffered data associated with the plex and
                create a snapshot that is written out to both plexes.
                The snapshot allows for efficient resynchronization
                when the plex is subsequently brought back online.
        """
        return self.request( "aggr-offline", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'unmount_volumes': [ unmount_volumes, 'unmount-volumes', [ bool, 'None' ], False ],
            'cifs_delay_seconds': [ cifs_delay_seconds, 'cifs-delay-seconds', [ int, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_scrub_start(self, aggregate=None, raidgroup=None, plex=None):
        """
        Start parity scrubbing on the named aggregate, plex,
        or RAID group.  Parity scrubbing compares the data
        disks to the parity disk in a RAID group, correcting
        the parity disk's contents as necessary.
        If no name is given, then parity scrubbing is started
        on all online aggregates.  If an aggregate name is
        given, scrubbing is started on all RAID groups in
        the aggregate.  If a plex name is given, scrubbing
        is started on all RAID groups contained in the plex.
        If a RAID group name is given, scrubbing is started
        only on that group.  Use "aggr-scrub-list-info" to
        check scrubbing status.
        
        :param aggregate: Name or UUID of the entity for which scrubbing is to start.
                See the synopsis for name/UUID format and restrictions.
        
        :param raidgroup: If provided, this specifies the RAID group. ex. rg2
                Must be used in conjunction with aggregate and plex inputs.
        
        :param plex: If provided, this specifies the plex name. ex. plex0
                Must be used in conjunction with aggregate input.
        """
        return self.request( "aggr-scrub-start", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'raidgroup': [ raidgroup, 'raidgroup', [ basestring, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_wafliron_commit(self, aggregate_uuid, force=None):
        """
        Invoke "IOC commit", to write the IOC changes to aggregate
        or traditional volume.  IOC, or Wafliron Optional Commit, is
        a special mode of Wafliron, in which users will be able to
        choose to accept or reject Wafliron changes.
        <p>
        This interface returns as soon as possible after it sends
        the request for IOC commit operation.  There will be a
        time window before the commit request starts being processed.
        <p>
        Because the ZAPI returns immediately after sending the
        commit, the final result of the commit operation will not
        be known until it is finished.  If any early checks of this
        operation fail, an appropriate error code is returned.
        Otherwise, user must check the success of the commit
        operation by checking the EMS messages, or by checking the
        status of the aggregate or traditional volume by calling
        the 'aggr-list-info' ZAPI.
        <p>
        IOC commit operation is an advanced operation.  It must
        be run only by the technical support of the vendor.
        <p>
        USAGE:
        <p>
        IOC is invoked on aggregates or traditional volumes.
        It stores the changes that will be made to file system
        somewhere out of the file system.  Users can accept or
        reject the changes after reviewing the changes.  If user
        accepts the changes, IOC commit operation can be used to apply
        the changes to the file system to fix the corruption(s).
        <p>
        WHAT IT DOES:
        <p>
        IOC commit operation reads the to-be-made changes and
        writes them to the aggregate or traditional volume.
        After commit operation is done all the changes are final.
        <p>
        CAVEAT:
        <p>
        After the IOC commit operation returns, there will no
        way to abort it.
        <p>
        AFTER IT COMPLETES:
        <p>
        At the end of commit operation, an asynchronous offline
        request is issued to offline the aggregate or traditional
        volume.  There might be a delay before the offline request
        starts being processed.  It might also take some time to
        finish offlining all the volumes inside an aggregate and
        eventually the aggregate itself.
        <p>
        LOGGING and EMS:
        All the messages related to the IOC commit operation are
        logged by issuing WAFL EMS messages.
        
        :param aggregate_uuid: UUID of the aggregate or the traditional volume on which
                IOC commit will be started.
                <p>
                For more information about UUID, please refer to
                the description of the 'aggregate' input of the
                'aggr-wafliron-start' ZAPI.
        
        :param force: The default value for this parameter is 'false'.
                <p>
                Force committing even when SnapMirror relation is going
                to break.
                <p>
                If not specified or 'false' is passed as the value of this
                input, that means check for possibility of breaking SnapMirror
                relation, and return appropriate error if found any.
                This includes Qtree and SnapMirror relations.
        """
        return self.request( "aggr-wafliron-commit", {
            'aggregate_uuid': [ aggregate_uuid, 'aggregate-uuid', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def aggr_split(self, aggregate, new_aggr_name):
        """
        Remove the specified plex from a mirrored aggregate
        and create a new unmirrored aggregate with the
        specified name that contains the plex.  The original
        mirrored aggregate thus becomes unmirrored.  The plex
        to be split from the original aggregate must be
        functional (not partial), but it can otherwise be
        inactive, resyncing, or out-of-date.  "Aggr split"
        can therefore be used to gain access to a plex that
        isn't up to date with respect to its partner plex if
        its partner plex is currently failed.  If the plex
        is offline at the time of the split, the resulting
        aggregate will be offline.  Otherwise, the resulting
        aggregate will be in the same online/offline/restricted
        state as the original aggregate.  A split mirror can
        be joined back together via the "victim-aggregate"
        option to "aggr-mirror".
        
        :param aggregate: Name of the plex to split out of its aggregate, using
                the following format:
                [/vol/]<aggrname>[<plexinfo>][<groupinfo>]
        
        :param new_aggr_name: Name of the new aggregate to create from the split plex.
        """
        return self.request( "aggr-split", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'new_aggr_name': [ new_aggr_name, 'new-aggr-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_online(self, aggregate, keep_same_uuid=None, force_online=None, plex=None):
        """
        Bring the specified aggregate or plex online.  This
        command takes effect immediately.  All volumes on the
        aggregate are brought to whatever state they were in
        before the aggregate was restricted or taken offline.
        If there are CIFS shares associated with the any of
        the aggregate's volumes that were also onlined, they
        are enabled.
        
        :param aggregate: Name of the existing aggregate or plex to online,
                using the following format:
                [/vol/]<aggrname>[<plexinfo>]
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
                If an aggregate is specified, it must currently be
                offline, restricted, or foreign (consisting of disks
                moved from another filer, and never having been brought
                online on the current filer).  If the aggregate is
                foreign, it will be made native before being brought
                online on the current filer.  Aggregates that aren't
                foreign are termed "native".
                If the aggregate is inconsistent but has not lost
                data, it is advisable to run WAFL_check or wafliron
                (or do a "snapmirror initialize" in case of a replica
                aggregate) prior to bringing it online.  Bringing an
                inconsistent aggregate online increases the risk of
                further file system corruption.  If the aggregate is
                inconsistent and has experienced possible loss of
                data, it can't be brought online unless WAFL_check
                or wafliron (or snapmirror initialize) is run on it.
                If a plex is specified, it must be part of an online
                mirrored aggregate.  The system initiates resynchro-
                nization of the plex as part of online processing.
                For ontap-cluster, plexinfo is being deprecated
                in lieu of the plex parameter.
        
        :param keep_same_uuid: Keep existing foreign raidtree id (aggregate uuid).
                Normally when a foreign raidtree is onlined, the
                raidtree rtid (aggregate uuid) is changed to guarantee
                uniqueness.  The behavior is overridden when this
                option is set "true."
                By default, "keep-same-uuid" is "false."
        
        :param force_online: An aggregate can not normally be brought online
                under the following conditions:
                1. It has only 1 plex that is offline and not
                up-to-date.
                2. It is an unmirrored or CFO aggregate that has
                been switched over to its DR partner as part
                of an MCC configuration.
                This behavior is overridden when this option is
                set "true". By default, "force-online" is "false".
        
        :param plex: Name of a particular plex to online.  If no plex is
                specified, then the aggregate will be onlined. If
                a plex is specified, it must be part of an online
                mirrored aggregate.  The system initiates resynchro-
                nization of the plex as part of online processing.
        """
        return self.request( "aggr-online", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'keep_same_uuid': [ keep_same_uuid, 'keep-same-uuid', [ bool, 'None' ], False ],
            'force_online': [ force_online, 'force-online', [ bool, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_verify_start(self, aggregate=None, fix_plex=None, log_only=None):
        """
        Start RAID mirror verification on the named aggregate.
        Verification compares the data in both plexes of a
        mirrored aggregate.  In the default case, any blocks that
        differ are logged and no changes are made. The fix-plex
        option is used to fix any mismatches. It specifies which
        plex to fix.
        If no name is given, then mirror verification is
        started on all online aggregates.  Use the
        "aggr-verify-list-info" API to check mirror
        verification status. If the fix-plex option is used, then
        a name must be specified.
        
        :param aggregate: Name of the mirrored aggregate to verify.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        
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
        return self.request( "aggr-verify-start", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'fix_plex': [ fix_plex, 'fix-plex', [ int, 'None' ], False ],
            'log_only': [ log_only, 'log-only', [ bool, 'None' ], False ],
        }, {
        } )
    
    def aggr_rename(self, aggregate, new_aggregate_name):
        """
        Rename the specified aggregate.
        
        :param aggregate: Name or UUID of the aggregate to rename.
                See the synopsis for name/UUID format and restrictions.
        
        :param new_aggregate_name: The new name desired for the aggregate.
        """
        return self.request( "aggr-rename", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'new_aggregate_name': [ new_aggregate_name, 'new-aggregate-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_destroy(self, aggregate, force=None, plex=None):
        """
        Destroys the specified aggregate or plex.  If an
        aggregate is specified, all plexes in the aggregate
        are destroyed.  If the aggregate is embedded in a
        traditional volume, then the entire traditional
        volume is destroyed.
        If a plex is specified, only that plex is destroyed,
        leaving an unmirrored aggregate containing the
        remaining plex.  The disks in the destroyed object
        become spare disks.  Only offline aggregates and plexes
        can be destroyed.
        Note: Offline aggregates will be destroyed even
        if they contain one or more flexible volumes,
        which should not typically be the case.
        From cluster interface only aggregates are supported and
        plexes are not supported.
        
        :param aggregate: Name of the existing aggregate or plex to be
                destroyed, using the following format:
                [/vol/]<aggrname>[<plexinfo>]
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        
        :param force: When using "aggr-destroy" on a traditional volume,
                force the destruction of the volume even if a
                non-default vfiler has storage on it.  Normally,
                the system will not destroy such a volume and
                will instead return EVOLUME_HAS_VFILER_STORAGE.
        
        :param plex: Name of a particular plex to destroy.
        """
        return self.request( "aggr-destroy", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_scrub_stop(self, aggregate=None, raidgroup=None, plex=None):
        """
        Stop parity scrubbing on the named aggregate, plex,
        or RAID group.  If no name is given, scrubbing will
        stop on all RAID groups currently being scrubbed.
        Use "aggr-scrub-list-info" to check scrubbing status.
        
        :param aggregate: Name or UUID of the entity for which scrubbing is to stop.
                See the synopsis for name/UUID format and restrictions.
        
        :param raidgroup: If provided, this specifies the RAID group. ex. rg2
                Must be used in conjunction with aggregate and plex inputs.
        
        :param plex: If provided, this specifies the plex name. ex. plex0
                Must be used in conjunction with aggregate input.
        """
        return self.request( "aggr-scrub-stop", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'raidgroup': [ raidgroup, 'raidgroup', [ basestring, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_scrub_resume(self, aggregate=None, raidgroup=None, plex=None):
        """
        Resume parity scrubbing on the named aggregate, plex,
        or RAID group.  If no name is given, then resume
        parity scrubbing on all RAID groups for which it has
        been suspended.  Use "aggr-scrub-list-info" to
        check scrubbing status.
        
        :param aggregate: Name or UUID of the entity for which scrubbing is to resume.
                See the synopsis for name/UUID format and restrictions.
        
        :param raidgroup: If provided, this specifies the RAID group. ex. rg2
                Must be used in conjunction with aggregate and plex inputs.
        
        :param plex: If provided, this specifies the plex name. ex. plex0
                Must be used in conjunction with aggregate input.
        """
        return self.request( "aggr-scrub-resume", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'raidgroup': [ raidgroup, 'raidgroup', [ basestring, 'None' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_wafliron_review(self, aggregate_uuid, cookie=None, size=None):
        """
        Return the changes that will be performed by IOC to fix
        corruptions to the aggregate or traditional volume.  IOC,
        or Wafliron Optional Commit, is a special mode of Wafliron,
        in which users will be able to choose to accept or reject
        Wafliron changes.
        <p>
        This interface returns a description of the changes that
        IOC will make to the file system in order to fix the
        corruption(s).  The list of operations might be too long
        to be returned in one call, so it might be necessary
        to make more than one ZAPI call.
        <p>
        The information returned by this call is useful to
        determine if the changes should be committed or rejected
        by doing 'aggr-wafliron-commit' or 'aggr-wafliron-reject',
        respectively.
        <p>
        The descriptions returned by this ZAPI are strings separated
        by '\\n' character.  No partial string (without the ending
        newline character) will be returned as the last one.
        <p>
        USAGE:
        <p>
        IOC is invoked on aggregates or traditional volumes.
        When it finds a corruption, it stores the changes that will
        be made to file system somewhere out of the file system.
        The descriptions for these changes are also saved in memory.
        The descriptions of changes are returned by this ZAPI.
        <p>
        WHAT IT DOES:
        <p>
        It retrieves the description of the changes that IOC
        will make.  If the list of changes is long, it must be
        retrieved by multiple calls to retrieve all of it.
        
        :param aggregate_uuid: UUID of the aggregate or the traditional volume on which
                IOC reject will be started.
                <p>
                For more information about UUID, please refer to
                the description of the 'aggregate' input of the
                'aggr-wafliron-start' ZAPI.
        
        :param cookie: The opaque cookie to determine where the previous call to
                this ZAPI left off.
                If not provided, the ZAPI will return the description of
                changes from the start of the list.
        
        :param size: Maximum size of the data that must be retrieved.  If there
                is more description of the changes, they must be retrieved
                in the next iteration or call.
                <p>
                The size cannot be more than 4KB.  That is a hard-limit.
                If no size is specified, a 4KB size will be considered as
                the default value.
        """
        return self.request( "aggr-wafliron-review", {
            'aggregate_uuid': [ aggregate_uuid, 'aggregate-uuid', [ basestring, 'None' ], False ],
            'cookie': [ cookie, 'cookie', [ int, 'None' ], False ],
            'size': [ size, 'size', [ int, 'None' ], False ],
        }, {
            'messages': [ basestring, False ],
            'next-cookie': [ int, False ],
        } )
    
    def aggr_verify_resume(self, aggregate=None):
        """
        Resume RAID mirror verification on the named aggregate.
        If no name is given, then resume mirror verification on
        all aggregates that have been suspended.
        
        :param aggregate: Name of the existing aggregate for which mirror
                verification is to resume.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        """
        return self.request( "aggr-verify-resume", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_verify_suspend(self, aggregate=None):
        """
        Suspend RAID mirror verification on the named aggregate.
        If no name is given, suspend mirror verification on
        all aggregates currently being verified.
        
        :param aggregate: Name of the aggregate for which we are to suspend
                mirror verification.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        """
        return self.request( "aggr-verify-suspend", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_verify_stop(self, aggregate=None):
        """
        Stop RAID mirror verification on the named aggregate.
        If no name is given, stop mirror verification on all
        aggregates currently being verified.
        
        :param aggregate: Name of the aggregate for which we are to stop mirror
                verification.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        """
        return self.request( "aggr-verify-stop", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of aggrgate objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                aggr object.
                All aggr objects matching this query up to 'max-records' will be
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
        return self.request( "aggr-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AggrAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AggrAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ AggrAttributes, True ],
        } )
    
    def aggr_wafliron_stop(self, aggregate):
        """
        Terminate "wafliron", the online WAFL file system
        check/repair tool.
        For more details on wafliron, read the description
        for 'aggr-wafliron-start'.
        After the 'aggr-wafliron-start' ZAPI is issued, there is
        a small window until which wafliron does not actually
        start since the start operation is attempted in the
        background. During this window, any attempt to stop
        wafliron will fail. However, once past this window, this
        call will initiate the abort process.
        
        :param aggregate: UUID of the aggregate or the traditional volume on which
                wafliron should be aborted.
                <p>
                UUIDs are formatted as 36-character strings.
                These strings are composed of 32 hexadecimal
                characters broken up into five groupings
                separated by '-'s.  The first grouping has 8
                hex characters, the second through fourth
                groupings have four hex characters each, and
                the fifth and final grouping has 12 hex
                characters.  Note that a leading '0x' is not
                used.
                <p>
                Example: 49e370d6-5b5a-11d9-9eb5-000100000529
                <p>
                If wafliron is aborted successfully, the volumes in the
                aggregate will be left in their current state. However,
                consistency checking will not continue after wafliron
                has been aborted.
        """
        return self.request( "aggr-wafliron-stop", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_verify_list_info(self, aggregate=None):
        """
        Get the status of RAID mirror verification on the
        named aggregate.  Status includes percentage complete
        and whether it's currently suspended.
        
        :param aggregate: Name of an existing aggregate.  If no name is given,
                then mirror verification status is generated for all
                aggregates currently being verified.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        """
        return self.request( "aggr-verify-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
        }, {
            'verify-details': [ VerifyDetailInfo, True ],
        } )
    
    def aggr_wafliron_start(self, aggregate, force=None, prev_cp=None, is_optional_commit=None, backup=None, use_backup=None):
        """
        Invoke "wafliron", the online WAFL file system
        check/repair tool.
        <p>
        This interface returns as soon as possible while wafliron
        starts in the background. After the 'aggr-wafliron-start'
        ZAPI is issued, there is a small window until which
        wafliron does not actually start since it is preparing
        to start.
        <p>
        Since this ZAPI returns as quickly as possible, while
        the start operation is attempted in the background, the
        actual error code for 'aggr-wafliron-start' is made
        available in the 'last-start-errno' element that is part
        of the 'aggr-wafliron-info' element. This information
        can be obtained using the 'aggr-list-info' ZAPI. Please
        see the list of all possible error codes below.
        <p>
        Wafliron is an advanced operation that should only be
        run under the direction of your vendor's customer
        support organization.
        <p>
        USAGE:
        <p>
        Wafliron is invoked on an aggregate or on a traditional
        volume. It cannot be run directly on a flexible volume.
        When run against an aggregate, it will check/repair the
        aggregate and all the associated flexible volumes.
        <p>
        USAGE RESTRICTION:
        <p>
        In order to run wafliron on an aggregate containing a
        node's root volume or on a root traditional volume, a
        special boot menu option must be used. So downtime must
        first be scheduled for the entire node, as the node is
        forced to reboot.
        <p>
        In order to run wafliron on an aggregate or on a
        traditional volume running CIFS services, either the aggregate
        or volume should be offlined or CIFS services should be
        terminated on the target aggregate or traditional volume prior
        to starting wafliron. The aggregate or the traditional volume
        can be onlined and CIFS services restored once the remount
        of aggregate or traditional volume is completed.
        <p>
        WHAT WAFLIRON DOES:
        <p>
        Wafliron causes the target aggregate and its
        associated flexible volumes to be unmounted and remounted
        during an initial set of checks.  Clients thus cannot
        access the affected volumes during this phase.
        After the volumes are remounted, their data is
        actively served while wafliron continues to perform
        its checks.
        <p>
        This interface works for gridiron as well.  Gridiron is a
        flexible volume centric operation: it is automatically
        activated whenever wafliron running on an aggregate finds
        that it has bumped into a striped meta-data volume (MDV).
        <p>
        CAVEAT:
        <p>
        By default, wafliron skips certain flexible volumes in
        the specified aggregate. The 'force' option can be used
        to override this behavior. See the description of the
        'force' option for more details.
        <p>
        AUTO ABORT CONDITIONS:
        <p>
        1. During a takeover of an aggregate, wafliron is stopped
        if it is running on that aggregate.
        <p>
        2. A sendhome/giveback of an aggregate does not happen if
        wafliron is running on it. If it is a forced
        sendhome/giveback, wafliron is stopped on that aggregate.
        The same applies for aggregate migration.
        <p>
        PROGRESS:
        <p>
        The aggregate level wafliron progress can be obtained
        using 'aggr-list-info'. The progress is available in
        the 'aggr-wafliron-info' element inside of 'aggr-info'
        element.
        <p>
        The volume level wafliron progress can be obtained using
        'd-volume-list-info'. The progress is available in
        the 'd-wafliron-info' element inside of 'd-volume-info'
        element.
        <p>
        AFTER WAFLIRON COMPLETES:
        <p>
        After wafliron completes or is aborted on an aggregate, a
        metafile scan (kireeti) occurs on the flexible volumes as
        a background process. All SnapMirror functions will be
        delayed until after the scan(s) are completed for the
        source flexible volumes in the aggregate that was ironed.
        <p>
        LOGGING and EMS:
        <p>
        Historically in Data ONTAP 7G, all wafliron information was
        logged to the node's console as well as the to the
        '/etc/messages' file. On a Data ONTAP GX, it was logged to
        the file '/mroot/log/messages.log'. The messages logged
        include wafliron start time, changes made, a summary of
        the changes, and the completion time for the aggregate
        and all flexible volumes. On the converged node the
        locations for the console log and the EMS messages are
        yet to be determined.
        <p>
        When parameter optional-commit is specified,
        WAFLIron will be started in optional commit mode.
        It is invoked when an administrator wants to manually
        review the fixes made by wafliron to the affected
        file system and then decide whether to accept or reject
        the changes. The aggregate must be offline before
        starting wafliron in this mode.
        Only the affected aggregate will be unavailable for
        data access. All other aggregates/volumes will be online
        and available.
        <p>
        When parameter prev-cp is specified,
        WAFLIron will be started in prev_cp mode.
        This mode requires wafliron to be started in optional
        commit mode.
        It is invoked when an administrator wants to restore
        some flexvols to previous snapshots before starting
        wafliron on them. It is often used to verify the
        sanity of a snapshot for a badly corrupted active
        filesystem in a flexvol.
        
        :param aggregate: UUID of the aggregate or the traditional volume on which
                wafliron will be started.
                <p>
                UUIDs are formatted as 36-character strings.
                These strings are composed of 32 hexadecimal
                characters broken up into five groupings
                separated by '-'s.  The first grouping has 8
                hex characters, the second through fourth
                groupings have four hex characters each, and
                the fifth and final grouping has 12 hex
                characters.  Note that a leading '0x' is not
                used.
                <p>
                Example: 49e370d6-5b5a-11d9-9eb5-000100000529
                <p>
                If the specified aggregate contains the node's root
                volume, the call will fail with EAGGR_HAS_ROOT_VOLUME.
                A special boot menu option must be used instead.
                <p>
                The specified aggregate could be a constituent striped
                aggregate.
        
        :param force: The default value for this parameter is FALSE.
                <p>
                Wafliron skips the following volumes on the specified
                aggregate ignoring the 'force' parameter.
                <p>
                1. LS (Load Sharing) mirror destination volumes.
                Currently, the only way to fix inconsistencies on the
                LS mirrored destination volumes is to break the mirror
                relationships and resynchronize from the source.
                <p>
                2. Quiesced flexible volumes.
                <p>
                3. Volume-move mirrors created for the purpose of moving
                volumes.
                <p>
                When the 'force' parameter is set to FALSE, the following
                volumes are skipped by wafliron on the specified
                aggregate.
                <p>
                1. SnapMirror/SnapVault destination volumes.
                <p>
                2. DR (Disaster Recovery) mirror destination volumes
                (10-mode).
                <p>
                3. Wafliron will fail to start if the aggregate contains
                any Qtree SnapMirror/SnapVault destination volumes.
                <p>
                When the 'force' parameter is set to TRUE, one or more of
                the following are true:
                <p>
                1. It forces wafliron to work on the SnapMirror/SnapVault
                destination volumes by breaking the mirror
                relationships.
                <p>
                2. It forces wafliron to work on the volumes containing
                qtree SnapMirror/SnapVault destination replicas by
                breaking SnapMirror/SnapVault relationships to the
                destination qtrees.
                <p>
                3. It forces wafliron to work on the DR (Disaster
                Recovery) mirror destination volumes (10-mode) by
                breaking the mirror relationships.
                <p>
                4. In all the cases in which the mirror relationships are
                broken, the replica volumes must match the file system
                version of the node. If the replica volumes are
                mirrored from a node that has an older version of the
                file system, wafliron will fail to start on the
                specified aggregate when the 'force' parameter is set
                to TRUE.
        
        :param prev_cp: Start WAFLIron in prev_cp mode.
                Load specified inofiles in specified flexvols.
                <p>
                The parameter contains a list of flexvols
                which wafliron will perform prev_cp and
                which inofiles to load in the mount phase.
        
        :param is_optional_commit: The default value for this parameter is false.
                Start WAFLIron in optional commit mode.
        
        :param backup: Control SnapIron snapshot when starting wafliron.
                <p>
                Possible values are:
                <ul>
                <li>"yes": Create a SnapIron snapshot if one does not exist.
                Continue even if one can not be created.
                Do nothing if one already exists.
                <br>
                <li>"force": Delete the existing SnapIron snapshot if it
                already exists. Create a new one.
                <br>
                <li>"no": Do not try to create a SnapIron snapshot.
                </ul>
                <p>
                The default value for this parameter is "yes".
        
        :param use_backup: Pick SnapIron snapshot instead of active file system and start
        """
        return self.request( "aggr-wafliron-start", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'prev_cp': [ prev_cp, 'prev-cp', [ PrevCpInofileInfo, 'None' ], True ],
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'is_optional_commit': [ is_optional_commit, 'is-optional-commit', [ bool, 'None' ], False ],
            'backup': [ backup, 'backup', [ basestring, 'None' ], False ],
            'use_backup': [ use_backup, 'use-backup', [ bool, 'None' ], False ],
        }, {
        } )
    
    def aggr_add(self, aggregate, disk_size_with_unit=None, mirror_disks=None, disk_size=None, disks=None, force_spare_pool=None, disk_type=None, checksum_style=None, group_selection_mode=None, raid_group=None, cache_raid_type=None, ignore_pool_checks=None, pre_check=None, simulate=None, force_cache_size=None, allow_mixed_rpm=None, allow_same_carrier=None, disk_count=None):
        """
        Add disks to the specified aggregate, whether it is
        free-standing or embedded in a traditional volume.
        The disks to add are specified in the same way as for
        "aggr-create".  Disks cannot be added to a mirrored
        aggregate if one or more of the plexes is offline.
        By the time the API returns, the disk(s) may not yet
        be completely added.  Use 'aggr-list-info' to query
        the aggregate status to determine when it has finished
        growing due to the added disk(s). Same can be done using
        'aggr-get-iter' when requested from Admin Vserver LIF.
        When the upgrade-64bit-mode input is provided to this API,
        the API produces a set of results in the background. These
        results are not available as output from aggr-add. Use the
        'aggr-list-info' and 'volume-list-info' APIs to query the
        results of the 64-bit upgrade process on the aggregate and
        flexible volumes, respectively.
        
        :param aggregate: Name or UUID of the aggregate to which the disks will be
                added.
                See the synopsis for name/UUID format and restrictions.
        
        :param disk_size_with_unit: This parameter accepts a disk size in the specified unit.
                It is a positive integer number followed by unit of "T", "G",
                "M" or "K". For example, these are accepted: 72G, 36G, 1T
                and 32M. But "72" will not be accepted.
                This "disk-size-with-unit"
                option is ignored if a specific list of disks is
                specified through the "disks" parameter.
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear,
                an error message will be returned.
        
        :param mirror_disks: Specific list of mirror disks needed to accompany
                the list in the "disks" parameter.  This list must
                contain the same number of disks as specified in
                "disks".
        
        :param disk_size: The individual disk size in 4KB blocks.  For example, a
                disk-size of 131072000 represents a 500GB drive
                (131072000 * 4 * 1024 = 500 * 1024 * 1024 * 1024).  Disks that
                are within approximately 20% of the specified size will be
                selected.
                If neither the "disk-size" nor the
                "disk-size-with-unit" argument is specified,
                existing groups are appended with disks that are
                the best match by size for the largest disk in
                the group.  When starting new groups, disks
                that are the best match by size for the largest disk in the
                last raidgroup are selected first, then smaller
                disks, and finally larger disks.  This "disk-size"
                option is ignored if a specific list of disks is
                specified through the "disks" parameter.
                Range : [0..2^31-1].
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear,
                an error message will be returned.
        
        :param disks: Specific list of disks to add to the aggregate.
                If the aggregate is mirrored and a specific list
                of disks is supplied, another list ("mirror-disks")
                must also be supplied with the same number of disks.
                Either the "disks" or "disk-count" argument must
                be specified.
        
        :param force_spare_pool: Disks in a plex are not normally permitted to span
                spare pools.  This behavior is overridden with this
                option when it is set to true.
                This is a deprecated parameter. Use the allow-mixed-rpm
                and ignore-pool-checks parameters instead.
        
        :param disk_type: Type of disks to use : ATA, BSAS, EATA, FCAL, FSAS, LUN, MSATA,
                SAS, SATA, SCSI, XATA, XSAS, or SSD.
                This option is required when converting an existing aggregate
                to a hybrid one, or when operating on a hybrid aggregate.
                Otherwise, the option is not required.
        
        :param checksum_style: Specifies the checksum style for the disks to be added to
                an aggregate. This input is not allowed if a list of disks to
                use is specified through the "disks" parameter. The possible values:
                <ul>
                <li> "advanced_zoned"    - advanced_zoned checksum (azcs),
                <li> "block"             - block.
                </ul>
                By default, disks with same checksum style as the aggregate are selected.
                Use this option to override that behavior and create a mixed checksum aggregate.
                "zoned" is not supported as one of the possible values as a mixed checksum
                aggregate can support only block and advanced_zoned checksum styles.
        
        :param group_selection_mode: Specifies how DATA ONTAP adds the specified disks to
                raidgroups. Legitimate values are "last", "one", "new"
                or "all".
                group-selection-mode is an optional argument, and the
                behavior when it is not used is selected by value of
                raid-group. If raid-group is used, the behavior is the same
                as for group-selection-mode "one". If raid-group is not used,
                the behavior is the same as for group-selection-mode "last".
                The raid-group option must be used with group-selection-mode
                value "one", and it cannnot be used with others.
                If the string value is "last", Data ONTAP adds the specified
                disks to the existing last RAID group first. After the
                last RAID group is full, it creates one or more new RAID
                groups and adds the remaining disks to the new groups.
                If the string value is "one", Data ONTAP adds the specified
                disks to the existing RAID group specified by raid-group
                option until this specified RAID group is full.
                If the string value is "new", Data ONTAP creates one or more
                new RAID groups and adds the specified disks to the new
                groups, even if they would fit into an existing RAID group.
                The name of new RAID groups are selected
                automatically.  It is not possible to specify the name
                for the new RAID groups.
                If the string value is "all", Data ONTAP adds the specified
                disks to existing RAID groups first. Only after all existing
                RAID groups are full, it creates one or more new RAID groups
                and adds the remaining disks to the new groups.
        
        :param raid_group: Specifies the RAID group (for example rg0) to which
                the indicated disks are to be added.   When a RAID
                group other than the last RAID group is specified,
                the aggregate can no longer be reverted to a version
                of Data ONTAP prior to 6.2.  In such a case, the
                "force-spare-pool" option must be specified as well.
                By default, the filer fills up one RAID group with
                disks before starting another RAID group.  Suppose
                an aggregate currently has one RAID group of 12 disks
                and its RAID group size is 14.  If you add 5 disks
                to this aggregate, it will have one RAID group with
                14 disks and another RAID group with 3 disks.  The
                filer does not evenly distribute disks among RAID
                groups.
        
        :param cache_raid_type: Specifies the raid-type of the new RAID groups being
                created as part of the disk add operation. This option should
                be used while adding SSD disks for the first time to a hybrid-enabled
                aggregate. Possible values: raid4 and raid_dp only. If not
                specified, the default value is the raid-type of the aggregate.
        
        :param ignore_pool_checks: Disks in a plex are normally required to come from the
                same spare pool.  Similarly, disks in different plexes of
                a mirrored aggregate are required to come from different
                spare pools. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param pre_check: Only check for the warnings without actually adding the disks.
                This option cannot be used when "simulate" is specified or
                "upgrade-64bit-mode" is set to "check".  Default value is false.
        
        :param simulate: Simulates the addition of disks to the given aggregate or UUID of the aggregate.
                If set to "true", addition of disks won't happen but returns the list of disks
                that would be automatically selected for the addition of the aggregate. By default,
                simulate option is set to false.
        
        :param force_cache_size: When set to true this parameter forces the addition of SSD disks to hybrid
                enabled aggregate by skipping the check for total (local + partner) hybrid
                SSD capacity. This can be used when the partner's cache capacity cannot be
                retrieved.
                Default value is false.
                Warning: If force-cache-size is set to true, the administrator is responsible
                to ensure that the total limit will not be exceeded.
        
        :param allow_mixed_rpm: Disks in an aggregate are normally required to have the
                same RPM. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param allow_same_carrier: Using two disks from one carrier that houses multiple disks
                in one RAID group is not desirable. If that happens,
                Data ONTAP initiates a series of disk copy operations to
                correct that situation.
                Sometimes, selection of available spare disks makes it
                impossible to avoid placing two disks from one carrier in one
                RAID group. Setting this option to true allows placing two
                disks from one carrier in one RAID group.
                This option has an effect only when disks to be used are
                specified in 'disks'. This option is ignored when 'disk-count'
                is used.
                @input        upgrade-64bit-mode
                @type         string, optional
                @desc         Allows the aggregate to grow past 16 TB and begin
                64-bit upgrade. If not supplied, adding disks past
                16 TB to a 32-bit aggregate will fail. Legitimate
                values are "check", "grow_all", "grow_none", and
                "grow_reserved".
                If the "check" value is specified,
                aggr-add produces a summary of
                the space impact which would result from
                upgrading the aggregate to 64-bit. This summary
                includes the space usage of each contained
                volume after the volume is upgraded to 64-bit
                and the amount of space that must be added to
                the volume to successfully complete the 64-bit upgrade.
                The summary can be obtained by querying the
                'aggr-list-info' and 'volume-list-info' APIs.
                The aggregate's summary is made available in the 'check'
                element that is part of the 'aggr-64bit-upgrade-info'
                typedef. The flexible volumes' summary is made available
                in the 'check' element that is part of the
                'volume-64bit-upgrade-info' typedef.
                This option does not result in an upgrade
                to 64-bit or addition of disks.
                If the "grow_all" value is specified,
                "aggr-add" upgrades the aggregate to 64-bit
                if the total aggregate size after adding the specified
                disks exceeds 16TB. This option allows "aggr-add" to
                automatically grow volumes as needed if they run out
                of space due to the 64-bit upgrade. The volumes will
                be grown to accommodate all the files within these volumes.
                This option does not affect volumes which have autosize
                enabled.
                If the "grow_none" value is specified,
                "aggr-add" upgrades the aggregate to 64-bit if the
                total aggregate size after adding the specified disks
                exceeds 16TB. This option does not allow "aggr-add" to
                automatically grow volumes if they run out of space
                due to the 64-bit upgrade.
                If the "grow_reserved" value is specified,
                "aggr-add" upgrades the aggregate to 64-bit
                if the total aggregate size after adding the specified
                disks exceeds 16TB. This option allows "aggr-add" to
                automatically grow volumes if they run out of space
                due to the 64-bit upgrade, but only to accommodate
                the space reserved files within these volumes.
                This option does not affect volumes which have autosize
                enabled.
        
        :param disk_count: Number of disks to add, including the parity disks.
                The disks will come from the pool of spare disks.
                The smallest disks in this pool join the aggregate
                first, unless the "disk-size" argument is specified.
                Either the "disk-count" or "disks" argument must
                be specified.
                Range : [0..2^31-1].
        """
        return self.request( "aggr-add", {
            'disk_size_with_unit': [ disk_size_with_unit, 'disk-size-with-unit', [ basestring, 'None' ], False ],
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'disk_size': [ disk_size, 'disk-size', [ int, 'None' ], False ],
            'disks': [ disks, 'disks', [ DiskInfo, 'None' ], True ],
            'force_spare_pool': [ force_spare_pool, 'force-spare-pool', [ bool, 'None' ], False ],
            'disk_type': [ disk_type, 'disk-type', [ basestring, 'None' ], False ],
            'checksum_style': [ checksum_style, 'checksum-style', [ basestring, 'None' ], False ],
            'group_selection_mode': [ group_selection_mode, 'group-selection-mode', [ basestring, 'None' ], False ],
            'raid_group': [ raid_group, 'raid-group', [ basestring, 'None' ], False ],
            'cache_raid_type': [ cache_raid_type, 'cache-raid-type', [ basestring, 'None' ], False ],
            'ignore_pool_checks': [ ignore_pool_checks, 'ignore-pool-checks', [ bool, 'None' ], False ],
            'pre_check': [ pre_check, 'pre-check', [ bool, 'None' ], False ],
            'simulate': [ simulate, 'simulate', [ bool, 'None' ], False ],
            'force_cache_size': [ force_cache_size, 'force-cache-size', [ bool, 'None' ], False ],
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'allow_mixed_rpm': [ allow_mixed_rpm, 'allow-mixed-rpm', [ bool, 'None' ], False ],
            'allow_same_carrier': [ allow_same_carrier, 'allow-same-carrier', [ bool, 'None' ], False ],
            'disk_count': [ disk_count, 'disk-count', [ int, 'None' ], False ],
        }, {
            'pre-check-results': [ WarningCode, True ],
            'is-upgrade-64bit-invalid': [ bool, False ],
            'bad-disks': [ DiskInfo, True ],
            'upgrade-64bit-cookie': [ int, False ],
            'is-upgrade-64bit-ignore': [ bool, False ],
            'selected-disks': [ DiskInfo, True ],
            'selected-mirror-disks': [ DiskInfo, True ],
        } )
    
    def aggr_mirror(self, aggregate, mirror_disks=None, victim_aggregate=None, ignore_pool_checks=None, force=None, override_vfiler_ownership=None, pre_check=None, allow_mixed_rpm=None, allow_same_carrier=None):
        """
        Turns an unmirrored aggregate into a mirrored
        aggregate by adding a plex to it.  The plex is
        either newly formed from disks chosen from a spare
        pool or, if the "victim-aggregate" option is
        specified, taken from another existing unmirrored
        aggregate.  The named aggregate must currently be
        unmirrored.  Disks may be specified explicitly
        using the "mirror-disks" list option in the same
        way as with the "aggr-create" and "aggr-add"
        commands.  The number of disks indicated must
        match the number present in the existing aggregate.
        If disks are not specified explicitly, then disks
        are automatically selected to match those in the
        aggregate's existing plex.
        
        :param aggregate: Name of the existing aggregate to be mirrored.
                UUID can be specified instead of aggregate name.
                See the synopsis for name/UUID format and restrictions.
        
        :param mirror_disks: Specific list of mirror disks to add.  This list must
                match the number of disks present on the existing
                aggregate.  The specified disks are not permitted to
                span disk pools unless overridden with the
                "force-spare-pool" option.
        
        :param victim_aggregate: The "victim" aggregate to cannibalize in order to
                mirror the named aggregate.  The "victim-aggregate"
                must have been previously joined with the aggregate
                to be mirrored and then split from it.  The resulting
                mirrored aggregate is otherwise identical to the
                original aggregate before the operation.  The
                "victim-aggregate" (and all its volumes) is effec-
                tively destroyed.  "victim-aggregate" (and all its
                volumes) must be offline.
        
        :param ignore_pool_checks: Disks in a plex are normally required to come from the
                same spare pool.  Similarly, disks in different plexes of
                a mirrored aggregate are required to come from different
                spare pools. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param force: Force the mirroring operation through, past the
                normal roadblocks that would otherwise cause it to
                be aborted.  For example, disks in a plex are not
                normally permitted to span spare pools.  Also, the
                victim cannot normally be accepted when it is owned
                by one or more vfilers.  All these safety-driven
                behaviors are overridden when this option is set
                to true.
                This is a deprecated parameter. Use the allow-mixed-rpm
                and ignore-pool-checks parameters instead.
        
        :param override_vfiler_ownership: The victim aggregate cannot normally be accepted when it is
                owned by one or more vfilers.  This option may be set to
                true in order to override that restriction.  The option
                is ignored if 'victim-aggregate' is not specified.
        
        :param pre_check: Only check for the warnings without actually mirroring the
                aggregate. Default value is false.
        
        :param allow_mixed_rpm: Disks in an aggregate are normally required to have the
                same RPM. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param allow_same_carrier: Using two disks from one carrier that houses multiple disks
                in one RAID group is not desirable.  If that happens,
                Data ONTAP initiates a series of disk copy operations to
                correct that situation.
                Sometimes, selection of available spare disks makes it
                impossible to avoid placing two disks from one carrier in one
                RAID group. Setting this option to true allows placing two
                disks from one carrier in one RAID group.
                This option has an effect only when disks to be used are
                specified in 'disks'. This option is ignored when 'disk-count'
                is used.
        """
        return self.request( "aggr-mirror", {
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'victim_aggregate': [ victim_aggregate, 'victim-aggregate', [ basestring, 'None' ], False ],
            'ignore_pool_checks': [ ignore_pool_checks, 'ignore-pool-checks', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'override_vfiler_ownership': [ override_vfiler_ownership, 'override-vfiler-ownership', [ bool, 'None' ], False ],
            'pre_check': [ pre_check, 'pre-check', [ bool, 'None' ], False ],
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'allow_mixed_rpm': [ allow_mixed_rpm, 'allow-mixed-rpm', [ bool, 'None' ], False ],
            'allow_same_carrier': [ allow_same_carrier, 'allow-same-carrier', [ bool, 'None' ], False ],
        }, {
            'pre-check-results': [ WarningCode, True ],
            'bad-disks': [ DiskInfo, True ],
        } )
    
    def aggr_check_spare_low(self, node_name=None):
        """
        Return true if there is no suitable spare disk available
        for any filesystem (parity or data) disk.
        
        :param node_name: Low spare condition checked on the requested node.
                When requested from Admin Vserver LIF and node name not
                specified, status for the cluster is returned.
        """
        return self.request( "aggr-check-spare-low", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
            'is-spare-low': [ bool, False ],
        } )
    
    def aggr_get_filer_info(self, node_name):
        """
        Get information on what possibilities and parameters
        exist for aggregates on a given filer.
        
        :param node_name: Name of the node (filer)
        """
        return self.request( "aggr-get-filer-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
            'disk-types': [ basestring, False ],
            'default-raidtype': [ basestring, False ],
            'checksum-types': [ basestring, False ],
            'root-volume': [ basestring, False ],
            'max-named-disks-per-request': [ int, False ],
            'raidgroup-size': [ RaidgroupSizeInfo, True ],
            'allowed-raidtypes': [ RaidtypeInfo, True ],
            'snapshots-max': [ int, False ],
        } )
    
    def aggr_create(self, aggregate, disk_size=None, ignore_pool_checks=None, ha_policy=None, language_code=None, checksum_style=None, is_snaplock=None, rpm=None, raid_type=None, spare_pool=None, pre_check=None, striping=None, nodes=None, type=None, allow_same_carrier=None, disk_size_with_unit=None, disk_type=None, raid_size=None, snaplock_type=None, simulate=None, block_type=None, mirror_disks=None, force_zcs=None, force_spare_pool=None, force_small_aggregate=None, disks=None, is_mirrored=None, allow_mixed_rpm=None, disk_count=None):
        """
        Create a new aggregate with the given name.  The
        maximum number of aggregates that can be created on
        a filer varies by the type of configuration.  In a
        standalone configuration, up to 200 aggregates can
        be created on a filer (including the aggregates
        that are "embedded" in traditional volumes, which
        must be created as a side effect of a traditional
        volume creation).  In an HA configuration, this
        number drops to 100 and to 50 in a C-mode MetroCluster
        configuration. The aggregate may not yet be
        operational immediately after the API returns.
        Use 'aggr-list-info' to query the status of
        the newly-created aggregate to determine when it is
        fully operational. Same can be done using 'aggr-get-iter'
        when requested from Admin Vserver LIF.
        NOTE: If ECANT_USE_ALL_DISKS is returned, then the
        requested aggregate was indeed created, just
        not with all the disks that were specified.
        
        :param aggregate: Name of the aggregate to create.  The aggregate name
                can contain letters, numbers, and the underscore
                character(_), but the first character must be a
                letter or underscore. The maximum length of the
                aggregate name is 255.
        
        :param disk_size: Disk size in 4KB blocks.  Disks that are within 10% of the
                specified size will be selected for use in the
                aggregate.   If neither "disk-size" nor
                "disk-size-with-unit" is specified, existing groups are
                appended with disks that are the best match for the
                largest disk in the group.  When starting new groups,
                the smallest disks are selected first.  This option
                is ignored if a specific list of disks to use is
                specified through the "disks" parameter.
                Range [0..2^31-1].
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear, an error
                message will be returned.
        
        :param ignore_pool_checks: Disks in a plex are normally required to come from the
                same spare pool.  Similarly, disks in different plexes of
                a mirrored aggregate are required to come from different
                spare pools. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param ha_policy: Aggregate's HA policy. The only allowed values
                are "cfo" and "sfo". In clustered environments
                default value is 'sfo' if not specified. In unclustered
                environments, it is not allowed to specify this
                attribute as it is always be 'cfo' internally.
                EINVALIDINPUTERROR is returned if value is other
                than "cfo" and "sfo".
                EOP_CLUSTER_ATTR_DISALLOWED is returned if this
                attribute is used in unclustered environments.
        
        :param language_code: Specifies the language to use for the new traditional volume
                via a language code.   The default language is the one
                used by the filer's root volume.  This option may be used
                only when creating a traditional volume, i.e. when "type" is
                "trad."
                <p>
                For the full list of available language codes, see
                'volume-create'.
        
        :param checksum_style: Specifies the checksum style for the aggregate. This input is
                not allowed if a list of disks to use is specified through the
                "disks" parameter. The possible values:
                <ul>
                <li> "advanced_zoned"    - advanced_zoned checksum (azcs),
                <li> "block"             - block,
                </ul>
        
        :param is_snaplock: Specifies the creation of a SnapLock aggregate.
                By default, is-snaplock is not specified.
                When is-snaplock is "true" the type of snaplock aggregate is
                determined in the following way -
                1> If snaplock-type is set, create the type specified in
                snaplock-type (see snaplock-type for more details)
                2> Otherwise, create a Snaplock enterprise aggregate
                if a Snaplock enterprise license has been installed.
                3> Otherwise, create a Snaplock compliance aggregate.
                ESERVICENOTLICENSED is returned if the required Snaplock
                Compliance or Enterprise license is not installed.
                EONTAPI_EWORMNOCLOCK is returned if SnapLock
                Compliance Clock is not running.
                If you need to create a snaplock aggregate, the suggested
                method is to specify snaplock-type as "compliance" or
                "enterprise" and not specify is-snaplock at all.
                If you want to create a non-snaplock aggregate, the
                suggested method is to specify neither snaplock-type nor
                is-snaplock.
        
        :param rpm: Rotational speed of disks in revolutions per minute.
                Possible values are: 5400, 7200, 10000, and 15000.
                This option is needed only when disks with different
                rotational speeds are connected to the filer.  It is not
                allowed if a list of disks to use is specified through the
                "disks" parameter.
        
        :param raid_type: Specifies the type of RAID groups to use in the
                new aggregate.  Possible values: raid4, raid_dp.
                The default value is raid4 on most platforms.
        
        :param spare_pool: Specifies the spare pool from which to select spare
                disks to use in creation of a new aggregate. This
                option is not allowed if a list of disks specified
                through the "disks" parameter. This option cannot be
                used when "is-mirrored" is set to true.
                Possible values:
                <ul>
                <li> "Pool0"   - Disks associated with spare Pool0.
                <li> "Pool1"   - Disks associated with spare Pool1.
                </ul>
        
        :param pre_check: Only check for the warnings without actually creating the
                aggregate. This option cannot be used when "simulate"
                is specified. Default value is false.
        
        :param striping: Specifies the striping information about new
                aggregate. The only allowed values are "striped"
                and "not_striped". Default value is "not_striped".
                "striped" value creates striped aggregate on node.
                This attribute is not allowed in unclustered
                environments.
                EINVALIDINPUTERROR is returned if value is other
                than "striped" and "not_striped".
                EOP_CLUSTER_ATTR_DISALLOWED is returned if this
                attribute is used in unclustered environments.
                EOP_DISALLOWED_ON_CFO_AGGR is returned if this
                attribute is set to "striped" when aggregate being
                created with 'cfo' HA policy.
        
        :param nodes: Target node to create aggregate. If no node name is
                provided, aggregate will be created on the local node.
                If one node name is provided, aggregate(striped or
                not_striped based on the striping input) will be created
                on that node.When multiple nodes are specified, striped
                aggregate will be created across multiple nodes.
        
        :param type: The type of the aggregate.
                Possible values: aggr, trad.
                - "aggr" (aggregate contains flexible volumes)
                - "trad" (aggregate contains exactly one traditional volume)
                If not specified, the default is "aggr."
                The value "trad" is invalid when the request is sent to the
                Admin Vserver LIF.
        
        :param allow_same_carrier: Using two disks from one carrier that houses multiple disks
                in one RAID group is not desirable. If that happens,
                Data ONTAP initiates a series of disk copy operations to
                correct that situation.
                Sometimes, selection of available spare disks makes it
                impossible to avoid placing two disks from one carrier in one
                RAID group. Setting this option to true allows placing two
                disks from one carrier in one RAID group.
                This option has an effect only when disks to be used are
                specified in 'disks'. This option is ignored when 'disk-count'
                is used.
        
        :param disk_size_with_unit: Disk size in the specified unit. It is a positive
                integer number followed by unit of "T", "G", "M" or "K".
                This "disk-size-with-unit"
                option is ignored if a specific list of disks is
                specified through the "disks" parameter.
                You must only use one of either "disk-size" or
                "disk-size-with-unit" parameters. If both appear, an error
                message will be returned.
        
        :param disk_type: Type of disks to use: ATA, BSAS, EATA, FCAL, FSAS, LUN, MSATA,
                SAS, SATA, SCSI, SSD, XATA, or XSAS.
                This option is needed only when disks of different types are
                connected to the filer.  It is not allowed if a list of
                disks to use is specified through the "disks" parameter.
                The ability to mix compatible disk types in one aggregate
                is controlled by the system option 'raid.disktype.enable'.
        
        :param raid_size: Specifies the maximum number of disks in each RAID
                group in the aggregate.  The maximum value for this
                parameter is 28.  The default value is platform-
                dependent.  The valid range of values is also
                platform-dependent, but never wider than [2..28].
        
        :param snaplock_type: Specifies the type of Snaplock aggregate to be
                created.
                Possible values - "compliance" or "enterprise"
                ESERVICENOTLICENSED is returned if the necessary Snaplock
                compliance or enterprise license has not been installed.
                EINVALIDINPUTERROR is returned if snaplock-type has an illegal
                value or if is-snaplock has been set to "false".
                EONTAPI_EWORMNOCLOCK is returned if SnapLock
                Compliance Clock is not running.
        
        :param simulate: Specifies to return the list of disks getting used to create
                the new aggregate. If set to "true", new aggregate won't be
                created but returns the disks that would be automatically
                selected for the creation of the aggregate. By default,
                simulate option is set to false.
        
        :param block_type: The indirect block format that the aggregate can have. It
                can be either 32_bit or 64_bit. Specifying 64_bit allows
                creation of aggregates that can be larger than 16TB. The
                default is 64_bit.
                Possible values: 32_bit, 64_bit
        
        :param mirror_disks: List of mirror disks to use.  It must contain the
                same number of disks specified in "disks".
        
        :param force_zcs: Specifies that the new aggregate will be zoned checksum.
                If set to true, then the new aggregate is zoned
                checksum. By default, the new aggregate's checksum
                type will be decided by disks selected and the default
                is to select disks for block checksum if they are available.
                This option should be used only for test.
        
        :param force_spare_pool: Disks in a plex are not normally permitted to span
                spare pools.  This behavior is overridden with this
                option when it is set to true.
                This is a deprecated parameter. Use the allow-mixed-rpm
                and ignore-pool-checks parameters instead.
        
        :param force_small_aggregate: Forces the creation of a 2-disk RAID4 aggregate, or a
                3-disk or 4-disk RAID-DP aggregate. The default value
                is false.
        
        :param disks: Specific list of disks to use for the new aggregate.
                If "mirrored" is set to true and a specific list
                of disks is supplied, the "mirror-disks" list with
                the same number of disks must also be supplied.
                Either "disk-count" or "disks" must be supplied.
        
        :param is_mirrored: Specifies that the new aggregate be mirrored (have
                two plexes).  If set to true, then the indicated
                disks will be split across the two plexes.  By
                default, the new aggregate will not be mirrored.
        
        :param allow_mixed_rpm: Disks in an aggregate are normally required to have the
                same RPM. This behavior is overridden with this
                option when it is set to true. Default value is false.
        
        :param disk_count: Number of disks to place into the aggregate,
                including parity disks.  The disks in this newly-
                created aggregate come from the spare disk pool.
                The smallest disks in this pool join the aggregate
                first, unless the "disk-size" argument is provided.
                Either "disk-count" or "disks" must be supplied.
                Range [0..2^31-1].
        """
        return self.request( "aggr-create", {
            'disk_size': [ disk_size, 'disk-size', [ int, 'None' ], False ],
            'ignore_pool_checks': [ ignore_pool_checks, 'ignore-pool-checks', [ bool, 'None' ], False ],
            'ha_policy': [ ha_policy, 'ha-policy', [ basestring, 'ha-policy-type' ], False ],
            'language_code': [ language_code, 'language-code', [ basestring, 'None' ], False ],
            'checksum_style': [ checksum_style, 'checksum-style', [ basestring, 'None' ], False ],
            'is_snaplock': [ is_snaplock, 'is-snaplock', [ bool, 'None' ], False ],
            'rpm': [ rpm, 'rpm', [ int, 'None' ], False ],
            'raid_type': [ raid_type, 'raid-type', [ basestring, 'None' ], False ],
            'spare_pool': [ spare_pool, 'spare-pool', [ basestring, 'None' ], False ],
            'pre_check': [ pre_check, 'pre-check', [ bool, 'None' ], False ],
            'striping': [ striping, 'striping', [ basestring, 'striping-type' ], False ],
            'nodes': [ nodes, 'nodes', [ basestring, 'node-name' ], True ],
            'type': [ type, 'type', [ basestring, 'None' ], False ],
            'allow_same_carrier': [ allow_same_carrier, 'allow-same-carrier', [ bool, 'None' ], False ],
            'disk_size_with_unit': [ disk_size_with_unit, 'disk-size-with-unit', [ basestring, 'None' ], False ],
            'disk_type': [ disk_type, 'disk-type', [ basestring, 'None' ], False ],
            'raid_size': [ raid_size, 'raid-size', [ int, 'None' ], False ],
            'snaplock_type': [ snaplock_type, 'snaplock-type', [ basestring, 'None' ], False ],
            'simulate': [ simulate, 'simulate', [ bool, 'None' ], False ],
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'block_type': [ block_type, 'block-type', [ basestring, 'None' ], False ],
            'mirror_disks': [ mirror_disks, 'mirror-disks', [ DiskInfo, 'None' ], True ],
            'force_zcs': [ force_zcs, 'force-zcs', [ bool, 'None' ], False ],
            'force_spare_pool': [ force_spare_pool, 'force-spare-pool', [ bool, 'None' ], False ],
            'force_small_aggregate': [ force_small_aggregate, 'force-small-aggregate', [ bool, 'None' ], False ],
            'disks': [ disks, 'disks', [ DiskInfo, 'None' ], True ],
            'is_mirrored': [ is_mirrored, 'is-mirrored', [ bool, 'None' ], False ],
            'allow_mixed_rpm': [ allow_mixed_rpm, 'allow-mixed-rpm', [ bool, 'None' ], False ],
            'disk_count': [ disk_count, 'disk-count', [ int, 'None' ], False ],
        }, {
            'pre-check-results': [ WarningCode, True ],
            'selected-disks': [ DiskInfo, True ],
            'bad-disks': [ DiskInfo, True ],
            'nonzeroed-disks': [ int, False ],
            'selected-mirror-disks': [ DiskInfo, True ],
        } )
    
    def aggr_plex_offline(self, aggregate, plex):
        """
        auto generated : Offline a plex
        
        :param aggregate: Aggregate
        
        :param plex: Plex
        """
        return self.request( "aggr-plex-offline", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'aggr-name' ], False ],
            'plex': [ plex, 'plex', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def aggr_verify(self, aggregate, action, plex_to_fix=None):
        """
        auto generated : Verify an aggregate
        
        :param aggregate: Aggregate
        
        :param action: Action
                Possible values:
                <ul>
                <li> "start"     - Start Verifying,
                <li> "stop"      - Stop Verifying,
                <li> "resume"    - Resume Verifying,
                <li> "suspend"   - Suspend Verifying,
                <li> "status"    - Check Verifying Status
                </ul>
        
        :param plex_to_fix: Plex to be Corrected in Case of Mismatches
        """
        return self.request( "aggr-verify", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'aggr-name' ], False ],
            'action': [ action, 'action', [ basestring, 'aggrverifyactiontype' ], False ],
            'plex_to_fix': [ plex_to_fix, 'plex-to-fix', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def raidgroup_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of raidgroup objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                raidgroup object.
                All raidgroup objects matching this query up to 'max-records'
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
        return self.request( "raidgroup-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ RaidgroupInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ RaidgroupInfo, 'None' ], False ],
        }, {
            'attributes-list': [ RaidgroupInfo, True ],
        } )
    
    def aggr_64bit_upgrade_start(self, aggregate, upgrade_64bit_mode=None):
        """
        Trigger upgrade from 32-bit to 64-bit on the specified
        aggregate without adding disks. This API produces a set of
        results in the background. These results are not available as
        output from aggr-64bit-upgrade-start. Use the 'aggr-list-info'
        and 'volume-list-info' APIs to query the results of the 64-bit
        upgrade process on the aggregate and contained flexible
        volumes, respectively.
        
        :param aggregate: Name or UUID of the aggregate for which to trigger
                64-bit upgrade.
        
        :param upgrade_64bit_mode: Option to specify if and how to grow volumes
                during the 64-bit upgrade. Legitimate values are "check",
                "grow_all", "grow_none", and "grow_reserved".
                If the "check" value is specified,
                aggr-64bit-upgrade-start produces a summary of
                the space impact which would result from
                upgrading the aggregate to 64-bit. This summary
                includes the space usage of each contained
                volume after the volume is upgraded to 64-bit
                and the amount of space that must be added to
                the volume to successfully complete the 64-bit upgrade.
                The summary can be obtained by querying the
                'aggr-list-info' and 'volume-list-info' APIs.
                The aggregate's summary is made available in the 'check'
                element that is part of the 'aggr-64bit-upgrade-info'
                typedef. The flexible volumes' summary is made available
                in the 'check' element that is part of the
                'volume-64bit-upgrade-info' typedef.
                This option does not result in an upgrade to 64-bit.
                If the "grow_all" value is specified,
                aggr-64bit-upgrade-start upgrades the aggregate to 64-bit.
                This option allows aggr-64bit-upgrade-start to
                automatically grow volumes as needed if they run out
                of space due to the 64-bit upgrade. The volumes will
                be grown to accommodate all the files within these volumes.
                This option does not affect volumes which have autosize
                enabled.
                If the "grow_none" value is specified,
                aggr-64bit-upgrade-start upgrades the aggregate to
                64-bit. This option does not allow aggr-64bit-upgrade-start
                to automatically grow volumes if they run out of space
                due to the 64-bit upgrade.
                If the "grow_reserved" value is specified,
                aggr-64bit-upgrade-start upgrades the aggregate to 64-bit.
                This option allows aggr-64bit-upgrade-start to
                automatically grow volumes if they run out of space
                due to the 64-bit upgrade, but only to accommodate
                the space reserved files within these volumes.
                This option does not affect volumes which have autosize
                enabled.
                The default is "grow_none".
        """
        return self.request( "aggr-64bit-upgrade-start", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'upgrade_64bit_mode': [ upgrade_64bit_mode, 'upgrade-64bit-mode', [ basestring, 'None' ], False ],
        }, {
            'upgrade-64bit-cookie': [ int, False ],
        } )
    
    def aggr_list_info(self, aggregate=None, filter_attrs=None, verbose=None):
        """
        Get aggregate status.
        
        :param aggregate: The aggregate name or UUID to get status for.
                See the synopsis for name/UUID format.
                If not supplied, get status of all aggregates
                owned by the local node.
        
        :param filter_attrs: This input is used as a discriminant when status is
                required for one or more aggregates. This option will
                be ignored when an aggregate name is specified.
                If no argument is supplied, default value is NULL.
                If this is NULL or all of its elements are not supplied,
                then this filter has no effect and the behavior is
                the same as described in the 'aggregate' input description.
        
        :param verbose: If set to "true", detailed volume and plex
                information (including all the RAID group and
                disk information) is returned.  If not supplied
                or set to "false", this extra information is not
                returned.
        """
        return self.request( "aggr-list-info", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'filter_attrs': [ filter_attrs, 'filter-attrs', [ FilterAttrsInfo, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'aggregates': [ AggrInfo, True ],
        } )
    
    def aggr_restrict(self, aggregate, unmount_volumes=None, cifs_delay_seconds=None):
        """
        Restrict the specified aggregate.  If the aggregate
        is embedded in a traditional volume, the entire
        traditional volume will be restricted.  An aggregate
        with one or more flexible volumes cannot be restricted;
        all of its contained volumes must first be destroyed.
        
        :param aggregate: Name or UUID of the aggregate to restrict.
                See the synopsis for name/UUID format and restrictions.
        
        :param unmount_volumes: If set to "TRUE", this option specifies that all of
                the volumes hosted by the given aggregate are to be
                unmounted before the restrict operation is executed.
                By default, the system will reject any attempt to
                restrict an aggregate that hosts one or more online
                volumes.
        
        :param cifs_delay_seconds: The number of seconds to wait before restricting any
                volumes that are hosted in the given aggregate that
                have active CIFS shares (if any).  A value of 0 means
                that all such volumes are to be offlined immediately
                with no warning.  CIFS users can lose data if they
                aren't given a chance to terminate applications
                gracefully.  By default, "cifs-delay-seconds" is 0.
                NOTE: This argument may ONLY appear if the
                "unmount-volumes" argument (see above) also appears
                and is set to "true".
        """
        return self.request( "aggr-restrict", {
            'aggregate': [ aggregate, 'aggregate', [ basestring, 'None' ], False ],
            'unmount_volumes': [ unmount_volumes, 'unmount-volumes', [ bool, 'None' ], False ],
            'cifs_delay_seconds': [ cifs_delay_seconds, 'cifs-delay-seconds', [ int, 'None' ], False ],
        }, {
        } )
