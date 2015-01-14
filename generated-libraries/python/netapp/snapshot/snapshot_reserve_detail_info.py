from netapp.netapp_object import NetAppObject

class SnapshotReserveDetailInfo(NetAppObject):
    """
    Information about a volume's snapshot space reservation
    configuration.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        Name of volume.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
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
    
    _percentage = None
    @property
    def percentage(self):
        """
        Percentage of volume reserved for snapshots.
        Range : [0 - 100].
        """
        return self._percentage
    @percentage.setter
    def percentage(self, val):
        if val != None:
            self.validate('percentage', val)
        self._percentage = val
    
    _size = None
    @property
    def size(self):
        """
        Size in bytes of volume reserved for snapshots.
        Range : [0 - 2^64-1].
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-reserve-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'vserver',
            'percentage',
            'size',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'percentage': { 'class': int, 'is_list': False, 'required': 'required' },
            'size': { 'class': int, 'is_list': False, 'required': 'required' },
        }
