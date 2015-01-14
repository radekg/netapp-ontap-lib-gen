from netapp.netapp_object import NetAppObject

class DiskAggregateInfo(NetAppObject):
    """
    Details giving disk's basic disposition within its overlying
    aggregate or traditional volume.  Information that is specific
    to a disk contained within an aggregate or traditional volume
    is returned here.  Returned only if 'container-type' is
    "aggregate" or "volume".
    """
    
    _is_media_scrubbing = None
    @property
    def is_media_scrubbing(self):
        """
        True if media scrub is currently active for this disk.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_media_scrubbing
    @is_media_scrubbing.setter
    def is_media_scrubbing(self, val):
        if val != None:
            self.validate('is_media_scrubbing', val)
        self._is_media_scrubbing = val
    
    _is_replacing = None
    @property
    def is_replacing(self):
        """
        True if the admin issued 'disk replace' to
        replace this disk with a specified replacement
        disk.  This flag is expected to remain true until
        the system has copied the contents of this disk
        to the admin-specified replacement disk.  At that
        point this disk is expected to be released to the
        spare pool.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._is_replacing
    @is_replacing.setter
    def is_replacing(self, val):
        if val != None:
            self.validate('is_replacing', val)
        self._is_replacing = val
    
    _checksum_type = None
    @property
    def checksum_type(self):
        """
        The checksum type that has been assigned to this disk.
        Omitted if information is unavailable,
        or if excluded by 'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "advanced_zoned" - Advanced zoned checksum.
        <li> "block"		- Block checksum.
        <li> "none"		- No checksum type assigned.
        <li> "wafl"		- WAFL checksum.
        <li> "zoned"		- Zoned checksum.
        </ul>
        """
        return self._checksum_type
    @checksum_type.setter
    def checksum_type(self, val):
        if val != None:
            self.validate('checksum_type', val)
        self._checksum_type = val
    
    _aggregate_name = None
    @property
    def aggregate_name(self):
        """
        Name of aggregate or traditional volume with which
        this disk is associated.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._aggregate_name
    @aggregate_name.setter
    def aggregate_name(self, val):
        if val != None:
            self.validate('aggregate_name', val)
        self._aggregate_name = val
    
    _is_evacuating = None
    @property
    def is_evacuating(self):
        """
        True if Data ONTAP is copying the disk that is housed
        in the same carrier with a failed disk.  This flag is
        expected to remain true until the system has copied
        the contents of this disk to the replacement disk.
        At that time this disk is expected to be failed
        with the reason "evacuated".  Omitted if excluded
        by 'desired-attributes'.
        """
        return self._is_evacuating
    @is_evacuating.setter
    def is_evacuating(self, val):
        if val != None:
            self.validate('is_evacuating', val)
        self._is_evacuating = val
    
    _copy_destination_name = None
    @property
    def copy_destination_name(self):
        """
        name of copy destination.  Omitted if both
        'is-prefailed' and 'is-replacing' are false,
        or if excluded by 'desired-attributes'.
        """
        return self._copy_destination_name
    @copy_destination_name.setter
    def copy_destination_name(self, val):
        if val != None:
            self.validate('copy_destination_name', val)
        self._copy_destination_name = val
    
    _copy_percent_complete = None
    @property
    def copy_percent_complete(self):
        """
        Percent completion of disk copy.
        Omitted if no copy operation involving this
        disk is in progress.  So omitted if neither
        'is-prefailed' nor 'is-replacing' is true,
        and if position is not "copy".
        """
        return self._copy_percent_complete
    @copy_percent_complete.setter
    def copy_percent_complete(self, val):
        if val != None:
            self.validate('copy_percent_complete', val)
        self._copy_percent_complete = val
    
    _zeroing_percent_complete = None
    @property
    def zeroing_percent_complete(self):
        """
        Percent completion of disk zeroing.
        Omitted if is-zeroing' is not true,
        or if excluded by 'desired-attributes'.
        """
        return self._zeroing_percent_complete
    @zeroing_percent_complete.setter
    def zeroing_percent_complete(self, val):
        if val != None:
            self.validate('zeroing_percent_complete', val)
        self._zeroing_percent_complete = val
    
    _is_zeroed = None
    @property
    def is_zeroed(self):
        """
        True if disk is in pre-zeroed state.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_zeroed
    @is_zeroed.setter
    def is_zeroed(self, val):
        if val != None:
            self.validate('is_zeroed', val)
        self._is_zeroed = val
    
    _copy_reason = None
    @property
    def copy_reason(self):
        """
        The reason this disk has been marked for a disk copy
        operation. Possible values include:
        <ul>
        <li> "evacuation"             - Disk is marked for evacuation.
        <li> "layout_optimization"    - Disk is marked for layout
        optimization.
        </ul>
        Omitted if disk copy is not in progress or excluded by
        'desired-attributes'.
        """
        return self._copy_reason
    @copy_reason.setter
    def copy_reason(self, val):
        if val != None:
            self.validate('copy_reason', val)
        self._copy_reason = val
    
    _is_offline = None
    @property
    def is_offline(self):
        """
        True if disk is offline.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_offline
    @is_offline.setter
    def is_offline(self, val):
        if val != None:
            self.validate('is_offline', val)
        self._is_offline = val
    
    _is_reconstructing = None
    @property
    def is_reconstructing(self):
        """
        True if disk is in process of being reconstructed.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_reconstructing
    @is_reconstructing.setter
    def is_reconstructing(self, val):
        if val != None:
            self.validate('is_reconstructing', val)
        self._is_reconstructing = val
    
    _is_prefailed = None
    @property
    def is_prefailed(self):
        """
        True if the admin issued a 'disk fail' or if the
        the system marked this disk for Rapid RAID
        Recovery.  This flag is expected to remain set until
        the system has copied the contents of this disk to
        a system-selected replacement disk.  At that point,
        this disk is expected to be removed from service and
        placed in in the broken pool. Omitted if excluded
        by 'desired-attributes'.
        """
        return self._is_prefailed
    @is_prefailed.setter
    def is_prefailed(self, val):
        if val != None:
            self.validate('is_prefailed', val)
        self._is_prefailed = val
    
    _reconstruct_percent_complete = None
    @property
    def reconstruct_percent_complete(self):
        """
        Percent completion of disk reconstruction.
        Omitted if 'is-reconstructing' is not true,
        or if excluded by 'desired-attributes'.
        """
        return self._reconstruct_percent_complete
    @reconstruct_percent_complete.setter
    def reconstruct_percent_complete(self, val):
        if val != None:
            self.validate('reconstruct_percent_complete', val)
        self._reconstruct_percent_complete = val
    
    _raid_group_name = None
    @property
    def raid_group_name(self):
        """
        Name of RAID group to which this disk belongs.
        Omitted if disk does not belong to a RAID group,
        or if excluded by 'desired-attributes'.
        """
        return self._raid_group_name
    @raid_group_name.setter
    def raid_group_name(self, val):
        if val != None:
            self.validate('raid_group_name', val)
        self._raid_group_name = val
    
    _is_zeroing = None
    @property
    def is_zeroing(self):
        """
        True only if disk position is 'pending' and disk
        is in process of being zeroed.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_zeroing
    @is_zeroing.setter
    def is_zeroing(self, val):
        if val != None:
            self.validate('is_zeroing', val)
        self._is_zeroing = val
    
    _plex_name = None
    @property
    def plex_name(self):
        """
        Name of plex with which this disk is associated.
        Omitted if disk is not associated with a plex, or
        if excluded by 'desired-attributes'.
        """
        return self._plex_name
    @plex_name.setter
    def plex_name(self, val):
        if val != None:
            self.validate('plex_name', val)
        self._plex_name = val
    
    @staticmethod
    def get_api_name():
          return "disk-aggregate-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-media-scrubbing',
            'is-replacing',
            'checksum-type',
            'aggregate-name',
            'is-evacuating',
            'copy-destination-name',
            'copy-percent-complete',
            'zeroing-percent-complete',
            'is-zeroed',
            'copy-reason',
            'is-offline',
            'is-reconstructing',
            'is-prefailed',
            'reconstruct-percent-complete',
            'raid-group-name',
            'is-zeroing',
            'plex-name',
        ]
    
    def describe_properties(self):
        return {
            'is_media_scrubbing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_replacing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'checksum_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggregate_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_evacuating': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'copy_destination_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'copy_percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'zeroing_percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_zeroed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'copy_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_offline': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_reconstructing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_prefailed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'reconstruct_percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'raid_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_zeroing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'plex_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
