from netapp.netapp_object import NetAppObject

class SpaceInfo(NetAppObject):
    """
    Space configuration info
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
    
    _total_used_percent = None
    @property
    def total_used_percent(self):
        """
        Total used space in the volume including snapshot reserve
        as a percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._total_used_percent
    @total_used_percent.setter
    def total_used_percent(self, val):
        if val != None:
            self.validate('total_used_percent', val)
        self._total_used_percent = val
    
    _snapshot_spill = None
    @property
    def snapshot_spill(self):
        """
        This field represents space used by Snapshot copies when
        it exceeds the size of the Snapshot reserve in bytes.
        It is computed as Snapshot used minus Snapshot reserve
        when Snapshot used exceeds Snapshot reserve.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_spill
    @snapshot_spill.setter
    def snapshot_spill(self, val):
        if val != None:
            self.validate('snapshot_spill', val)
        self._snapshot_spill = val
    
    _quota_metafiles_percent = None
    @property
    def quota_metafiles_percent(self):
        """
        This field represents space used by quota metafiles as a
        percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._quota_metafiles_percent
    @quota_metafiles_percent.setter
    def quota_metafiles_percent(self, val):
        if val != None:
            self.validate('quota_metafiles_percent', val)
        self._quota_metafiles_percent = val
    
    _filesystem_metadata_percent = None
    @property
    def filesystem_metadata_percent(self):
        """
        This field represents volume filesystem metadata as a
        percentage of volume size
        Attributes: non-creatable, non-modifiable
        """
        return self._filesystem_metadata_percent
    @filesystem_metadata_percent.setter
    def filesystem_metadata_percent(self, val):
        if val != None:
            self.validate('filesystem_metadata_percent', val)
        self._filesystem_metadata_percent = val
    
    _snapshot_reserve_percent = None
    @property
    def snapshot_reserve_percent(self):
        """
        This field represents the snapshot reserve as a
        percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_reserve_percent
    @snapshot_reserve_percent.setter
    def snapshot_reserve_percent(self, val):
        if val != None:
            self.validate('snapshot_reserve_percent', val)
        self._snapshot_reserve_percent = val
    
    _snapshot_reserve = None
    @property
    def snapshot_reserve(self):
        """
        The size (in bytes) in the volume that has been set aside
        as reserve for snapshot usage.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_reserve
    @snapshot_reserve.setter
    def snapshot_reserve(self, val):
        if val != None:
            self.validate('snapshot_reserve', val)
        self._snapshot_reserve = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the Vserver that contains the volumes for which
        the space usage is requested.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _filesystem_metadata = None
    @property
    def filesystem_metadata(self):
        """
        This field represents volume filesystem metadata in
        bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._filesystem_metadata
    @filesystem_metadata.setter
    def filesystem_metadata(self, val):
        if val != None:
            self.validate('filesystem_metadata', val)
        self._filesystem_metadata = val
    
    _dedupe_metafiles_temporary = None
    @property
    def dedupe_metafiles_temporary(self):
        """
        This field represents space used by temporary
        deduplication metafiles in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_temporary
    @dedupe_metafiles_temporary.setter
    def dedupe_metafiles_temporary(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary', val)
        self._dedupe_metafiles_temporary = val
    
    _user_data_percent = None
    @property
    def user_data_percent(self):
        """
        This field represents user data as a percentage of volume
        size.
        Attributes: non-creatable, non-modifiable
        """
        return self._user_data_percent
    @user_data_percent.setter
    def user_data_percent(self, val):
        if val != None:
            self.validate('user_data_percent', val)
        self._user_data_percent = val
    
    _inodes_percent = None
    @property
    def inodes_percent(self):
        """
        This field represents space used by inode metadata as a
        percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._inodes_percent
    @inodes_percent.setter
    def inodes_percent(self, val):
        if val != None:
            self.validate('inodes_percent', val)
        self._inodes_percent = val
    
    _tape_backup_metadata = None
    @property
    def tape_backup_metadata(self):
        """
        This fields represents the tape backup metadata in
        bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._tape_backup_metadata
    @tape_backup_metadata.setter
    def tape_backup_metadata(self, val):
        if val != None:
            self.validate('tape_backup_metadata', val)
        self._tape_backup_metadata = val
    
    _dedupe_metafiles_percent = None
    @property
    def dedupe_metafiles_percent(self):
        """
        This field represents space used by deduplication
        metafiles as a percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_percent
    @dedupe_metafiles_percent.setter
    def dedupe_metafiles_percent(self, val):
        if val != None:
            self.validate('dedupe_metafiles_percent', val)
        self._dedupe_metafiles_percent = val
    
    _user_data = None
    @property
    def user_data(self):
        """
        This field represents user data in bytes.
        Alternatively, this is the space reserved to overwrite
        the data in the volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._user_data
    @user_data.setter
    def user_data(self, val):
        if val != None:
            self.validate('user_data', val)
        self._user_data = val
    
    _dedupe_metafiles = None
    @property
    def dedupe_metafiles(self):
        """
        This field represents space used by deduplication
        metafiles in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles
    @dedupe_metafiles.setter
    def dedupe_metafiles(self, val):
        if val != None:
            self.validate('dedupe_metafiles', val)
        self._dedupe_metafiles = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume for which the space usage is
        requested.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _snapmirror_metadata_percent = None
    @property
    def snapmirror_metadata_percent(self):
        """
        This field represents space used by metafiles during
        SnapMirror operations as a percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapmirror_metadata_percent
    @snapmirror_metadata_percent.setter
    def snapmirror_metadata_percent(self, val):
        if val != None:
            self.validate('snapmirror_metadata_percent', val)
        self._snapmirror_metadata_percent = val
    
    _tape_backup_metadata_percent = None
    @property
    def tape_backup_metadata_percent(self):
        """
        This field represents the tape backup metadata as a
        percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._tape_backup_metadata_percent
    @tape_backup_metadata_percent.setter
    def tape_backup_metadata_percent(self, val):
        if val != None:
            self.validate('tape_backup_metadata_percent', val)
        self._tape_backup_metadata_percent = val
    
    _quota_metafiles = None
    @property
    def quota_metafiles(self):
        """
        This field represents space used by quota metafiles in
        bytes.
        Attributes: non-creatable, non-modifiable
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
        Total used space in the volume including snapshot reserve
        in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._total_used
    @total_used.setter
    def total_used(self, val):
        if val != None:
            self.validate('total_used', val)
        self._total_used = val
    
    _snapshot_spill_percent = None
    @property
    def snapshot_spill_percent(self):
        """
        This field represents Snapshot spill as a percentage of
        volume size.
        It is computed as Snapshot used minus Snapshot reserve
        when Snapshot used exceeds Snapshot reserve.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_spill_percent
    @snapshot_spill_percent.setter
    def snapshot_spill_percent(self, val):
        if val != None:
            self.validate('snapshot_spill_percent', val)
        self._snapshot_spill_percent = val
    
    _dedupe_metafiles_temporary_percent = None
    @property
    def dedupe_metafiles_temporary_percent(self):
        """
        This field represents space used by temporary
        deduplication metafiles as a percentage of volume size.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_temporary_percent
    @dedupe_metafiles_temporary_percent.setter
    def dedupe_metafiles_temporary_percent(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary_percent', val)
        self._dedupe_metafiles_temporary_percent = val
    
    _snapmirror_metadata = None
    @property
    def snapmirror_metadata(self):
        """
        This field represents space used by metafiles during
        SnapMirror operations in bytes.
        Attributes: non-creatable, non-modifiable
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
        Attributes: non-creatable, non-modifiable
        """
        return self._inodes
    @inodes.setter
    def inodes(self, val):
        if val != None:
            self.validate('inodes', val)
        self._inodes = val
    
    @staticmethod
    def get_api_name():
          return "space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'total-used-percent',
            'snapshot-spill',
            'quota-metafiles-percent',
            'filesystem-metadata-percent',
            'snapshot-reserve-percent',
            'snapshot-reserve',
            'vserver',
            'filesystem-metadata',
            'dedupe-metafiles-temporary',
            'user-data-percent',
            'inodes-percent',
            'tape-backup-metadata',
            'dedupe-metafiles-percent',
            'user-data',
            'dedupe-metafiles',
            'volume',
            'snapmirror-metadata-percent',
            'tape-backup-metadata-percent',
            'quota-metafiles',
            'total-used',
            'snapshot-spill-percent',
            'dedupe-metafiles-temporary-percent',
            'snapmirror-metadata',
            'inodes',
        ]
    
    def describe_properties(self):
        return {
            'total_used_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_spill': { 'class': int, 'is_list': False, 'required': 'optional' },
            'quota_metafiles_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'filesystem_metadata_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_reserve_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'filesystem_metadata': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_temporary': { 'class': int, 'is_list': False, 'required': 'optional' },
            'user_data_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodes_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'tape_backup_metadata': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'user_data': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapmirror_metadata_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'tape_backup_metadata_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'quota_metafiles': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_spill_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_temporary_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapmirror_metadata': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodes': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
