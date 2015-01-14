from netapp.netapp_object import NetAppObject

class DiskFilesysUsageDetailInfo(NetAppObject):
    """
    Available disk space details for a given volume, aggregate or their
    respective snapshots
    """
    
    _status = None
    @property
    def status(self):
        """
        The status of the file system. Possible values:
        "unmounted", "mounted", "frozen", "destroying",
        "creating", "mounting", "unmounting", "nofsinfo",
        "replaying", "replayed".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _used_space = None
    @property
    def used_space(self):
        """
        The total disk space in KBytes that is in use
        on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._used_space
    @used_space.setter
    def used_space(self, val):
        if val != None:
            self.validate('used_space', val)
        self._used_space = val
    
    _percent_saved = None
    @property
    def percent_saved(self):
        """
        The percentage of disk space saved by
        eliminating the duplicated blocks on the
        referenced file system. Range: [0 - 100]
        """
        return self._percent_saved
    @percent_saved.setter
    def percent_saved(self, val):
        if val != None:
            self.validate('percent_saved', val)
        self._percent_saved = val
    
    _total_percent_saved = None
    @property
    def total_percent_saved(self):
        """
        Percentage of total disk space that is saved by compressing
        blocks, deduplication and file cloning. Range: [0 - 100]
        """
        return self._total_percent_saved
    @total_percent_saved.setter
    def total_percent_saved(self, val):
        if val != None:
            self.validate('total_percent_saved', val)
        self._total_percent_saved = val
    
    _total_reserved_space = None
    @property
    def total_reserved_space(self):
        """
        The total disk space in KBytes that is reserved
        on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._total_reserved_space
    @total_reserved_space.setter
    def total_reserved_space(self, val):
        if val != None:
            self.validate('total_reserved_space', val)
        self._total_reserved_space = val
    
    _filesys_name = None
    @property
    def filesys_name(self):
        """
        The name for the referenced file system.
        """
        return self._filesys_name
    @filesys_name.setter
    def filesys_name(self, val):
        if val != None:
            self.validate('filesys_name', val)
        self._filesys_name = val
    
    _mirror_status = None
    @property
    def mirror_status(self):
        """
        Overall mirror status of the file system.
        Possible values: "invalid", "uninitialized",
        "needcpcheck", "cpcheckwait", "unmirrored",
        "normal", "degraded", "resyncing", "failed",
        "limbo".
        """
        return self._mirror_status
    @mirror_status.setter
    def mirror_status(self, val):
        if val != None:
            self.validate('mirror_status', val)
        self._mirror_status = val
    
    _percent_used_capacity = None
    @property
    def percent_used_capacity(self):
        """
        The percentage of disk space currently
        in use on the referenced file system.
        Range: [0 - 100]
        """
        return self._percent_used_capacity
    @percent_used_capacity.setter
    def percent_used_capacity(self, val):
        if val != None:
            self.validate('percent_used_capacity', val)
        self._percent_used_capacity = val
    
    _inodes_used = None
    @property
    def inodes_used(self):
        """
        The total number of inodes in use on the
        referenced file system. Range: [0 - 2^32-1]
        """
        return self._inodes_used
    @inodes_used.setter
    def inodes_used(self, val):
        if val != None:
            self.validate('inodes_used', val)
        self._inodes_used = val
    
    _available_space = None
    @property
    def available_space(self):
        """
        The total disk space in KBytes that is free
        for use on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._available_space
    @available_space.setter
    def available_space(self, val):
        if val != None:
            self.validate('available_space', val)
        self._available_space = val
    
    _type = None
    @property
    def type(self):
        """
        Indicates the type of container. Possible
        values: "traditionalVolume", "flexibleVolume",
        "aggregate"
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _compression_bytes_saved = None
    @property
    def compression_bytes_saved(self):
        """
        The total disk space in bytes that is saved
        by compressing blocks on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._compression_bytes_saved
    @compression_bytes_saved.setter
    def compression_bytes_saved(self, val):
        if val != None:
            self.validate('compression_bytes_saved', val)
        self._compression_bytes_saved = val
    
    _percent_inode_capacity = None
    @property
    def percent_inode_capacity(self):
        """
        The percentage of disk space currently in use
        based on inode counts, on the referenced file
        system. Range: [0 - 100]
        """
        return self._percent_inode_capacity
    @percent_inode_capacity.setter
    def percent_inode_capacity(self, val):
        if val != None:
            self.validate('percent_inode_capacity', val)
        self._percent_inode_capacity = val
    
    _plex_count = None
    @property
    def plex_count(self):
        """
        Number of plexes in this file system.
        Range: [0 - 2^32-1]
        """
        return self._plex_count
    @plex_count.setter
    def plex_count(self, val):
        if val != None:
            self.validate('plex_count', val)
        self._plex_count = val
    
    _maxfiles_used = None
    @property
    def maxfiles_used(self):
        """
        The count of the number of files currently in use on
        the referenced file system. Range: [0 - 2^32-1]
        """
        return self._maxfiles_used
    @maxfiles_used.setter
    def maxfiles_used(self, val):
        if val != None:
            self.validate('maxfiles_used', val)
        self._maxfiles_used = val
    
    _sis_saved_space = None
    @property
    def sis_saved_space(self):
        """
        The total disk space in KBytes that is saved
        by storing only one copy of the duplicated
        blocks on the referenced file system. Range: [0 - 2^64-1]
        """
        return self._sis_saved_space
    @sis_saved_space.setter
    def sis_saved_space(self, val):
        if val != None:
            self.validate('sis_saved_space', val)
        self._sis_saved_space = val
    
    _maxfiles_possible = None
    @property
    def maxfiles_possible(self):
        """
        The largest value to which the maxfiles-available
        parameter can be increased by reconfiguration
        on the referenced file system. Range: [0 - 2^32-1]
        """
        return self._maxfiles_possible
    @maxfiles_possible.setter
    def maxfiles_possible(self, val):
        if val != None:
            self.validate('maxfiles_possible', val)
        self._maxfiles_possible = val
    
    _inodes_free = None
    @property
    def inodes_free(self):
        """
        The total number of free inodes on the referenced
        file system. Range: [0 - 2^32-1]
        """
        return self._inodes_free
    @inodes_free.setter
    def inodes_free(self, val):
        if val != None:
            self.validate('inodes_free', val)
        self._inodes_free = val
    
    _sis_shared_space = None
    @property
    def sis_shared_space(self):
        """
        The total amount of data in KBytes that is
        shared by more that one instance on the
        referenced file system. Range: [0 - 2^64-1]
        """
        return self._sis_shared_space
    @sis_shared_space.setter
    def sis_shared_space(self, val):
        if val != None:
            self.validate('sis_shared_space', val)
        self._sis_shared_space = val
    
    _total_bytes_saved = None
    @property
    def total_bytes_saved(self):
        """
        Total space saved in bytes in the volume due to deduplication,
        compression, and file cloning. Range: [0 - 2^64-1]
        """
        return self._total_bytes_saved
    @total_bytes_saved.setter
    def total_bytes_saved(self, val):
        if val != None:
            self.validate('total_bytes_saved', val)
        self._total_bytes_saved = val
    
    _compression_percent_saved = None
    @property
    def compression_percent_saved(self):
        """
        Percentage of the total disk space that is saved by
        compressing blocks on the referenced filesystem.
        Range: [0 - 100]
        """
        return self._compression_percent_saved
    @compression_percent_saved.setter
    def compression_percent_saved(self, val):
        if val != None:
            self.validate('compression_percent_saved', val)
        self._compression_percent_saved = val
    
    _mounted_on = None
    @property
    def mounted_on(self):
        """
        The name of the file on which this file
        system is mounted.
        """
        return self._mounted_on
    @mounted_on.setter
    def mounted_on(self, val):
        if val != None:
            self.validate('mounted_on', val)
        self._mounted_on = val
    
    _maxfiles_available = None
    @property
    def maxfiles_available(self):
        """
        The count of the maximum number of files allowable
        on the referenced file system. Range: [0 - 2^32-1]
        """
        return self._maxfiles_available
    @maxfiles_available.setter
    def maxfiles_available(self, val):
        if val != None:
            self.validate('maxfiles_available', val)
        self._maxfiles_available = val
    
    _total_space = None
    @property
    def total_space(self):
        """
        The total capacity in KBytes for the
        referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._total_space
    @total_space.setter
    def total_space(self, val):
        if val != None:
            self.validate('total_space', val)
        self._total_space = val
    
    @staticmethod
    def get_api_name():
          return "disk-filesys-usage-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'used-space',
            'percent-saved',
            'total-percent-saved',
            'total-reserved-space',
            'filesys-name',
            'mirror-status',
            'percent-used-capacity',
            'inodes-used',
            'available-space',
            'type',
            'compression-bytes-saved',
            'percent-inode-capacity',
            'plex-count',
            'maxfiles-used',
            'sis-saved-space',
            'maxfiles-possible',
            'inodes-free',
            'sis-shared-space',
            'total-bytes-saved',
            'compression-percent-saved',
            'mounted-on',
            'maxfiles-available',
            'total-space',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'used_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'percent_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_percent_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_reserved_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'filesys_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mirror_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_used_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodes_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'available_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'compression_bytes_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'percent_inode_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'plex_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'maxfiles_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'sis_saved_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'maxfiles_possible': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodes_free': { 'class': int, 'is_list': False, 'required': 'required' },
            'sis_shared_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_bytes_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'compression_percent_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'mounted_on': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'maxfiles_available': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_space': { 'class': int, 'is_list': False, 'required': 'required' },
        }
