from netapp.netapp_object import NetAppObject

class AggrSnapshotAttributes(NetAppObject):
    """
    A structure returning consolidated size-related
    information for all snapshots of the given aggregate.
    """
    
    _size_available = None
    @property
    def size_available(self):
        """
        [not settable, online-only]
        Number of bytes still available in the referenced file
        system. If the referenced file system is restricted or
        offline, a value of 0 is returned.
        """
        return self._size_available
    @size_available.setter
    def size_available(self, val):
        if val != None:
            self.validate('size_available', val)
        self._size_available = val
    
    _maxfiles_used = None
    @property
    def maxfiles_used(self):
        """
        [not settable, online-only]
        The count of the number of files currently in use on
        the referenced file system.
        """
        return self._maxfiles_used
    @maxfiles_used.setter
    def maxfiles_used(self, val):
        if val != None:
            self.validate('maxfiles_used', val)
        self._maxfiles_used = val
    
    _maxfiles_possible = None
    @property
    def maxfiles_possible(self):
        """
        [not settable, always]
        The largest value to which the maxfiles-available
        parameter can be increased by reconfiguration,
        on the referenced file system.
        """
        return self._maxfiles_possible
    @maxfiles_possible.setter
    def maxfiles_possible(self, val):
        if val != None:
            self.validate('maxfiles_possible', val)
        self._maxfiles_possible = val
    
    _is_snapshot_auto_create_enabled = None
    @property
    def is_snapshot_auto_create_enabled(self):
        """
        This option determines if auto snapshot is enabled on
        the aggregate. Default value is true.
        """
        return self._is_snapshot_auto_create_enabled
    @is_snapshot_auto_create_enabled.setter
    def is_snapshot_auto_create_enabled(self, val):
        if val != None:
            self.validate('is_snapshot_auto_create_enabled', val)
        self._is_snapshot_auto_create_enabled = val
    
    _maxfiles_available = None
    @property
    def maxfiles_available(self):
        """
        [not settable, always]
        The count of the maximum number of files allowable
        on the referenced file system.
        """
        return self._maxfiles_available
    @maxfiles_available.setter
    def maxfiles_available(self, val):
        if val != None:
            self.validate('maxfiles_available', val)
        self._maxfiles_available = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        [not settable, online-only]
        Number of bytes used in the referenced file system.
        If the referenced file system is restricted or offline, a
        value of 0 is returned.
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _files_total = None
    @property
    def files_total(self):
        """
        [settable, online-only]
        Total file (inode) count, i.e., current maximum
        number of files (inodes) that this referenced file
        system can currently hold. If the referenced file
        system is restricted or offline, a value of 0 is
        returned.
        """
        return self._files_total
    @files_total.setter
    def files_total(self, val):
        if val != None:
            self.validate('files_total', val)
        self._files_total = val
    
    _percent_used_capacity = None
    @property
    def percent_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use on
        the referenced file system.
        """
        return self._percent_used_capacity
    @percent_used_capacity.setter
    def percent_used_capacity(self, val):
        if val != None:
            self.validate('percent_used_capacity', val)
        self._percent_used_capacity = val
    
    _size_total = None
    @property
    def size_total(self):
        """
        [not settable, online-only]
        Total size (in bytes) of the referenced file system. If
        the referenced file system is restricted or offline, a
        value 0 is returned.
        """
        return self._size_total
    @size_total.setter
    def size_total(self, val):
        if val != None:
            self.validate('size_total', val)
        self._size_total = val
    
    _snapshot_reserve_percent = None
    @property
    def snapshot_reserve_percent(self):
        """
        The percentage of aggregate disk space that has been
        set aside as reserve for snapshot usage. Default value
        is 0.
        """
        return self._snapshot_reserve_percent
    @snapshot_reserve_percent.setter
    def snapshot_reserve_percent(self, val):
        if val != None:
            self.validate('snapshot_reserve_percent', val)
        self._snapshot_reserve_percent = val
    
    _percent_inode_used_capacity = None
    @property
    def percent_inode_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use based
        on file (inode) count on the referenced file system.
        """
        return self._percent_inode_used_capacity
    @percent_inode_used_capacity.setter
    def percent_inode_used_capacity(self, val):
        if val != None:
            self.validate('percent_inode_used_capacity', val)
        self._percent_inode_used_capacity = val
    
    _is_snapshot_auto_delete_enabled = None
    @property
    def is_snapshot_auto_delete_enabled(self):
        """
        This option determines if the snapshot auto delete is
        currently enabled for the aggregate. Default value is
        true.
        """
        return self._is_snapshot_auto_delete_enabled
    @is_snapshot_auto_delete_enabled.setter
    def is_snapshot_auto_delete_enabled(self, val):
        if val != None:
            self.validate('is_snapshot_auto_delete_enabled', val)
        self._is_snapshot_auto_delete_enabled = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        [not settable, online-only]
        Number of files (inodes) used in the referenced file
        system. If the referenced file system is restricted
        or offline, a value of 0 is returned.
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "aggr-snapshot-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'size-available',
            'maxfiles-used',
            'maxfiles-possible',
            'is-snapshot-auto-create-enabled',
            'maxfiles-available',
            'size-used',
            'files-total',
            'percent-used-capacity',
            'size-total',
            'snapshot-reserve-percent',
            'percent-inode-used-capacity',
            'is-snapshot-auto-delete-enabled',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'size_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maxfiles_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maxfiles_possible': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_snapshot_auto_create_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'maxfiles_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_used_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_reserve_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_inode_used_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_snapshot_auto_delete_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
