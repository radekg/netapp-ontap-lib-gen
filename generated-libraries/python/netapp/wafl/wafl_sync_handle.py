from netapp.netapp_object import NetAppObject

class WaflSyncHandle(NetAppObject):
    """
    Handle representing a specific wafl-sync operation on a
    volume.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        Volume name on which wafl-sync operation being performed.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _handle = None
    @property
    def handle(self):
        """
        Opaque handle that represents a specific wafl-sync
        operation.
        """
        return self._handle
    @handle.setter
    def handle(self, val):
        if val != None:
            self.validate('handle', val)
        self._handle = val
    
    _volume_uuid = None
    @property
    def volume_uuid(self):
        """
        Volume UUID on which wafl-sync operation being performed.
        """
        return self._volume_uuid
    @volume_uuid.setter
    def volume_uuid(self, val):
        if val != None:
            self.validate('volume_uuid', val)
        self._volume_uuid = val
    
    @staticmethod
    def get_api_name():
          return "wafl-sync-handle"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'handle',
            'volume-uuid',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'handle': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
