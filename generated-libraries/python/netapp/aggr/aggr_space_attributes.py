from netapp.netapp_object import NetAppObject

class AggrSpaceAttributes(NetAppObject):
    """
    A structure returning space-related information for
    a given aggregate's Active File System (AFS).
    """
    
    _hybrid_cache_size_total = None
    @property
    def hybrid_cache_size_total(self):
        """
        [not settable, online-only]
        Total cache size (in bytes) in a hybrid aggregate. If
        the referenced aggregate is restricted or offline, or
        if it is not a hybrid aggregate, a value of 0 is returned.
        """
        return self._hybrid_cache_size_total
    @hybrid_cache_size_total.setter
    def hybrid_cache_size_total(self, val):
        if val != None:
            self.validate('hybrid_cache_size_total', val)
        self._hybrid_cache_size_total = val
    
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
    
    _used_including_snapshot_reserve = None
    @property
    def used_including_snapshot_reserve(self):
        """
        This field represents space used by the aggregate
        including the aggregate's Snapshot reserve in bytes
        Range : [0..2^64-1]
        """
        return self._used_including_snapshot_reserve
    @used_including_snapshot_reserve.setter
    def used_including_snapshot_reserve(self, val):
        if val != None:
            self.validate('used_including_snapshot_reserve', val)
        self._used_including_snapshot_reserve = val
    
    _total_reserved_space = None
    @property
    def total_reserved_space(self):
        """
        [not settable, online-only]
        The total disk space in bytes that is reserved on the referenced
        file system. The reserved space is already counted in the used space,
        so this element can be used to see what portion of the used space
        represents space reserved for future use.
        """
        return self._total_reserved_space
    @total_reserved_space.setter
    def total_reserved_space(self, val):
        if val != None:
            self.validate('total_reserved_space', val)
        self._total_reserved_space = val
    
    _aggregate_metadata = None
    @property
    def aggregate_metadata(self):
        """
        This field represents space used by filesystem metadata
        of the aggregate.
        Range : [0..2^64-1]
        """
        return self._aggregate_metadata
    @aggregate_metadata.setter
    def aggregate_metadata(self, val):
        if val != None:
            self.validate('aggregate_metadata', val)
        self._aggregate_metadata = val
    
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
        Total size (in bytes) of the referenced file system  . If
        the referenced file system is restricted or offline, a
        value of 0 is returned.
        """
        return self._size_total
    @size_total.setter
    def size_total(self, val):
        if val != None:
            self.validate('size_total', val)
        self._size_total = val
    
    _volume_footprints = None
    @property
    def volume_footprints(self):
        """
        This field represents space used by the sum of all data
        and metadata of all Volumes in the
        aggregate.
        Range : [0..2^64-1]
        """
        return self._volume_footprints
    @volume_footprints.setter
    def volume_footprints(self, val):
        if val != None:
            self.validate('volume_footprints', val)
        self._volume_footprints = val
    
    @staticmethod
    def get_api_name():
          return "aggr-space-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hybrid-cache-size-total',
            'size-available',
            'used-including-snapshot-reserve',
            'total-reserved-space',
            'aggregate-metadata',
            'size-used',
            'percent-used-capacity',
            'size-total',
            'volume-footprints',
        ]
    
    def describe_properties(self):
        return {
            'hybrid_cache_size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'used_including_snapshot_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_reserved_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'aggregate_metadata': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_used_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_footprints': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
