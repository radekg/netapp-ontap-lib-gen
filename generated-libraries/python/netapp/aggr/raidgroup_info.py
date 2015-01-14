from netapp.netapp_object import NetAppObject

class RaidgroupInfo(NetAppObject):
    """
    auto generated
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _raidgroup = None
    @property
    def raidgroup(self):
        """
        Raidgroup Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._raidgroup
    @raidgroup.setter
    def raidgroup(self, val):
        if val != None:
            self.validate('raidgroup', val)
        self._raidgroup = val
    
    _recomputing_parity_percentage = None
    @property
    def recomputing_parity_percentage(self):
        """
        Reparity Percentage
        Attributes: non-creatable, non-modifiable
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
        Raidgroup Checksum style
        Attributes: non-creatable, non-modifiable
        """
        return self._checksum_style
    @checksum_style.setter
    def checksum_style(self, val):
        if val != None:
            self.validate('checksum_style', val)
        self._checksum_style = val
    
    _plex = None
    @property
    def plex(self):
        """
        Plex Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._plex
    @plex.setter
    def plex(self, val):
        if val != None:
            self.validate('plex', val)
        self._plex = val
    
    _is_recomputing_parity = None
    @property
    def is_recomputing_parity(self):
        """
        Is reparity active ?
        Attributes: non-creatable, non-modifiable
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
        Is Reconstructing
        Attributes: non-creatable, non-modifiable
        """
        return self._is_reconstructing
    @is_reconstructing.setter
    def is_reconstructing(self, val):
        if val != None:
            self.validate('is_reconstructing', val)
        self._is_reconstructing = val
    
    _aggregate = None
    @property
    def aggregate(self):
        """
        Aggregate
        Attributes: key, non-creatable, non-modifiable
        """
        return self._aggregate
    @aggregate.setter
    def aggregate(self, val):
        if val != None:
            self.validate('aggregate', val)
        self._aggregate = val
    
    _reconstruction_percent = None
    @property
    def reconstruction_percent(self):
        """
        Reconstruction Percentage
        Attributes: non-creatable, non-modifiable
        """
        return self._reconstruction_percent
    @reconstruction_percent.setter
    def reconstruction_percent(self, val):
        if val != None:
            self.validate('reconstruction_percent', val)
        self._reconstruction_percent = val
    
    _is_cache_tier = None
    @property
    def is_cache_tier(self):
        """
        Is cache tier ?
        Attributes: non-creatable, non-modifiable
        """
        return self._is_cache_tier
    @is_cache_tier.setter
    def is_cache_tier(self, val):
        if val != None:
            self.validate('is_cache_tier', val)
        self._is_cache_tier = val
    
    @staticmethod
    def get_api_name():
          return "raidgroup-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raidgroup',
            'recomputing-parity-percentage',
            'checksum-style',
            'plex',
            'is-recomputing-parity',
            'is-reconstructing',
            'aggregate',
            'reconstruction-percent',
            'is-cache-tier',
        ]
    
    def describe_properties(self):
        return {
            'raidgroup': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'recomputing_parity_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'plex': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_recomputing_parity': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_reconstructing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'reconstruction_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_cache_tier': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
