from netapp.netapp_object import NetAppObject

class VolumeCloneInfo(NetAppObject):
    """
    Volume FlexClone typedef
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
    
    _qos_policy_group_name = None
    @property
    def qos_policy_group_name(self):
        """
        QoS Policy Group Name
        Attributes: optional-for-create, non-modifiable
        """
        return self._qos_policy_group_name
    @qos_policy_group_name.setter
    def qos_policy_group_name(self, val):
        if val != None:
            self.validate('qos_policy_group_name', val)
        self._qos_policy_group_name = val
    
    _junction_path = None
    @property
    def junction_path(self):
        """
        Junction Path
        Attributes: optional-for-create, non-modifiable
        """
        return self._junction_path
    @junction_path.setter
    def junction_path(self, val):
        if val != None:
            self.validate('junction_path', val)
        self._junction_path = val
    
    _space_guarantee_enabled = None
    @property
    def space_guarantee_enabled(self):
        """
        Space Guarantee In Effect
        Attributes: non-creatable, non-modifiable
        """
        return self._space_guarantee_enabled
    @space_guarantee_enabled.setter
    def space_guarantee_enabled(self, val):
        if val != None:
            self.validate('space_guarantee_enabled', val)
        self._space_guarantee_enabled = val
    
    _size = None
    @property
    def size(self):
        """
        FlexClone Size
        Attributes: non-creatable, non-modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    _inodes_total = None
    @property
    def inodes_total(self):
        """
        Total Inodes
        Attributes: non-creatable, non-modifiable
        """
        return self._inodes_total
    @inodes_total.setter
    def inodes_total(self, val):
        if val != None:
            self.validate('inodes_total', val)
        self._inodes_total = val
    
    _parent_volume = None
    @property
    def parent_volume(self):
        """
        FlexClone Parent Volume
        Attributes: required-for-create, non-modifiable
        """
        return self._parent_volume
    @parent_volume.setter
    def parent_volume(self, val):
        if val != None:
            self.validate('parent_volume', val)
        self._parent_volume = val
    
    _blocks_updated = None
    @property
    def blocks_updated(self):
        """
        Blocks Updated
        Attributes: non-creatable, non-modifiable
        """
        return self._blocks_updated
    @blocks_updated.setter
    def blocks_updated(self, val):
        if val != None:
            self.validate('blocks_updated', val)
        self._blocks_updated = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _state = None
    @property
    def state(self):
        """
        FlexClone Volume State
        Possible values are:
        <ul>
        <li>'online',</li>
        <li>'offline',</li>
        <li>'restricted'.</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _inode_percentage_complete = None
    @property
    def inode_percentage_complete(self):
        """
        Percentage Complete
        Attributes: non-creatable, non-modifiable
        """
        return self._inode_percentage_complete
    @inode_percentage_complete.setter
    def inode_percentage_complete(self, val):
        if val != None:
            self.validate('inode_percentage_complete', val)
        self._inode_percentage_complete = val
    
    _junction_active = None
    @property
    def junction_active(self):
        """
        Junction Active
        Attributes: optional-for-create, non-modifiable
        """
        return self._junction_active
    @junction_active.setter
    def junction_active(self, val):
        if val != None:
            self.validate('junction_active', val)
        self._junction_active = val
    
    _volume_type = None
    @property
    def volume_type(self):
        """
        The type of the volume to be created.
        <p>
        Possible values:
        <ul>
        <li> 'rw' ... read-write volume,
        <li> 'dp' ... data-protection volume
        </ul>
        <p>
        Default value is 'rw'.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._volume_type
    @volume_type.setter
    def volume_type(self, val):
        if val != None:
            self.validate('volume_type', val)
        self._volume_type = val
    
    _msid = None
    @property
    def msid(self):
        """
        FlexClone Master Data Set ID
        Attributes: non-creatable, non-modifiable
        """
        return self._msid
    @msid.setter
    def msid(self, val):
        if val != None:
            self.validate('msid', val)
        self._msid = val
    
    _used = None
    @property
    def used(self):
        """
        Used Size
        Attributes: non-creatable, non-modifiable
        """
        return self._used
    @used.setter
    def used(self, val):
        if val != None:
            self.validate('used', val)
        self._used = val
    
    _volume = None
    @property
    def volume(self):
        """
        FlexClone Volume
        Attributes: key, required-for-create, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _blocks_scanned = None
    @property
    def blocks_scanned(self):
        """
        Blocks Scanned
        Attributes: non-creatable, non-modifiable
        """
        return self._blocks_scanned
    @blocks_scanned.setter
    def blocks_scanned(self, val):
        if val != None:
            self.validate('blocks_scanned', val)
        self._blocks_scanned = val
    
    _aggregate = None
    @property
    def aggregate(self):
        """
        FlexClone Aggregate
        Attributes: non-creatable, non-modifiable
        """
        return self._aggregate
    @aggregate.setter
    def aggregate(self, val):
        if val != None:
            self.validate('aggregate', val)
        self._aggregate = val
    
    _parent_snapshot = None
    @property
    def parent_snapshot(self):
        """
        FlexClone Parent Snapshot
        Attributes: optional-for-create, non-modifiable
        """
        return self._parent_snapshot
    @parent_snapshot.setter
    def parent_snapshot(self, val):
        if val != None:
            self.validate('parent_snapshot', val)
        self._parent_snapshot = val
    
    _inodes_processed = None
    @property
    def inodes_processed(self):
        """
        Inodes Processed
        Attributes: non-creatable, non-modifiable
        """
        return self._inodes_processed
    @inodes_processed.setter
    def inodes_processed(self, val):
        if val != None:
            self.validate('inodes_processed', val)
        self._inodes_processed = val
    
    _split_estimate = None
    @property
    def split_estimate(self):
        """
        Split Estimate
        Attributes: non-creatable, non-modifiable
        """
        return self._split_estimate
    @split_estimate.setter
    def split_estimate(self, val):
        if val != None:
            self.validate('split_estimate', val)
        self._split_estimate = val
    
    _space_reserve = None
    @property
    def space_reserve(self):
        """
        Space Guarantee Style
        Attributes: optional-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "none"      ,
        <li> "volume"    ,
        <li> "file"
        </ul>
        """
        return self._space_reserve
    @space_reserve.setter
    def space_reserve(self, val):
        if val != None:
            self.validate('space_reserve', val)
        self._space_reserve = val
    
    _dsid = None
    @property
    def dsid(self):
        """
        FlexClone Data Set ID
        Attributes: non-creatable, non-modifiable
        """
        return self._dsid
    @dsid.setter
    def dsid(self, val):
        if val != None:
            self.validate('dsid', val)
        self._dsid = val
    
    @staticmethod
    def get_api_name():
          return "volume-clone-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'qos-policy-group-name',
            'junction-path',
            'space-guarantee-enabled',
            'size',
            'inodes-total',
            'parent-volume',
            'blocks-updated',
            'vserver',
            'state',
            'inode-percentage-complete',
            'junction-active',
            'volume-type',
            'msid',
            'used',
            'volume',
            'blocks-scanned',
            'aggregate',
            'parent-snapshot',
            'inodes-processed',
            'split-estimate',
            'space-reserve',
            'dsid',
        ]
    
    def describe_properties(self):
        return {
            'qos_policy_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'junction_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'space_guarantee_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodes_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'parent_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'blocks_updated': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'inode_percentage_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'junction_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'volume_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'msid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'blocks_scanned': { 'class': int, 'is_list': False, 'required': 'optional' },
            'aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'parent_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'inodes_processed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'split_estimate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_reserve': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
