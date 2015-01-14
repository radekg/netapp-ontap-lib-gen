from netapp.aggr.disk_info import DiskInfo
from netapp.netapp_object import NetAppObject

class RaidGroupInfo(NetAppObject):
    """
    Information for a particular RAID
    group.
    """
    
    _is_scrub_suspended = None
    @property
    def is_scrub_suspended(self):
        """
        Suspended state of the scrub on that RAID group.
        """
        return self._is_scrub_suspended
    @is_scrub_suspended.setter
    def is_scrub_suspended(self, val):
        if val != None:
            self.validate('is_scrub_suspended', val)
        self._is_scrub_suspended = val
    
    _scrub_percentage_complete = None
    @property
    def scrub_percentage_complete(self):
        """
        Scrub percentage complete. If scrub is
        not active, this value will not be returned.
        Range: [0..100].
        """
        return self._scrub_percentage_complete
    @scrub_percentage_complete.setter
    def scrub_percentage_complete(self, val):
        if val != None:
            self.validate('scrub_percentage_complete', val)
        self._scrub_percentage_complete = val
    
    _reconstruction_percentage = None
    @property
    def reconstruction_percentage(self):
        """
        If reconstruction is going on,
        the the completion percentage.
        Range : [0-100]
        """
        return self._reconstruction_percentage
    @reconstruction_percentage.setter
    def reconstruction_percentage(self, val):
        if val != None:
            self.validate('reconstruction_percentage', val)
        self._reconstruction_percentage = val
    
    _name = None
    @property
    def name(self):
        """
        RAID group name.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _recomputing_parity_percentage = None
    @property
    def recomputing_parity_percentage(self):
        """
        The percentage of parity recomputation if
        is-recomputing-parity is set to true.
        Range : [0-100]
        """
        return self._recomputing_parity_percentage
    @recomputing_parity_percentage.setter
    def recomputing_parity_percentage(self, val):
        if val != None:
            self.validate('recomputing_parity_percentage', val)
        self._recomputing_parity_percentage = val
    
    _checksum_style = None
    @property
    def checksum_style(self):
        """
        Checksum style. The possible values:
        <ul>
        <li> "advanced_zoned"  - advanced_zoned checksum (azcs),
        <li> "block"           - block,
        <li> "mixed"           - mixed,
        <li> "none"            - none,
        <li> "unknown"         - unknown,
        <li> "wafl"            - wafl,
        <li> "zoned"           - zoned.
        </ul>
        """
        return self._checksum_style
    @checksum_style.setter
    def checksum_style(self, val):
        if val != None:
            self.validate('checksum_style', val)
        self._checksum_style = val
    
    _is_recomputing_parity = None
    @property
    def is_recomputing_parity(self):
        """
        "true" if the RAID group is
        currently recomputing parity.
        """
        return self._is_recomputing_parity
    @is_recomputing_parity.setter
    def is_recomputing_parity(self, val):
        if val != None:
            self.validate('is_recomputing_parity', val)
        self._is_recomputing_parity = val
    
    _disks = None
    @property
    def disks(self):
        """
        List of disks in this plex.
        """
        return self._disks
    @disks.setter
    def disks(self, val):
        if val != None:
            self.validate('disks', val)
        self._disks = val
    
    _is_reconstructing = None
    @property
    def is_reconstructing(self):
        """
        "true" if the RAID group is
        currently reconstructing.
        """
        return self._is_reconstructing
    @is_reconstructing.setter
    def is_reconstructing(self, val):
        if val != None:
            self.validate('is_reconstructing', val)
        self._is_reconstructing = val
    
    _last_scrub_timestamp = None
    @property
    def last_scrub_timestamp(self):
        """
        Time at which the last full scrub completed.
        If a scrub has never been performed, this
        value will not be returned.  The time value
        is in seconds since January 1, 1970.
        Range : [0..2^31-1].
        """
        return self._last_scrub_timestamp
    @last_scrub_timestamp.setter
    def last_scrub_timestamp(self, val):
        if val != None:
            self.validate('last_scrub_timestamp', val)
        self._last_scrub_timestamp = val
    
    _is_cache_tier = None
    @property
    def is_cache_tier(self):
        """
        "true" if the RAID group is
        composed of SSDs and the owning
        aggregate is hybrid (group is not
        part of usable space).
        """
        return self._is_cache_tier
    @is_cache_tier.setter
    def is_cache_tier(self, val):
        if val != None:
            self.validate('is_cache_tier', val)
        self._is_cache_tier = val
    
    @staticmethod
    def get_api_name():
          return "raid-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-scrub-suspended',
            'scrub-percentage-complete',
            'reconstruction-percentage',
            'name',
            'recomputing-parity-percentage',
            'checksum-style',
            'is-recomputing-parity',
            'disks',
            'is-reconstructing',
            'last-scrub-timestamp',
            'is-cache-tier',
        ]
    
    def describe_properties(self):
        return {
            'is_scrub_suspended': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'scrub_percentage_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'reconstruction_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'recomputing_parity_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_recomputing_parity': { 'class': bool, 'is_list': False, 'required': 'required' },
            'disks': { 'class': DiskInfo, 'is_list': True, 'required': 'required' },
            'is_reconstructing': { 'class': bool, 'is_list': False, 'required': 'required' },
            'last_scrub_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_cache_tier': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
