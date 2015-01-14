from netapp.snapshot.snapshot_owner import SnapshotOwner
from netapp.netapp_object import NetAppObject

class SnapshotInfo(NetAppObject):
    """
    One snapshot contained in the specified volume. This type is used
    by snapshot-get-iter, snapshot-modify-iter and snapshot-list-info
    ZAPIs. When using this type to modify snapshot information, every
    field except snapmirror-label is non-modifiable.
    """
    
    _volume_provenance_uuid = None
    @property
    def volume_provenance_uuid(self):
        """
        Provenance UUID of the volume at the time the snapshot
        was created. Refer to the volume-get-iter API for a
        description of the volume provenance UUID.
        """
        return self._volume_provenance_uuid
    @volume_provenance_uuid.setter
    def volume_provenance_uuid(self, val):
        if val != None:
            self.validate('volume_provenance_uuid', val)
        self._volume_provenance_uuid = val
    
    _total = None
    @property
    def total(self):
        """
        Number of 1024 byte blocks in the snapshot. If the
        "terse" input is true, this value is omitted.
        """
        return self._total
    @total.setter
    def total(self, val):
        if val != None:
            self.validate('total', val)
        self._total = val
    
    _snapshot_owners_list = None
    @property
    def snapshot_owners_list(self):
        """
        The list of owners of a busy snapshot.
        """
        return self._snapshot_owners_list
    @snapshot_owners_list.setter
    def snapshot_owners_list(self, val):
        if val != None:
            self.validate('snapshot_owners_list', val)
        self._snapshot_owners_list = val
    
    _busy = None
    @property
    def busy(self):
        """
        True if the snapshot is being used by an application.
        """
        return self._busy
    @busy.setter
    def busy(self, val):
        if val != None:
            self.validate('busy', val)
        self._busy = val
    
    _percentage_of_total_blocks = None
    @property
    def percentage_of_total_blocks(self):
        """
        Percentage of blocks owned by this snapshot, relative to
        the total number of blocks in the volume.
        """
        return self._percentage_of_total_blocks
    @percentage_of_total_blocks.setter
    def percentage_of_total_blocks(self, val):
        if val != None:
            self.validate('percentage_of_total_blocks', val)
        self._percentage_of_total_blocks = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the vserver to which this volume belongs.
        This field is returned only when request is sent to
        Admin Vserver LIF.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _cumulative_percentage_of_used_blocks = None
    @property
    def cumulative_percentage_of_used_blocks(self):
        """
        Percentage of blocks owned by this snapshot and all
        more recent snapshots, relative to the number of blocks
        currently used in the volume. Not returned for Infinite
        Volumes.
        """
        return self._cumulative_percentage_of_used_blocks
    @cumulative_percentage_of_used_blocks.setter
    def cumulative_percentage_of_used_blocks(self, val):
        if val != None:
            self.validate('cumulative_percentage_of_used_blocks', val)
        self._cumulative_percentage_of_used_blocks = val
    
    _state = None
    @property
    def state(self):
        """
        The state of the snapshot.
        Possible values:
        <ul>
        <li> 'valid' ... The snapshot is complete and consistent
        <li> 'invalid' ... The namespace constituent snapshot is missing
        <li> 'partial' ... One or more data constituent snapshots are missing
        </ul>
        Only a snapshot on an Infinite Volume can have a state of partial or invalid.
        <p>
        The default value is valid.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _is_7_mode_snapshot = None
    @property
    def is_7_mode_snapshot(self):
        """
        True if the snapshot is a 7-mode snapshot.
        """
        return self._is_7_mode_snapshot
    @is_7_mode_snapshot.setter
    def is_7_mode_snapshot(self, val):
        if val != None:
            self.validate('is_7_mode_snapshot', val)
        self._is_7_mode_snapshot = val
    
    _snapmirror_label = None
    @property
    def snapmirror_label(self):
        """
        A human readable SnapMirror Label attached with
        the snapshot. Size of the label can be at most 31
        characters. This label will be used by the
        vaulting system to identify a vaulting scheme.
        """
        return self._snapmirror_label
    @snapmirror_label.setter
    def snapmirror_label(self, val):
        if val != None:
            self.validate('snapmirror_label', val)
        self._snapmirror_label = val
    
    _access_time = None
    @property
    def access_time(self):
        """
        The volume access time when the snapshot was created
        in seconds since Jan 1, 1970.  This value will
        not change even if the snapshot is accessed.
        """
        return self._access_time
    @access_time.setter
    def access_time(self, val):
        if val != None:
            self.validate('access_time', val)
        self._access_time = val
    
    _volume = None
    @property
    def volume(self):
        """
        Volume name.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _percentage_of_used_blocks = None
    @property
    def percentage_of_used_blocks(self):
        """
        Percentage of blocks owned by this snapshot, relative to
        the number of blocks currently used in the volume.
        """
        return self._percentage_of_used_blocks
    @percentage_of_used_blocks.setter
    def percentage_of_used_blocks(self, val):
        if val != None:
            self.validate('percentage_of_used_blocks', val)
        self._percentage_of_used_blocks = val
    
    _snapshot_instance_uuid = None
    @property
    def snapshot_instance_uuid(self):
        """
        The 128 bit unique snapshot identifier expressed in
        the form of UUID.  This field uniquely identifies the
        snapshot's physical data layout.
        """
        return self._snapshot_instance_uuid
    @snapshot_instance_uuid.setter
    def snapshot_instance_uuid(self, val):
        if val != None:
            self.validate('snapshot_instance_uuid', val)
        self._snapshot_instance_uuid = val
    
    _contains_lun_clones = None
    @property
    def contains_lun_clones(self):
        """
        This snapshots contains lun clones.
        If true, this snapshot contains lun clones. This is
        available only if the 'lun-clone-snapshot' option is
        specified.
        """
        return self._contains_lun_clones
    @contains_lun_clones.setter
    def contains_lun_clones(self, val):
        if val != None:
            self.validate('contains_lun_clones', val)
        self._contains_lun_clones = val
    
    _cumulative_total = None
    @property
    def cumulative_total(self):
        """
        Cumulative total of 1024 byte blocks of
        this snapshot and previous snapshots. If the "terse"
        input is true, this value is omitted.
        """
        return self._cumulative_total
    @cumulative_total.setter
    def cumulative_total(self, val):
        if val != None:
            self.validate('cumulative_total', val)
        self._cumulative_total = val
    
    _is_constituent_snapshot = None
    @property
    def is_constituent_snapshot(self):
        """
        True if the snapshot is a constituent snapshot.
        """
        return self._is_constituent_snapshot
    @is_constituent_snapshot.setter
    def is_constituent_snapshot(self, val):
        if val != None:
            self.validate('is_constituent_snapshot', val)
        self._is_constituent_snapshot = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the snapshot to be listed.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _fs_block_format = None
    @property
    def fs_block_format(self):
        """
        Filesystem block format of the snapshot.
        Possible values: 32_bit, mixed, 64_bit.
        """
        return self._fs_block_format
    @fs_block_format.setter
    def fs_block_format(self, val):
        if val != None:
            self.validate('fs_block_format', val)
        self._fs_block_format = val
    
    _snapshot_version_uuid = None
    @property
    def snapshot_version_uuid(self):
        """
        The 128 bit unique snapshot identifier expressed in
        the form of UUID.  This field uniquely identifies the
        snapshot's logical data layout.
        """
        return self._snapshot_version_uuid
    @snapshot_version_uuid.setter
    def snapshot_version_uuid(self, val):
        if val != None:
            self.validate('snapshot_version_uuid', val)
        self._snapshot_version_uuid = val
    
    _dependency = None
    @property
    def dependency(self):
        """
        Application(s) dependent on this snapshot.
        Possible values include "snapmirror", "snapvault",
        "dump", "vclone", "LUNs", "snaplock".  Comma separated
        if more than one application depends on this snapshot.
        """
        return self._dependency
    @dependency.setter
    def dependency(self, val):
        if val != None:
            self.validate('dependency', val)
        self._dependency = val
    
    _cumulative_percentage_of_total_blocks = None
    @property
    def cumulative_percentage_of_total_blocks(self):
        """
        Percentage of blocks owned by this snapshot and all
        more recent snapshots, relative to the total number
        of blocks in the volume. Not returned for Infinite
        Volumes.
        """
        return self._cumulative_percentage_of_total_blocks
    @cumulative_percentage_of_total_blocks.setter
    def cumulative_percentage_of_total_blocks(self, val):
        if val != None:
            self.validate('cumulative_percentage_of_total_blocks', val)
        self._cumulative_percentage_of_total_blocks = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-provenance-uuid',
            'total',
            'snapshot-owners-list',
            'busy',
            'percentage-of-total-blocks',
            'vserver',
            'cumulative-percentage-of-used-blocks',
            'state',
            'is-7-mode-snapshot',
            'snapmirror-label',
            'access-time',
            'volume',
            'percentage-of-used-blocks',
            'snapshot-instance-uuid',
            'contains-lun-clones',
            'cumulative-total',
            'is-constituent-snapshot',
            'name',
            'fs-block-format',
            'snapshot-version-uuid',
            'dependency',
            'cumulative-percentage-of-total-blocks',
        ]
    
    def describe_properties(self):
        return {
            'volume_provenance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_owners_list': { 'class': SnapshotOwner, 'is_list': True, 'required': 'optional' },
            'busy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'percentage_of_total_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cumulative_percentage_of_used_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_7_mode_snapshot': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snapmirror_label': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'access_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'percentage_of_used_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_instance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'contains_lun_clones': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cumulative_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_constituent_snapshot': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fs_block_format': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapshot_version_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dependency': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cumulative_percentage_of_total_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
