from netapp.netapp_object import NetAppObject

class FsSpaceInfo(NetAppObject):
    """
    A structure returning size-related information for a given aggregate.
    """
    
    _fs_files_total = None
    @property
    def fs_files_total(self):
        """
        [settable, online-only]
        Total user-visible file (inode) count, i.e.,
        maximum number of user-visible files (inodes)
        that this referenced file system can currently
        hold. If the referenced file system is restricted
        or offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_files_total
    @fs_files_total.setter
    def fs_files_total(self, val):
        if val != None:
            self.validate('fs_files_total', val)
        self._fs_files_total = val
    
    _fs_maxfiles_used = None
    @property
    def fs_maxfiles_used(self):
        """
        [not settable, online-only]
        The number of user-visible files currently in use on
        the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._fs_maxfiles_used
    @fs_maxfiles_used.setter
    def fs_maxfiles_used(self, val):
        if val != None:
            self.validate('fs_maxfiles_used', val)
        self._fs_maxfiles_used = val
    
    _fs_size_available = None
    @property
    def fs_size_available(self):
        """
        [not settable, online-only]
        Number of bytes still available in the referenced file
        system. If the referenced file system is restricted or
        offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_size_available
    @fs_size_available.setter
    def fs_size_available(self, val):
        if val != None:
            self.validate('fs_size_available', val)
        self._fs_size_available = val
    
    _fs_sis_percent_saved = None
    @property
    def fs_sis_percent_saved(self):
        """
        [not settable, online-only]
        The percentage of disk space saved by eliminating
        the duplicated blocks on the referenced file system.
        Range: [0...100]
        """
        return self._fs_sis_percent_saved
    @fs_sis_percent_saved.setter
    def fs_sis_percent_saved(self, val):
        if val != None:
            self.validate('fs_sis_percent_saved', val)
        self._fs_sis_percent_saved = val
    
    _fs_percent_inode_used_capacity = None
    @property
    def fs_percent_inode_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use based
        on user-visible file (inode) count on the referenced
        file system.
        Range: [0...100]
        """
        return self._fs_percent_inode_used_capacity
    @fs_percent_inode_used_capacity.setter
    def fs_percent_inode_used_capacity(self, val):
        if val != None:
            self.validate('fs_percent_inode_used_capacity', val)
        self._fs_percent_inode_used_capacity = val
    
    _fs_sis_shared_space = None
    @property
    def fs_sis_shared_space(self):
        """
        [not settable, online-only]
        The amount of data in bytes that is shared by more
        than one instance on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._fs_sis_shared_space
    @fs_sis_shared_space.setter
    def fs_sis_shared_space(self, val):
        if val != None:
            self.validate('fs_sis_shared_space', val)
        self._fs_sis_shared_space = val
    
    _fs_maxfiles_possible = None
    @property
    def fs_maxfiles_possible(self):
        """
        [not settable, always]
        The largest value to which the fs-maxfiles-available
        parameter can be increased by reconfiguration,
        on the referenced file system. Range: [0 - 2^64-1]
        Range: [0 - 2^64-1]
        """
        return self._fs_maxfiles_possible
    @fs_maxfiles_possible.setter
    def fs_maxfiles_possible(self, val):
        if val != None:
            self.validate('fs_maxfiles_possible', val)
        self._fs_maxfiles_possible = val
    
    _fs_sis_saved_space = None
    @property
    def fs_sis_saved_space(self):
        """
        [not settable, online-only]
        The total disk space in bytes that is saved by storing
        only one copy of the duplicated blocks on the
        referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._fs_sis_saved_space
    @fs_sis_saved_space.setter
    def fs_sis_saved_space(self, val):
        if val != None:
            self.validate('fs_sis_saved_space', val)
        self._fs_sis_saved_space = val
    
    _fs_inodefile_public_capacity = None
    @property
    def fs_inodefile_public_capacity(self):
        """
        [not settable, online-only]
        Number of inodes that can currently be stored
        on disk for user-visible files.  This number
        will dynamically increase as more user-visible
        files are created.
        Range: [0 - 2^64-1]
        """
        return self._fs_inodefile_public_capacity
    @fs_inodefile_public_capacity.setter
    def fs_inodefile_public_capacity(self, val):
        if val != None:
            self.validate('fs_inodefile_public_capacity', val)
        self._fs_inodefile_public_capacity = val
    
    _fs_volume_footprints = None
    @property
    def fs_volume_footprints(self):
        """
        This field represents space used by the sum of all data
        and metadata of all volumes in the aggregate
        in bytes.
        Range : [0..2^64-1]
        """
        return self._fs_volume_footprints
    @fs_volume_footprints.setter
    def fs_volume_footprints(self, val):
        if val != None:
            self.validate('fs_volume_footprints', val)
        self._fs_volume_footprints = val
    
    _fs_size_total = None
    @property
    def fs_size_total(self):
        """
        [not settable, online-only]
        Total size (in bytes) of the referenced file system  . If
        the referenced file system is restricted or offline, a
        value 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_size_total
    @fs_size_total.setter
    def fs_size_total(self, val):
        if val != None:
            self.validate('fs_size_total', val)
        self._fs_size_total = val
    
    _fs_aggregate_metadata = None
    @property
    def fs_aggregate_metadata(self):
        """
        This field represents space used by filesystem metadata
        of the aggregate in bytes.
        Range : [0..2^64-1]
        """
        return self._fs_aggregate_metadata
    @fs_aggregate_metadata.setter
    def fs_aggregate_metadata(self, val):
        if val != None:
            self.validate('fs_aggregate_metadata', val)
        self._fs_aggregate_metadata = val
    
    _fs_total_reserved_space = None
    @property
    def fs_total_reserved_space(self):
        """
        [not settable, online-only]
        The total disk space in bytes that is reserved on the referenced
        file system. The reserved space is already counted in the used space,
        so this element can be used to see what portion of the used space
        represents space reserved for future use.
        Range: [0 - 2^64-1]
        """
        return self._fs_total_reserved_space
    @fs_total_reserved_space.setter
    def fs_total_reserved_space(self, val):
        if val != None:
            self.validate('fs_total_reserved_space', val)
        self._fs_total_reserved_space = val
    
    _fs_files_private_used = None
    @property
    def fs_files_private_used(self):
        """
        [not settable, online-only]
        Number of system (not user-visible) files (inodes)
        used.  If the referenced file system is restricted
        or offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_files_private_used
    @fs_files_private_used.setter
    def fs_files_private_used(self, val):
        if val != None:
            self.validate('fs_files_private_used', val)
        self._fs_files_private_used = val
    
    _fs_size_used = None
    @property
    def fs_size_used(self):
        """
        [not settable, online-only]
        Number of bytes used in the referenced file system.
        If the referenced file system is restricted or offline, a
        value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_size_used
    @fs_size_used.setter
    def fs_size_used(self, val):
        if val != None:
            self.validate('fs_size_used', val)
        self._fs_size_used = val
    
    _fs_hybrid_cache_size_total = None
    @property
    def fs_hybrid_cache_size_total(self):
        """
        [not settable, online-only]
        Total cache size (in bytes) in a hybrid aggregate. If
        the referenced aggregate is restricted or offline, or
        if it is not a hybrid aggregate, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_hybrid_cache_size_total
    @fs_hybrid_cache_size_total.setter
    def fs_hybrid_cache_size_total(self, val):
        if val != None:
            self.validate('fs_hybrid_cache_size_total', val)
        self._fs_hybrid_cache_size_total = val
    
    _fs_percent_used_capacity = None
    @property
    def fs_percent_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use on
        the referenced file system.
        Range: [0...100]
        """
        return self._fs_percent_used_capacity
    @fs_percent_used_capacity.setter
    def fs_percent_used_capacity(self, val):
        if val != None:
            self.validate('fs_percent_used_capacity', val)
        self._fs_percent_used_capacity = val
    
    _fs_inodefile_private_capacity = None
    @property
    def fs_inodefile_private_capacity(self):
        """
        [not settable, online-only]
        Number of inodes that can currently be stored
        on disk for system (not user-visible) files.
        This number will dynamically increase as more
        system files are created.
        Range: [0 - 2^64-1]
        """
        return self._fs_inodefile_private_capacity
    @fs_inodefile_private_capacity.setter
    def fs_inodefile_private_capacity(self, val):
        if val != None:
            self.validate('fs_inodefile_private_capacity', val)
        self._fs_inodefile_private_capacity = val
    
    _fs_files_used = None
    @property
    def fs_files_used(self):
        """
        [not settable, online-only]
        Number of user-visible files (inodes) used in the
        referenced file system. If the referenced file system
        is restricted or offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._fs_files_used
    @fs_files_used.setter
    def fs_files_used(self, val):
        if val != None:
            self.validate('fs_files_used', val)
        self._fs_files_used = val
    
    _fs_maxfiles_available = None
    @property
    def fs_maxfiles_available(self):
        """
        [not settable, always]
        The count of the maximum number of user-visible files
        currently allowable on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._fs_maxfiles_available
    @fs_maxfiles_available.setter
    def fs_maxfiles_available(self, val):
        if val != None:
            self.validate('fs_maxfiles_available', val)
        self._fs_maxfiles_available = val
    
    _fs_used_including_snapshot_reserve = None
    @property
    def fs_used_including_snapshot_reserve(self):
        """
        This field represents space used by the aggregate
        including the aggregate's Snapshot reserve
        in bytes.
        Range : [0..2^64-1]
        """
        return self._fs_used_including_snapshot_reserve
    @fs_used_including_snapshot_reserve.setter
    def fs_used_including_snapshot_reserve(self, val):
        if val != None:
            self.validate('fs_used_including_snapshot_reserve', val)
        self._fs_used_including_snapshot_reserve = val
    
    @staticmethod
    def get_api_name():
          return "fs-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fs-files-total',
            'fs-maxfiles-used',
            'fs-size-available',
            'fs-sis-percent-saved',
            'fs-percent-inode-used-capacity',
            'fs-sis-shared-space',
            'fs-maxfiles-possible',
            'fs-sis-saved-space',
            'fs-inodefile-public-capacity',
            'fs-volume-footprints',
            'fs-size-total',
            'fs-aggregate-metadata',
            'fs-total-reserved-space',
            'fs-files-private-used',
            'fs-size-used',
            'fs-hybrid-cache-size-total',
            'fs-percent-used-capacity',
            'fs-inodefile-private-capacity',
            'fs-files-used',
            'fs-maxfiles-available',
            'fs-used-including-snapshot-reserve',
        ]
    
    def describe_properties(self):
        return {
            'fs_files_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_maxfiles_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_size_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_sis_percent_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_percent_inode_used_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_sis_shared_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_maxfiles_possible': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_sis_saved_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_inodefile_public_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_volume_footprints': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_aggregate_metadata': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_total_reserved_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_files_private_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_hybrid_cache_size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_percent_used_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_inodefile_private_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_files_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_maxfiles_available': { 'class': int, 'is_list': False, 'required': 'required' },
            'fs_used_including_snapshot_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
