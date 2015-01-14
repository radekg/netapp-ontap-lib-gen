from netapp.netapp_object import NetAppObject

class CloneStatusInfo(NetAppObject):
    """
    Status of a cloning.
    """
    
    _path = None
    @property
    def path(self):
        """
        LUN path being cloned.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _blocks_completed = None
    @property
    def blocks_completed(self):
        """
        Number of blocks completed.
        """
        return self._blocks_completed
    @blocks_completed.setter
    def blocks_completed(self, val):
        if val != None:
            self.validate('blocks_completed', val)
        self._blocks_completed = val
    
    _blocks_total = None
    @property
    def blocks_total(self):
        """
        Total blocks to clone.  The percentage complete is
        (completed * 100) / total
        """
        return self._blocks_total
    @blocks_total.setter
    def blocks_total(self, val):
        if val != None:
            self.validate('blocks_total', val)
        self._blocks_total = val
    
    @staticmethod
    def get_api_name():
          return "clone-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'path',
            'blocks-completed',
            'blocks-total',
        ]
    
    def describe_properties(self):
        return {
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'blocks_completed': { 'class': int, 'is_list': False, 'required': 'required' },
            'blocks_total': { 'class': int, 'is_list': False, 'required': 'required' },
        }
