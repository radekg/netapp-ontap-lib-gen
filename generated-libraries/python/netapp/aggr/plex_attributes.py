from netapp.aggr.raidgroup_attributes import RaidgroupAttributes
from netapp.netapp_object import NetAppObject

class PlexAttributes(NetAppObject):
    """
    Information about a plex.
    """
    
    _is_online = None
    @property
    def is_online(self):
        """
        "true" if the plex is online, "false"
        otherwise.
        """
        return self._is_online
    @is_online.setter
    def is_online(self, val):
        if val != None:
            self.validate('is_online', val)
        self._is_online = val
    
    _plex_status = None
    @property
    def plex_status(self):
        """
        Plex status. Possible values:
        "normal", "failed", "empty", "invalid",
        "uninitialized", "failed assimilation",
        "limbo", "active", "inactive", "resyncing",
        These values may appear by themselves or
        in combination separated by commas
        (e.g., "normal,active")
        """
        return self._plex_status
    @plex_status.setter
    def plex_status(self, val):
        if val != None:
            self.validate('plex_status', val)
        self._plex_status = val
    
    _resync_level = None
    @property
    def resync_level(self):
        """
        If the plex is currently being
        resynced, then the resync level.
        """
        return self._resync_level
    @resync_level.setter
    def resync_level(self, val):
        if val != None:
            self.validate('resync_level', val)
        self._resync_level = val
    
    _resyncing_percentage = None
    @property
    def resyncing_percentage(self):
        """
        If the plex is currently being
        resynced, then the completion
        percentage.
        """
        return self._resyncing_percentage
    @resyncing_percentage.setter
    def resyncing_percentage(self, val):
        if val != None:
            self.validate('resyncing_percentage', val)
        self._resyncing_percentage = val
    
    _is_resyncing = None
    @property
    def is_resyncing(self):
        """
        "true" if the plex is currently
        resyncing, "false" otherwise.
        """
        return self._is_resyncing
    @is_resyncing.setter
    def is_resyncing(self, val):
        if val != None:
            self.validate('is_resyncing', val)
        self._is_resyncing = val
    
    _raidgroups = None
    @property
    def raidgroups(self):
        """
        List of all RAID groups in the plex.
        """
        return self._raidgroups
    @raidgroups.setter
    def raidgroups(self, val):
        if val != None:
            self.validate('raidgroups', val)
        self._raidgroups = val
    
    _plex_name = None
    @property
    def plex_name(self):
        """
        Name of the plex.
        """
        return self._plex_name
    @plex_name.setter
    def plex_name(self, val):
        if val != None:
            self.validate('plex_name', val)
        self._plex_name = val
    
    _pool = None
    @property
    def pool(self):
        """
        The pool to which the majority
        of disks in the plex belong.
        """
        return self._pool
    @pool.setter
    def pool(self, val):
        if val != None:
            self.validate('pool', val)
        self._pool = val
    
    @staticmethod
    def get_api_name():
          return "plex-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-online',
            'plex-status',
            'resync-level',
            'resyncing-percentage',
            'is-resyncing',
            'raidgroups',
            'plex-name',
            'pool',
        ]
    
    def describe_properties(self):
        return {
            'is_online': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'plex_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'resync_level': { 'class': int, 'is_list': False, 'required': 'optional' },
            'resyncing_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_resyncing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'raidgroups': { 'class': RaidgroupAttributes, 'is_list': True, 'required': 'optional' },
            'plex_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pool': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
