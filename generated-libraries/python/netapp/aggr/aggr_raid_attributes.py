from netapp.aggr.plex_attributes import PlexAttributes
from netapp.netapp_object import NetAppObject

class AggrRaidAttributes(NetAppObject):
    """
    RAID specific information of the aggregate
    """
    
    _cache_raid_group_size = None
    @property
    def cache_raid_group_size(self):
        """
        Current maximum cache RAID group size of hybrid aggregate.
        RAID group size is the maximum number of disks that can be added
        to a RAID group.
        This information will only be returned for a hybrid aggregate i.e.
        whose "is-hybrid" field is set to true.
        """
        return self._cache_raid_group_size
    @cache_raid_group_size.setter
    def cache_raid_group_size(self, val):
        if val != None:
            self.validate('cache_raid_group_size', val)
        self._cache_raid_group_size = val
    
    _raid_status = None
    @property
    def raid_status(self):
        """
        RAID status.  Possible values: "copying", "degraded",
        "foreign", "growing", "initializing", "invalid", "ironing",
        "mirror degraded", "mirrored", "needs check", "normal",
        "noparity", "out-of-date", "partial", "reconstruct",
        "raid0", "raid4", "raid_dp", "mixed_raid_type",
        "resyncing", "SnapMirrored", "verifying".  These values
        may appear by themselves or in combination
        separated by commas (e.g., "reconstruct,growing").
        For striped aggregate, additional possible value is "various".
        For details on raid-type, refer description of element
        'raid-type' below
        """
        return self._raid_status
    @raid_status.setter
    def raid_status(self, val):
        if val != None:
            self.validate('raid_status', val)
        self._raid_status = val
    
    _plex_count = None
    @property
    def plex_count(self):
        """
        Number of plexes in the aggregate.  This
        value tells us the size of the returned
        "plex" array.
        """
        return self._plex_count
    @plex_count.setter
    def plex_count(self, val):
        if val != None:
            self.validate('plex_count', val)
        self._plex_count = val
    
    _checksum_status = None
    @property
    def checksum_status(self):
        """
        Checksum status. Possible values:
        "active", "initializing", "none", "off",
        "reinitialized", "reinitializing", "reverting",
        "unknown", "upgrading_phase1", "upgrading_phase2"
        This information will not be returned for a striped aggregate.
        """
        return self._checksum_status
    @checksum_status.setter
    def checksum_status(self, val):
        if val != None:
            self.validate('checksum_status', val)
        self._checksum_status = val
    
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
    
    _raid_size = None
    @property
    def raid_size(self):
        """
        Current RAID group size.
        This information will not be returned for a striped aggregate.
        """
        return self._raid_size
    @raid_size.setter
    def raid_size(self, val):
        if val != None:
            self.validate('raid_size', val)
        self._raid_size = val
    
    _raid_type = None
    @property
    def raid_type(self):
        """
        Possible values:
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
        return self._raid_type
    @raid_type.setter
    def raid_type(self, val):
        if val != None:
            self.validate('raid_type', val)
        self._raid_type = val
    
    _has_partner_root = None
    @property
    def has_partner_root(self):
        """
        Whether the aggregate contains the
        partner's root volume.
        This information will not be returned for a striped aggregate.
        Default value is false.
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
    
    _state = None
    @property
    def state(self):
        """
        Aggregate State
        Possible values:
        <ul>
        <li> "creating"            ,
        <li> "destroying"          ,
        <li> "failed"              ,
        <li> "frozen"              ,
        <li> "inconsistent"        ,
        <li> "iron_restricted"     ,
        <li> "mounting"            ,
        <li> "online"             ,
        <li> "offline"             ,
        <li> "partial"             ,
        <li> "quiesced"            ,
        <li> "quiescing"           ,
        <li> "restricted"          ,
        <li> "reverted"            ,
        <li> "unknown"             ,
        <li> "unmounted"           ,
        <li> "unmounting"          ,
        <li> "relocating"
        </ul>
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
        Aggregate's mirror status.  Possible values:
        "invalid", "uninitialized", "needs CP count check",
        "CP count check in progress", "unmirrored", "mirrored",
        "mirror degraded, "mirror resynchronizing", "failed",
        "limbo" and <unknown mirror state>.
        This information will not be returned for a striped aggregate.
        """
        return self._mirror_status
    @mirror_status.setter
    def mirror_status(self, val):
        if val != None:
            self.validate('mirror_status', val)
        self._mirror_status = val
    
    _is_checksum_enabled = None
    @property
    def is_checksum_enabled(self):
        """
        Is checksumming enabled for the aggregate?
        Default value is false.
        """
        return self._is_checksum_enabled
    @is_checksum_enabled.setter
    def is_checksum_enabled(self, val):
        if val != None:
            self.validate('is_checksum_enabled', val)
        self._is_checksum_enabled = val
    
    _is_inconsistent = None
    @property
    def is_inconsistent(self):
        """
        Whether or not the aggregate is inconsistent.
        Default value is false.
        """
        return self._is_inconsistent
    @is_inconsistent.setter
    def is_inconsistent(self, val):
        if val != None:
            self.validate('is_inconsistent', val)
        self._is_inconsistent = val
    
    _plexes = None
    @property
    def plexes(self):
        """
        List of plexes in the aggregate
        """
        return self._plexes
    @plexes.setter
    def plexes(self, val):
        if val != None:
            self.validate('plexes', val)
        self._plexes = val
    
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
    
    _disk_count = None
    @property
    def disk_count(self):
        """
        Number of disks in the aggregate.
        """
        return self._disk_count
    @disk_count.setter
    def disk_count(self, val):
        if val != None:
            self.validate('disk_count', val)
        self._disk_count = val
    
    _mount_state = None
    @property
    def mount_state(self):
        """
        [not settable, always]
        This field shows the volume's mount state. Possible
        values: "creating", "destroying", "frozen", "inconsistent",
        "iron_restricted", "mounting", "online", "quiescing",
        "quiesced", "reverted", "unmounted", "unmounting"
        This information will not be returned for a striped aggregate.
        """
        return self._mount_state
    @mount_state.setter
    def mount_state(self, val):
        if val != None:
            self.validate('mount_state', val)
        self._mount_state = val
    
    _has_local_root = None
    @property
    def has_local_root(self):
        """
        Whether the aggregate contains the
        local root volume.
        This information will not be returned for a striped aggregate.
        Default value is false.
        """
        return self._has_local_root
    @has_local_root.setter
    def has_local_root(self, val):
        if val != None:
            self.validate('has_local_root', val)
        self._has_local_root = val
    
    @staticmethod
    def get_api_name():
          return "aggr-raid-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cache-raid-group-size',
            'raid-status',
            'plex-count',
            'checksum-status',
            'ha-policy',
            'is-hybrid',
            'raid-size',
            'raid-type',
            'has-partner-root',
            'checksum-style',
            'raid-lost-write-state',
            'state',
            'mirror-status',
            'is-checksum-enabled',
            'is-inconsistent',
            'plexes',
            'is-hybrid-enabled',
            'disk-count',
            'mount-state',
            'has-local-root',
        ]
    
    def describe_properties(self):
        return {
            'cache_raid_group_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'raid_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'plex_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ha_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_hybrid': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'raid_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'raid_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'has_partner_root': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'raid_lost_write_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mirror_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_checksum_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_inconsistent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'plexes': { 'class': PlexAttributes, 'is_list': True, 'required': 'optional' },
            'is_hybrid_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'disk_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mount_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'has_local_root': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
