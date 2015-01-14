from netapp.netapp_object import NetAppObject

class SnapshotSpaceInfo(NetAppObject):
    """
    A structure returning consolidated size-related information for all snapshots
    of the given volume.
    """
    
    _snapshot_sis_percent_saved = None
    @property
    def snapshot_sis_percent_saved(self):
        """
        [not settable, online-only]
        The percentage of disk space saved by eliminating
        the duplicated blocks on the referenced file system.
        Range: [0...100]
        """
        return self._snapshot_sis_percent_saved
    @snapshot_sis_percent_saved.setter
    def snapshot_sis_percent_saved(self, val):
        if val != None:
            self.validate('snapshot_sis_percent_saved', val)
        self._snapshot_sis_percent_saved = val
    
    _snapshot_percent_used_capacity = None
    @property
    def snapshot_percent_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use on
        the referenced file system.
        Range: [0...100]
        """
        return self._snapshot_percent_used_capacity
    @snapshot_percent_used_capacity.setter
    def snapshot_percent_used_capacity(self, val):
        if val != None:
            self.validate('snapshot_percent_used_capacity', val)
        self._snapshot_percent_used_capacity = val
    
    _snapshot_size_used = None
    @property
    def snapshot_size_used(self):
        """
        [not settable, online-only]
        Number of bytes used in the referenced file system.
        If the referenced file system is restricted or offline, a
        value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_size_used
    @snapshot_size_used.setter
    def snapshot_size_used(self, val):
        if val != None:
            self.validate('snapshot_size_used', val)
        self._snapshot_size_used = val
    
    _snapshot_files_total = None
    @property
    def snapshot_files_total(self):
        """
        [settable, online-only]
        Total file (inode) count, i.e., current maximum
        number of files (inodes) that this referenced file
        system can currently hold. If the referenced file
        system is restricted or offline, a value of 0 is
        returned.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_files_total
    @snapshot_files_total.setter
    def snapshot_files_total(self, val):
        if val != None:
            self.validate('snapshot_files_total', val)
        self._snapshot_files_total = val
    
    _snapshot_maxfiles_used = None
    @property
    def snapshot_maxfiles_used(self):
        """
        [not settable, online-only]
        The count of the number of files currently in use on
        the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_maxfiles_used
    @snapshot_maxfiles_used.setter
    def snapshot_maxfiles_used(self, val):
        if val != None:
            self.validate('snapshot_maxfiles_used', val)
        self._snapshot_maxfiles_used = val
    
    _snapshot_files_used = None
    @property
    def snapshot_files_used(self):
        """
        [not settable, online-only]
        Number of files (inodes) used in the referenced file
        system. If the referenced file system is restricted
        or offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_files_used
    @snapshot_files_used.setter
    def snapshot_files_used(self, val):
        if val != None:
            self.validate('snapshot_files_used', val)
        self._snapshot_files_used = val
    
    _snapshot_size_total = None
    @property
    def snapshot_size_total(self):
        """
        [not settable, online-only]
        Total size (in bytes) of the referenced file system. If
        the referenced file system is restricted or offline, a
        value 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_size_total
    @snapshot_size_total.setter
    def snapshot_size_total(self, val):
        if val != None:
            self.validate('snapshot_size_total', val)
        self._snapshot_size_total = val
    
    _snapshot_size_available = None
    @property
    def snapshot_size_available(self):
        """
        [not settable, online-only]
        Number of bytes still available in the referenced file
        system. If the referenced file system is restricted or
        offline, a value of 0 is returned.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_size_available
    @snapshot_size_available.setter
    def snapshot_size_available(self, val):
        if val != None:
            self.validate('snapshot_size_available', val)
        self._snapshot_size_available = val
    
    _snapshot_maxfiles_available = None
    @property
    def snapshot_maxfiles_available(self):
        """
        [not settable, always]
        The count of the maximum number of files allowable
        on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_maxfiles_available
    @snapshot_maxfiles_available.setter
    def snapshot_maxfiles_available(self, val):
        if val != None:
            self.validate('snapshot_maxfiles_available', val)
        self._snapshot_maxfiles_available = val
    
    _snapshot_maxfiles_possible = None
    @property
    def snapshot_maxfiles_possible(self):
        """
        [not settable, always]
        The largest value to which the maxfiles-available
        parameter can be increased by reconfiguration,
        on the referenced file system. Range: [0 - 2^64-1]
        """
        return self._snapshot_maxfiles_possible
    @snapshot_maxfiles_possible.setter
    def snapshot_maxfiles_possible(self, val):
        if val != None:
            self.validate('snapshot_maxfiles_possible', val)
        self._snapshot_maxfiles_possible = val
    
    _snapshot_sis_saved_space = None
    @property
    def snapshot_sis_saved_space(self):
        """
        [not settable, online-only]
        The total disk space in bytes that is saved by storing
        only one copy of the duplicated blocks on the
        referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_sis_saved_space
    @snapshot_sis_saved_space.setter
    def snapshot_sis_saved_space(self, val):
        if val != None:
            self.validate('snapshot_sis_saved_space', val)
        self._snapshot_sis_saved_space = val
    
    _snapshot_percent_inode_used_capacity = None
    @property
    def snapshot_percent_inode_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use based
        on file (inode) count on the referenced file system.
        Range: [0...100]
        """
        return self._snapshot_percent_inode_used_capacity
    @snapshot_percent_inode_used_capacity.setter
    def snapshot_percent_inode_used_capacity(self, val):
        if val != None:
            self.validate('snapshot_percent_inode_used_capacity', val)
        self._snapshot_percent_inode_used_capacity = val
    
    _snapshot_sis_shared_space = None
    @property
    def snapshot_sis_shared_space(self):
        """
        [not settable, online-only]
        The amount of data in bytes that is shared by more
        than one instance on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._snapshot_sis_shared_space
    @snapshot_sis_shared_space.setter
    def snapshot_sis_shared_space(self, val):
        if val != None:
            self.validate('snapshot_sis_shared_space', val)
        self._snapshot_sis_shared_space = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snapshot-sis-percent-saved',
            'snapshot-percent-used-capacity',
            'snapshot-size-used',
            'snapshot-files-total',
            'snapshot-maxfiles-used',
            'snapshot-files-used',
            'snapshot-size-total',
            'snapshot-size-available',
            'snapshot-maxfiles-available',
            'snapshot-maxfiles-possible',
            'snapshot-sis-saved-space',
            'snapshot-percent-inode-used-capacity',
            'snapshot-sis-shared-space',
        ]
    
    def describe_properties(self):
        return {
            'snapshot_sis_percent_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_percent_used_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_files_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_maxfiles_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_files_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_size_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_maxfiles_available': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_maxfiles_possible': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_sis_saved_space': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_percent_inode_used_capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_sis_shared_space': { 'class': int, 'is_list': False, 'required': 'required' },
        }
