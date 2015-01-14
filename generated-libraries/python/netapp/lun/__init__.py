from netapp.connection import NaConnection
from invalid_nodename_setting_info import InvalidNodenameSettingInfo # 2 properties
from lun_stats_info import LunStatsInfo # 10 properties
from mixed_ostype_initiator_info import MixedOstypeInitiatorInfo # 5 properties
from lun_histogram_entry import LunHistogramEntry # 2 properties
from lun_bind_info import LunBindInfo # 8 properties
from invalid_vsa_setting_info import InvalidVsaSettingInfo # 3 properties
from lun_alignment_info import LunAlignmentInfo # 7 properties
from scsi_rev import ScsiRev # 0 properties
from resv_protocol import ResvProtocol # 0 properties
from lun_stats_get_iter_key_td import LunStatsGetIterKeyTd # 5 properties
from conflicting_initiator_info import ConflictingInitiatorInfo # 3 properties
from alignment_state import AlignmentState # 0 properties
from invalid_use_partner_cfmode_setting_info import InvalidUsePartnerCfmodeSettingInfo # 2 properties
from lun_copy_get_iter_key_td import LunCopyGetIterKeyTd # 3 properties
from iscsi_pr_nexus import IscsiPrNexus # 5 properties
from lun_alignment_get_iter_key_td import LunAlignmentGetIterKeyTd # 5 properties
from lunselect_enum import LunselectEnum # 0 properties
from lun_clone_lists_info import LunCloneListsInfo # 1 properties
from lba_hole_range_info import LbaHoleRangeInfo # 2 properties
from persistent_reservation_info import PersistentReservationInfo # 6 properties
from fcp_pr_nexus import FcpPrNexus # 3 properties
from lun_attribute_info import LunAttributeInfo # 2 properties
from san_size import SanSize # 0 properties
from time_interval import TimeInterval # 0 properties
from fcp_down_hba_info import FcpDownHbaInfo # 2 properties
from invalid_use_partner_ostype_setting_info import InvalidUsePartnerOstypeSettingInfo # 3 properties
from partition_list_entry import PartitionListEntry # 2 properties
from read_histogram_entry import ReadHistogramEntry # 2 properties
from alua_setting_mismatch_initiator_info import AluaSettingMismatchInitiatorInfo # 3 properties
from write_histogram_entry import WriteHistogramEntry # 2 properties
from lun_align_info import LunAlignInfo # 11 properties
from lun_map_get_iter_key_td import LunMapGetIterKeyTd # 6 properties
from lun_info import LunInfo # 32 properties
from partition_scheme import PartitionScheme # 0 properties
from conflict_wwpn import ConflictWwpn # 0 properties
from lunclass import Lunclass # 0 properties
from lun_os_type import LunOsType # 0 properties
from conflicting_luns_list import ConflictingLunsList # 1 properties
from lun_bind_get_iter_key_td import LunBindGetIterKeyTd # 5 properties
from invalid_cfmode_setting_info import InvalidCfmodeSettingInfo # 2 properties
from invalid_ostype_cfmode_setting_info import InvalidOstypeCfmodeSettingInfo # 2 properties
from mixed_vsa_initiator_info import MixedVsaInitiatorInfo # 5 properties
from lun_get_iter_key_td import LunGetIterKeyTd # 5 properties
from lun_map_info import LunMapInfo # 6 properties
from alua_setting_mismatch_initiator_group import AluaSettingMismatchInitiatorGroup # 3 properties
from lun_snap_usage_lun_info import LunSnapUsageLunInfo # 3 properties
from lun_copy_info import LunCopyInfo # 16 properties
from clone_status_info import CloneStatusInfo # 3 properties
from conflicting_map_info import ConflictingMapInfo # 2 properties

class LunConnection(NaConnection):
    
    def lun_config_check_single_image_info(self):
        """
        Returns a list of configuration warnings that
        pertain to problems specific to the 'single_image' fcp
        cfmode.  These errors must befixed prior to
        upgrading any filer cluster to run in 'single_image' mode.
        """
        return self.request( "lun-config-check-single-image-info", {
        }, {
            'conflicting-initiators': [ ConflictingInitiatorInfo, True ],
            'conflicting-maps': [ ConflictingMapInfo, True ],
            'invalid-nodename-settings': [ InvalidNodenameSettingInfo, False ],
        } )
    
    def lun_config_check_wwpn_conflicts_info(self):
        """
        Determine if duplicate World Wide Port Names (WWPNs) are present on a cluster pair.
        """
        return self.request( "lun-config-check-wwpn-conflicts-info", {
        }, {
            'conflicting-wwpns': [ basestring, True ],
        } )
    
    def lun_initiator_logged_in(self, initiator):
        """
        Determine if an initiator is logged in via FCP or iSCSI.
        
        :param initiator: Name of FCP or iSCSI initiator to check.
        """
        return self.request( "lun-initiator-logged-in", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
        }, {
            'is-logged-in': [ bool, False ],
        } )
    
    def lun_get_select_attribute(self, path):
        """
        Get the select attribute for the specified LUN.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-get-select-attribute", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'creation-time': [ basestring, False ],
            'previous-serial': [ basestring, False ],
            'creation-timestamp': [ int, False ],
            'select-attribute': [ basestring, False ],
        } )
    
    def lun_get_vdisk_attributes(self, serial_number):
        """
        Lookup a LUN path and storage system by serial number.
        
        :param serial_number: Serial number for the LUN.
        """
        return self.request( "lun-get-vdisk-attributes", {
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
        }, {
            'path': [ basestring, False ],
            'filer-name': [ basestring, False ],
            'vdisk-snapshot-name': [ basestring, False ],
        } )
    
    def lun_delete_vld_metadir_entry(self, path):
        """
        Deletes a VLD metadir entry.
        *** NOTE *** VLD support will be
        removed after the Anchorsteam release (the first major release
        after 6.5) of ONTAP, so this API will not work in
        subsequent major version of ONTAP.
        
        :param path: Path of the VLD to be deleted.
        """
        return self.request( "lun-delete-vld-metadir-entry", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_clone_list_info(self, volume, snapshot):
        """
        Lists all LUN clones with valid backing snapshots in the given snapshot.
        
        :param volume: Name of the volume.
        
        :param snapshot: Name of the snapshot.
        """
        return self.request( "lun-clone-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'lun-clone-list': [ LunCloneListsInfo, True ],
        } )
    
    def lun_get_comment(self, path):
        """
        Get the optional descriptive comment for a LUN.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-get-comment", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'comment': [ basestring, False ],
        } )
    
    def lun_snap_usage_list_info(self, volume, snapshot):
        """
        Lists all LUNs backed by data in the specified snapshot.
        It also lists the corresponding snapshots in which
        these LUNs exist.
        
        :param volume: Name of the volume.
        
        :param snapshot: Name of the snapshot.
        """
        return self.request( "lun-snap-usage-list-info", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'snapshot': [ snapshot, 'snapshot', [ basestring, 'None' ], False ],
        }, {
            'lun-snap-usage-luns': [ LunSnapUsageLunInfo, True ],
        } )
    
    def lun_lba_hole_range_query(self, end_lba, start_lba, lun_path):
        """
        Returns an array of start and end Logical Block Address (LBA)
        that are holes from WAFL perspective.  Each level-0 WAFL block,
        known as File Block Number (FBN), can accommodate 8 LBAs of
        size 512 bytes each.  As these LBAs are already holes, SDW/SDU
        will avoid punching holes to the FBN unnecessarily. A maximum
        of 32768 LBAs can be queried.
        NOTE: The LBAs must not overlap with prefix or suffix regions
        of LUN.
        
        :param end_lba: The ending LBA of the LUN where the scan for holes should end.
                The end-lba "must" be greater than start-lba. Difference
                between start-lba and end-lba should not exceed 32768
                (both inclusive).
        
        :param start_lba: The starting LBA of the LUN from where the scan for holes
                should begin.
        
        :param lun_path: The full path of the LUN for which hole information is to be
                queried. Format must be of the following - /vol/my_vol/my_lun
                NOTE: The LUN must not be a LUN clone.
        """
        return self.request( "lun-lba-hole-range-query", {
            'end_lba': [ end_lba, 'end-lba', [ int, 'None' ], False ],
            'start_lba': [ start_lba, 'start-lba', [ int, 'None' ], False ],
            'lun_path': [ lun_path, 'lun-path', [ basestring, 'None' ], False ],
        }, {
            'holes': [ LbaHoleRangeInfo, True ],
        } )
    
    def lun_get_occupied_size(self, path):
        """
        Get the size occupied by the LUN in the active FS.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-get-occupied-size", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'occupied-size': [ int, False ],
        } )
    
    def lun_copy_modify(self, destination_path, max_throughput, job_uuid):
        """
        Modify an ongoing LUN copy operation.
        
        :param destination_path: Destination Path
        
        :param max_throughput: Maximum Scanner Speed
        
        :param job_uuid: LUN Copy Job UUID
        """
        return self.request( "lun-copy-modify", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'max_throughput': [ max_throughput, 'max-throughput', [ int, 'None' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def lun_read_raw(self, path, length, offset):
        """
        Read raw data from LUN.  Used mainly to read label on
        a LUN.
        
        :param path: Path of the LUN.
        
        :param length: Number of bytes to write.
        
        :param offset: Offset to start writing.
        """
        return self.request( "lun-read-raw", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
        }, {
            'encoded-data': [ basestring, False ],
        } )
    
    def lun_set_space_reservation_info(self, path, enable):
        """
        Sets the space reservation settings for the named
        LUN.
        
        :param path: Path to the LUN for which the space
                reservations need to be set.
        
        :param enable: Enable or disable space reservation on this LUN.
        """
        return self.request( "lun-set-space-reservation-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'enable': [ enable, 'enable', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_reset_stats(self, path=None):
        """
        Resets (zeroes) block-protocol access statistics for LUN(s).
        
        :param path: Path of the LUN.  If path is specified, the stats of that
                LUN will be reset.  If path is not specified, stats of
                all LUNs are reset.
        """
        return self.request( "lun-reset-stats", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_unbind(self, protocol_endpoint_path, vvol_path, force=None):
        """
        Decrement the refcount for the given Vvol LUN binding. If the
        resulting reference count is 0, the Vvol binding will be removed
        and no longer available for client access at the specified
        protocol endpoint.
        
        :param protocol_endpoint_path: Protocol Endpoint
        
        :param vvol_path: VVol Path
        
        :param force: If true, unbind the Vvol completely even if the current reference
                count is greater than 1. The default is false.
        """
        return self.request( "lun-unbind", {
            'protocol_endpoint_path': [ protocol_endpoint_path, 'protocol-endpoint-path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'vvol_path': [ vvol_path, 'vvol-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_testmap(self, usenextref, rowcount, igroup, qtree=None, volume=None, lun_id=None, path=None, lun=None):
        """
        auto generated : Test the Map LUN performance
        
        :param usenextref: update the nextrefid table
        
        :param rowcount: number of ruows to test
        
        :param igroup: Initiator Group Name
        
        :param qtree: Qtree hosting the LUN
        
        :param volume: Volume hosting the LUN
        
        :param lun_id: The LUN ID to assign for the mapping.
        
        :param path: Path of the LUN
        
        :param lun: LUN name
        """
        return self.request( "lun-testmap", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'usenextref': [ usenextref, 'usenextref', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'rowcount': [ rowcount, 'rowcount', [ int, 'None' ], False ],
            'lun_id': [ lun_id, 'lun-id', [ int, 'None' ], False ],
            'igroup': [ igroup, 'igroup', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'lun': [ lun, 'lun', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_set_share(self, path, share_type):
        """
        Enables file system protocol-based access to a lun.
        By default, all accesses are disallowed. Note that file
        permissions and ACL entries still apply.
        
        :param path: Path of the LUN.
        
        :param share_type: Possible values: all, none, read, write
        """
        return self.request( "lun-set-share", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'share_type': [ share_type, 'share-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_map_list_info(self, path):
        """
        Returns a list of initiator groups and their members
        (the initiators) mapped to the given LUN.
        
        :param path: LUN for which the initiator group list is requested.
        """
        return self.request( "lun-map-list-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'initiator-groups': [ InitiatorGroupInfo, True ],
        } )
    
    def lun_initiator_list_map_info(self, initiator):
        """
        List all the luns mapped to an initiator
        
        :param initiator: initiator to check
        """
        return self.request( "lun-initiator-list-map-info", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
        }, {
            'lun-maps': [ LunMapInfo, True ],
        } )
    
    def lun_bind(self, protocol_endpoint_path, vvol_path):
        """
        Bind a Vvol LUN to a protocol endpoint. If the Vvol is already
        bound to the requested PE, the reference count for the binding
        will be incremented.
        
        :param protocol_endpoint_path: Protocol Endpoint
        
        :param vvol_path: VVol Path
        """
        return self.request( "lun-bind", {
            'protocol_endpoint_path': [ protocol_endpoint_path, 'protocol-endpoint-path', [ basestring, 'None' ], False ],
            'vvol_path': [ vvol_path, 'vvol-path', [ basestring, 'None' ], False ],
        }, {
            'secondary-lun': [ int, False ],
            'protocol-endpoint-identifier': [ basestring, False ],
        } )
    
    def lun_clone_split_status_list_info(self, path):
        """
        Get the cloning status of LUN(s).
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-clone-split-status-list-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'clone-status': [ CloneStatusInfo, True ],
        } )
    
    def lun_copy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of LUN copy job detail objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the LUN
                copy job detail object.
                All LUN copy job detail objects matching this query up to
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
        return self.request( "lun-copy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunCopyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunCopyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunCopyInfo, True ],
        } )
    
    def lun_create_by_size(self, path, size, space_reservation_enabled=None, qos_policy_group=None, prefix_size=None, ostype=None, type=None, class=None):
        """
        Create a new lun of given size, with initially zero contents.
        The lun is created at the path given. No file should
        already exist at the given path. The directory specified
        in the path must be a qtree root directory.
        The size of the created lun could be larger than the size
        specified, in order to get an integral number of cylinders
        while reporting the geometry using SAN protocols.
        
        :param path: Path of the LUN.
        
        :param size: New size for the LUN in bytes.
        
        :param space_reservation_enabled: By default, the lun is space-reserved. If it is desired to
                manage space usage manually instead, this can be set to "false"
                which will create a LUN without any space being reserved.
        
        :param qos_policy_group: QoS policy group defines measurable Service Level Objectives (SLOs)
                that apply to the storage objects with which the policy group is
                associated. If you do not assign a policy group to a lun, the system will
                not monitor and control the traffic to it.
                This field is available in Data ONTAP 8.2 and later
        
        :param prefix_size: The size of the prefix stream for this lun in bytes. Certain OS types store a small portion
                of the data corresponding to partition tables (or similar structures) in the prefix
                stream. This is part of the lun data and is transparent to hosts that access the LUN
                via block protocols.
                The default size is based on the ostype. Giving a value here overrides the default,
                but, it is strongly recommended to avoid changing this default size.
                The value in this field must be a multiple of 512 bytes.
                Note that this value has no effect when the lun-os-type is "image".
                This option is available in Data ONTAP 8.1 and later.
        
        :param ostype: The os type for the LUN. The default type if not specified
                is "image".
                It is strongly recommended for the caller of this
                API to avoid using the "image" type because it could
                result in misconfigured LUNs.  For example, a lun with
                ostype "image" could suffer major performance penalties
                when a Windows host is trying to access it.
        
        :param type: In lieu of ostype, for backward compatibility. Note that
                this parameter will be ignored if ostype is specified.
        
        :param class: The class of the LUN. Possible values:
                <ul>
                <li>"regular" - The LUN is for normal blocks access,
                <li>"protocol_endpoint" - The LUN is a vvol protocol endpoint,
                <li>"vvol" - The LUN is a vvol data LUN.
                </ul>
                The default value is "regular".
        """
        return self.request( "lun-create-by-size", {
            'space_reservation_enabled': [ space_reservation_enabled, 'space-reservation-enabled', [ bool, 'None' ], False ],
            'qos_policy_group': [ qos_policy_group, 'qos-policy-group', [ basestring, 'None' ], False ],
            'prefix_size': [ prefix_size, 'prefix-size', [ int, 'None' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'lun-os-type' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'lun-os-type' ], False ],
            'class': [ class, 'class', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'None' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def lun_copy_resume(self, destination_path, job_uuid):
        """
        Resume a paused LUN copy operation.
        
        :param destination_path: Destination Path
        
        :param job_uuid: LUN Copy Job UUID
        """
        return self.request( "lun-copy-resume", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def lun_online(self, path, force=None):
        """
        Re-enables block-protocol accesses to the lun.
        
        :param path: Path of the LUN.
        
        :param force: Forcibly online the lun, disabling mapping onflict checks
                with the high-availability partner.  If not specified all conflict
                checks are performed.
                In Data ONTAP Cluster-Mode, this field is accepted for backwards
                compatibility and is ignored.
        """
        return self.request( "lun-online", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_list_info(self, path=None, get_clone_backing_snapshot=None, volume_name=None):
        """
        Get the status (size, online/offline state, shared
        state, comment string, serial number, LUN mapping)
        of the given LUN, or all LUNs.
        
        :param path: Path of LUN. If specified, only the information of that
                LUN is returned. This option can only be used if volume-name
                is not used.
        
        :param get_clone_backing_snapshot: If specified, the name of the backing snapshot for a LUN clone
                is returned.
                The default value is false.
        
        :param volume_name: Name of a volume. If specified, only the information of the
                LUNs in that volume is returned. This option can only be used if
                path is not specified.
        """
        return self.request( "lun-list-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'get_clone_backing_snapshot': [ get_clone_backing_snapshot, 'get-clone-backing-snapshot', [ bool, 'None' ], False ],
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
        }, {
            'are-vols-busy': [ bool, False ],
            'luns': [ LunInfo, True ],
            'are-vols-onlining': [ bool, False ],
        } )
    
    def lun_clear_persistent_reservation_info(self, path):
        """
        Clear the SCSI-2 reservation or SCSI-3 persistent reservation
        information for a given LUN.
        Note: In Data ONTAP Cluster-Mode, the LUN must either be
        offline or not mapped to clear the persistent reservation
        information.
        
        :param path: Path of the lun.  The path should start with '/vol/'.
        """
        return self.request( "lun-clear-persistent-reservation-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_destroy(self, path, destroy_fenced_lun=None, force=None):
        """
        Destroy the specified LUN.  This operation will fail if
        the LUN is currently mapped and is online.  The force option
        can be used to destroy it regardless of being online or mapped.
        
        :param path: Path of the LUN.
        
        :param destroy_fenced_lun: If "true", override checks that prevent a LUN from being destroyed
                while it is fenced. If "false", attempting to destroy a fenced LUN
                will fail. The default if not specified is "false".
                This field is available in Data ONTAP 8.2 and later.
        
        :param force: If "true", override checks that prevent a LUN from being destroyed
                if it is online and mapped. If "false", destroying an online and
                mapped LUN will fail. The default if not specified is "false".
        """
        return self.request( "lun-destroy", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'destroy_fenced_lun': [ destroy_fenced_lun, 'destroy-fenced-lun', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_cleanup_qtree_nondisruptive_restore(self, transaction_id, qtree_path):
        """
        This API will destroy all the remaining luns stored in the temporary
        staging area after a non-disruptive restore. A successful preserve call
        followed by a restore call will automatically cleanup the staging area
        luns for that transaction. However, if for some reason, the restore was
        aborted or encountered an error, invoking this API will cleanup
        the stray temporary luns.
        
        :param transaction_id: The transaction ID is unique per qtree restore operation.
        
        :param qtree_path: Specifies the complete path of the qtree to be cleared.
                e.g., /vol/vol1/qtree1
        """
        return self.request( "lun-cleanup-qtree-nondisruptive-restore", {
            'transaction_id': [ transaction_id, 'transaction-id', [ int, 'None' ], False ],
            'qtree_path': [ qtree_path, 'qtree-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_copy_pause(self, destination_path, job_uuid):
        """
        Pause an ongoing LUN copy operation.
        
        :param destination_path: Destination Path
        
        :param job_uuid: LUN Copy Job UUID
        """
        return self.request( "lun-copy-pause", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def lun_get_attributes(self, path, name=None):
        """
        Get named attributes for a given LUN.
        
        :param path: Path of the LUN.
        
        :param name: Filter for the requested attribute names.
                SMF wildcards are allowed.
                If not specified, all available attributes on the
                LUN will be returned.
        """
        return self.request( "lun-get-attributes", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ LunAttributeInfo, True ],
        } )
    
    def lun_alignment_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of lun objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the lun
                object.
                All lun objects matching this query up to 'max-records' will be
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
        return self.request( "lun-alignment-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunAlignInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunAlignInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunAlignInfo, True ],
        } )
    
    def lun_stats_list_info(self, path=None):
        """
        Get block-protocol access statistics (in bytes) for LUN(s).
        
        :param path: Path of the LUN.  If path is specified, only the stats of
                that LUN is returned.  If path is not specified, stats
                of all LUNs are returned.
        """
        return self.request( "lun-stats-list-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'lun-stats': [ LunStatsInfo, True ],
        } )
    
    def lun_move(self, path, new_path):
        """
        Move (rename) a LUN.
        
        :param path: Path of the LUN to be moved.
        
        :param new_path: New path of the LUN being moved to.
        """
        return self.request( "lun-move", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'new_path': [ new_path, 'new-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_set_comment(self, comment, path):
        """
        Set the optional descriptive comment for a LUN.
        
        :param comment: Comment to set for given LUN.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-set-comment", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_write_raw(self, path, length, encoded_data, offset):
        """
        Write raw data to LUN.  Used mainly to write label on
        a LUN that is created from a snapshot.  Since the format
        of the label is dependent on the host, the filers will not
        be able to write the format themselves.
        
        :param path: Path of the LUN.
        
        :param length: Number of bytes to write.
        
        :param encoded_data: Base64 encoded data.
        
        :param offset: Offset to start writing.
        """
        return self.request( "lun-write-raw", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'length': [ length, 'length', [ int, 'None' ], False ],
            'encoded_data': [ encoded_data, 'encoded-data', [ basestring, 'None' ], False ],
            'offset': [ offset, 'offset', [ int, 'None' ], False ],
        }, {
        } )
    
    def lun_create_from_snapshot(self, path, snapshot_lun_path, space_reservation_enabled=None, type=None):
        """
        Creates a LUN in the active file system. The lun has
        the same initial contents as the referenced snapshot copy
        of an existing lun. (Note that no copy of the data is made.)
        Future writes go into the new lun. Reads of unmodified data
        are satisfied from the snapshot location.  Reads of modified
        data are satisfied by first attempting to find the required
        buffer in the new lun.  If a buffer is not found
        (buffer corresponds to a hole), it is looked for in the
        snapshot copy instead.
        
        :param path: Path of the LUN.
        
        :param snapshot_lun_path: LUN path in the snapshot to be created from.
        
        :param space_reservation_enabled: By default, the lun is space-reserved. If it is desired to
                manage space usage manually instead, this can be set to "false"
                which will create a LUN without any space being reserved.
        
        :param type: The os type for the LUN. The default type if not specified
                is "image".
                It is strongly recommended for the caller of this
                API to avoid using the "image" type because it could
                result in misconfigured LUNs.  For example, a lun with
                ostype "image" could suffer major performance penalties
                when a Windows host is trying to access it.
        """
        return self.request( "lun-create-from-snapshot", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'space_reservation_enabled': [ space_reservation_enabled, 'space-reservation-enabled', [ bool, 'None' ], False ],
            'snapshot_lun_path': [ snapshot_lun_path, 'snapshot-lun-path', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'lun-os-type' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def lun_lba_is_hole(self, lba, lun_path):
        """
        Determine if the given Logical Block Address (LBA) is hole.
        If the LBA is a hole, the WAFL File Block Number (FBN) that
        houses the LBA is a hole (un-allocated block in WAFL).  A
        single FBN of 4096 bytes accommodates 8 LBAs each of 512 bytes.
        
        :param lba: The LBA of the LUN to be inspected for hole
        
        :param lun_path: The full path of the LUN for which hole information is to be
                queried. Format must be of the following - /vol/my_vol/my_lun
                NOTE: The LUN must not be a LUN clone.
        """
        return self.request( "lun-lba-is-hole", {
            'lba': [ lba, 'lba', [ int, 'None' ], False ],
            'lun_path': [ lun_path, 'lun-path', [ basestring, 'None' ], False ],
        }, {
            'is-lba-hole': [ bool, False ],
        } )
    
    def lun_set_attribute(self, path, name, value):
        """
        Set a named attribute for a given LUN.
        Attributes are arbitrary key/value pairs for
        application-defined use.
        
        :param path: Path of the LUN.
        
        :param name: Application-defined attribute to set. In order to prevent
                conflicts between separate applications, it is recommended
                that applications prefix attribute names with their
                registered Internet domain name reversed component by
                component, and an application identifier. For example:
                "com.example.widgetapp.attribute".
                The following attributes are reserved by the system and may
                not be set: "custom", "cylinder_size", "dev_id", "enabled",
                "extent_size", "host_stamp", "path_last", "pserial",
                "pSerial", "serial", "snapshot", "snapshot_path_last", "type".
                In older versions of Data ONTAP, attempting to set a
                system-reserved attribute may adversely affect data
                integrity and availability of the storage system. Clients
                of this API must therefore take special care to not use any
                system-reserved attribute names.
        
        :param value: Value to set the attribute to.
                In Data ONTAP Cluster-mode, the combined size of "name" and
                "value" must not exceed 4092 bytes.
        """
        return self.request( "lun-set-attribute", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'value': [ value, 'value', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_unset_attribute(self, path, name):
        """
        Clear a named attribute for a given LUN.
        
        :param path: Path of the LUN.
        
        :param name: Name of attribute to unset.
                The following attributes are reserved by the system and may
                not be unset: "custom", "cylinder_size", "dev_id", "enabled",
                "extent_size", "host_stamp", "path_last", "pserial",
                "pSerial", "serial", "snapshot", "snapshot_path_last", "type".
                In older versions of Data ONTAP, attempting to unset a
                system-reserved attribute may adversely affect data
                integrity and availability of the storage system. Clients
                of this API must therefore take special care to not use any
                system-reserved attribute names.
        """
        return self.request( "lun-unset-attribute", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_clone_split_stop(self, path):
        """
        Stop the cloning of the given LUN.
        
        :param path: Path of the LUN to stop cloning.
        """
        return self.request( "lun-clone-split-stop", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_clone_start(self, path):
        """
        Start the cloning of the given LUN.
        
        :param path: Path of the LUN to clone.
        """
        return self.request( "lun-clone-start", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_start(self, path):
        """
        Starts block-protocol accesses to the lun.
        
        :param path: Path of the LUN. The path should start with '/vol/' (for example, "/vol/vol0/lun1").
        """
        return self.request( "lun-start", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_get_persistent_reservation_info(self, path):
        """
        Get the persistent reservation information for a given LUN.
        
        :param path: Path of the lun.  The path should start with '/vol/'.
        """
        return self.request( "lun-get-persistent-reservation-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'persistent-reservation': [ PersistentReservationInfo, True ],
        } )
    
    def lun_alignment_list_info(self, volume_name=None, verbose=None, lun_path=None):
        """
        Check the alignment of a specified LUN or all the
        LUNs in the controller.
        
        :param volume_name: Alignment state of LUNs belonging to only a specified volume name
                is displayed.
        
        :param verbose: Verbose output showing SCSI Ops details. Default is false. When this
                option is set to true disk-utilization, scsi-writes-percentage,
                misaligned-scsi-writes-percentage, aligned-scsi-writes-percentage
                partial-scsi-writes-percentage fields are displayed in output. This
                input cannot be used along with lun-path or volume inputs.
        
        :param lun_path: Complete LUN path for which LUN alignment has to be displayed.
                Format /vol/<vol-name>/<qtree-name>/<lun-name>
        """
        return self.request( "lun-alignment-list-info", {
            'volume_name': [ volume_name, 'volume-name', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
            'lun_path': [ lun_path, 'lun-path', [ basestring, 'None' ], False ],
        }, {
            'luns': [ LunAlignmentInfo, True ],
            'scsi-aligned-writes-percentage': [ int, False ],
            'scsi-writes-percentage': [ int, False ],
            'disk-utilization': [ basestring, False ],
            'scsi-partial-writes-percentage': [ int, False ],
            'scsi-misaligned-writes-percentage': [ int, False ],
        } )
    
    def lun_set_read_only(self, is_read_only, path):
        """
        Set or unset read-only attribute on a LUN.
        LUN must be offline.
        This attribute is supported on igroup types:windows,hyper_v.
        
        :param is_read_only: true or false to set or unset read_only attribute on LUN.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-set-read-only", {
            'is_read_only': [ is_read_only, 'is-read-only', [ bool, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_get_attribute(self, path, name):
        """
        Get a named attribute for a given LUN.
        
        :param path: Path of the LUN.
        
        :param name: Attribute to get.
        """
        return self.request( "lun-get-attribute", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
            'value': [ basestring, False ],
        } )
    
    def lun_get_maxsize(self, path, type):
        """
        Returns the maximum possible size in bytes of a lun on a given
        volume or qtree. The user can pass the path to a volume
        or qtree in which the lun is to be created. This
        returns the maximum size for different types of luns and
        the possible maximum size with or without snapshot reserves.
        
        :param path: Path of the volume or qtree.
        
        :param type: OS type of the LUN.
        """
        return self.request( "lun-get-maxsize", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'lun-os-type' ], False ],
        }, {
            'without-snapshot-reserve': [ int, False ],
            'with-snapshot-reserve': [ int, False ],
            'with-complete-snapshot-reserve': [ int, False ],
        } )
    
    def lun_set_device_id(self, path, device_id, device_id_type=None):
        """
        Set a SCSI peripheral device identifying information
        value on a LUN.
        In Data ONTAP 7-Mode, the value set will be returned
        in response to the vendor unique SCSI command GET DEV ID.
        In Data ONTAP Cluster-Mode, the value set will be returned
        in response to the SCSI command REPORT IDENTIFYING INFORMATION
        for the appropriate INFORMATION TYPE:
        <ul>
        <li> 0000000b - Peripheral Device Identifying Information,
        a binary string 1 to 64 bytes long. In addition, if
        the Peripheral Device Identifying Information is between
        00000001h (1d) and 0000270Fh (9999d), it will be
        returned in response to the vendor unique SCSI command
        GET DEV ID.
        <li> 0000010b - Peripheral Device Text Identifying
        Information, a UTF-8 string 1 to 255 bytes long.
        </ul>
        Either or both peripheral device identifying information
        values may be set or cleared independently.
        
        :param path: Path of the LUN.
        
        :param device_id: SCSI Peripheral Device Identifying Information.
                In Data ONTAP 7-Mode or if device-id-type is "legacy",
                the value must be an integer in the range [1..9999].
                If device-id-type is "binary", the value must be a
                1 to 64 byte value encoded as a hexadecimal string,
                for example "0000270F".
                If device-id-type is "text", the value is a free-form
                UTF-8 string between 1 and 255 bytes in length.
        
        :param device_id_type: Indicate which peripheral device identifying information
                value to change. Possible values:
                <ul>
                <li> "legacy" - Set the Peripheral Device Identifying
                Information for REPORT IDENTIFYING INFORMATION
                (INFORMATION TYPE 0000000b) appropriate for the
                the vendor unique SCSI command GET DEV ID and
                in the format compatible with Data ONTAP 7-Mode,
                <li> "binary" - Set the Peripheral Device Identifying
                Information for REPORT IDENTIFYING INFORMATION
                (INFORMATION TYPE 0000000b). This format allows setting
                all 64 bytes of the identifying information,
                <li> "text" - Set the Peripheral Device Text Identifying
                Information for REPORT IDENTIFYING INFORMATION
                (INFORMATION TYPE 0000010b).
                </ul>
                The default value is "legacy".
        """
        return self.request( "lun-set-device-id", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'device_id_type': [ device_id_type, 'device-id-type', [ basestring, 'None' ], False ],
            'device_id': [ device_id, 'device-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_get_space_reservation_info(self, path):
        """
        Queries the space reservation settings for the named
        LUN.
        
        :param path: Name of the LUN to be queried.
        """
        return self.request( "lun-get-space-reservation-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'is-enabled': [ bool, False ],
        } )
    
    def lun_clone_split_start(self, path, space_efficient_split_disabled=None):
        """
        Start the cloning of the given LUN.
        
        :param path: Path of the clone to split from the underlying parent.
        
        :param space_efficient_split_disabled: By default 'false', space-efficient LUN clone splitting
                is allowed. This parameter, if set to 'true', disables
                space-efficient splitting for this specific operation.
        """
        return self.request( "lun-clone-split-start", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'space_efficient_split_disabled': [ space_efficient_split_disabled, 'space-efficient-split-disabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_map_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of LUN map detail objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the LUN
                map detail object.
                All LUN map detail objects matching this query up to
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
        return self.request( "lun-map-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunMapInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunMapInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunMapInfo, True ],
        } )
    
    def lun_set_space_alloc(self, path, enable):
        """
        Modify the attributes of lun object.
        
        :param path: Path of the LUN
        
        :param enable: LUN space alloc setting
        """
        return self.request( "lun-set-space-alloc", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'enable': [ enable, 'enable', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_unmap(self, path, initiator_group):
        """
        Reverses the effect of lun-map on the specified LUN for
        the specified group.
        
        :param path: Path of the LUN.
        
        :param initiator_group: Initiator group to unmap from.
        """
        return self.request( "lun-unmap", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'initiator_group': [ initiator_group, 'initiator-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_set_select_attribute(self, select_value, path):
        """
        Set the select attribute for the specified LUN.
        The select attribute is used by mult-pathing software to
        discriminate between luns when  mirrored or cloned copies
        of a vdisk are mapped to the same host.
        
        :param select_value: Sets the select attribute for the lun.  Possible values:
                <ul>
                <li> "active" - this is an active lun,
                <li> "copy"   - this is a clone or copy of an active lun,
                <li> "mirror" - this is a mirror of an active lun.
                </ul>
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-set-select-attribute", {
            'select_value': [ select_value, 'select-value', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_create_clone(self, path, parent_snap, parent_lun_path, space_reservation_enabled=None):
        """
        Create a LUN clone.
        
        :param path: Path of the LUN clone.
        
        :param parent_snap: LUN path of the backing snapshot.
        
        :param parent_lun_path: Path of original LUN.
        
        :param space_reservation_enabled: By default, the lun is space-reserved. If it is desired to
                manage space usage manually instead, this can be set to "false"
                which will create a LUN without any space being reserved.
        """
        return self.request( "lun-create-clone", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'space_reservation_enabled': [ space_reservation_enabled, 'space-reservation-enabled', [ bool, 'None' ], False ],
            'parent_snap': [ parent_snap, 'parent-snap', [ basestring, 'None' ], False ],
            'parent_lun_path': [ parent_lun_path, 'parent-lun-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_get_geometry(self, path):
        """
        Get SCSI disk geometry for a given LUN.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-get-geometry", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'sectors-per-track': [ int, False ],
            'cylinders': [ int, False ],
            'bytes-per-sector': [ int, False ],
            'max-resize-size': [ int, False ],
            'tracks-per-cylinder': [ int, False ],
            'size': [ int, False ],
        } )
    
    def lun_get_serial_number(self, path):
        """
        Get the serial number for the specified LUN.
        Prior to Data ONTAP 8.1 release, the serial number
        is a 12-character string formed of
        upper and lower-case letters, numbers, and slash (/)
        and hyphen (-) characters.
        Starting Data ONTAP 8.1 release, the serial number is a
        12-character string formed of upper and lower-case letters,
        numbers, and the characters /-#$%&*+<=>?[!]^~@ .
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-get-serial-number", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'serial-number': [ basestring, False ],
        } )
    
    def lun_test_vdisk_size(self, size):
        """
        auto generated : Test vdisk_cmd_print_size functionality
        
        :param size: Size
        """
        return self.request( "lun-test-vdisk-size", {
            'size': [ size, 'size', [ int, 'san-size' ], False ],
        }, {
        } )
    
    def lun_set_qos_policy_group(self, path, qos_policy_group):
        """
        @desc
        
        :param path: Path of the LUN
        
        :param qos_policy_group: QoS Policy Group for the lun. Setting this value to 'none'
                removes the lun from a policy group
        """
        return self.request( "lun-set-qos-policy-group", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'qos_policy_group': [ qos_policy_group, 'qos-policy-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_clone_status_list_info(self, path=None):
        """
        Get the cloning status of LUN(s).
        
        :param path: Path of the LUN.  If path is specified, only
                the status of that clone is retuned.  If path is not
                specified, then all cloning status are returned.
        """
        return self.request( "lun-clone-status-list-info", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'clone-status': [ CloneStatusInfo, True ],
        } )
    
    def lun_resize(self, path, size, force=None):
        """
        Changes the size of the lun. Note that client-side operations
        may be needed to ensure that client software recognizes the
        changed size.
        
        :param path: Path of the LUN.
        
        :param size: New size for the LUN.
        
        :param force: Forcibly reduce the size.  This is required for reducing the
                size of the LUN to avoid accidentally reducing the LUN size.
        """
        return self.request( "lun-resize", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'size': [ size, 'size', [ int, 'None' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def lun_clone_stop(self, path):
        """
        Stop the cloning of the given LUN.
        
        :param path: Path of the LUN to stop cloning.
        """
        return self.request( "lun-clone-stop", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_stats_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of lun objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the lun
                object.
                All lun objects matching this query up to 'max-records' will be
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
        return self.request( "lun-stats-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunStatsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunStatsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunStatsInfo, True ],
        } )
    
    def lun_restore_status(self, path):
        """
        Get state of LUN restore.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-restore-status", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'is-running': [ bool, False ],
        } )
    
    def lun_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of lun objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the lun
                object.
                All lun objects matching this query up to 'max-records' will be
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
        return self.request( "lun-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunInfo, True ],
        } )
    
    def lun_get_target_device_id(self, lun_serial_id):
        """
        Returns the SCSI Target Device Id.
        
        :param lun_serial_id: Serial number of the lun.
        """
        return self.request( "lun-get-target-device-id", {
            'lun_serial_id': [ lun_serial_id, 'lun-serial-id', [ basestring, 'None' ], False ],
        }, {
            'target-device-id': [ basestring, False ],
        } )
    
    def lun_config_check_info(self):
        """
        Returns a list of lun/fcp configuration warnings.
        These warnings are not related to filer cluster
        configuration.
        """
        return self.request( "lun-config-check-info", {
        }, {
            'mixed-vsa-initiators': [ MixedVsaInitiatorInfo, True ],
            'alua-setting-mismatch-initiators': [ AluaSettingMismatchInitiatorInfo, True ],
            'mixed-ostype-initiators': [ MixedOstypeInitiatorInfo, True ],
            'fcp-down-hbas': [ FcpDownHbaInfo, True ],
            'invalid-vsa-settings': [ InvalidVsaSettingInfo, True ],
            'alua-setting-mismatch-info': [ AluaSettingMismatchInitiatorGroup, True ],
        } )
    
    def lun_restore_qtree_nondisruptive_restore(self, transaction_id, qtree_path):
        """
        This API will restore the maps and attributes of the luns stored in the
        temporary staging area to the luns in the restored qtree. Host
        applications will now be mapped to the luns in the restored qtree.
        
        :param transaction_id: The transaction ID is unique per qtree restore operation.
        
        :param qtree_path: Specifies the complete path of the qtree to be restored.
                e.g., /vol/vol1/qtree1
        """
        return self.request( "lun-restore-qtree-nondisruptive-restore", {
            'transaction_id': [ transaction_id, 'transaction-id', [ int, 'None' ], False ],
            'qtree_path': [ qtree_path, 'qtree-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_copy_destroy(self, destination_path, job_uuid, force=None):
        """
        Abort an ongoing LUN copy operation.
        
        :param destination_path: Destination Path
        
        :param job_uuid: LUN Copy Job UUID
        
        :param force: Force destroy
        """
        return self.request( "lun-copy-destroy", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def lun_get_minsize(self, type):
        """
        Returns the minimum possible size in bytes.  This
        returns the minimum size for different types of luns (based
        on the specified OS type).  Space reservation does not
        affect the minimum lun size, thus only a single minimum
        size is returned.
        
        :param type: OS type of the LUN.
        """
        return self.request( "lun-get-minsize", {
            'type': [ type, 'type', [ basestring, 'lun-os-type' ], False ],
        }, {
            'min-size': [ int, False ],
        } )
    
    def lun_id_swap(self, destination_path, source_path):
        """
        This API swaps the maps and attributes of two LUNs. The LUNs may
        exist in any volume or qtree. Before invoking this ZAPI make
        sure no application or the OS is using either the LUN. The requirments
        for this interface are still being decided on, see the functional spec.
        for newest details. Additionally, this zapi requests scsitgt to change
        the state of both LUNs (prior to the swap) so that new I/O requests
        will not be queued. At the time of that request all currently queued
        I/Os will be allowed to complete. However, if they dont complete
        within a set period this zapi will fail with the error code below.
        
        :param destination_path: Specifies the complete path of the destination lun.
        
        :param source_path: Specifies the complete path of the source lun.
                e.g., /vol/vol1/qtree1/lun1
        """
        return self.request( "lun-id-swap", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_create_vld_metadir_entry(self, path):
        """
        Creates a VLD metadir entry.  The VLD path must already
        exist (created with some form of lun-create-*).
        *** NOTE *** VLD support will be
        removed after the Anchorsteam release (the first major release
        after 6.5) of ONTAP, so this API will not work in
        subsequent major version of ONTAP.
        
        :param path: Path of the VLD to be created.
        """
        return self.request( "lun-create-vld-metadir-entry", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_get_inquiry_info(self, initiator_group_name):
        """
        Get the SCSI INQUIRY response data for vendor id (vid),
        product id (pid), and firmware revision (rev) based on the
        igroup that the lun in question is mapped to.
        
        :param initiator_group_name: The initiator group for which the vid/pid/rev information
                is to be returned.
        """
        return self.request( "lun-get-inquiry-info", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
        }, {
            'firmware-revision': [ basestring, False ],
            'product-id': [ basestring, False ],
            'vendor-id': [ basestring, False ],
        } )
    
    def lun_has_scsi_reservations(self, path):
        """
        Queries for all types of scsi reservations covering both
        iSCSI and FCP.
        
        :param path: Path of the lun.  The path should start with '/vol/'.
        """
        return self.request( "lun-has-scsi-reservations", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'is-reservation-held': [ bool, False ],
        } )
    
    def lun_lun_rescan(self, volume, vserver, build_oovc=None, sync=None, sync_new_identifiers=None, build_vtoc=None, sync_oovc_to_vol=None):
        """
        auto generated : Rescan the volume again to find all the LUN
        objects.
        
        :param volume: Volume Name
        
        :param vserver: Vserver Name
        
        :param build_oovc: Build OOVC
        
        :param sync: Sync
        
        :param sync_new_identifiers: Sync New IDs
        
        :param build_vtoc: Build VTOC
        
        :param sync_oovc_to_vol: Sync OOVC to Vol
        """
        return self.request( "lun-lun-rescan", {
            'build_oovc': [ build_oovc, 'build-oovc', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'sync': [ sync, 'sync', [ bool, 'None' ], False ],
            'sync_new_identifiers': [ sync_new_identifiers, 'sync-new-identifiers', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'build_vtoc': [ build_vtoc, 'build-vtoc', [ bool, 'None' ], False ],
            'sync_oovc_to_vol': [ sync_oovc_to_vol, 'sync-oovc-to-vol', [ bool, 'None' ], False ],
        }, {
        } )
    
    def lun_create_from_file(self, file_name, path, space_reservation_enabled=None, ostype=None, qos_policy_group=None, class=None):
        """
        Create a lun from an existing file. A new lun is created,
        at the given lun path (which must be at a qtree root).
        A hard link is created to the existing file. The file
        contents are not copied or changed. The file can be resized
        to a larger size, rounding up to a cylinder boundary.
        
        :param file_name: A fully qualified filer path to the file to create the LUN from.
                This must be in the same qtree as the LUN being created.
                The file must also be in the root of the volume or in a qtree/regular
                directory in the root of the volume or in a regular directory
                in a qtree.
        
        :param path: Would be Path of the newly created LUN if successful.
                This Path must not exist already (i.e a file or dir
                with this same path).
        
        :param space_reservation_enabled: By default, the lun is space-reserved. If it is desired to
                manage space usage manually instead, this can be set to "false"
                which will create a LUN without any space being reserved.
        
        :param ostype: The os type for the LUN. The default type if not specified
                is "image".
                It is strongly recommended for the caller of this
                API to avoid using the "image" type because it could
                result in misconfigured LUNs.  For example, a lun with
                ostype "image" could suffer major performance penalties
                when a Windows host is trying to access it.
        
        :param qos_policy_group: QoS policy group defines measurable Service Level Objectives (SLOs)
                that apply to the storage objects with which the policy group is
                associated. If you do not assign a policy group to a lun, the system will
                not monitor and control the traffic to it.
                This field is available in Data ONTAP 8.2 and later
        
        :param class: The class of the LUN. Possible values:
                <ul>
                <li>"regular" - The LUN is for normal blocks access,
                <li>"protocol_endpoint" - The LUN is a vvol protocol endpoint,
                <li>"vvol" - The LUN is a vvol data LUN.
                </ul>
                The default value is "regular".
        """
        return self.request( "lun-create-from-file", {
            'space_reservation_enabled': [ space_reservation_enabled, 'space-reservation-enabled', [ bool, 'None' ], False ],
            'file_name': [ file_name, 'file-name', [ basestring, 'None' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'lun-os-type' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'qos_policy_group': [ qos_policy_group, 'qos-policy-group', [ basestring, 'None' ], False ],
            'class': [ class, 'class', [ basestring, 'None' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def lun_copy_start(self, destination_path, source_path, promote_early=None, scanner_paused=None, max_throughput=None):
        """
        Starts the LUN copy
        
        :param destination_path: Destination Path
        
        :param source_path: Source Path
        
        :param promote_early: Default: false
        
        :param scanner_paused: Default: false
        
        :param max_throughput: Maximum Scanner Speed
        """
        return self.request( "lun-copy-start", {
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'promote_early': [ promote_early, 'promote-early', [ bool, 'None' ], False ],
            'scanner_paused': [ scanner_paused, 'scanner-paused', [ bool, 'None' ], False ],
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
            'max_throughput': [ max_throughput, 'max-throughput', [ int, 'None' ], False ],
        }, {
            'job-uuid': [ basestring, False ],
        } )
    
    def lun_unset_device_id(self, path, device_id_type=None):
        """
        Remove a SCSI peripheral device identifying information
        value from a LUN.
        
        :param path: Path of the LUN.
        
        :param device_id_type: Indicate which peripheral device identifying information to
                remove. Possible values:
                <ul>
                <li> "binary" - Remove the Peripheral Device Identifying
                Information returned in response to the SCSI commands
                REPORT IDENTIFYING INFORMATION (INFORMATION TYPE 0000000b)
                and GET DEV ID,
                <li> "text" - Remove the Peripheral Device Text Identifying
                Information returned in response to the SCSI command
                REPORT IDENTIFYING INFORMATION (INFORMATION TYPE 0000010b).
                </ul>
                The default value is "binary".
        """
        return self.request( "lun-unset-device-id", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'device_id_type': [ device_id_type, 'device-id-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_offline(self, path):
        """
        Disables block-protocol accesses to the LUN. Mappings,
        if any, configured for the lun are not altered. Note that
        unless explicitly offlined, a lun is online.
        
        :param path: Path of the LUN.
        """
        return self.request( "lun-offline", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_set_serial_number(self, path, serial_number):
        """
        Set the serial number for the specified LUN.  The lun
        must first be made offline before changing the serial number.
        Prior to Data ONTAP 8.1 release, the serial number
        is a 12-character string formed of
        upper and lower-case letters, numbers, and slash (/)
        and hyphen (-) characters.
        Starting Data ONTAP 8.1 release, the serial number is a
        12-character string formed of upper and lower-case letters,
        numbers, and the characters /-#$%&*+<=>?[!]^~@ .
        
        :param path: Path of the LUN.
        
        :param serial_number: Serial number for the LUN.
        """
        return self.request( "lun-set-serial-number", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_port_has_scsi_reservations(self, portname, path):
        """
        Queries for all types of scsi reservations covering both
        iSCSI and FCP for a given initiator name. Initiator name can be
        FCP portname in case of FCP or ISCSI nodename for ISCSI.
        
        :param portname: Initiator FCP portname or ISCSI nodename .
        
        :param path: Path of the lun.  The path should start with '/vol/'.
        """
        return self.request( "lun-port-has-scsi-reservations", {
            'portname': [ portname, 'portname', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'is-reservation-held': [ bool, False ],
        } )
    
    def lun_map(self, path, initiator_group, force=None, lun_id=None):
        """
        Maps the LUN to all the initiators in the specified
        initiator group.
        
        :param path: Path of the LUN.
        
        :param initiator_group: Initiator group to map to the given LUN.
        
        :param force: Forcibly map the lun, disabling mapping conflict checks with
                the high-availability partner.  If not specified all conflict
                checks are performed.
                In Data ONTAP Cluster-Mode, this field is accepted for backwards
                compatibilty and is ignored.
        
        :param lun_id: If the lun-id is not specified, the smallest number
                that can be used for the various initiators in the
                group is automatically picked.
        """
        return self.request( "lun-map", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'initiator_group': [ initiator_group, 'initiator-group', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'lun_id': [ lun_id, 'lun-id', [ int, 'None' ], False ],
        }, {
            'lun-id-assigned': [ int, False ],
        } )
    
    def lun_bind_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Vvol LUN binding objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Vvol LUN binding object.
                All Vvol LUN binding objects matching this query up to
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
        return self.request( "lun-bind-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LunBindInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LunBindInfo, 'None' ], False ],
        }, {
            'attributes-list': [ LunBindInfo, True ],
        } )
    
    def lun_preserve_qtree_nondisruptive_restore(self, transaction_id, qtree_path):
        """
        This API will preserve the maps and attributes of the luns in the qtree
        being restored in a temporary staging area. As a result of this API,
        host applications will be mapped to the luns in the staging area.
        
        :param transaction_id: The transaction ID is unique per qtree restore operation.
        
        :param qtree_path: Specifies the complete path of the qtree to be preserved.
                e.g., /vol/vol1/qtree1
        """
        return self.request( "lun-preserve-qtree-nondisruptive-restore", {
            'transaction_id': [ transaction_id, 'transaction-id', [ int, 'None' ], False ],
            'qtree_path': [ qtree_path, 'qtree-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def lun_config_check_cfmode_info(self):
        """
        Returns a list of configuration warnings related to
        initiator groups and the fcp cfmode setting
        """
        return self.request( "lun-config-check-cfmode-info", {
        }, {
            'fcp-cfmode': [ basestring, False ],
            'invalid-cfmode-settings': [ InvalidCfmodeSettingInfo, False ],
            'invalid-use-partner-cfmode-settings': [ InvalidUsePartnerCfmodeSettingInfo, True ],
            'invalid-use-partner-ostype-settings': [ InvalidUsePartnerOstypeSettingInfo, True ],
            'invalid-ostype-cfmode-settings': [ InvalidOstypeCfmodeSettingInfo, True ],
        } )
    
    def lun_config_check_alua_conflicts_info(self):
        """
        Returns a list of luns that have both FCP and ISCSI
        maps at the same time when ALUA is enabled on atleast
        one of such FCP or ISCSI igroups. These conflicts must
        be resolved before any further maps (to those luns) can
        can take place.
        """
        return self.request( "lun-config-check-alua-conflicts-info", {
        }, {
            'conflicting-luns': [ ConflictingLunsList, True ],
        } )
