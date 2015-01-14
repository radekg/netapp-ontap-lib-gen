from netapp.netapp_object import NetAppObject

class VolumeSnapshotAttributes(NetAppObject):
    """
    Information about snapshot-related attributes in a volume.
    Volume disk space-related settings are excluded.
    """
    
    _snapshot_clone_dependency_enabled = None
    @property
    def snapshot_clone_dependency_enabled(self):
        """
        Controls the locking of LUN clones.
        <p>
        If true, all initial and intermediate backing snapshots
        are unlocked for all inactive LUN clones. For active LUN
        clones, only the backing snapshot will be locked.
        <p>
        If false, the backing snapshot will remain locked until
        all intermediate backing snapshots are deleted.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._snapshot_clone_dependency_enabled
    @snapshot_clone_dependency_enabled.setter
    def snapshot_clone_dependency_enabled(self, val):
        if val != None:
            self.validate('snapshot_clone_dependency_enabled', val)
        self._snapshot_clone_dependency_enabled = val
    
    _snapshot_policy = None
    @property
    def snapshot_policy(self):
        """
        The name of the snapshot policy.
        <p>
        The default policy name is 'default'.
        <p>
        This policy can be created using the
        'snapshot-policy-create' API. It can be managed using the
        'snapshot-policy-*' APIs.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._snapshot_policy
    @snapshot_policy.setter
    def snapshot_policy(self, val):
        if val != None:
            self.validate('snapshot_policy', val)
        self._snapshot_policy = val
    
    _auto_snapshots_enabled = None
    @property
    def auto_snapshots_enabled(self):
        """
        If true, enable automatic snapshots on the volume.
        <p>
        The default value is true.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._auto_snapshots_enabled
    @auto_snapshots_enabled.setter
    def auto_snapshots_enabled(self, val):
        if val != None:
            self.validate('auto_snapshots_enabled', val)
        self._auto_snapshots_enabled = val
    
    _snapshot_count = None
    @property
    def snapshot_count(self):
        """
        Number of Snapshot copies in the volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_count
    @snapshot_count.setter
    def snapshot_count(self, val):
        if val != None:
            self.validate('snapshot_count', val)
        self._snapshot_count = val
    
    _snapdir_access_enabled = None
    @property
    def snapdir_access_enabled(self):
        """
        If true, enable the visible '.snapshot' directory that is
        normally present at system internal mount points.  This
        value also turns on access to all other '.snapshot'
        directories in the volume.
        <p>
        The default value is true.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._snapdir_access_enabled
    @snapdir_access_enabled.setter
    def snapdir_access_enabled(self, val):
        if val != None:
            self.validate('snapdir_access_enabled', val)
        self._snapdir_access_enabled = val
    
    @staticmethod
    def get_api_name():
          return "volume-snapshot-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snapshot-clone-dependency-enabled',
            'snapshot-policy',
            'auto-snapshots-enabled',
            'snapshot-count',
            'snapdir-access-enabled',
        ]
    
    def describe_properties(self):
        return {
            'snapshot_clone_dependency_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snapshot_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'auto_snapshots_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snapshot_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapdir_access_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
