from netapp.clone.block_range import BlockRange
from netapp.clone.clone_id_info import CloneIdInfo
from netapp.netapp_object import NetAppObject

class OpsInfo(NetAppObject):
    """
    Structure containing information of a clone operation.
    """
    
    _percent_done = None
    @property
    def percent_done(self):
        """
        Percentage cloning completed for running clone operation.
        """
        return self._percent_done
    @percent_done.setter
    def percent_done(self, val):
        if val != None:
            self.validate('percent_done', val)
        self._percent_done = val
    
    _destination_file = None
    @property
    def destination_file(self):
        """
        Destination file path. For sub-file/sub-LUN cloning within
        the same file/LUN, source-file and destination file will be
        same.
        """
        return self._destination_file
    @destination_file.setter
    def destination_file(self, val):
        if val != None:
            self.validate('destination_file', val)
        self._destination_file = val
    
    _error = None
    @property
    def error(self):
        """
        Error code corresponding to reason of failure. If error
        code is EDENSE_SHUTDOWN or EDENSE_FAILOVER, the clone
        operation will be restarted automatically after
        giveback/takeover or next reboot. If user has not aborted
        the clone operation using clone-stop, then for any other
        error code user should do clone-clear.
        """
        return self._error
    @error.setter
    def error(self, val):
        if val != None:
            self.validate('error', val)
        self._error = val
    
    _total_blocks = None
    @property
    def total_blocks(self):
        """
        Total number of blocks to be cloned for running clone
        operation.
        """
        return self._total_blocks
    @total_blocks.setter
    def total_blocks(self, val):
        if val != None:
            self.validate('total_blocks', val)
        self._total_blocks = val
    
    _source_file = None
    @property
    def source_file(self):
        """
        Source file path.
        """
        return self._source_file
    @source_file.setter
    def source_file(self, val):
        if val != None:
            self.validate('source_file', val)
        self._source_file = val
    
    _clone_type = None
    @property
    def clone_type(self):
        """
        Type of clone. Possible types are 'file', 'sub_file', 'lun'
        and 'sub_lun'.
        """
        return self._clone_type
    @clone_type.setter
    def clone_type(self, val):
        if val != None:
            self.validate('clone_type', val)
        self._clone_type = val
    
    _block_ranges = None
    @property
    def block_ranges(self):
        """
        List of block ranges specified for sub-file/sub-LUN cloning.
        In case of complete file cloning there will be no output
        corresponding to this.
        """
        return self._block_ranges
    @block_ranges.setter
    def block_ranges(self, val):
        if val != None:
            self.validate('block_ranges', val)
        self._block_ranges = val
    
    _clone_id = None
    @property
    def clone_id(self):
        """
        Unique ID information of the clone operation.
        """
        return self._clone_id
    @clone_id.setter
    def clone_id(self, val):
        if val != None:
            self.validate('clone_id', val)
        self._clone_id = val
    
    _reason = None
    @property
    def reason(self):
        """
        Reason of failure if clone operation could not complete
        successfully.
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    _clone_state = None
    @property
    def clone_state(self):
        """
        State of the clone operation. It could be 'running', 'failed'
        or 'completed'. For 'completed' state there will be no
        other field in ops-info output.
        """
        return self._clone_state
    @clone_state.setter
    def clone_state(self, val):
        if val != None:
            self.validate('clone_state', val)
        self._clone_state = val
    
    _blocks_copied = None
    @property
    def blocks_copied(self):
        """
        Number of blocks that have been copied so far for running
        clone operation. The cloning operation shares destination
        blocks with source block. But if source block has already
        reached maximum number of sharing supported by WAFL, then
        block is copied for destination. It is recommended that if
        blocks are being copied, then user should change the source
        for next clone operation.
        """
        return self._blocks_copied
    @blocks_copied.setter
    def blocks_copied(self, val):
        if val != None:
            self.validate('blocks_copied', val)
        self._blocks_copied = val
    
    @staticmethod
    def get_api_name():
          return "ops-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'percent-done',
            'destination-file',
            'error',
            'total-blocks',
            'source-file',
            'clone-type',
            'block-ranges',
            'clone-id',
            'reason',
            'clone-state',
            'blocks-copied',
        ]
    
    def describe_properties(self):
        return {
            'percent_done': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'clone_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'block_ranges': { 'class': BlockRange, 'is_list': True, 'required': 'optional' },
            'clone_id': { 'class': CloneIdInfo, 'is_list': False, 'required': 'optional' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'clone_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'blocks_copied': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
