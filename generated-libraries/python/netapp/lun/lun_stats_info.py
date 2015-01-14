from netapp.netapp_object import NetAppObject

class LunStatsInfo(NetAppObject):
    """
    Stats for a LUN.
    """
    
    _last_zeroed = None
    @property
    def last_zeroed(self):
        """
        Total number of seconds since the statistics
        for this lun were last zeroed.
        """
        return self._last_zeroed
    @last_zeroed.setter
    def last_zeroed(self, val):
        if val != None:
            self.validate('last_zeroed', val)
        self._last_zeroed = val
    
    _block_size = None
    @property
    def block_size(self):
        """
        Disk block size for this LUN in bytes.
        This attribute is unavailable when the LUN is fenced for
        a restore operation.
        """
        return self._block_size
    @block_size.setter
    def block_size(self, val):
        if val != None:
            self.validate('block_size', val)
        self._block_size = val
    
    _scsi_errors = None
    @property
    def scsi_errors(self):
        """
        Total number of SCSI errors.
        """
        return self._scsi_errors
    @scsi_errors.setter
    def scsi_errors(self, val):
        if val != None:
            self.validate('scsi_errors', val)
        self._scsi_errors = val
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        Total number of SCSI write ops executed.
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _write_blocks = None
    @property
    def write_blocks(self):
        """
        Number of disk blocks written.
        This attribute is unavailable when the LUN is fenced for
        a restore operation.
        """
        return self._write_blocks
    @write_blocks.setter
    def write_blocks(self, val):
        if val != None:
            self.validate('write_blocks', val)
        self._write_blocks = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing the lun
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _other_ops = None
    @property
    def other_ops(self):
        """
        Total number of other SCSI ops executed.
        """
        return self._other_ops
    @other_ops.setter
    def other_ops(self, val):
        if val != None:
            self.validate('other_ops', val)
        self._other_ops = val
    
    _path = None
    @property
    def path(self):
        """
        path of the LUN.
        (for example, "/vol/vol0/lun1")
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _read_blocks = None
    @property
    def read_blocks(self):
        """
        Number of disk blocks read.
        This attribute is unavailable when the LUN is fenced for
        a restore operation.
        """
        return self._read_blocks
    @read_blocks.setter
    def read_blocks(self, val):
        if val != None:
            self.validate('read_blocks', val)
        self._read_blocks = val
    
    _read_ops = None
    @property
    def read_ops(self):
        """
        Total number of SCSI read ops executed.
        """
        return self._read_ops
    @read_ops.setter
    def read_ops(self, val):
        if val != None:
            self.validate('read_ops', val)
        self._read_ops = val
    
    @staticmethod
    def get_api_name():
          return "lun-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'last-zeroed',
            'block-size',
            'scsi-errors',
            'write-ops',
            'write-blocks',
            'vserver',
            'other-ops',
            'path',
            'read-blocks',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'last_zeroed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'block_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scsi_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'write_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'write_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'other_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'read_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'required' },
        }
