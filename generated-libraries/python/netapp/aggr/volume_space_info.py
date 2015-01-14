from netapp.netapp_object import NetAppObject

class VolumeSpaceInfo(NetAppObject):
    """
    List of flexible volumes in the aggregate and their
    space usage.
    """
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        Name of the volume
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _volume_used = None
    @property
    def volume_used(self):
        """
        Total space used by this volume.
        Range : [0..2^64-1]
        """
        return self._volume_used
    @volume_used.setter
    def volume_used(self, val):
        if val != None:
            self.validate('volume_used', val)
        self._volume_used = val
    
    _volume_allocated = None
    @property
    def volume_allocated(self):
        """
        Total space allocated for this volume in the
        aggregate.
        Range : [0..2^64-1]
        """
        return self._volume_allocated
    @volume_allocated.setter
    def volume_allocated(self, val):
        if val != None:
            self.validate('volume_allocated', val)
        self._volume_allocated = val
    
    _guarantee = None
    @property
    def guarantee(self):
        """
        Type of guarantee option set on this volume.
        Possible values: none, file, volume
        """
        return self._guarantee
    @guarantee.setter
    def guarantee(self, val):
        if val != None:
            self.validate('guarantee', val)
        self._guarantee = val
    
    @staticmethod
    def get_api_name():
          return "volume-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-name',
            'volume-used',
            'volume-allocated',
            'guarantee',
        ]
    
    def describe_properties(self):
        return {
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_used': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_allocated': { 'class': int, 'is_list': False, 'required': 'required' },
            'guarantee': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
