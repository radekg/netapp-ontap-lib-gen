from netapp.netapp_object import NetAppObject

class RaidgroupAttributes(NetAppObject):
    """
    Information about a raidgroup.
    """
    
    _reconstruction_percentage = None
    @property
    def reconstruction_percentage(self):
        """
        If reconstruction is going on,
        then the completion percentage.
        """
        return self._reconstruction_percentage
    @reconstruction_percentage.setter
    def reconstruction_percentage(self, val):
        if val != None:
            self.validate('reconstruction_percentage', val)
        self._reconstruction_percentage = val
    
    _recomputing_parity_percentage = None
    @property
    def recomputing_parity_percentage(self):
        """
        The percentage of parity recomputation completed,
        if is-recomputing-parity is true.
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
        Checksum style for the RAID group. The possible values are:
        "none", "zoned", "block", "wafl", "unknown" or "advanced_zoned".
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
        "True" if the RAID group is
        currently recomputing parity.
        """
        return self._is_recomputing_parity
    @is_recomputing_parity.setter
    def is_recomputing_parity(self, val):
        if val != None:
            self.validate('is_recomputing_parity', val)
        self._is_recomputing_parity = val
    
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
    
    _raidgroup_name = None
    @property
    def raidgroup_name(self):
        """
        Name of the RAID group.
        """
        return self._raidgroup_name
    @raidgroup_name.setter
    def raidgroup_name(self, val):
        if val != None:
            self.validate('raidgroup_name', val)
        self._raidgroup_name = val
    
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
          return "raidgroup-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'reconstruction-percentage',
            'recomputing-parity-percentage',
            'checksum-style',
            'is-recomputing-parity',
            'is-reconstructing',
            'raidgroup-name',
            'is-cache-tier',
        ]
    
    def describe_properties(self):
        return {
            'reconstruction_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'recomputing_parity_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_recomputing_parity': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_reconstructing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'raidgroup_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_cache_tier': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
