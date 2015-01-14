from netapp.netapp_object import NetAppObject

class LunSnapUsageLunInfo(NetAppObject):
    """
    Details of the LUN backed by specified snapshot.
    """
    
    _path = None
    @property
    def path(self):
        """
        Path of the LUN.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _snapshot = None
    @property
    def snapshot(self):
        """
        Name of the snapshot in which the LUN exists.
        """
        return self._snapshot
    @snapshot.setter
    def snapshot(self, val):
        if val != None:
            self.validate('snapshot', val)
        self._snapshot = val
    
    _backing_store = None
    @property
    def backing_store(self):
        """
        Path of the LUN serving as the backing store.
        """
        return self._backing_store
    @backing_store.setter
    def backing_store(self, val):
        if val != None:
            self.validate('backing_store', val)
        self._backing_store = val
    
    @staticmethod
    def get_api_name():
          return "lun-snap-usage-lun-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'path',
            'snapshot',
            'backing-store',
        ]
    
    def describe_properties(self):
        return {
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snapshot': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'backing_store': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
