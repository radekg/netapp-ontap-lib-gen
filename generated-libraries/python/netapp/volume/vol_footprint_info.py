from netapp.netapp_object import NetAppObject

class VolFootprintInfo(NetAppObject):
    """
    Details of space utilization footprint in the hosting aggregate.
    """
    
    _total_footprint = None
    @property
    def total_footprint(self):
        """
        This field represents the total footprint in bytes. It
        is based on the sum of all of the components of the
        volume's footprint in its parent aggregate.
        """
        return self._total_footprint
    @total_footprint.setter
    def total_footprint(self, val):
        if val != None:
            self.validate('total_footprint', val)
        self._total_footprint = val
    
    _volume_data_footprint = None
    @property
    def volume_data_footprint(self):
        """
        This field represents the footprint of data written to
        the volume in bytes.
        """
        return self._volume_data_footprint
    @volume_data_footprint.setter
    def volume_data_footprint(self, val):
        if val != None:
            self.validate('volume_data_footprint', val)
        self._volume_data_footprint = val
    
    _flexvol_metadata_footprint = None
    @property
    def flexvol_metadata_footprint(self):
        """
        This field represents flexible volume metadata in bytes.
        """
        return self._flexvol_metadata_footprint
    @flexvol_metadata_footprint.setter
    def flexvol_metadata_footprint(self, val):
        if val != None:
            self.validate('flexvol_metadata_footprint', val)
        self._flexvol_metadata_footprint = val
    
    _tape_backup_metafiles_footprint = None
    @property
    def tape_backup_metafiles_footprint(self):
        """
        This fields represents the tape backup metadata
        footprint in bytes.
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
        bytes. Alternatively, it is the space reserved for
        future writes in the volume.
        """
        return self._volume_guarantee_footprint
    @volume_guarantee_footprint.setter
    def volume_guarantee_footprint(self, val):
        if val != None:
            self.validate('volume_guarantee_footprint', val)
        self._volume_guarantee_footprint = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _dedupe_metafiles_footprint = None
    @property
    def dedupe_metafiles_footprint(self):
        """
        This field represents temporary deduplication metadata
        footprint in bytes.
        """
        return self._dedupe_metafiles_footprint
    @dedupe_metafiles_footprint.setter
    def dedupe_metafiles_footprint(self, val):
        if val != None:
            self.validate('dedupe_metafiles_footprint', val)
        self._dedupe_metafiles_footprint = val
    
    _snapmirror_destination_footprint = None
    @property
    def snapmirror_destination_footprint(self):
        """
        This field represents the SnapMirror destination
        footprint in bytes.
        """
        return self._snapmirror_destination_footprint
    @snapmirror_destination_footprint.setter
    def snapmirror_destination_footprint(self, val):
        if val != None:
            self.validate('snapmirror_destination_footprint', val)
        self._snapmirror_destination_footprint = val
    
    _dedupe_metafiles_temporary_footprint = None
    @property
    def dedupe_metafiles_temporary_footprint(self):
        """
        This field represents temporary deduplication metadata
        footprint in bytes.
        """
        return self._dedupe_metafiles_temporary_footprint
    @dedupe_metafiles_temporary_footprint.setter
    def dedupe_metafiles_temporary_footprint(self, val):
        if val != None:
            self.validate('dedupe_metafiles_temporary_footprint', val)
        self._dedupe_metafiles_temporary_footprint = val
    
    _aggregate_size = None
    @property
    def aggregate_size(self):
        """
        This field represents the total aggregate size in bytes.
        """
        return self._aggregate_size
    @aggregate_size.setter
    def aggregate_size(self, val):
        if val != None:
            self.validate('aggregate_size', val)
        self._aggregate_size = val
    
    _delayed_free_footprint = None
    @property
    def delayed_free_footprint(self):
        """
        This field represents the delayed free footprint in
        bytes. This system is used to improve delete performance
        by batching delete requests.
        """
        return self._delayed_free_footprint
    @delayed_free_footprint.setter
    def delayed_free_footprint(self, val):
        if val != None:
            self.validate('delayed_free_footprint', val)
        self._delayed_free_footprint = val
    
    @staticmethod
    def get_api_name():
          return "vol-footprint-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'total-footprint',
            'volume-data-footprint',
            'flexvol-metadata-footprint',
            'tape-backup-metafiles-footprint',
            'volume-guarantee-footprint',
            'volume',
            'dedupe-metafiles-footprint',
            'snapmirror-destination-footprint',
            'dedupe-metafiles-temporary-footprint',
            'aggregate-size',
            'delayed-free-footprint',
        ]
    
    def describe_properties(self):
        return {
            'total_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_data_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'flexvol_metadata_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'tape_backup_metafiles_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_guarantee_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'dedupe_metafiles_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'snapmirror_destination_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'dedupe_metafiles_temporary_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
            'aggregate_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'delayed_free_footprint': { 'class': int, 'is_list': False, 'required': 'required' },
        }
