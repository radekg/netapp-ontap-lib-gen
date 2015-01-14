from netapp.netapp_object import NetAppObject

class FootprintInfo(NetAppObject):
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
    
    _total_footprint = None
    @property
    def total_footprint(self):
        """
        This field represents the total footprint in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._total_footprint
    @total_footprint.setter
    def total_footprint(self, val):
        if val != None:
            self.validate('total_footprint', val)
        self._total_footprint = val
    
    _snapmirror_destination_footprint = None
    @property
    def snapmirror_destination_footprint(self):
        """
        This field represents the SnapMirror destination
        footprint in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapmirror_destination_footprint
    @snapmirror_destination_footprint.setter
    def snapmirror_destination_footprint(self, val):
        if val != None:
            self.validate('snapmirror_destination_footprint', val)
        self._snapmirror_destination_footprint = val
    
    _dedupe_metafiles_footprint = None
    @property
    def dedupe_metafiles_footprint(self):
        """
        This field represents temporary deduplication metadata
        footprint in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_footprint
    @dedupe_metafiles_footprint.setter
    def dedupe_metafiles_footprint(self, val):
        if val != None:
            self.validate('dedupe_metafiles_footprint', val)
        self._dedupe_metafiles_footprint = val
    
    _tape_backup_metafiles_footprint_percent = None
    @property
    def tape_backup_metafiles_footprint_percent(self):
        """
        This field represents the tape backup metadata footprint
        as a percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._tape_backup_metafiles_footprint_percent
    @tape_backup_metafiles_footprint_percent.setter
    def tape_backup_metafiles_footprint_percent(self, val):
        if val != None:
            self.validate('tape_backup_metafiles_footprint_percent', val)
        self._tape_backup_metafiles_footprint_percent = val
    
    _tape_backup_metafiles_footprint = None
    @property
    def tape_backup_metafiles_footprint(self):
        """
        This fields represents the tape backup metadata footprint
        in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._tape_backup_metafiles_footprint
    @tape_backup_metafiles_footprint.setter
    def tape_backup_metafiles_footprint(self, val):
        if val != None:
            self.validate('tape_backup_metafiles_footprint', val)
        self._tape_backup_metafiles_footprint = val
    
    _volume_guarantee_footprint = None
    @property
    def volume_guarantee_footprint(self):
        """
        This field represents the volume guarantee footprint in
        bytes.
        Alternatively, it is the space reserved for future writes
        in the volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_guarantee_footprint
    @volume_guarantee_footprint.setter
    def volume_guarantee_footprint(self, val):
        if val != None:
            self.validate('volume_guarantee_footprint', val)
        self._volume_guarantee_footprint = val
    
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
    
    _snapmirror_destination_footprint_percent = None
    @property
    def snapmirror_destination_footprint_percent(self):
        """
        This field represents the SnapMirror destination
        footprint as a percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapmirror_destination_footprint_percent
    @snapmirror_destination_footprint_percent.setter
    def snapmirror_destination_footprint_percent(self, val):
        if val != None:
            self.validate('snapmirror_destination_footprint_percent', val)
        self._snapmirror_destination_footprint_percent = val
    
    _dedupe_metafiles_temporary_footprint_percent = None
    @property
    def dedupe_metafiles_temporary_footprint_percent(self):
        """
        This field represents deduplication metadata footprint as
        a percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_temporary_footprint_percent
    @dedupe_metafiles_temporary_footprint_percent.setter
    def dedupe_metafiles_temporary_footprint_percent(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary_footprint_percent', val)
        self._dedupe_metafiles_temporary_footprint_percent = val
    
    _volume_blocks_footprint = None
    @property
    def volume_blocks_footprint(self):
        """
        This field represents the footprint of blocks written to
        the volume in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_blocks_footprint
    @volume_blocks_footprint.setter
    def volume_blocks_footprint(self, val):
        if val != None:
            self.validate('volume_blocks_footprint', val)
        self._volume_blocks_footprint = val
    
    _flexvol_metadata_footprint = None
    @property
    def flexvol_metadata_footprint(self):
        """
        This field represents flexible volume metadata in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._flexvol_metadata_footprint
    @flexvol_metadata_footprint.setter
    def flexvol_metadata_footprint(self, val):
        if val != None:
            self.validate('flexvol_metadata_footprint', val)
        self._flexvol_metadata_footprint = val
    
    _volume_guarantee_footprint_percent = None
    @property
    def volume_guarantee_footprint_percent(self):
        """
        This field represents the volume guarantee footprint as a
        percentage of aggregate size.
        Alternatively, it is the percentage of space reserved for
        future writes in the volume.
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_guarantee_footprint_percent
    @volume_guarantee_footprint_percent.setter
    def volume_guarantee_footprint_percent(self, val):
        if val != None:
            self.validate('volume_guarantee_footprint_percent', val)
        self._volume_guarantee_footprint_percent = val
    
    _dedupe_metafiles_temporary_footprint = None
    @property
    def dedupe_metafiles_temporary_footprint(self):
        """
        This field represents temporary deduplication metadata
        footprint in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_temporary_footprint
    @dedupe_metafiles_temporary_footprint.setter
    def dedupe_metafiles_temporary_footprint(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary_footprint', val)
        self._dedupe_metafiles_temporary_footprint = val
    
    _delayed_free_footprint_percent = None
    @property
    def delayed_free_footprint_percent(self):
        """
        This field represents the delayed free blocks footprint
        as a percentage of aggregate size.
        This system is used to improve delete performance by
        batching delete requests.
        Attributes: non-creatable, non-modifiable
        """
        return self._delayed_free_footprint_percent
    @delayed_free_footprint_percent.setter
    def delayed_free_footprint_percent(self, val):
        if val != None:
            self.validate('delayed_free_footprint_percent', val)
        self._delayed_free_footprint_percent = val
    
    _flexvol_metadata_footprint_percent = None
    @property
    def flexvol_metadata_footprint_percent(self):
        """
        This field represents flexible volume metadata as a
        percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._flexvol_metadata_footprint_percent
    @flexvol_metadata_footprint_percent.setter
    def flexvol_metadata_footprint_percent(self, val):
        if val != None:
            self.validate('flexvol_metadata_footprint_percent', val)
        self._flexvol_metadata_footprint_percent = val
    
    _total_footprint_percent = None
    @property
    def total_footprint_percent(self):
        """
        This field represents the total footprint as a percentage
        of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._total_footprint_percent
    @total_footprint_percent.setter
    def total_footprint_percent(self, val):
        if val != None:
            self.validate('total_footprint_percent', val)
        self._total_footprint_percent = val
    
    _volume_blocks_footprint_percent = None
    @property
    def volume_blocks_footprint_percent(self):
        """
        This field represents the footprint of blocks written to
        the volume as a percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_blocks_footprint_percent
    @volume_blocks_footprint_percent.setter
    def volume_blocks_footprint_percent(self, val):
        if val != None:
            self.validate('volume_blocks_footprint_percent', val)
        self._volume_blocks_footprint_percent = val
    
    _dedupe_metafiles_footprint_percent = None
    @property
    def dedupe_metafiles_footprint_percent(self):
        """
        This field represents deduplication metadata footprint as
        a percentage of aggregate size.
        Attributes: non-creatable, non-modifiable
        """
        return self._dedupe_metafiles_footprint_percent
    @dedupe_metafiles_footprint_percent.setter
    def dedupe_metafiles_footprint_percent(self, val):
        if val != None:
            self.validate('dedupe_metafiles_footprint_percent', val)
        self._dedupe_metafiles_footprint_percent = val
    
    _delayed_free_footprint = None
    @property
    def delayed_free_footprint(self):
        """
        This field represents the delayed free blocks footprint
        in bytes.
        This system is used to improve delete performance by
        batching delete requests.
        Attributes: non-creatable, non-modifiable
        """
        return self._delayed_free_footprint
    @delayed_free_footprint.setter
    def delayed_free_footprint(self, val):
        if val != None:
            self.validate('delayed_free_footprint', val)
        self._delayed_free_footprint = val
    
    @staticmethod
    def get_api_name():
          return "footprint-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'total-footprint',
            'snapmirror-destination-footprint',
            'dedupe-metafiles-footprint',
            'tape-backup-metafiles-footprint-percent',
            'tape-backup-metafiles-footprint',
            'volume-guarantee-footprint',
            'vserver',
            'snapmirror-destination-footprint-percent',
            'dedupe-metafiles-temporary-footprint-percent',
            'volume-blocks-footprint',
            'flexvol-metadata-footprint',
            'volume-guarantee-footprint-percent',
            'dedupe-metafiles-temporary-footprint',
            'delayed-free-footprint-percent',
            'flexvol-metadata-footprint-percent',
            'total-footprint-percent',
            'volume-blocks-footprint-percent',
            'dedupe-metafiles-footprint-percent',
            'delayed-free-footprint',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'total_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapmirror_destination_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'tape_backup_metafiles_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'tape_backup_metafiles_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_guarantee_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapmirror_destination_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_temporary_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_blocks_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_metadata_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_guarantee_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_temporary_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
            'delayed_free_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_metadata_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_blocks_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dedupe_metafiles_footprint_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'delayed_free_footprint': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
