from netapp.volume.compression_info import CompressionInfo
from netapp.volume.clone_child_info import CloneChildInfo
from netapp.volume.autosize_info import AutosizeInfo
from netapp.volume.vm_align_info import VmAlignInfo
from netapp.aggr.plex_info import PlexInfo
from netapp.volume.sis_info import SisInfo
from netapp.volume.clone_parent_info import CloneParentInfo
from netapp.volume.snap_autodelete_info import SnapAutodeleteInfo
from netapp.volume.transition_info import TransitionInfo
from netapp.volume.volume_64bit_upgrade_info import Volume64BitUpgradeInfo
from netapp.netapp_object import NetAppObject

class VolumeInfo(NetAppObject):
    """
    Volume status information.
    """
    
    _is_wraparound = None
    @property
    def is_wraparound(self):
        """
        True if the date represented in expiry-date is a
        wrap around date. SnapLock wraps around the
        expiry date to indicate dates after 01/19/2038.
        It remaps 01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071.
        This field is not included if
        1. the volume has an infinite expiry date
        2. the volume is offline
        3. the volume has scan in progress
        4. the volume is regular volume (is-snaplock is "false")
        5. the volume has no expiry date. The volume is SnapLock
        volume (is-snaplock is "true") with no WORM files
        and no WORM snapshots.
        """
        return self._is_wraparound
    @is_wraparound.setter
    def is_wraparound(self, val):
        if val != None:
            self.validate('is_wraparound', val)
        self._is_wraparound = val
    
    _percentage_used = None
    @property
    def percentage_used(self):
        """
        Percentage of the volume size that is used.  If
        the volume is restricted or offline, a value of 0
        is returned.
        Range : [0..100].
        """
        return self._percentage_used
    @percentage_used.setter
    def percentage_used(self, val):
        if val != None:
            self.validate('percentage_used', val)
        self._percentage_used = val
    
    _inodefile_private_capacity = None
    @property
    def inodefile_private_capacity(self):
        """
        Number of inodes that can currently be stored
        on disk for system (not user-visible) files.
        This number will dynamically increase as more
        system files are created.  If the volume is
        restricted or offline, a value of zero is
        returned.
        Range : [0..2^64-1].
        """
        return self._inodefile_private_capacity
    @inodefile_private_capacity.setter
    def inodefile_private_capacity(self, val):
        if val != None:
            self.validate('inodefile_private_capacity', val)
        self._inodefile_private_capacity = val
    
    _filesystem_size = None
    @property
    def filesystem_size(self):
        """
        Filesystem size (in bytes) of the volume.  This is
        the total usable size of the volume, not including
        WAFL reserve.  This value is the same as Size except
        for certain SnapMirror destination volumes.  It is
        possible for destination volumes to have a different
        filesystem-size because the filesystem-size is sent
        across from the source volume.  If the volume is
        restricted or offline, a value of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._filesystem_size
    @filesystem_size.setter
    def filesystem_size(self, val):
        if val != None:
            self.validate('filesystem_size', val)
        self._filesystem_size = val
    
    _checksum_style = None
    @property
    def checksum_style(self):
        """
        The style of RAID checksum used (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        The possible values:
        <ul>
        <li> "advanced_zoned"    - advanced_zoned checksum (azcs),
        <li> "block"             - block,
        <li> "mixed"             - mixed,
        <li> "none"              - none,
        <li> "unknown"           - unknown
        <li> "wafl"              - wafl,
        <li> "zoned"             - zoned.
        </ul>
        """
        return self._checksum_style
    @checksum_style.setter
    def checksum_style(self, val):
        if val != None:
            self.validate('checksum_style', val)
        self._checksum_style = val
    
    _hybrid_cache_write_caching_ineligibility_reason = None
    @property
    def hybrid_cache_write_caching_ineligibility_reason(self):
        """
        informs why the volume cannot
        participate in write caching. This field
        is valid only if the volume can participate
        in read caching but not write caching.
        """
        return self._hybrid_cache_write_caching_ineligibility_reason
    @hybrid_cache_write_caching_ineligibility_reason.setter
    def hybrid_cache_write_caching_ineligibility_reason(self, val):
        if val != None:
            self.validate('hybrid_cache_write_caching_ineligibility_reason', val)
        self._hybrid_cache_write_caching_ineligibility_reason = val
    
    _provenance_uuid = None
    @property
    def provenance_uuid(self):
        """
        <b>Flexible</b> volumes only.
        Universal unique identifier (UUID) for the volume that
        is used to identify the source volume in a mirroring
        relationship. When the mirroring relationship is broken,
        a volume's Instance UUID and Provenance UUID are made
        identical. An unmirrored volume's Provenance UUID is the
        same as its Instance UUID.
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
        49e370d6-5b5a-11d9-9eb5-000100000529
        """
        return self._provenance_uuid
    @provenance_uuid.setter
    def provenance_uuid(self, val):
        if val != None:
            self.validate('provenance_uuid', val)
        self._provenance_uuid = val
    
    _plex_count = None
    @property
    def plex_count(self):
        """
        Number of plexes (for a traditional volume; for
        a flexible volume, the corresponding value of
        its containing aggregate).  This is also the
        size of the "plex" array that appears below.
        A plex is composed of one or more RAID groups
        that have been lashed together to serve as the
        unit for RAID mirroring.
        Range : [0..2^31-1]
        """
        return self._plex_count
    @plex_count.setter
    def plex_count(self, val):
        if val != None:
            self.validate('plex_count', val)
        self._plex_count = val
    
    _is_unrecoverable = None
    @property
    def is_unrecoverable(self):
        """
        Whether or not there is known inconsistency in the
        associated file system and it is not recoverable.
        This value is only present for flexible volumes.
        <p>
        By default, this field is FALSE.
        """
        return self._is_unrecoverable
    @is_unrecoverable.setter
    def is_unrecoverable(self, val):
        if val != None:
            self.validate('is_unrecoverable', val)
        self._is_unrecoverable = val
    
    _compression = None
    @property
    def compression(self):
        """
        Note that the use of this element is deprecated,
        refer to the 'dense-status' element for compression
        status instead.
        """
        return self._compression
    @compression.setter
    def compression(self, val):
        if val != None:
            self.validate('compression', val)
        self._compression = val
    
    _snaplock_volume_compliance_clock = None
    @property
    def snaplock_volume_compliance_clock(self):
        """
        If Compliance Clock is initialized then time in seconds
        in the standard UNIX format (since 01/01/1970 00:00:00)
        is displayed.
        This field will be present only for SnapLock volumes.
        Range:[0..2^64-1].
        """
        return self._snaplock_volume_compliance_clock
    @snaplock_volume_compliance_clock.setter
    def snaplock_volume_compliance_clock(self, val):
        if val != None:
            self.validate('snaplock_volume_compliance_clock', val)
        self._snaplock_volume_compliance_clock = val
    
    _is_invalid = None
    @property
    def is_invalid(self):
        """
        Whether or not this volume is invalid.
        Volumes typically become invalid as a
        result of an aborted 'vol copy' or SnapMirror(R)
        initial transfer.  In such a case a volume is in
        a half created state and cannot be recovered.
        <p>
        By default, this field is FALSE.
        """
        return self._is_invalid
    @is_invalid.setter
    def is_invalid(self, val):
        if val != None:
            self.validate('is_invalid', val)
        self._is_invalid = val
    
    _is_snaplock = None
    @property
    def is_snaplock(self):
        """
        Whether or not this is a SnapLock volume.
        """
        return self._is_snaplock
    @is_snaplock.setter
    def is_snaplock(self, val):
        if val != None:
            self.validate('is_snaplock', val)
        self._is_snaplock = val
    
    _formatted_expiry_date = None
    @property
    def formatted_expiry_date(self):
        """
        Expiry date of the SnapLock volume in a
        human-readable format
        <month> <day of month> <hour>:<min>:<sec> <year>
        is displayed.
        A value of "infinite" indicates that the volume has
        an infinite expiry date.
        A value of "scan_in_progress" indicates that expiry
        date is not displayed since worm scan on the volume is
        in progress.
        A value of "no_expiry_date" indicates that expiry
        date is not displayed since the SnapLock volume has
        no WORM files and WORM snapshots.
        This field is not included if the volume is offline or
        the volume is regular volume (is-snaplock is "false").
        """
        return self._formatted_expiry_date
    @formatted_expiry_date.setter
    def formatted_expiry_date(self, val):
        if val != None:
            self.validate('formatted_expiry_date', val)
        self._formatted_expiry_date = val
    
    _raid_status = None
    @property
    def raid_status(self):
        """
        The current RAID status (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        Possible values:
        copying, degraded, foreign, growing,
        initializing, invalid, ironing,
        mirror degraded, mirrored, needs check,
        noparity, normal, out-of-date, partial,
        raid0, raid4, raid_dp, reconstruct,
        resyncing, snapmirrored, verifying,
        unrecoverable.
        This field can contain a combination of the
        above status values in a comma separated list;
        for example: "reconstruct,growing".
        """
        return self._raid_status
    @raid_status.setter
    def raid_status(self, val):
        if val != None:
            self.validate('raid_status', val)
        self._raid_status = val
    
    _clone_children = None
    @property
    def clone_children(self):
        """
        <b>Flexible</b> volumes only.
        This field appears for a flexible volume if
        it is the parent of one or more clones.
        """
        return self._clone_children
    @clone_children.setter
    def clone_children(self, val):
        if val != None:
            self.validate('clone_children', val)
        self._clone_children = val
    
    _autosize = None
    @property
    def autosize(self):
        """
        Display autosize settings of the volume.
        Appears only under "verbose" mode.
        """
        return self._autosize
    @autosize.setter
    def autosize(self, val):
        if val != None:
            self.validate('autosize', val)
        self._autosize = val
    
    _size_available = None
    @property
    def size_available(self):
        """
        Number of bytes still available in the volume.  If
        the volume is restricted or offline, a value of 0
        is returned.
        Range : [0..2^64-1].
        """
        return self._size_available
    @size_available.setter
    def size_available(self, val):
        if val != None:
            self.validate('size_available', val)
        self._size_available = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Universal unique identifier (UUID) for the
        volume.
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _vm_align = None
    @property
    def vm_align(self):
        """
        Information related to the Virtual Machine alignment
        settings on the volume.
        """
        return self._vm_align
    @vm_align.setter
    def vm_align(self, val):
        if val != None:
            self.validate('vm_align', val)
        self._vm_align = val
    
    _expiry_date = None
    @property
    def expiry_date(self):
        """
        Expiry date of the SnapLock volume in seconds
        in the standard UNIX format
        (since 01/01/1970 00:00:00) is displayed.
        Range:[0..2^64-1].
        The flag is-wraparound indicates if this date is in
        the normal format or is wrapped around.
        This field is not included if
        1. the volume has an infinite expiry-date
        2. the volume is offline
        3. the volume has scan in progress
        4. the volume is regular volume
        5. the volume has no expiry date. The volume is SnapLock
        volume (is-snaplock is "true") with no WORM files
        and no WORM snapshots.
        """
        return self._expiry_date
    @expiry_date.setter
    def expiry_date(self, val):
        if val != None:
            self.validate('expiry_date', val)
        self._expiry_date = val
    
    _state = None
    @property
    def state(self):
        """
        State of the volume.
        Possible values:
        "offline", "online", "restricted" and "unknown"
        for both flexible and traditional volumes, and
        "creating", "failed", and "partial" specifically
        for traditional volumes.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _mirror_status = None
    @property
    def mirror_status(self):
        """
        The RAID mirror status (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        Possible values:
        CP count check in progress, failed,
        invalid, limbo, mirror degraded,
        mirror resynchronizing, mirrored,
        needs CP count check, uninitialized,
        &ltunknown mirror state&gt, and unmirrored.
        """
        return self._mirror_status
    @mirror_status.setter
    def mirror_status(self, val):
        if val != None:
            self.validate('mirror_status', val)
        self._mirror_status = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        Number of bytes used in the volume.  If the volume
        is restricted or offline, a value of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _files_total = None
    @property
    def files_total(self):
        """
        Total user-visible file (inode) count, i.e.,
        current maximum number of user-visible files
        (inodes) that this volume can currently hold.
        If the volume is restricted or offline, a value
        of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._files_total
    @files_total.setter
    def files_total(self, val):
        if val != None:
            self.validate('files_total', val)
        self._files_total = val
    
    _space_reserve_enabled = None
    @property
    def space_reserve_enabled(self):
        """
        <b>Flexible</b> volumes only.
        Whether or not the storage guarantee associated
        with the flexible volume is currently in effect.
        This field does not appear if the flexible volume
        is restricted or offline.
        """
        return self._space_reserve_enabled
    @space_reserve_enabled.setter
    def space_reserve_enabled(self, val):
        if val != None:
            self.validate('space_reserve_enabled', val)
        self._space_reserve_enabled = val
    
    _is_in_snapmirror_jumpahead = None
    @property
    def is_in_snapmirror_jumpahead(self):
        """
        True when the volume is in the process of SnapMirror
        jump ahead. Default value is false. This field is
        returned only for online volumes.
        """
        return self._is_in_snapmirror_jumpahead
    @is_in_snapmirror_jumpahead.setter
    def is_in_snapmirror_jumpahead(self, val):
        if val != None:
            self.validate('is_in_snapmirror_jumpahead', val)
        self._is_in_snapmirror_jumpahead = val
    
    _plexes = None
    @property
    def plexes(self):
        """
        List of plexes for this volume (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        """
        return self._plexes
    @plexes.setter
    def plexes(self, val):
        if val != None:
            self.validate('plexes', val)
        self._plexes = val
    
    _hybrid_cache_eligibility = None
    @property
    def hybrid_cache_eligibility(self):
        """
        hybrid cache eligibility. Valid values
        are "read","read-write" and "none". Volumes which
        report "read" can support only read caching.
        Volumes which report "read-write" support both
        read and write caching. "none" means no hybrid
        caching support.
        """
        return self._hybrid_cache_eligibility
    @hybrid_cache_eligibility.setter
    def hybrid_cache_eligibility(self, val):
        if val != None:
            self.validate('hybrid_cache_eligibility', val)
        self._hybrid_cache_eligibility = val
    
    _snapshot_blocks_reserved = None
    @property
    def snapshot_blocks_reserved(self):
        """
        The number of 1024 byte blocks that has been set aside as
        reserve for snapshot usage. This is same as "blocks-reserved"
        in snapshot-get-reserve API output.
        Range : [0..2^64-1].
        """
        return self._snapshot_blocks_reserved
    @snapshot_blocks_reserved.setter
    def snapshot_blocks_reserved(self, val):
        if val != None:
            self.validate('snapshot_blocks_reserved', val)
        self._snapshot_blocks_reserved = val
    
    _reserve_used = None
    @property
    def reserve_used(self):
        """
        Number of reserved bytes that is not available
        for new overwrites.
        The number includes both reserved bytes which
        have actually been used for overwrites as well
        as bytes which were never allocated in the first place.
        On a volume without free space, the "never allocated"
        component can become non-zero when
        reserve-required increases as holes are filled in.
        Because of this,
        the reserve-used value can
        exceed the number of snapshotted bytes.
        The reserve-used value can also exceed the value of
        reserve-required, as the filer maintains
        a small hidden reserve of last resort.
        If the volume is restricted or offline, a value
        of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._reserve_used
    @reserve_used.setter
    def reserve_used(self, val):
        if val != None:
            self.validate('reserve_used', val)
        self._reserve_used = val
    
    _sis = None
    @property
    def sis(self):
        """
        Display the Single Instance Storage (SIS) related
        status and statistics if the volume is a SIS volume.
        """
        return self._sis
    @sis.setter
    def sis(self, val):
        if val != None:
            self.validate('sis', val)
        self._sis = val
    
    _raid_size = None
    @property
    def raid_size(self):
        """
        The current RAID group size (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        Range : [0..2^31-1].
        """
        return self._raid_size
    @raid_size.setter
    def raid_size(self, val):
        if val != None:
            self.validate('raid_size', val)
        self._raid_size = val
    
    _remote_location = None
    @property
    def remote_location(self):
        """
        Displays the remote host and remote volume where
        the origin of the cache is located. Returned in format:
        <Remote-Host>:<Remote-Volume>
        Present only if flex volume is a FlexCache.
        Remote Host: Should be formatted as either the DNS
        hostname or as an IP address.
        Remote Volume: Should be formatted the same as a
        volume name.
        """
        return self._remote_location
    @remote_location.setter
    def remote_location(self, val):
        if val != None:
            self.validate('remote_location', val)
        self._remote_location = val
    
    _snaplock_type = None
    @property
    def snaplock_type(self):
        """
        The type of the snaplock volume.
        It is present for snaplock volumes only,
        i.e. volumes for which is-snaplock is "true".
        Possible values -
        "compliance" or "enterprise"
        """
        return self._snaplock_type
    @snaplock_type.setter
    def snaplock_type(self, val):
        if val != None:
            self.validate('snaplock_type', val)
        self._snaplock_type = val
    
    _clone_parent = None
    @property
    def clone_parent(self):
        """
        <b>Flexible</b> volumes only.
        This field appears for a flexible volume if
        it is a clone of another flexible volume,
        describing the clone's parentage.
        """
        return self._clone_parent
    @clone_parent.setter
    def clone_parent(self, val):
        if val != None:
            self.validate('clone_parent', val)
        self._clone_parent = val
    
    _files_private_used = None
    @property
    def files_private_used(self):
        """
        Number of system (not user-visible) files (inodes)
        used.  If the volume is restricted or offline, a
        a value of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._files_private_used
    @files_private_used.setter
    def files_private_used(self, val):
        if val != None:
            self.validate('files_private_used', val)
        self._files_private_used = val
    
    _containing_aggregate = None
    @property
    def containing_aggregate(self):
        """
        <b>Flexible</b> volumes only.
        The name of the aggregate in which the given
        flexible volume resides.
        """
        return self._containing_aggregate
    @containing_aggregate.setter
    def containing_aggregate(self, val):
        if val != None:
            self.validate('containing_aggregate', val)
        self._containing_aggregate = val
    
    _space_reserve = None
    @property
    def space_reserve(self):
        """
        <b>Flexible</b> volumes only.
        The storage guarantee associated with the
        flexible volume.  Possible values: none, file,
        volume.  This field does not appear if the flexible
        volume is restricted or offline.
        """
        return self._space_reserve
    @space_reserve.setter
    def space_reserve(self, val):
        if val != None:
            self.validate('space_reserve', val)
        self._space_reserve = val
    
    _instance_uuid = None
    @property
    def instance_uuid(self):
        """
        <b>Flexible</b> volumes only.
        Universal unique identifier (UUID) for the volume that
        remains unchanged when the volume is moved to a new
        location. This differs from the volume's regular UUID
        which changes after a move. The instance UUID can be
        used to identify a volume even after it is moved.
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
        49e370d6-5b5a-11d9-9eb5-000100000529
        """
        return self._instance_uuid
    @instance_uuid.setter
    def instance_uuid(self, val):
        if val != None:
            self.validate('instance_uuid', val)
        self._instance_uuid = val
    
    _is_inconsistent = None
    @property
    def is_inconsistent(self):
        """
        Whether or not there is known inconsistency
        in the associated file system.
        """
        return self._is_inconsistent
    @is_inconsistent.setter
    def is_inconsistent(self, val):
        if val != None:
            self.validate('is_inconsistent', val)
        self._is_inconsistent = val
    
    _snapshot_percent_reserved = None
    @property
    def snapshot_percent_reserved(self):
        """
        The percentage of disk space that has been set aside as reserve
        for snapshot usage. This is same as "percent-reserved" in
        snapshot-get-reserve API output.
        Range : [0..100].
        """
        return self._snapshot_percent_reserved
    @snapshot_percent_reserved.setter
    def snapshot_percent_reserved(self, val):
        if val != None:
            self.validate('snapshot_percent_reserved', val)
        self._snapshot_percent_reserved = val
    
    _quota_init = None
    @property
    def quota_init(self):
        """
        Quota state and percent initialized.
        100% means that quotas are on, 0% means quotas
        are off, and anywhere inbetween means that
        quotas are initializing.
        Range : [0..100].
        """
        return self._quota_init
    @quota_init.setter
    def quota_init(self, val):
        if val != None:
            self.validate('quota_init', val)
        self._quota_init = val
    
    _is_checksum_enabled = None
    @property
    def is_checksum_enabled(self):
        """
        Whether RAID checksums are enabled (for a
        traditional volume; for a flexible volume, the
        corresponding value of its containing aggregate).
        """
        return self._is_checksum_enabled
    @is_checksum_enabled.setter
    def is_checksum_enabled(self, val):
        if val != None:
            self.validate('is_checksum_enabled', val)
        self._is_checksum_enabled = val
    
    _owning_vfiler = None
    @property
    def owning_vfiler(self):
        """
        Name of the vfiler which owns this volume. This value
        will be returned only if the request is coming to
        vfiler0 and MultiStore is licensed.
        """
        return self._owning_vfiler
    @owning_vfiler.setter
    def owning_vfiler(self, val):
        if val != None:
            self.validate('owning_vfiler', val)
        self._owning_vfiler = val
    
    _block_type = None
    @property
    def block_type(self):
        """
        The indirect block format of the volume.
        Possible values: 32_bit, 64_bit.
        """
        return self._block_type
    @block_type.setter
    def block_type(self, val):
        if val != None:
            self.validate('block_type', val)
        self._block_type = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        Number of user-visible files (inodes) used.
        If the volume is restricted or offline, a value
        0 returned.
        Range : [0..2^64-1].
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    _inodefile_public_capacity = None
    @property
    def inodefile_public_capacity(self):
        """
        Number of inodes that can currently be stored
        on disk for user-visible files.  This number
        will dynamically increase as more user-visible
        files are created.  If the volume is restricted
        or offline, a value of zero is returned.
        Range : [0..2^64-1].
        """
        return self._inodefile_public_capacity
    @inodefile_public_capacity.setter
    def inodefile_public_capacity(self, val):
        if val != None:
            self.validate('inodefile_public_capacity', val)
        self._inodefile_public_capacity = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the volume.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _snap_autodelete = None
    @property
    def snap_autodelete(self):
        """
        Display the snapshot autodelete policy related status
        of the volume. Appears only under "verbose" mode.
        """
        return self._snap_autodelete
    @snap_autodelete.setter
    def snap_autodelete(self, val):
        if val != None:
            self.validate('snap_autodelete', val)
        self._snap_autodelete = val
    
    _type = None
    @property
    def type(self):
        """
        The type of volume.
        Possible values: "flex" for flexible volumes, and
        "trad" for traditional volumes.
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _transition = None
    @property
    def transition(self):
        """
        Information relating to any transition jobs
        running or previously run on this volume.
        """
        return self._transition
    @transition.setter
    def transition(self, val):
        if val != None:
            self.validate('transition', val)
        self._transition = val
    
    _reserve_required = None
    @property
    def reserve_required(self):
        """
        The number of reserved bytes that are required
        to ensure that the reserved space is sufficient
        to allow all space reserved files and LUNs to
        be overwritten when the volume is full.
        If the volume is restricted or offline, a value
        of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._reserve_required
    @reserve_required.setter
    def reserve_required(self, val):
        if val != None:
            self.validate('reserve_required', val)
        self._reserve_required = val
    
    _formatted_snaplock_volume_compliance_clock = None
    @property
    def formatted_snaplock_volume_compliance_clock(self):
        """
        If Compliance Clock is initialized then
        human readable time
        <day> <month> <day of month> <hour>:<min>:<sec> <year>
        is displayed.
        This field will be present only for SnapLock volumes.
        """
        return self._formatted_snaplock_volume_compliance_clock
    @formatted_snaplock_volume_compliance_clock.setter
    def formatted_snaplock_volume_compliance_clock(self, val):
        if val != None:
            self.validate('formatted_snaplock_volume_compliance_clock', val)
        self._formatted_snaplock_volume_compliance_clock = val
    
    _size_total = None
    @property
    def size_total(self):
        """
        Total usable size (in bytes) of the volume, not
        including WAFL reserve or volume snapshot
        reserve.  If the volume is restricted or offline,
        a value of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._size_total
    @size_total.setter
    def size_total(self, val):
        if val != None:
            self.validate('size_total', val)
        self._size_total = val
    
    _volume_64bit_upgrade = None
    @property
    def volume_64bit_upgrade(self):
        """
        Information related to 64-bit upgrade. After 64-bit
        upgrade completes, this information is no longer
        available.
        """
        return self._volume_64bit_upgrade
    @volume_64bit_upgrade.setter
    def volume_64bit_upgrade(self, val):
        if val != None:
            self.validate('volume_64bit_upgrade', val)
        self._volume_64bit_upgrade = val
    
    _reserve_used_actual = None
    @property
    def reserve_used_actual(self):
        """
        Number of reserved bytes that have been used.
        This value is computed as the smaller of: (1) snapshotted
        bytes not in the active filesystem, and (2) reserve-used.
        This formula comes
        from the observation that you
        cannot have used more overwrite
        reserved than have actually overwritten data.
        This value can exceed the value of
        reserve-required, as the filer maintains
        a small hidden reserve of last resort.
        If the volume is restricted or offline, a value
        of 0 is returned.
        Range : [0..2^64-1].
        """
        return self._reserve_used_actual
    @reserve_used_actual.setter
    def reserve_used_actual(self, val):
        if val != None:
            self.validate('reserve_used_actual', val)
        self._reserve_used_actual = val
    
    _disk_count = None
    @property
    def disk_count(self):
        """
        Total number of associated disks (for a traditional
        volume; for a flexible volume, the corresponding
        value of its containing aggregate).
        Range : [0..2^31-1]
        """
        return self._disk_count
    @disk_count.setter
    def disk_count(self, val):
        if val != None:
            self.validate('disk_count', val)
        self._disk_count = val
    
    _reserve = None
    @property
    def reserve(self):
        """
        Number of bytes reserved for overwriting snapshotted
        data in an otherwise full volume.  This space is
        usable only by space-reserved LUNs and files,
        and then only when the volume is full.  It is
        equal to reserve-required if the value of the
        fractional_reserve option is set to the default
        value of 100%, but otherwise may be less than
        reserve-required.
        If the volume is restricted or offline, a value
        of 0 is returned.
        Range : [0..2^64-1]
        """
        return self._reserve
    @reserve.setter
    def reserve(self, val):
        if val != None:
            self.validate('reserve', val)
        self._reserve = val
    
    @staticmethod
    def get_api_name():
          return "volume-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-wraparound',
            'percentage-used',
            'inodefile-private-capacity',
            'filesystem-size',
            'checksum-style',
            'hybrid-cache-write-caching-ineligibility-reason',
            'provenance-uuid',
            'plex-count',
            'is-unrecoverable',
            'compression',
            'snaplock-volume-compliance-clock',
            'is-invalid',
            'is-snaplock',
            'formatted-expiry-date',
            'raid-status',
            'clone-children',
            'autosize',
            'size-available',
            'uuid',
            'vm-align',
            'expiry-date',
            'state',
            'mirror-status',
            'size-used',
            'files-total',
            'space-reserve-enabled',
            'is-in-snapmirror-jumpahead',
            'plexes',
            'hybrid-cache-eligibility',
            'snapshot-blocks-reserved',
            'reserve-used',
            'sis',
            'raid-size',
            'remote-location',
            'snaplock-type',
            'clone-parent',
            'files-private-used',
            'containing-aggregate',
            'space-reserve',
            'instance-uuid',
            'is-inconsistent',
            'snapshot-percent-reserved',
            'quota-init',
            'is-checksum-enabled',
            'owning-vfiler',
            'block-type',
            'files-used',
            'inodefile-public-capacity',
            'name',
            'snap-autodelete',
            'type',
            'transition',
            'reserve-required',
            'formatted-snaplock-volume-compliance-clock',
            'size-total',
            'volume-64bit-upgrade',
            'reserve-used-actual',
            'disk-count',
            'reserve',
        ]
    
    def describe_properties(self):
        return {
            'is_wraparound': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'percentage_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodefile_private_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'filesystem_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'hybrid_cache_write_caching_ineligibility_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'provenance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'plex_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_unrecoverable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'compression': { 'class': CompressionInfo, 'is_list': False, 'required': 'required' },
            'snaplock_volume_compliance_clock': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_invalid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_snaplock': { 'class': bool, 'is_list': False, 'required': 'required' },
            'formatted_expiry_date': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'raid_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'clone_children': { 'class': CloneChildInfo, 'is_list': True, 'required': 'optional' },
            'autosize': { 'class': AutosizeInfo, 'is_list': False, 'required': 'optional' },
            'size_available': { 'class': int, 'is_list': False, 'required': 'required' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vm_align': { 'class': VmAlignInfo, 'is_list': False, 'required': 'optional' },
            'expiry_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mirror_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'files_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'space_reserve_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_in_snapmirror_jumpahead': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'plexes': { 'class': PlexInfo, 'is_list': True, 'required': 'required' },
            'hybrid_cache_eligibility': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snapshot_blocks_reserved': { 'class': int, 'is_list': False, 'required': 'required' },
            'reserve_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'sis': { 'class': SisInfo, 'is_list': False, 'required': 'optional' },
            'raid_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'remote_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snaplock_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'clone_parent': { 'class': CloneParentInfo, 'is_list': True, 'required': 'optional' },
            'files_private_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'containing_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'space_reserve': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'instance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_inconsistent': { 'class': bool, 'is_list': False, 'required': 'required' },
            'snapshot_percent_reserved': { 'class': int, 'is_list': False, 'required': 'required' },
            'quota_init': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_checksum_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'owning_vfiler': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'block_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodefile_public_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snap_autodelete': { 'class': SnapAutodeleteInfo, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'transition': { 'class': TransitionInfo, 'is_list': False, 'required': 'optional' },
            'reserve_required': { 'class': int, 'is_list': False, 'required': 'required' },
            'formatted_snaplock_volume_compliance_clock': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_64bit_upgrade': { 'class': Volume64BitUpgradeInfo, 'is_list': False, 'required': 'optional' },
            'reserve_used_actual': { 'class': int, 'is_list': False, 'required': 'required' },
            'disk_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'reserve': { 'class': int, 'is_list': False, 'required': 'required' },
        }
