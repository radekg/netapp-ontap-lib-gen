from netapp.netapp_object import NetAppObject

class VolumeSpaceAttributes(NetAppObject):
    """
    Information about volume space management-related settings
    including on-disk layout.
    """
    
    _percentage_snapshot_reserve_used = None
    @property
    def percentage_snapshot_reserve_used(self):
        """
        Percentage of the volume reserved for snapshots that has
        been used. Note that in some scenarios, it is possible to
        pass 100% of the space allocated.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percentage_snapshot_reserve_used
    @percentage_snapshot_reserve_used.setter
    def percentage_snapshot_reserve_used(self, val):
        if val != None:
            self.validate('percentage_snapshot_reserve_used', val)
        self._percentage_snapshot_reserve_used = val
    
    _percentage_size_used = None
    @property
    def percentage_size_used(self):
        """
        Percentage of the volume size that is used.  This field
        is valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percentage_size_used
    @percentage_size_used.setter
    def percentage_size_used(self, val):
        if val != None:
            self.validate('percentage_size_used', val)
        self._percentage_size_used = val
    
    _filesystem_size = None
    @property
    def filesystem_size(self):
        """
        Filesystem size (in bytes) of the volume.  This is the
        total usable size of the volume, not including WAFL
        reserve.  This value is the same as Size except for
        certain SnapMirror destination volumes.  It is possible
        for destination volumes to have a different
        filesystem-size because the filesystem-size is sent
        across from the source volume.  This field is valid only
        when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._filesystem_size
    @filesystem_size.setter
    def filesystem_size(self, val):
        if val != None:
            self.validate('filesystem_size', val)
        self._filesystem_size = val
    
    _overwrite_reserve_required = None
    @property
    def overwrite_reserve_required(self):
        """
        The reserved size (in bytes) that is required to ensure
        that the reserved space is sufficient to allow all
        space-reserved files and LUNs to be overwritten when the
        volume is full. This field is valid only when the volume
        is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._overwrite_reserve_required
    @overwrite_reserve_required.setter
    def overwrite_reserve_required(self, val):
        if val != None:
            self.validate('overwrite_reserve_required', val)
        self._overwrite_reserve_required = val
    
    _size = None
    @property
    def size(self):
        """
        Filesystem size (in bytes) of the volume.  This is the
        total usable size of the volume, not including WAFL
        reserve.
        <p>
        This field can not be set on Infinite Volumes that are
        managed by storage services.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    _percentage_fractional_reserve = None
    @property
    def percentage_fractional_reserve(self):
        """
        This field can be used to change the amount of space
        reserved for overwrites of reserved objects (e.g., files,
        LUNs) in a volume.  This field is expressed as a
        percent.
        <p>
        By default, it is set to 100, indicating that 100% of the
        required reserved space will actually be reserved so the
        objects are fully protected for overwrites.
        <p>
        Using a value of less than 100 indicates the percentage
        of the required reserved space should actually be
        reserved.  This returns the extra space to the available
        space for the volume, decreasing the total amount of
        space used. However, this does leave the protected
        objects in the volume vulnerable to out of space errors,
        since less than 100% of the required reserved space is
        actually reserved.  If reserved space becomes exhausted,
        this will cause disruptions on the hosts using the
        objects.  If the percentage is decreased below 100%, it
        is highly recommended that the administrator actively
        monitor the space usage on the volume and take corrective
        action if the reserved space nears exhaustion.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._percentage_fractional_reserve
    @percentage_fractional_reserve.setter
    def percentage_fractional_reserve(self, val):
        if val != None:
            self.validate('percentage_fractional_reserve', val)
        self._percentage_fractional_reserve = val
    
    _size_available = None
    @property
    def size_available(self):
        """
        The size (in bytes) that is still available in the
        volume. This field is valid only when the volume is
        online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._size_available
    @size_available.setter
    def size_available(self, val):
        if val != None:
            self.validate('size_available', val)
        self._size_available = val
    
    _space_mgmt_option_try_first = None
    @property
    def space_mgmt_option_try_first(self):
        """
        This field controls the strategy to try first when this
        volume is space-challenged.
        <p>
        There are two available settings:
        <ul>
        <li> 'volume_grow' ... (default setting) Causes the
        volume to increase in size before deleting snapshots,
        <li> 'snap_delete' ... Causes snapshots to be deleted
        before the volume size is increased.
        </ul>
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._space_mgmt_option_try_first
    @space_mgmt_option_try_first.setter
    def space_mgmt_option_try_first(self, val):
        if val != None:
            self.validate('space_mgmt_option_try_first', val)
        self._space_mgmt_option_try_first = val
    
    _overwrite_reserve_used_actual = None
    @property
    def overwrite_reserve_used_actual(self):
        """
        The reserved size (in bytes) that has been used. This
        value is computed as the smaller of: (1) snapshotted size
        not in the active filesystem, and (2)
        'overwrite-reserve-used'. This formula comes from the
        observation that you cannot have used more overwrite
        reserved than have actually overwritten data. This value
        can exceed the value of 'overwrite-reserve-required', as
        the filer maintains a small hidden reserve of last
        resort. This field is valid only when the volume is
        online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._overwrite_reserve_used_actual
    @overwrite_reserve_used_actual.setter
    def overwrite_reserve_used_actual(self, val):
        if val != None:
            self.validate('overwrite_reserve_used_actual', val)
        self._overwrite_reserve_used_actual = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        The size (in bytes) that is used in the volume. This
        field is valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _overwrite_reserve_used = None
    @property
    def overwrite_reserve_used(self):
        """
        The reserved size (in bytes) that is not available for
        new overwrites. The number includes both the reserved
        size which has actually been used for overwrites as well
        as the size which was never allocated in the first place.
        On a volume without free space, the 'never allocated'
        component can become non-zero when
        'overwrite-reserve-required' increases as holes are
        filled in. Because of this, the 'overwrite-reserve-used'
        value can exceed the snapshotted size. The
        'overwrite-reserve-used' value can also exceed the value
        of 'overwrite-reserve-required', as the filer maintains a
        small hidden reserve of last resort. This field is valid
        only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._overwrite_reserve_used
    @overwrite_reserve_used.setter
    def overwrite_reserve_used(self, val):
        if val != None:
            self.validate('overwrite_reserve_used', val)
        self._overwrite_reserve_used = val
    
    _snapshot_reserve_size = None
    @property
    def snapshot_reserve_size(self):
        """
        The size (in bytes) in the volume that has been set aside
        as reserve for snapshot usage.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_reserve_size
    @snapshot_reserve_size.setter
    def snapshot_reserve_size(self, val):
        if val != None:
            self.validate('snapshot_reserve_size', val)
        self._snapshot_reserve_size = val
    
    _is_filesys_size_fixed = None
    @property
    def is_filesys_size_fixed(self):
        """
        If true, this field causes the file system to remain the
        same size (and not grow) when a SnapMirror relationship
        is broken.
        <p>
        This option is automatically set to 'true' when a volume
        becomes SnapMirrored.  It remains true after the
        SnapMirror relationship is broken for the volume.  This
        field allows a volume to be SnapMirrored back to the
        source without needing to grow the source volume.  If the
        volume size is larger than the file system size, setting
        this field to false forces the file system to grow to the
        size of the volume.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._is_filesys_size_fixed
    @is_filesys_size_fixed.setter
    def is_filesys_size_fixed(self, val):
        if val != None:
            self.validate('is_filesys_size_fixed', val)
        self._is_filesys_size_fixed = val
    
    _overwrite_reserve = None
    @property
    def overwrite_reserve(self):
        """
        The size (in bytes) that is reserved for overwriting
        snapshotted data in an otherwise full volume. This space
        is usable only by space-reserved LUNs and files, and then
        only when the volume is full. It is equal to
        'overwrite-reserve-required' if the value of
        'percentage-fractional-reserve' is set to the default
        value of 100%, but otherwise may be less than
        'overwrite-reserve-required'. This field is valid only
        when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._overwrite_reserve
    @overwrite_reserve.setter
    def overwrite_reserve(self, val):
        if val != None:
            self.validate('overwrite_reserve', val)
        self._overwrite_reserve = val
    
    _size_available_for_snapshots = None
    @property
    def size_available_for_snapshots(self):
        """
        Total free space (in bytes) available in the volume and
        the snapshot reserve. If this value is 0, a new snapshot
        cannot be created.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._size_available_for_snapshots
    @size_available_for_snapshots.setter
    def size_available_for_snapshots(self, val):
        if val != None:
            self.validate('size_available_for_snapshots', val)
        self._size_available_for_snapshots = val
    
    _percentage_snapshot_reserve = None
    @property
    def percentage_snapshot_reserve(self):
        """
        The percentage of volume disk space that has been set
        aside as reserve for snapshot usage.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._percentage_snapshot_reserve
    @percentage_snapshot_reserve.setter
    def percentage_snapshot_reserve(self, val):
        if val != None:
            self.validate('percentage_snapshot_reserve', val)
        self._percentage_snapshot_reserve = val
    
    _is_space_guarantee_enabled = None
    @property
    def is_space_guarantee_enabled(self):
        """
        Whether or not the storage guarantee associated with the
        flexible volume is currently in effect. This field is
        valid only if this is a flexible volume and it is
        online.
        <p>
        By default, space guarantee is enabled.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_space_guarantee_enabled
    @is_space_guarantee_enabled.setter
    def is_space_guarantee_enabled(self, val):
        if val != None:
            self.validate('is_space_guarantee_enabled', val)
        self._is_space_guarantee_enabled = val
    
    _space_guarantee = None
    @property
    def space_guarantee(self):
        """
        The storage guarantee option that is associated with the
        flexible volume.
        <p>
        Possible options:
        <ul>
        <li> 'none',
        <li> 'volume' (default option),
        <li> 'file'
        </ul>
        <p>
        This field is valid only if the volume is online. For
        data-cache volumes, this field is not returned.
        <p>
        This field can not be set on Infinite Volumes that are
        managed by storage services.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._space_guarantee
    @space_guarantee.setter
    def space_guarantee(self, val):
        if val != None:
            self.validate('space_guarantee', val)
        self._space_guarantee = val
    
    _size_used_by_snapshots = None
    @property
    def size_used_by_snapshots(self):
        """
        The size (in bytes) that is used by snapshots in the
        volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._size_used_by_snapshots
    @size_used_by_snapshots.setter
    def size_used_by_snapshots(self, val):
        if val != None:
            self.validate('size_used_by_snapshots', val)
        self._size_used_by_snapshots = val
    
    _space_nearly_full_threshold_percent = None
    @property
    def space_nearly_full_threshold_percent(self):
        """
        This field defines the used space threshold percentage at
        which EMS warnings regarding the volume fullness will be
        generated. The default value is 95%. Setting this
        threshold to 0 disables the volume nearly full space
        alerts.
        <p>
        This field is valid only if this is a flexible volume and
        it is online.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._space_nearly_full_threshold_percent
    @space_nearly_full_threshold_percent.setter
    def space_nearly_full_threshold_percent(self, val):
        if val != None:
            self.validate('space_nearly_full_threshold_percent', val)
        self._space_nearly_full_threshold_percent = val
    
    _space_full_threshold_percent = None
    @property
    def space_full_threshold_percent(self):
        """
        This field defines the used space threshold percentage at
        which EMS critical errors regarding the volume fullness
        will be generated. The default value is 98%. Setting this
        threshold to 0 disables the volume full space alerts.
        <p>
        This field is valid only if this is a flexible volume and
        it is online.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._space_full_threshold_percent
    @space_full_threshold_percent.setter
    def space_full_threshold_percent(self, val):
        if val != None:
            self.validate('space_full_threshold_percent', val)
        self._space_full_threshold_percent = val
    
    _size_total = None
    @property
    def size_total(self):
        """
        Total usable size (in bytes) of the volume, not including
        WAFL reserve or volume snapshot reserve.  This field is
        valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._size_total
    @size_total.setter
    def size_total(self, val):
        if val != None:
            self.validate('size_total', val)
        self._size_total = val
    
    @staticmethod
    def get_api_name():
          return "volume-space-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'percentage-snapshot-reserve-used',
            'percentage-size-used',
            'filesystem-size',
            'overwrite-reserve-required',
            'size',
            'percentage-fractional-reserve',
            'size-available',
            'space-mgmt-option-try-first',
            'overwrite-reserve-used-actual',
            'size-used',
            'overwrite-reserve-used',
            'snapshot-reserve-size',
            'is-filesys-size-fixed',
            'overwrite-reserve',
            'size-available-for-snapshots',
            'percentage-snapshot-reserve',
            'is-space-guarantee-enabled',
            'space-guarantee',
            'size-used-by-snapshots',
            'space-nearly-full-threshold-percent',
            'space-full-threshold-percent',
            'size-total',
        ]
    
    def describe_properties(self):
        return {
            'percentage_snapshot_reserve_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'filesystem_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'overwrite_reserve_required': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_fractional_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_mgmt_option_try_first': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'overwrite_reserve_used_actual': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'overwrite_reserve_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_reserve_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_filesys_size_fixed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'overwrite_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_available_for_snapshots': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_snapshot_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_space_guarantee_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'space_guarantee': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size_used_by_snapshots': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_nearly_full_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_full_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_total': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
