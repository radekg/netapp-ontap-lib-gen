from netapp.netapp_object import NetAppObject

class CloneSplitDetailInfo(NetAppObject):
    """
    Status information about an active clone split.
    """
    
    _inodes_total = None
    @property
    def inodes_total(self):
        """
        Total number of inodes in the clone.
        """
        return self._inodes_total
    @inodes_total.setter
    def inodes_total(self, val):
        if val != None:
            self.validate('inodes_total', val)
        self._inodes_total = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the clone being split.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _blocks_updated = None
    @property
    def blocks_updated(self):
        """
        Total number of the clone's blocks that have been
        updated to date by the split.
        """
        return self._blocks_updated
    @blocks_updated.setter
    def blocks_updated(self, val):
        if val != None:
            self.validate('blocks_updated', val)
        self._blocks_updated = val
    
    _blocks_scanned = None
    @property
    def blocks_scanned(self):
        """
        Number of the clone's blocks that have been
        scanned to date by the split.
        """
        return self._blocks_scanned
    @blocks_scanned.setter
    def blocks_scanned(self, val):
        if val != None:
            self.validate('blocks_scanned', val)
        self._blocks_scanned = val
    
    _inode_percentage_complete = None
    @property
    def inode_percentage_complete(self):
        """
        Percent of the clone's inodes processed to date
        by the split.
        """
        return self._inode_percentage_complete
    @inode_percentage_complete.setter
    def inode_percentage_complete(self, val):
        if val != None:
            self.validate('inode_percentage_complete', val)
        self._inode_percentage_complete = val
    
    _inodes_processed = None
    @property
    def inodes_processed(self):
        """
        Number of the clone's inodes processed to date
        by the split.
        """
        return self._inodes_processed
    @inodes_processed.setter
    def inodes_processed(self, val):
        if val != None:
            self.validate('inodes_processed', val)
        self._inodes_processed = val
    
    @staticmethod
    def get_api_name():
          return "clone-split-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'inodes-total',
            'name',
            'blocks-updated',
            'blocks-scanned',
            'inode-percentage-complete',
            'inodes-processed',
        ]
    
    def describe_properties(self):
        return {
            'inodes_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'blocks_updated': { 'class': int, 'is_list': False, 'required': 'required' },
            'blocks_scanned': { 'class': int, 'is_list': False, 'required': 'required' },
            'inode_percentage_complete': { 'class': int, 'is_list': False, 'required': 'required' },
            'inodes_processed': { 'class': int, 'is_list': False, 'required': 'required' },
        }
