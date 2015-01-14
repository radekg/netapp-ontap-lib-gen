from netapp.connection import NaConnection
from maint_start_status_info import MaintStartStatusInfo # 2 properties
from disk_sanown_filer_detail_info import DiskSanownFilerDetailInfo # 2 properties
from v_series_detail_info import VSeriesDetailInfo # 17 properties
from disk_sanown_detail_info import DiskSanownDetailInfo # 13 properties
from maint_test_id import MaintTestId # 0 properties
from maint_test_iteration import MaintTestIteration # 0 properties
from disk_detail_info import DiskDetailInfo # 52 properties
from maint_test_status_info import MaintTestStatusInfo # 7 properties
from maint_abort_status_info import MaintAbortStatusInfo # 2 properties
from storage_ssd_info import StorageSsdInfo # 3 properties
from maint_test_list_info import MaintTestListInfo # 2 properties
from disk_filesys_usage_detail_info import DiskFilesysUsageDetailInfo # 24 properties
from maint_test_result_info import MaintTestResultInfo # 6 properties
from maint_disk_name import MaintDiskName # 0 properties
from nvramid import Nvramid # 0 properties
from diskchecksumstyle import Diskchecksumstyle # 0 properties
from disktype import Disktype # 0 properties

class DiskConnection(NaConnection):
    
    def disk_sanown_filer_list_info(self, node):
        """
        Get sanown filer information.
        
        :param node: Node name for which info is requested
        """
        return self.request( "disk-sanown-filer-list-info", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'disk-sanown-filer-details': [ DiskSanownFilerDetailInfo, True ],
        } )
    
    def disk_replace_stop(self, disk):
        """
        Abort disk replace.
        
        :param disk: Name of the file system disk being replaced.
        """
        return self.request( "disk-replace-stop", {
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_fail(self, disk, is_immediate=None):
        """
        Fail a file system disk.
        Removes the specified file system disk from the RAID
        configuration, spinning the disk down when removal is
        complete. disk fail is used to remove a file system
        disk that may be logging excessive errors and requires
        replacement. Note that if optional input parameter
        'is-immediate' is true, the specified disk will be
        immediately failed out, and the RAID group to which
        the disk belongs will enter degraded mode (meaning a
        disk is missing from the RAID group). If a spare disk
        at least as large as the disk being removed is
        available, the contents of the disk being removed will
        be reconstructed onto that spare disk. If 'is-immediate'
        options is false or not specified, system will prefail
        the disk and its content will be copied to a replacement
        disk if a suitable spare disk is available, and afterwards
        the prefailed disk will be failed out. This process can be
        observed by polling disk-list-info for this disk and tracking
        values of elements copy-destination and copy-percent.
        Same can be done using 'storage-disk-get-iter' when
        requested from Admin Vserver LIF.
        The disk being failed is marked as ``broken'', so
        that if it remains in the disk shelf, it will not be
        used by the filer as a spare disk. If the disk is
        moved to another filer, that filer will use it as a
        spare. This is not a recommended course of action, as
        the reason that the disk was failed may have been
        because it needed to be replaced.
        NOTE: Data ONTAP 7.0 and earlier releases don't indicate
        failure code properly.
        
        :param disk: Name of the disk to fail, e.g. "v0.1".
                On Admin Vserver LIF, this will be disk path name
                with format of "<Node Name>:<Disk Name>".
                e.g. "Filer01:v0.1"
        
        :param is_immediate: Specify 'true' if disk is to be failed out immediately.
                If disk is to be prefailed, specify 'false'. Default value
                is 'false'.
        """
        return self.request( "disk-fail", {
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'is_immediate': [ is_immediate, 'is-immediate', [ bool, 'None' ], False ],
        }, {
        } )
    
    def disk_sanown_assign(self, disk_type=None, all=None, force=None, checksum=None, node_name=None, auto=None, owner=None, owner_id=None, disk=None, pool=None, disk_count=None):
        """
        Assigns ownership of a disk. The normal usage is when the
        disk is unowned, or to assign a disk to a pool.
        
        :param disk_type: Assign specified type of disk(or set of disks).
                The disk-count parameter is mandatory.
                Type of disk: ATA, BSAS, EATA, FCAL, FSAS, LUN, MSATA,
                SAS, SATA, SCSI, SSD, BSSD, XATA, XSAS, or unknown.
        
        :param all: Assign all unowned visible disks to the specified node.
                The node parameter is mandatory. No other parameter is allowed
                with this option.
        
        :param force: Force flag need to be set to 'true' if assigning disks
                which are already owned a Filer.  However, if that Filer
                is up and has put a reservation on the disk, even the
                force option won't work.
        
        :param checksum: Assign checksum type to disk. Option may only be specified on
                a RAID array LUNs. Possible values: 'block' or 'zoned'.
        
        :param node_name: Used only with auto or all parameter. It specifies the node
                to which autoassignment or assignment of all unowned disks
                must be done.
        
        :param auto: Auto-assign unowned disks which are on loops where only 1 filer
                owns the disks and the pool information is the same, to the
                specified node. The node parameter is mandatory.
                No other parameter is allowed with this option.
        
        :param owner: Assign disk to specific owner.Either owner or owner-id is
                mandatory
        
        :param owner_id: Assign disk to specific owner ID (NVRAM ID or serial number).
                Either owner or owner-id is mandatory
                Range : [0..2^32-1].
        
        :param disk: Name of disk to assign.
                Wildcarding for disk string is supported. Either owner or owner-id
                is mandatory. The node parameter is not allowed with this option.
        
        :param pool: Assign disk to specific pool, e.g. '0' or '1'.
        
        :param disk_count: Assign specified count of disks
        """
        return self.request( "disk-sanown-assign", {
            'disk_type': [ disk_type, 'disk-type', [ basestring, 'None' ], False ],
            'all': [ all, 'all', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'checksum': [ checksum, 'checksum', [ basestring, 'None' ], False ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'auto': [ auto, 'auto', [ bool, 'None' ], False ],
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'owner_id': [ owner_id, 'owner-id', [ int, 'None' ], False ],
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'pool': [ pool, 'pool', [ int, 'None' ], False ],
            'disk_count': [ disk_count, 'disk-count', [ int, 'None' ], False ],
        }, {
        } )
    
    def disk_set_led(self, disk, led_state):
        """
        Set the disk LED state
        Internal error.
        The specified disk was invalid. This will
        cause the command to fail immediately. No action will be taken.
        The specified led-state was invalid.
        
        :param disk: Disk to set the LED state
        
        :param led_state: The LED state to set
                Possible values are 'evac-start', 'evac-end', 'led-on', 'led-off'
        """
        return self.request( "disk-set-led", {
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'led_state': [ led_state, 'led-state', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_zero_spares(self, node_name=None):
        """
        Set up all non-zeroed spares owned by the filer to start
        zeroing.  This operation is asynchronous, and therefore
        returns no errors that might occur when the zeroing
        operation actually starts, which could be several seconds
        after this API operation completes.
        Zeroing progress can be monitored via the disk-list-info
        API. Same can be done using 'storage-disk-get-iter' when
        requested from Admin Vserver LIF.
        The "zeroing-percent" element of disk-detail-info
        is returned if disk zeroing has started, and "is-zeroed"
        returns TRUE once the zeroing has completed (or, if zeroing
        wasn't necessary in the first place).
        
        :param node_name: Name of the node on which spare disks to be zeroed
                When requested from Admin Vserver LIF and node name is not
                specified, spare disks from all nodes in the cluster will
                be zeroed.
        """
        return self.request( "disk-zero-spares", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_release_all_reservations(self):
        """
        Release reservations on all reserved disks.
        When invoked from maintenance mode, all reservations
        are released on all disks until the system is rebooted.
        When not in maintenance mode, then the system will
        automatically re-issue reservations for disks it owns.
        In sanown environment the system will reserve its
        disks everu 30 seconds.
        Reservations are disabled on this system.
        Command failed. Was unable to release reservations on one
        or more disks.
        """
        return self.request( "disk-release-all-reservations", {
        }, {
        } )
    
    def disk_sanown_reassign(self, new_owner=None, new_owner_id=None, force=None, old_owner=None, old_owner_id=None):
        """
        Changes ownership on disks already belonging to an owner.
        
        :param new_owner: Name of new owner.  This form will assign all the disks
                belonging to the old owner to the specific owner.
        
        :param new_owner_id: ID of new owner.  This form will assign all the disks
                belonging to the old owner to the specific owner ID.
                Either new-owner or new-owner-id (or both) must be
                specified.  Range : [0..2^32-1].
        
        :param force: Force flag need to be set to 'true' if reassigning disks
                which are owned by another Filer.  However, if that Filer
                is up and has put a reservation on the disk, even the
                force option won't work.  In this case reassign will
                need to be run on the Filer which owns the disks.
        
        :param old_owner: Name of old owner.  This form takes all disks currently
                belonging to the specific old owner, and reassigns them
                to a new owner.
        
        :param old_owner_id: ID of old owner.  This form takes all disks currently
                belonging to the specific old owner ID, and reassign them
                to a new owner.  Either old-owner or old-owner-id must
                be specified, but not both.  Range : [0..2^32-1].
        """
        return self.request( "disk-sanown-reassign", {
            'new_owner': [ new_owner, 'new-owner', [ basestring, 'None' ], False ],
            'new_owner_id': [ new_owner_id, 'new-owner-id', [ int, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'old_owner': [ old_owner, 'old-owner', [ basestring, 'None' ], False ],
            'old_owner_id': [ old_owner_id, 'old-owner-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def disk_maint_abort(self, disks):
        """
        Abort running Maintenance Center tests.
        
        :param disks: Abort Maintenance Center tests for given disk(s), e.g. "v0.1".
        """
        return self.request( "disk-maint-abort", {
            'disks': [ disks, 'disks', [ basestring, 'maint-disk-name' ], True ],
        }, {
            'maint-abort-status': [ MaintAbortStatusInfo, True ],
        } )
    
    def disk_remove(self, disk, remove_reason=None):
        """
        Remove a spare disk.
        Removes the specified spare disk from the RAID
        configuration, spinning the disk down when removal
        is complete. You can use disk remove to remove a spare
        disk so that it can be used by another filer (as a
        replacement for a failed disk or to expand file system space).
        NOTE: Data ONTAP 7.0 and earlier releases don't indicate
        failure code properly.
        
        :param disk: Name of the disk to remove, e.g. "v0.1".
                On Admin Vserver LIF, this will be disk path name
                with format of "<Node Name>:Disk Name".
                e.g. "Filer01:2a.32"
        
        :param remove_reason: The reason for failing the disk.  Possible values are:
                <ul>
                <li> "admin_removed"          - Admin removed disk.
                <li> "evacuation"             - Disk is marked for evacuation.
                </ul>
                The default value is "admin_removed".
                The failure disk will be recorded with "admin removed" as
                the failure reason  by default. If the remove reason is
                "evacuation", the failure reason of the disk will be
                recorded as "evacuated".
        """
        return self.request( "disk-remove", {
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'remove_reason': [ remove_reason, 'remove-reason', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_mung(self, disk_name, block_number, num_bits=None):
        """
        The command creates ECC errors for any valid sector.
        The corruption then makes it appear that the data
        contained in that sector cannot be recovered, and so
        the disk generates an unrecoverable error. Bad blocks
        are created by this utility on fully initialized systems.
        Care has to be taken in ensuring that sectors are not
        getting munged in the same stripe. Disk scrub will not
        be able to correct more than 1 block correction across
        the same stripe.Do not munge the disk sectors on any
        of the disks in the raid-group (except reconstructing
        disk) if raid-group is in degraded mode. If the raid
        group is in degraded mode, the filer will drop
        to "ok" prompt on hitting an unrecoverable error while
        reconstruction. This API is available on unpromoted builds
        only.
        FOR INTERNAL TEST ONLY.
        
        :param disk_name: Name of disk to be munged. Example: "0a.10".
        
        :param block_number: Block on the disk to be corrupted
                Approximately 20MB of disk space at the start of each
                disk is reserved for raid labels, boot image, and
                Core dump. This is equal to 41984 sectors. Hence,
                do not munge the sectors below 41984. Range: [0..2^64-1].
        
        :param num_bits: Number of consecutive bits to be munged. If not specified
                all 512 bytes(4096 bits) are munged. Range: [1..4096].
        """
        return self.request( "disk-mung", {
            'disk_name': [ disk_name, 'disk-name', [ basestring, 'None' ], False ],
            'num_bits': [ num_bits, 'num-bits', [ int, 'None' ], False ],
            'block_number': [ block_number, 'block-number', [ int, 'None' ], False ],
        }, {
        } )
    
    def disk_sanown_list_info(self, node=None, disk=None, ownership_type=None):
        """
        Get sanown disk information. This API is not supported as of Data ONTAP 8.2. Use storage-disk-get-iter instead.
        
        :param node: Node name for which info is requested
        
        :param disk: Get ownership status for given disk, if not supplied,
                get ownership for all disks or if onership-type is
                supplied, get ownership info for disks of specific type.
                '6a*' wildcarding is supported.
        
        :param ownership_type: Possible values are 'all' which will list all disks.
                'unowned' which will list all disks without owners.
                'owned' which will list all disks with owners.
                'visible' which will list all disks belonging to the
                local and partner filer.  Default is 'all'.  If specific disk is
                specified, ownership-type will be ignored.
        """
        return self.request( "disk-sanown-list-info", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'ownership_type': [ ownership_type, 'ownership-type', [ basestring, 'None' ], False ],
        }, {
            'disk-sanown-details': [ DiskSanownDetailInfo, True ],
        } )
    
    def disk_maint_list(self):
        """
        Get list of Maintenance Center tests.
        """
        return self.request( "disk-maint-list", {
        }, {
            'maint-test-list': [ MaintTestListInfo, True ],
        } )
    
    def disk_swap(self):
        """
        Prepare (quiet) bus for swap.
        Applies to SCSI disks only. It stalls all I/O on the
        filer to allow a disk to be physically added or
        removed from a disk shelf. Typically, this command
        would be used to allow removal of a failed disk, or
        of a file system or spare disk that was prepared for
        removal using the disk fail or disk remove command.
        Once a disk is physically added or removed from a disk
        shelf, system I/O will automatically continue.
        NOTE: It is important to issue the disk swap command
        only when you have a disk that you want to physically
        remove or add to a disk shelf, because all I/O will
        stall until a disk is added or removed from the shelf.
        This API is not supported in Data ONTAP 8.0 and later.
        """
        return self.request( "disk-swap", {
        }, {
        } )
    
    def disk_replace_start(self, disk, replacement_disk, allow_same_carrier=None, force=None, replace_reason=None):
        """
        Initiate replacing a file system disk with an appropriate
        spare disk.
        Uses Rapid RAID Recovery to copy data from the source file
        system disk to the destination spare disk.  Roles of disks
        are reversed at the end of that process.  The spare disk will
        replace the file system disk in the RAID group and the file
        system disk will become a spare.
        This interface returns as soon as possible while
        disk replace starts in the background.
        This process can be
        observed by polling disk-list-info for this disk and tracking
        values of elements copy-destination and copy-percent.
        Note: The operation performs limited error checking.
        Disk replace starts asynchronously in the background, and it
        can fail even if ZAPI reports success.
        
        :param disk: Name of the file system disk to replace.
        
        :param replacement_disk: Name of the spare disk to use as a replacement.
        
        :param allow_same_carrier: Using two disks from one carrier that houses multiple disks
                in one RAID group is not desirable.  If that happens,
                Data ONTAP initiates a series of disk copy operations to
                correct that situation.
                Sometimes, selection of available spare disks makes it
                impossible to avoid placing two disks from one carrier in one
                RAID group. Setting this option to true allows placing two
                disks from one carrier in one RAID group.
        
        :param force: Allow replacement-disk to come from the opposite spare pool.
                Also allow replacement-disk not matching rotational speed of
                majority of disks in the aggregate.
        
        :param replace_reason: The reason for replacing the disk.  Possible values are:
                <ul>
                <li> "evacuation"             - Disk is marked for evacuation.
                <li> "layout_optimization"    - Disk is marked for layout
                optimization.
                <li> "none"
                </ul>
                The default value is "none". If the replace reason is
                "none", the replaced disk will become a non-zeroed spare
                after disk copy.  If the replace reason is "evacuation",
                the replaced disk will be failed after disk copy, and the
                "evacuated" failure reason will be recorded for that disk.
                If the replace reason is "layout_optimization", the replaced
                disk will become zeroed spare.
        """
        return self.request( "disk-replace-start", {
            'allow_same_carrier': [ allow_same_carrier, 'allow-same-carrier', [ bool, 'None' ], False ],
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'replacement_disk': [ replacement_disk, 'replacement-disk', [ basestring, 'None' ], False ],
            'replace_reason': [ replace_reason, 'replace-reason', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_unswap(self):
        """
        Undo disk swap and resume service.
        This API is not supported in Data ONTAP 8.0 and later.
        """
        return self.request( "disk-unswap", {
        }, {
        } )
    
    def disk_unfail(self, disk, make_spare=None):
        """
        Unfail a disk in the broken pool, by clearing its FDR
        (Failed Disk Registry) entry and unfailing it at the
        Storage Layer, as necessary.  If the "make-spare" option
        is set to B_TRUE, the disk is returned to the spare pool.
        Otherwise, label assimilation will bring the disk back
        according to its on-disk labels, with one of four
        possible outcomes.
        1. Disk becomes a spare.  This is the common case.  The
        disk becomes a spare upon unfail, because its parent
        volume is complete and online.
        2. Disk is assimilated into former volume.  This is a
        recovery scenario.  The disk is brought back into an
        existing volume, which may result in this volume
        coming back online.
        3. Disk is assimilated into a new partial volume.  This
        may occur in the rare case that the disk's former
        volume was destroyed or moved.
        4. Disk returned to broken pool.  This is the case if
        a fatal error occurs in process of unfailing the disk.
        
        :param disk: Name of the disk, e.g. "v0.1".
                On Admin Vserver LIF, this will be disk path name
                with format of "<Node Name>:Disk Name".
                e.g. "Filer01:2a.32"
        
        :param make_spare: Specify 'true' to force the disk to become a spare upon
                unfail.  Default value is 'false'.
        """
        return self.request( "disk-unfail", {
            'make_spare': [ make_spare, 'make-spare', [ bool, 'None' ], False ],
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_maint_status(self, disks=None):
        """
        Get status of running Maintenance Center tests.
        
        :param disks: Get status of Maintenance Center tests for given disk(s), e.g. "v0.1".
                If not supplied, get status for all disks running Maintenance Center tests.
        """
        return self.request( "disk-maint-status", {
            'disks': [ disks, 'disks', [ basestring, 'maint-disk-name' ], True ],
        }, {
            'maint-test-status-list': [ MaintTestStatusInfo, True ],
        } )
    
    def disk_sanown_remove_ownership(self, owner=None, disk_list=None, all=None, force=None, owner_id=None):
        """
        Removes ownership information on a disk. Default usage is
        to remove ownership information for all disks owned by the
        local node, in maintenance mode.
        Signifies that a wrong input combination has been given.
        One of the specified disks could not be found.
        The filer being asked to remove ownership for a disk, does
        not own the disk.
        The filer being asked to remove ownership for a disk, does
        not own reservation for the drive.
        No disks were found for the specified systemid.
        The system is not in maintenance mode which is where
        this option is allowed.
        Internal error.
        Specified disk is a failed disk.
        
        :param owner: Remove ownership of all disks owned by owner. Either owner or
                owner-id is mandatory
        
        :param disk_list: List of disks to remove ownership information from.
                Example: 4a.18 5b.16 switch1:10.126L4
        
        :param all: If 'true' remove ownership information from all disks.
                (maintenance mode only)
        
        :param force: If 'true' override the RAID checks. Eg: Disk is part of
                aggregate. Otherwise defaults to false.
        
        :param owner_id: Remove ownership of all disks owned by this owner-id
                (maintenance mode only). Range [0..2^32-1]
        """
        return self.request( "disk-sanown-remove-ownership", {
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'disk_list': [ disk_list, 'disk-list', [ basestring, 'disk-name' ], True ],
            'all': [ all, 'all', [ bool, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'owner_id': [ owner_id, 'owner-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def disk_maint_start(self, disks, maint_tests=None, is_immediate=None, maint_test_iterations=None, maint_cycle_count=None):
        """
        Start Maintenance Center tests on one or more disks.
        
        :param disks: Start Maintenance Center tests for given disk(s), e.g. "v0.1".
        
        :param maint_tests: Maintenance Center tests to run. Default is to run every test.
        
        :param is_immediate: If is-immediate is true, the disk(s) will be immediately removed from the raid group
                for testing if it doesn't cause the volume to fail. If is-immediate is false, a disk copy
                will be performed to a spare disk before the disk is removed. The default is false.
                This option only applies for filesystem disks.
        
        :param maint_test_iterations: Number of iterations to run each test before running the next test. Default is one.
        
        :param maint_cycle_count: Number of cycles to run entire test sequence. Default is one.
        """
        return self.request( "disk-maint-start", {
            'maint_tests': [ maint_tests, 'maint-tests', [ basestring, 'maint-test-id' ], True ],
            'disks': [ disks, 'disks', [ basestring, 'maint-disk-name' ], True ],
            'is_immediate': [ is_immediate, 'is-immediate', [ bool, 'None' ], False ],
            'maint_test_iterations': [ maint_test_iterations, 'maint-test-iterations', [ int, 'maint-test-iteration' ], True ],
            'maint_cycle_count': [ maint_cycle_count, 'maint-cycle-count', [ int, 'None' ], False ],
        }, {
            'maint-start-status': [ MaintStartStatusInfo, True ],
        } )
    
    def disk_update_disk_fw(self, node_name, disk_list=None):
        """
        Start disk firmware download process to update firmware on disks.
        This operation is asynchronous, and therefore returns
        no errors that might occur during the download process.
        This operation will only update firmware on
        disks that do not have the latest firmware revision.
        The firmware revision on the disk can be monitored via
        the disk-list-info API.
        Internal error.
        One or more of the specified disks were invalid. This will
        cause the command to fail immediately. No action will be taken.
        An empty disk-list was specified.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system
                name the command will be executed on.
        
        :param disk_list: List of disks to be updated. If not specified, all disks are
                updated.
                Example: 4a.18 5b.16 switch1:10.126L4
        """
        return self.request( "disk-update-disk-fw", {
            'disk_list': [ disk_list, 'disk-list', [ basestring, 'disk-name' ], True ],
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def disk_filesys_usage_list_info(self, aggr_uuid=None, is_snapinfo=None, vol_dsid=None):
        """
        This API is deprecated starting from Data ONTAP 8.1.
        This API is used in Data ONTAP 8.0 and 8.0.x for
        obtaining space-related details for volumes, aggregates,
        and their snapshots.
        These space-related details can be obtained using
        the 'd-volume-list-info' and 'aggr-list-info' D-Blade APIs
        for volumes and aggregates, respectively.
        
        :param aggr_uuid: UUID of an aggregate. Either this must be specified as input or
                aggr-uuid, but not both at the same time. If both are given, then
                EINVALIDINPUTERROR is returned. Both can be skipped as well.
        
        :param is_snapinfo: Default value is always false. However, when this is specified as
                true, then either vol-dsid or the aggr-uuid must also be given as the
                input. If neither is given, then this flag is ignored. When set to true,
                it indicates this ZAPI to return the available disk space details of the
                snapshot information associated with the given aggregate or the
                volume.
        
        :param vol_dsid: DSID of a volume. Either this must be specified as input or
                aggr-uuid, but not both at the same time. If both are given, then
                EINVALIDINPUTERROR is returned. The volume UUID can also be
                specified as an alternative identifier.
        """
        return self.request( "disk-filesys-usage-list-info", {
            'aggr_uuid': [ aggr_uuid, 'aggr-uuid', [ basestring, 'None' ], False ],
            'is_snapinfo': [ is_snapinfo, 'is-snapinfo', [ bool, 'None' ], False ],
            'vol_dsid': [ vol_dsid, 'vol-dsid', [ basestring, 'None' ], False ],
        }, {
            'disk-filesys-usage-details': [ DiskFilesysUsageDetailInfo, True ],
        } )
    
    def disk_list_info(self, disk=None, ownership_type=None):
        """
        Get disk/array LUN status information from RAID.  By default, only
        disks/array LUNs owned by the storage system or its partner are eligible
        for inclusion in the returned list.  Unowned disks/array LUNs may
        be displayed by using the ownership-type option. To obtain information
        about disks/array LUNs connected to the storage system, but owned by a
        system other than the local system or its CFO partner use the
        disk-sanown-list-info api.
        
        :param disk: Get status for given disk, if not supplied, get status
                for all disks owned by the system and its CFO partner.
        
        :param ownership_type: This field is used to specify which disks/array LUNs are listed.
                Valid values are 'assigned', 'unassigned' and 'all'. If ownership-type
                is set to 'assigned' then only assigned disks/array LUNs are returned.
                If ownership-type is set to 'unassigned' then only unassigned disks/array
                LUNs are returned. If ownership-type is set to 'all' then both assigned
                and unassigned disks/array-LUNs are returned. The default is to return
                assigned disks/array LUNs. Default: 'assigned'.
        """
        return self.request( "disk-list-info", {
            'disk': [ disk, 'disk', [ basestring, 'None' ], False ],
            'ownership_type': [ ownership_type, 'ownership-type', [ basestring, 'None' ], False ],
        }, {
            'disk-details': [ DiskDetailInfo, True ],
        } )
