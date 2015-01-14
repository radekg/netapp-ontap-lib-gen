from netapp.aggr.aggr_wafliron_info import AggrWaflironInfo
from netapp.aggr.mirror_count_info import MirrorCountInfo
from netapp.aggr.plex_info import PlexInfo
from netapp.aggr.contained_volume_info import ContainedVolumeInfo
from netapp.aggr.aggregate_space_info import AggregateSpaceInfo
from netapp.aggr.aggr_64bit_upgrade_info import Aggr64BitUpgradeInfo
from netapp.netapp_object import NetAppObject

class AggrInfo(NetAppObject):
    """
    Aggregate status information.
    """
    
    _wafliron = None
    @property
    def wafliron(self):
        """
        Information related to wafliron, the online WAFL
        file system check/repair tool. This information
        is returned only when wafliron specific
        information is available.
        """
        return self._wafliron
    @wafliron.setter
    def wafliron(self, val):
        if val != None:
            self.validate('wafliron', val)
        self._wafliron = val
    
    _ha_policy = None
    @property
    def ha_policy(self):
        """
        Aggregate's HA policy.
        Possible return values:
        "cfo", "sfo", "none"
        """
        return self._ha_policy
    @ha_policy.setter
    def ha_policy(self, val):
        if val != None:
            self.validate('ha_policy', val)
        self._ha_policy = val
    
    _home_name = None
    @property
    def home_name(self):
        """
        Name of the node to which this aggregate's
        disks have been administratively assigned.
        """
        return self._home_name
    @home_name.setter
    def home_name(self, val):
        if val != None:
            self.validate('home_name', val)
        self._home_name = val
    
    _volume_count_quiesced = None
    @property
    def volume_count_quiesced(self):
        """
        When present, this field indicates the number of
        quiesced online volumes.
        <p>
        Range: [0..2^31-1]
        """
        return self._volume_count_quiesced
    @volume_count_quiesced.setter
    def volume_count_quiesced(self, val):
        if val != None:
            self.validate('volume_count_quiesced', val)
        self._volume_count_quiesced = val
    
    _inodefile_private_capacity = None
    @property
    def inodefile_private_capacity(self):
        """
        Number of inodes that can currently be stored
        on disk for system (not user-visible) files.
        This number will dynamically increase as more
        system files are created.
        Range: [0..2^64-1].
        """
        return self._inodefile_private_capacity
    @inodefile_private_capacity.setter
    def inodefile_private_capacity(self, val):
        if val != None:
            self.validate('inodefile_private_capacity', val)
        self._inodefile_private_capacity = val
    
    _has_partner_root = None
    @property
    def has_partner_root(self):
        """
        Whether the aggregate (or tradvol) contains the
        partner's root volume.
        """
        return self._has_partner_root
    @has_partner_root.setter
    def has_partner_root(self, val):
        if val != None:
            self.validate('has_partner_root', val)
        self._has_partner_root = val
    
    _checksum_style = None
    @property
    def checksum_style(self):
        """
        Checksum style.  The possible values:
        <ul>
        <li> "advanced_zoned"      - advanced_zoned checksum (azcs),
        <li> "block"               - block,
        <li> "mixed"               - mixed,
        <li> "none"                - none,
        <li> "unknown"             - unknown
        <li> "wafl"                - wafl,
        <li> "zoned"               - zoned.
        </ul>
        """
        return self._checksum_style
    @checksum_style.setter
    def checksum_style(self, val):
        if val != None:
            self.validate('checksum_style', val)
        self._checksum_style = val
    
    _raid_lost_write_state = None
    @property
    def raid_lost_write_state(self):
        """
        State of the RAID Lost Write feature for an aggregate. The possible values are:
        <ul>
        <li> "aborted" - The RAID Lost Write scrub is no longer running and was aborted on all RAID groups
        in this aggregate, possibly due to an error. </li>
        <li> "illegal" - The aggregate contains RAID groups with RAID Lost Write disabled and other RAID
        groups with RAID Lost Write enabled. This is an invalid state. </li>
        <li> "inoperative" - The RAID Lost Write scrub is allowed on the aggregate, but it cannot start
        because the system-wide RAID Lost Write option "raid.lost_write.enable" is set to
        "off".</li>
        <li> "off" - RAID Lost Write protection and scrub are disabled on this aggregate. </li>
        <li> "on" - The aggregate is RAID Lost Write protected and that the RAID Lost Write scrub completed
        successfully on all RAID groups in this aggregate. </li>
        <li> "partial" - The RAID Lost Write scrub completed successfully on some of the RAID groups in this
        aggregate, but was aborted on at least one of the RAID groups. </li>
        <li> "unknown" - The RAID Lost Write scrub status could not be determined. </li>
        <li> "upgrade_partial" - The RAID Lost Write scrub is still in progress on some of the RAID groups
        in this aggregate and was aborted on at least one of the RAID groups. </li>
        <li> "upgrading" - The RAID Lost Write scrub is still not completed or not yet started on at least
        one of the RAID groups in this aggregate. </li>
        </ul>
        """
        return self._raid_lost_write_state
    @raid_lost_write_state.setter
    def raid_lost_write_state(self, val):
        if val != None:
            self.validate('raid_lost_write_state', val)
        self._raid_lost_write_state = val
    
    _volume_count_collective = None
    @property
    def volume_count_collective(self):
        """
        Number of striped volume constituents in the
        aggregate which also represent a collective
        striped volume.
        This field is for internal use only.
        Range: [0..2^31-1].
        """
        return self._volume_count_collective
    @volume_count_collective.setter
    def volume_count_collective(self, val):
        if val != None:
            self.validate('volume_count_collective', val)
        self._volume_count_collective = val
    
    _checksum_status = None
    @property
    def checksum_status(self):
        """
        Checksum status. Possible values:
        "active", "off", "reverting", "none", "unknown",
        "initializing",  "reinitializing", "reinitialized",
        "upgrading_phase1", "upgrading_phase2"
        """
        return self._checksum_status
    @checksum_status.setter
    def checksum_status(self, val):
        if val != None:
            self.validate('checksum_status', val)
        self._checksum_status = val
    
    _volume_count_mirrors = None
    @property
    def volume_count_mirrors(self):
        """
        Various counts information for mirror volumes in the
        aggregate. This information is returned only when the
        aggregate contains mirror volumes.
        """
        return self._volume_count_mirrors
    @volume_count_mirrors.setter
    def volume_count_mirrors(self, val):
        if val != None:
            self.validate('volume_count_mirrors', val)
        self._volume_count_mirrors = val
    
    _volume_count = None
    @property
    def volume_count(self):
        """
        Number of volumes in the aggregate.
        Range: [0..2^31-1].
        """
        return self._volume_count
    @volume_count.setter
    def volume_count(self, val):
        if val != None:
            self.validate('volume_count', val)
        self._volume_count = val
    
    _size_percentage_used = None
    @property
    def size_percentage_used(self):
        """
        Percentage of aggregate used.  This value is
        not returned if the aggregate is unusable
        (i.e., it's offline).
        Range : [0..100].
        """
        return self._size_percentage_used
    @size_percentage_used.setter
    def size_percentage_used(self, val):
        if val != None:
            self.validate('size_percentage_used', val)
        self._size_percentage_used = val
    
    _is_snaplock = None
    @property
    def is_snaplock(self):
        """
        Whether or not it's a SnapLock aggregate.
        """
        return self._is_snaplock
    @is_snaplock.setter
    def is_snaplock(self, val):
        if val != None:
            self.validate('is_snaplock', val)
        self._is_snaplock = val
    
    _is_hybrid_enabled = None
    @property
    def is_hybrid_enabled(self):
        """
        If true, aggregate is eligible to contain both
        SSD and non-SSD RAID groups.
        """
        return self._is_hybrid_enabled
    @is_hybrid_enabled.setter
    def is_hybrid_enabled(self, val):
        if val != None:
            self.validate('is_hybrid_enabled', val)
        self._is_hybrid_enabled = val
    
    _owner_name = None
    @property
    def owner_name(self):
        """
        Name of node which currently owns this
        aggregate's disks.
        Normally, home-name matches owner-name.  But these
        may be changed by SFO takeover to match the
        takeover node, and restored by SFO giveback
        to match home-name. CFO takeover and giveback
        do not affect owner-name.
        """
        return self._owner_name
    @owner_name.setter
    def owner_name(self, val):
        if val != None:
            self.validate('owner_name', val)
        self._owner_name = val
    
    _cache_raid_group_size = None
    @property
    def cache_raid_group_size(self):
        """
        Current maximum cache RAID group size of hybrid aggregate.  Range : [1..28].
        RAID group size is the maximum number of disks that can be added
        to a RAID group.
        This information will only be returned for hybrid aggregate i.e. for the aggregates
        whose "is-hybrid" field is set to true.
        """
        return self._cache_raid_group_size
    @cache_raid_group_size.setter
    def cache_raid_group_size(self, val):
        if val != None:
            self.validate('cache_raid_group_size', val)
        self._cache_raid_group_size = val
    
    _size_available = None
    @property
    def size_available(self):
        """
        Available bytes in the aggregate.
        Range: [0..2^64-1].
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
        Aggregate's Universal Unique IDentifier.
        UUIDs are 16-byte quantities that are
        typically displayed as having five
        hexadecimal fields separated by hyphens.
        For example:
        d2da3566-da53-11d7-a841-000100000529
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _plex_count = None
    @property
    def plex_count(self):
        """
        Number of plexes in the aggregate.  This
        value tells us the size of the returned
        "plex" array.  Range: [0..2^31-1].
        """
        return self._plex_count
    @plex_count.setter
    def plex_count(self, val):
        if val != None:
            self.validate('plex_count', val)
        self._plex_count = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        Aggregate bytes used.  This value is not
        returned if the aggregate is unusable (i.e.,
        it's offline).
        Range: [0..2^64-1].
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _mirror_status = None
    @property
    def mirror_status(self):
        """
        Aggregate's mirror status.  Possible values:
        invalid, uninitialized, needs CP count check,
        CP count check in progress, unmirrored, mirrored,
        mirror degraded, mirror resynchronizing, failed,
        limbo, and <unknown mirror state>.
        """
        return self._mirror_status
    @mirror_status.setter
    def mirror_status(self, val):
        if val != None:
            self.validate('mirror_status', val)
        self._mirror_status = val
    
    _state = None
    @property
    def state(self):
        """
        Aggregate state.  The possible values:
        "creating", "destroying", "failed", "frozen", "inconsistent",
        "iron_restricted", "mounting", "offline", "online", "partial",
        "quiesced", "quiescing", "restricted", "reverted", "unknown",
        "unmounted", "unmounting".
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _files_total = None
    @property
    def files_total(self):
        """
        Total count of user-visible files.
        Range: [0..2^64-1].
        """
        return self._files_total
    @files_total.setter
    def files_total(self, val):
        if val != None:
            self.validate('files_total', val)
        self._files_total = val
    
    _fsid = None
    @property
    def fsid(self):
        """
        Aggregate's File System IDentifier.
        Range: [0..2^32-1]
        """
        return self._fsid
    @fsid.setter
    def fsid(self, val):
        if val != None:
            self.validate('fsid', val)
        self._fsid = val
    
    _striping = None
    @property
    def striping(self):
        """
        Specifies the striping information about the
        aggregate. Possible values are "striped",
        "not_striped" and "unknown"
        In unclustered environments, all aggregates
        are not striped. In clustered environments,
        aggregates can be either striped or not
        striped. When striping information is not
        known, "unknown" will be returned.
        """
        return self._striping
    @striping.setter
    def striping(self, val):
        if val != None:
            self.validate('striping', val)
        self._striping = val
    
    _plexes = None
    @property
    def plexes(self):
        """
        List of plexes in the aggregate.
        """
        return self._plexes
    @plexes.setter
    def plexes(self, val):
        if val != None:
            self.validate('plexes', val)
        self._plexes = val
    
    _volume_count_striped = None
    @property
    def volume_count_striped(self):
        """
        Number of striped volume constituents in the
        aggregate.  These volumes are also reported
        in the full volume-count value.
        This field is for internal use only.
        Range: [0..2^31-1].
        """
        return self._volume_count_striped
    @volume_count_striped.setter
    def volume_count_striped(self, val):
        if val != None:
            self.validate('volume_count_striped', val)
        self._volume_count_striped = val
    
    _type = None
    @property
    def type(self):
        """
        The type of aggregate.
        Possible values: aggr, trad
        "aggr" (for aggregates that can contain
        flexible volumes)
        "trad" (for aggregates embedded in traditional
        volumes)
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _raid_status = None
    @property
    def raid_status(self):
        """
        RAID status.  Possible values: normal,
        verifying, SnapMirrored, copying, ironing,
        mirrored, resyncing, mirror degraded, invalid,
        needs check, initializing, growing, partial,
        noparity, degraded, reconstruct, out-of-date,
        foreign, raid4, raid0, raid_dp, mixed_raid_type.
        These values may appear by themselves or in combination
        separated by commas (e.g., "reconstruct,growing").
        An aggregate could be of only one of the following
        RAID types:
        <ul>
        <li> "raid0" - All the raid groups in the aggregate
        are of type raid0,</li>
        <li> "raid4" - All the raid groups in the aggregate
        are of	type raid4,</li>
        <li> "raid_dp" - All the raid groups in the aggregate
        are of type raid_dp,</li>
        <li> "mixed_raid_type" - This aggregate contains RAID
        groups of different RAID
        types (raid0, raid4, raid_dp).</li>
        </ul>
        """
        return self._raid_status
    @raid_status.setter
    def raid_status(self, val):
        if val != None:
            self.validate('raid_status', val)
        self._raid_status = val
    
    _raid_size = None
    @property
    def raid_size(self):
        """
        Current RAID group size.  Range : [0..2^31-1].
        """
        return self._raid_size
    @raid_size.setter
    def raid_size(self, val):
        if val != None:
            self.validate('raid_size', val)
        self._raid_size = val
    
    _volumes = None
    @property
    def volumes(self):
        """
        List of volumes contained the aggregate.
        """
        return self._volumes
    @volumes.setter
    def volumes(self, val):
        if val != None:
            self.validate('volumes', val)
        self._volumes = val
    
    _max_write_alloc_blocks = None
    @property
    def max_write_alloc_blocks(self):
        """
        The maximum number of blocks used for write allocation.
        Some sequential read workloads may benefit from increasing
        this value. Default value is 0 which uses the
        controller-wide default value of 64. The default is optimal
        for most users. The controller-wide default can be adjusted
        with the bootarg "wafl-max-write-alloc-blocks"
        """
        return self._max_write_alloc_blocks
    @max_write_alloc_blocks.setter
    def max_write_alloc_blocks(self, val):
        if val != None:
            self.validate('max_write_alloc_blocks', val)
        self._max_write_alloc_blocks = val
    
    _snaplock_type = None
    @property
    def snaplock_type(self):
        """
        The type of the snaplock aggregate.
        It is present for snaplock aggrs only,
        i.e. aggrs for which is-snaplock is "true".
        Possible values -
        "compliance" or "enterprise"
        """
        return self._snaplock_type
    @snaplock_type.setter
    def snaplock_type(self, val):
        if val != None:
            self.validate('snaplock_type', val)
        self._snaplock_type = val
    
    _files_private_used = None
    @property
    def files_private_used(self):
        """
        Number of system (not user-visible) files used.
        Range: [0..2^64-1].
        """
        return self._files_private_used
    @files_private_used.setter
    def files_private_used(self, val):
        if val != None:
            self.validate('files_private_used', val)
        self._files_private_used = val
    
    _dr_home_id = None
    @property
    def dr_home_id(self):
        """
        NVRAM ID of the DR (disaster recovery) node to
        which this aggregate's disks have been
        administratively assigned. This information
        derived from sanown information of aggregate's
        disk. See 'disk-sanown-detail-info'
        """
        return self._dr_home_id
    @dr_home_id.setter
    def dr_home_id(self, val):
        if val != None:
            self.validate('dr_home_id', val)
        self._dr_home_id = val
    
    _has_local_root = None
    @property
    def has_local_root(self):
        """
        Whether the aggregate (or tradvol) contains the
        local root volume.
        """
        return self._has_local_root
    @has_local_root.setter
    def has_local_root(self, val):
        if val != None:
            self.validate('has_local_root', val)
        self._has_local_root = val
    
    _free_space_realloc = None
    @property
    def free_space_realloc(self):
        """
        Indicate if free space reallocation (continuous
        segment cleaning) is enabled
        on a specific aggregate.
        Possible values: on, off, no_redirect
        "on"    (Free space reallocation enabled
        with automatically starting the
        redirect scanner)
        "off"   (Free space reallocation disabled)
        "no_redirect" (Free space reallocation enabled
        without running the redirect scanner)
        The default value for this option is "off"
        """
        return self._free_space_realloc
    @free_space_realloc.setter
    def free_space_realloc(self, val):
        if val != None:
            self.validate('free_space_realloc', val)
        self._free_space_realloc = val
    
    _is_inconsistent = None
    @property
    def is_inconsistent(self):
        """
        Whether or not the aggregate is inconsistent.
        """
        return self._is_inconsistent
    @is_inconsistent.setter
    def is_inconsistent(self, val):
        if val != None:
            self.validate('is_inconsistent', val)
        self._is_inconsistent = val
    
    _dr_home_name = None
    @property
    def dr_home_name(self):
        """
        Name of the DR node to which this aggregate's
        disks have been administratively assigned.
        """
        return self._dr_home_name
    @dr_home_name.setter
    def dr_home_name(self, val):
        if val != None:
            self.validate('dr_home_name', val)
        self._dr_home_name = val
    
    _is_checksum_enabled = None
    @property
    def is_checksum_enabled(self):
        """
        Is checksumming enabled for the aggregate?
        """
        return self._is_checksum_enabled
    @is_checksum_enabled.setter
    def is_checksum_enabled(self, val):
        if val != None:
            self.validate('is_checksum_enabled', val)
        self._is_checksum_enabled = val
    
    _mount_state = None
    @property
    def mount_state(self):
        """
        [not settable, always]
        This field shows the volume's mount state. Possible
        values: "unmounted", "online", "frozen", "destroying", "creating",
        "mounting", "unmounting", "inconsistent", "reverted", "quiescing",
        "quiesced", "iron_restricted"
        """
        return self._mount_state
    @mount_state.setter
    def mount_state(self, val):
        if val != None:
            self.validate('mount_state', val)
        self._mount_state = val
    
    _block_type = None
    @property
    def block_type(self):
        """
        The indirect block format that the aggregate can have.
        It can be either 32_bit or 64_bit. A 64_bit value
        indicates that associated aggregates can be larger than
        16TB.
        Possible values: 32_bit, 64_bit
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
        Number of user-visible files used.
        Range: [0..2^64-1].
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
        files are created.
        Range: [0..2^64-1].
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
        Aggregate name.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _is_hybrid = None
    @property
    def is_hybrid(self):
        """
        If true, aggregate currently contains both SSD
        and non-SSD RAID groups.
        """
        return self._is_hybrid
    @is_hybrid.setter
    def is_hybrid(self, val):
        if val != None:
            self.validate('is_hybrid', val)
        self._is_hybrid = val
    
    _aggregate_space_details = None
    @property
    def aggregate_space_details(self):
        """
        Contains all size-related information for
        the aggr and its set of snapshots.
        """
        return self._aggregate_space_details
    @aggregate_space_details.setter
    def aggregate_space_details(self, val):
        if val != None:
            self.validate('aggregate_space_details', val)
        self._aggregate_space_details = val
    
    _aggr_64bit_upgrade = None
    @property
    def aggr_64bit_upgrade(self):
        """
        Information related to 64-bit upgrade. After 64-bit
        upgrade completes, this information is no longer
        available.
        """
        return self._aggr_64bit_upgrade
    @aggr_64bit_upgrade.setter
    def aggr_64bit_upgrade(self, val):
        if val != None:
            self.validate('aggr_64bit_upgrade', val)
        self._aggr_64bit_upgrade = val
    
    _volume_count_not_online = None
    @property
    def volume_count_not_online(self):
        """
        When present, this field indicates the number of
        volumes that are not online (offline and restricted
        volumes).
        <p>
        Range: [0..2^31-1]
        """
        return self._volume_count_not_online
    @volume_count_not_online.setter
    def volume_count_not_online(self, val):
        if val != None:
            self.validate('volume_count_not_online', val)
        self._volume_count_not_online = val
    
    _is_mirrored = None
    @property
    def is_mirrored(self):
        """
        If true, aggregate is mirrored.
        """
        return self._is_mirrored
    @is_mirrored.setter
    def is_mirrored(self, val):
        if val != None:
            self.validate('is_mirrored', val)
        self._is_mirrored = val
    
    _home_id = None
    @property
    def home_id(self):
        """
        NVRAM ID of the node to which this aggregate's
        disks have been administratively assigned. This
        information derived from sanown information of
        aggregate's disk. See 'disk-sanown-detail-info'
        Range : [0..2^32-1].
        """
        return self._home_id
    @home_id.setter
    def home_id(self, val):
        if val != None:
            self.validate('home_id', val)
        self._home_id = val
    
    _size_total = None
    @property
    def size_total(self):
        """
        Aggregate total usable size in bytes, not including
        WAFL reserve and aggregate snapshot reserve.  If the
        aggregate is restricted or offline, a value of 0 is
        returned.
        Range : [0..2^64-1].
        """
        return self._size_total
    @size_total.setter
    def size_total(self, val):
        if val != None:
            self.validate('size_total', val)
        self._size_total = val
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        NVRAM ID of node which currently owns this
        aggregate's disks.
        Normally, home-id matches owner-id.  But these
        may be changed by SFO takeover to match the
        takeover node, and restored by SFO giveback
        to match home-id. CFO takeover and giveback
        do not affect owner-id.
        This information derived from sanown information of
        aggregate's disk. See 'disk-sanown-detail-info'
        Range : [0..2^32-1].
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _disk_count = None
    @property
    def disk_count(self):
        """
        Number of disks in the aggregate.  Range:
        [0..2^31-1].
        """
        return self._disk_count
    @disk_count.setter
    def disk_count(self, val):
        if val != None:
            self.validate('disk_count', val)
        self._disk_count = val
    
    @staticmethod
    def get_api_name():
          return "aggr-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'wafliron',
            'ha-policy',
            'home-name',
            'volume-count-quiesced',
            'inodefile-private-capacity',
            'has-partner-root',
            'checksum-style',
            'raid-lost-write-state',
            'volume-count-collective',
            'checksum-status',
            'volume-count-mirrors',
            'volume-count',
            'size-percentage-used',
            'is-snaplock',
            'is-hybrid-enabled',
            'owner-name',
            'cache-raid-group-size',
            'size-available',
            'uuid',
            'plex-count',
            'size-used',
            'mirror-status',
            'state',
            'files-total',
            'fsid',
            'striping',
            'plexes',
            'volume-count-striped',
            'type',
            'raid-status',
            'raid-size',
            'volumes',
            'max-write-alloc-blocks',
            'snaplock-type',
            'files-private-used',
            'dr-home-id',
            'has-local-root',
            'free-space-realloc',
            'is-inconsistent',
            'dr-home-name',
            'is-checksum-enabled',
            'mount-state',
            'block-type',
            'files-used',
            'inodefile-public-capacity',
            'name',
            'is-hybrid',
            'aggregate-space-details',
            'aggr-64bit-upgrade',
            'volume-count-not-online',
            'is-mirrored',
            'home-id',
            'size-total',
            'owner-id',
            'disk-count',
        ]
    
    def describe_properties(self):
        return {
            'wafliron': { 'class': AggrWaflironInfo, 'is_list': False, 'required': 'optional' },
            'ha_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'home_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume_count_quiesced': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodefile_private_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'has_partner_root': { 'class': bool, 'is_list': False, 'required': 'required' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'raid_lost_write_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume_count_collective': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_count_mirrors': { 'class': MirrorCountInfo, 'is_list': False, 'required': 'optional' },
            'volume_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_percentage_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_snaplock': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_hybrid_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'owner_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_raid_group_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_available': { 'class': int, 'is_list': False, 'required': 'required' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'plex_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'mirror_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'files_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'striping': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'plexes': { 'class': PlexInfo, 'is_list': True, 'required': 'required' },
            'volume_count_striped': { 'class': int, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'raid_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'raid_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'volumes': { 'class': ContainedVolumeInfo, 'is_list': True, 'required': 'required' },
            'max_write_alloc_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snaplock_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'files_private_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'dr_home_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'has_local_root': { 'class': bool, 'is_list': False, 'required': 'required' },
            'free_space_realloc': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_inconsistent': { 'class': bool, 'is_list': False, 'required': 'required' },
            'dr_home_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_checksum_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'mount_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'block_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodefile_public_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_hybrid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'aggregate_space_details': { 'class': AggregateSpaceInfo, 'is_list': False, 'required': 'optional' },
            'aggr_64bit_upgrade': { 'class': Aggr64BitUpgradeInfo, 'is_list': False, 'required': 'optional' },
            'volume_count_not_online': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_mirrored': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'home_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'owner_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
