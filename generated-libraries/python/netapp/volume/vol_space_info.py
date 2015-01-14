from netapp.netapp_object import NetAppObject

class VolSpaceInfo(NetAppObject):
    """
    Space utilization details.
    """
    
    _user_data = None
    @property
    def user_data(self):
        """
        This field represents user data in bytes. If space is
        reserved to overwrite data in the volume, it is included
        in this value.
        """
        return self._user_data
    @user_data.setter
    def user_data(self, val):
        if val != None:
            self.validate('user_data', val)
        self._user_data = val
    
    _quota_metafiles = None
    @property
    def quota_metafiles(self):
        """
        This field represents space used by quota metafiles in
        bytes.
        """
        return self._quota_metafiles
    @quota_metafiles.setter
    def quota_metafiles(self, val):
        if val != None:
            self.validate('quota_metafiles', val)
        self._quota_metafiles = val
    
    _total_used = None
    @property
    def total_used(self):
        """
        This field represents the total used space in the volume
        in bytes. This value is based on user data, metadata
        that resides in the volume, and Snapshot reserve.
        """
        return self._total_used
    @total_used.setter
    def total_used(self, val):
        if val != None:
            self.validate('total_used', val)
        self._total_used = val
    
    _volume_size = None
    @property
    def volume_size(self):
        """
        This field represents the total volume size in bytes.
        """
        return self._volume_size
    @volume_size.setter
    def volume_size(self, val):
        if val != None:
            self.validate('volume_size', val)
        self._volume_size = val
    
    _dedupe_metafiles = None
    @property
    def dedupe_metafiles(self):
        """
        This field represents space used by deduplication
        metafiles in bytes.
        """
        return self._dedupe_metafiles
    @dedupe_metafiles.setter
    def dedupe_metafiles(self, val):
        if val != None:
            self.validate('dedupe_metafiles', val)
        self._dedupe_metafiles = val
    
    _snapshot_reserve = None
    @property
    def snapshot_reserve(self):
        """
        This field represents the size in bytes in the volume of
        space that has been set aside as a reserve for Snapshot
        usage.
        """
        return self._snapshot_reserve
    @snapshot_reserve.setter
    def snapshot_reserve(self, val):
        if val != None:
            self.validate('snapshot_reserve', val)
        self._snapshot_reserve = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _dedupe_metafiles_temporary = None
    @property
    def dedupe_metafiles_temporary(self):
        """
        This field represents space used by temporary
        deduplication metafiles in bytes.
        """
        return self._dedupe_metafiles_temporary
    @dedupe_metafiles_temporary.setter
    def dedupe_metafiles_temporary(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary', val)
        self._dedupe_metafiles_temporary = val
    
    _filesystem_metadata = None
    @property
    def filesystem_metadata(self):
        """
        This field represents volume filesystem metadata in
        bytes.
        """
        return self._filesystem_metadata
    @filesystem_metadata.setter
    def filesystem_metadata(self, val):
        if val != None:
            self.validate('filesystem_metadata', val)
        self._filesystem_metadata = val
    
    _snapshot_spill = None
    @property
    def snapshot_spill(self):
        """
        This field represents space used by Snapshot copies when
        it exceeds the size of the Snapshot reserve in bytes. It
        is computed as Snapshot used minus Snapshot reserve when
        Snapshot used exceeds Snapshot reserve.
        """
        return self._snapshot_spill
    @snapshot_spill.setter
    def snapshot_spill(self, val):
        if val != None:
            self.validate('snapshot_spill', val)
        self._snapshot_spill = val
    
    _snapmirror_metadata = None
    @property
    def snapmirror_metadata(self):
        """
        This field represents space used by metafiles during
        SnapMirror operations in bytes.
        """
        return self._snapmirror_metadata
    @snapmirror_metadata.setter
    def snapmirror_metadata(self, val):
        if val != None:
            self.validate('snapmirror_metadata', val)
        self._snapmirror_metadata = val
    
    _inodes = None
    @property
    def inodes(self):
        """
        This field represents space used by inode metadata in
        bytes.
        """
        return self._inodes
    @inodes.setter
    def inodes(self, val):
        if val != None:
            self.validate('inodes', val)
        self._inodes = val
    
    @staticmethod
    def get_api_name():
          return "vol-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-data',
            'quota-metafiles',
            'total-used',
            'volume-size',
            'dedupe-metafiles',
            'snapshot-reserve',
            'volume',
            'dedupe-metafiles-temporary',
            'filesystem-metadata',
            'snapshot-spill',
            'snapmirror-metadata',
            'inodes',
        ]
    
    def describe_properties(self):
        return {
            'user_data': { 'class': int, 'is_list': False, 'required': 'required' },
            'quota_metafiles': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'dedupe_metafiles': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_reserve': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'dedupe_metafiles_temporary': { 'class': int, 'is_list': False, 'required': 'required' },
            'filesystem_metadata': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapshot_spill': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapmirror_metadata': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodes': { 'class': int, 'is_list': False, 'required': 'required' },
        }
