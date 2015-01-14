from netapp.aggr.volume_space_info import VolumeSpaceInfo
from netapp.netapp_object import NetAppObject

class AggrSpaceInfo(NetAppObject):
    """
    List of aggregates and their space usage information.
    """
    
    _aggregate_name = None
    @property
    def aggregate_name(self):
        """
        Name of the aggregate.
        """
        return self._aggregate_name
    @aggregate_name.setter
    def aggregate_name(self, val):
        if val != None:
            self.validate('aggregate_name', val)
        self._aggregate_name = val
    
    _size_metadata = None
    @property
    def size_metadata(self):
        """
        Total space used by aggregates metadata.
        Range : [0..2^64-1]
        """
        return self._size_metadata
    @size_metadata.setter
    def size_metadata(self, val):
        if val != None:
            self.validate('size_metadata', val)
        self._size_metadata = val
    
    _size_volume_allocated = None
    @property
    def size_volume_allocated(self):
        """
        Total space allocated to volumes in the aggregate.
        Range : [0..2^64-1]
        """
        return self._size_volume_allocated
    @size_volume_allocated.setter
    def size_volume_allocated(self, val):
        if val != None:
            self.validate('size_volume_allocated', val)
        self._size_volume_allocated = val
    
    _size_nominal = None
    @property
    def size_nominal(self):
        """
        Total space contained in the aggreate minus the
        wafl reserve space.
        Range : [0..2^64-1]
        """
        return self._size_nominal
    @size_nominal.setter
    def size_nominal(self, val):
        if val != None:
            self.validate('size_nominal', val)
        self._size_nominal = val
    
    _size_image_backup_used = None
    @property
    def size_image_backup_used(self):
        """
        Space used by Image Backup metafiles.
        Range : [0..2^64-1]
        """
        return self._size_image_backup_used
    @size_image_backup_used.setter
    def size_image_backup_used(self, val):
        if val != None:
            self.validate('size_image_backup_used', val)
        self._size_image_backup_used = val
    
    _size_bssm_nvlog_used = None
    @property
    def size_bssm_nvlog_used(self):
        """
        Space used by bi-directional Synchronous SnapMirror
        for NVLOG files. This element will be returned only if
        the value is not zero.
        Range : [0..2^64-1]
        """
        return self._size_bssm_nvlog_used
    @size_bssm_nvlog_used.setter
    def size_bssm_nvlog_used(self, val):
        if val != None:
            self.validate('size_bssm_nvlog_used', val)
        self._size_bssm_nvlog_used = val
    
    _size_asis_used = None
    @property
    def size_asis_used(self):
        """
        Space used by A-SIS metafiles.
        Range : [0..2^64-1]
        """
        return self._size_asis_used
    @size_asis_used.setter
    def size_asis_used(self, val):
        if val != None:
            self.validate('size_asis_used', val)
        self._size_asis_used = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        The total used space in the aggregate except the
        space used by snapshots.
        Range : [0..2^64-1]
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _size_snap_used = None
    @property
    def size_snap_used(self):
        """
        Space used by aggregate snapshots.
        Range : [0..2^64-1]
        """
        return self._size_snap_used
    @size_snap_used.setter
    def size_snap_used(self, val):
        if val != None:
            self.validate('size_snap_used', val)
        self._size_snap_used = val
    
    _volumes = None
    @property
    def volumes(self):
        """
        List of flexible volumes and their allocated space
        information.
        """
        return self._volumes
    @volumes.setter
    def volumes(self, val):
        if val != None:
            self.validate('volumes', val)
        self._volumes = val
    
    _size_free = None
    @property
    def size_free(self):
        """
        Total free space in the aggregate
        Range : [0..2^64-1]
        """
        return self._size_free
    @size_free.setter
    def size_free(self, val):
        if val != None:
            self.validate('size_free', val)
        self._size_free = val
    
    _volume_count = None
    @property
    def volume_count(self):
        """
        Count of online virtual volumes in the aggregate.
        Range : [0..2^64-1]
        """
        return self._volume_count
    @volume_count.setter
    def volume_count(self, val):
        if val != None:
            self.validate('volume_count', val)
        self._volume_count = val
    
    _size_volume_used = None
    @property
    def size_volume_used(self):
        """
        Total space used by volumes in the aggregate.
        Range : [0..2^64-1]
        """
        return self._size_volume_used
    @size_volume_used.setter
    def size_volume_used(self, val):
        if val != None:
            self.validate('size_volume_used', val)
        self._size_volume_used = val
    
    @staticmethod
    def get_api_name():
          return "aggr-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'aggregate-name',
            'size-metadata',
            'size-volume-allocated',
            'size-nominal',
            'size-image-backup-used',
            'size-bssm-nvlog-used',
            'size-asis-used',
            'size-used',
            'size-snap-used',
            'volumes',
            'size-free',
            'volume-count',
            'size-volume-used',
        ]
    
    def describe_properties(self):
        return {
            'aggregate_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'size_metadata': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_volume_allocated': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_nominal': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_image_backup_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_bssm_nvlog_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'size_asis_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_snap_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'volumes': { 'class': VolumeSpaceInfo, 'is_list': True, 'required': 'required' },
            'size_free': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'size_volume_used': { 'class': int, 'is_list': False, 'required': 'required' },
        }
