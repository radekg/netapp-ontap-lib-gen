from netapp.netapp_object import NetAppObject

class Aggr64BitUpgradeStatusInfo(NetAppObject):
    """
    Status information related to 64-bit upgrade.
    This information includes the block format
    of the aggregate and the progress of the 64-bit
    upgrade scanner.
    """
    
    _block_format = None
    @property
    def block_format(self):
        """
        The block format of the aggregate.
        Can be "32_bit", "64_bit", or
        "upgrading".
        """
        return self._block_format
    @block_format.setter
    def block_format(self, val):
        if val != None:
            self.validate('block_format', val)
        self._block_format = val
    
    _time_estimate = None
    @property
    def time_estimate(self):
        """
        Estimated time to completion of the
        64-bit upgrade in seconds. Valid only
        when the aggregate block format is
        "upgrading" and scanner status is
        "running". Value -1 indicates that
        time estimate is not available.
        Range: [-1..(2^32-1)/10].
        """
        return self._time_estimate
    @time_estimate.setter
    def time_estimate(self, val):
        if val != None:
            self.validate('time_estimate', val)
        self._time_estimate = val
    
    _space_progress = None
    @property
    def space_progress(self):
        """
        The inode space of the most recent
        inode the 64-bit upgrade scanner is
        working on. Can be "public" or
        "private". Valid only when the aggregate
        block format is "upgrading".
        """
        return self._space_progress
    @space_progress.setter
    def space_progress(self, val):
        if val != None:
            self.validate('space_progress', val)
        self._space_progress = val
    
    _inode_progress = None
    @property
    def inode_progress(self):
        """
        The most recent inode the 64-bit
        upgrade scanner is working on.
        Valid only when the aggregate block
        format is "upgrading". Value -1
        indicates inofile is being scanned.
        Range: [-1..2^32-2].
        """
        return self._inode_progress
    @inode_progress.setter
    def inode_progress(self, val):
        if val != None:
            self.validate('inode_progress', val)
        self._inode_progress = val
    
    _percent_complete = None
    @property
    def percent_complete(self):
        """
        Estimated percentage of how much of the
        filesystem has completed the 64-bit
        upgrade. Valid only when the aggregate
        block format is "upgrading".
        Range: [0..100].
        """
        return self._percent_complete
    @percent_complete.setter
    def percent_complete(self, val):
        if val != None:
            self.validate('percent_complete', val)
        self._percent_complete = val
    
    _total_inodes = None
    @property
    def total_inodes(self):
        """
        The total number of inodes in the file
        system. Valid only when the aggregate
        block format is "upgrading".
        Range: [0..2^32-1].
        """
        return self._total_inodes
    @total_inodes.setter
    def total_inodes(self, val):
        if val != None:
            self.validate('total_inodes', val)
        self._total_inodes = val
    
    _fbn_progress = None
    @property
    def fbn_progress(self):
        """
        The most recent fbn the 64-bit upgrade
        scanner is working on. Valid only
        when the aggregate block format is
        "upgrading".
        Range: [0..2^32-1].
        """
        return self._fbn_progress
    @fbn_progress.setter
    def fbn_progress(self, val):
        if val != None:
            self.validate('fbn_progress', val)
        self._fbn_progress = val
    
    _scanner_status = None
    @property
    def scanner_status(self):
        """
        The status of the 64-bit upgrade
        scanner. Can be "running" or "stopped"
        if the aggregate block format is
        "upgrading". Otherwise, no value is
        returned.
        """
        return self._scanner_status
    @scanner_status.setter
    def scanner_status(self, val):
        if val != None:
            self.validate('scanner_status', val)
        self._scanner_status = val
    
    @staticmethod
    def get_api_name():
          return "aggr-64bit-upgrade-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'block-format',
            'time-estimate',
            'space-progress',
            'inode-progress',
            'percent-complete',
            'total-inodes',
            'fbn-progress',
            'scanner-status',
        ]
    
    def describe_properties(self):
        return {
            'block_format': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'time_estimate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'inode_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_inodes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fbn_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
