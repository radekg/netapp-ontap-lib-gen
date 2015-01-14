from netapp.netapp_object import NetAppObject

class VolumePerformanceAttributes(NetAppObject):
    """
    Information about performance settings on a volume.
    """
    
    _minimal_read_ahead = None
    @property
    def minimal_read_ahead(self):
        """
        If true, the node performs minimal read-ahead for the
        volume.
        <p>
        By default, this field is false, causing the node that
        contains this volume to perform very aggressive
        read-ahead.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._minimal_read_ahead
    @minimal_read_ahead.setter
    def minimal_read_ahead(self, val):
        if val != None:
            self.validate('minimal_read_ahead', val)
        self._minimal_read_ahead = val
    
    _max_write_alloc_blocks = None
    @property
    def max_write_alloc_blocks(self):
        """
        The maximum number of blocks used for write allocation.
        <p>
        This option is deprecated.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._max_write_alloc_blocks
    @max_write_alloc_blocks.setter
    def max_write_alloc_blocks(self, val):
        if val != None:
            self.validate('max_write_alloc_blocks', val)
        self._max_write_alloc_blocks = val
    
    _fc_delegs_enabled = None
    @property
    def fc_delegs_enabled(self):
        """
        If true, FlexCache Read Delegations are turned on for
        this volume.
        <p>
        On by default, only settable in Diag mode.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._fc_delegs_enabled
    @fc_delegs_enabled.setter
    def fc_delegs_enabled(self, val):
        if val != None:
            self.validate('fc_delegs_enabled', val)
        self._fc_delegs_enabled = val
    
    _is_atime_update_enabled = None
    @property
    def is_atime_update_enabled(self):
        """
        If false, prevent the update of inode access times when a
        file is read.
        <p>
        This value is useful for volumes with extremely high read
        traffic, since it prevents writes to the inode file for
        the volume from contending with reads from other files.
        <p>
        By default, this value is true.
        <p>
        This field should be used carefully.  That is, use this
        field when you know in advance that the correct access
        time for inodes will not be needed for files on that
        volume.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._is_atime_update_enabled
    @is_atime_update_enabled.setter
    def is_atime_update_enabled(self, val):
        if val != None:
            self.validate('is_atime_update_enabled', val)
        self._is_atime_update_enabled = val
    
    _read_realloc = None
    @property
    def read_realloc(self):
        """
        Controls whether application reads cause optimization of
        the layout of parts of a file or LUN after the data has
        been read from disk and is in the controller's memory.
        This optimization is only supported for flexible
        volumes.
        <p>
        The following values are recognized:
        <ul>
        <li> 'on'              ... Perform this optimization
        on this volume.  This option may duplicate blocks from
        snapshots into the active file system, thereby using
        additional disk space.  Read performance from snapshots
        will not be changed.
        <li> 'space_optimized' ... Perform this optimization
        on this volume, but do not duplicated blocks from
        snapshots into the active file system, thereby using
        space conservatively.  Read performance from snapshots
        may be degraded.
        <li> 'off'             ... Don't perform this
        optimization on this volume.
        </ul>
        <p>
        By default, it is set to 'off'.
        <p>
        Using read reallocation may help workloads that perform a
        mixture of random writes and large sequential reads.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._read_realloc
    @read_realloc.setter
    def read_realloc(self, val):
        if val != None:
            self.validate('read_realloc', val)
        self._read_realloc = val
    
    _extent_enabled = None
    @property
    def extent_enabled(self):
        """
        If turned on, this field enables extents in the volume.
        This causes application writes to be written in the
        volume as a write of a larger group of related data
        blocks called an extent.
        <p>
        The following values are recognized:
        <ul>
        <li> 'on'              ... Perform this optimization
        on this volume.  This option may duplicate blocks from
        snapshots into the active file system, thereby using
        additional disk space.  Read performance from snapshots
        will not be changed.
        <li> 'space_optimized' ... Perform this optimization
        on this volume, but do not duplicate blocks from
        snapshots into the active file system, thereby using
        space conservatively.  Read performance from snapshots
        may be degraded.
        <li> 'off'             ... Don't perform this
        optimization on this volume.
        </ul>
        <p>
        By default, it is set to 'off'.
        <p>
        Using extents may help workloads that perform many small
        random writes followed by a large sequential read.
        However, using extents may increase the number of disk
        operations performed on the controller, so this field
        should only be turned on when applicable.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._extent_enabled
    @extent_enabled.setter
    def extent_enabled(self, val):
        if val != None:
            self.validate('extent_enabled', val)
        self._extent_enabled = val
    
    @staticmethod
    def get_api_name():
          return "volume-performance-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'minimal-read-ahead',
            'max-write-alloc-blocks',
            'fc-delegs-enabled',
            'is-atime-update-enabled',
            'read-realloc',
            'extent-enabled',
        ]
    
    def describe_properties(self):
        return {
            'minimal_read_ahead': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_write_alloc_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fc_delegs_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_atime_update_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'read_realloc': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'extent_enabled': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
