from netapp.netapp_object import NetAppObject

class VolumeSisAttributes(NetAppObject):
    """
    Statistics for Deduplication, file clone, compression, etc.
    """
    
    _total_space_saved = None
    @property
    def total_space_saved(self):
        """
        Total space saved (in bytes) in the volume due to
        deduplication, compression, and file cloning.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._total_space_saved
    @total_space_saved.setter
    def total_space_saved(self, val):
        if val != None:
            self.validate('total_space_saved', val)
        self._total_space_saved = val
    
    _deduplication_space_saved = None
    @property
    def deduplication_space_saved(self):
        """
        The total disk space (in bytes) that is saved by
        deduplication and file cloning.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._deduplication_space_saved
    @deduplication_space_saved.setter
    def deduplication_space_saved(self, val):
        if val != None:
            self.validate('deduplication_space_saved', val)
        self._deduplication_space_saved = val
    
    _deduplication_space_shared = None
    @property
    def deduplication_space_shared(self):
        """
        The total disk space shared due to deduplication and file
        cloning.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._deduplication_space_shared
    @deduplication_space_shared.setter
    def deduplication_space_shared(self, val):
        if val != None:
            self.validate('deduplication_space_shared', val)
        self._deduplication_space_shared = val
    
    _percentage_total_space_saved = None
    @property
    def percentage_total_space_saved(self):
        """
        Percentage of total disk space that is saved by
        compressing blocks, deduplication and file cloning.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percentage_total_space_saved
    @percentage_total_space_saved.setter
    def percentage_total_space_saved(self, val):
        if val != None:
            self.validate('percentage_total_space_saved', val)
        self._percentage_total_space_saved = val
    
    _is_sis_volume = None
    @property
    def is_sis_volume(self):
        """
        If true, it means that the volume contains shared
        (deduplication, file clones) or compressed data. If SIS
        is disabled, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_sis_volume
    @is_sis_volume.setter
    def is_sis_volume(self, val):
        if val != None:
            self.validate('is_sis_volume', val)
        self._is_sis_volume = val
    
    _percentage_deduplication_space_saved = None
    @property
    def percentage_deduplication_space_saved(self):
        """
        Percentage of the total disk space that is saved by
        deduplication and file cloning.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percentage_deduplication_space_saved
    @percentage_deduplication_space_saved.setter
    def percentage_deduplication_space_saved(self, val):
        if val != None:
            self.validate('percentage_deduplication_space_saved', val)
        self._percentage_deduplication_space_saved = val
    
    _compression_space_saved = None
    @property
    def compression_space_saved(self):
        """
        The total disk space (in bytes) that is saved by
        compressing blocks on the referenced file system.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._compression_space_saved
    @compression_space_saved.setter
    def compression_space_saved(self, val):
        if val != None:
            self.validate('compression_space_saved', val)
        self._compression_space_saved = val
    
    _percentage_compression_space_saved = None
    @property
    def percentage_compression_space_saved(self):
        """
        Percentage of the total disk space that is saved by
        compressing blocks on the referenced file system.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percentage_compression_space_saved
    @percentage_compression_space_saved.setter
    def percentage_compression_space_saved(self, val):
        if val != None:
            self.validate('percentage_compression_space_saved', val)
        self._percentage_compression_space_saved = val
    
    _is_sis_logging_enabled = None
    @property
    def is_sis_logging_enabled(self):
        """
        If true, it means that sis is enabled on the volume and
        fingerprints of newly-written data are being logged.
        <p>
        If SIS is enabled, this field is true. If SIS is
        disabled, this field is false.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_sis_logging_enabled
    @is_sis_logging_enabled.setter
    def is_sis_logging_enabled(self, val):
        if val != None:
            self.validate('is_sis_logging_enabled', val)
        self._is_sis_logging_enabled = val
    
    @staticmethod
    def get_api_name():
          return "volume-sis-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'total-space-saved',
            'deduplication-space-saved',
            'deduplication-space-shared',
            'percentage-total-space-saved',
            'is-sis-volume',
            'percentage-deduplication-space-saved',
            'compression-space-saved',
            'percentage-compression-space-saved',
            'is-sis-logging-enabled',
        ]
    
    def describe_properties(self):
        return {
            'total_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'deduplication_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'deduplication_space_shared': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_total_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_sis_volume': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'percentage_deduplication_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'compression_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_compression_space_saved': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_sis_logging_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
