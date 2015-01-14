from netapp.netapp_object import NetAppObject

class Nfsv2ClientStatsInfo(NetAppObject):
    """
    structure containing statistics for NFSv2 operations
    """
    
    _readdir_ops = None
    @property
    def readdir_ops(self):
        """
        total 'readdir' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._readdir_ops
    @readdir_ops.setter
    def readdir_ops(self, val):
        if val != None:
            self.validate('readdir_ops', val)
        self._readdir_ops = val
    
    _root_ops = None
    @property
    def root_ops(self):
        """
        total 'root' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._root_ops
    @root_ops.setter
    def root_ops(self, val):
        if val != None:
            self.validate('root_ops', val)
        self._root_ops = val
    
    _setattr_ops = None
    @property
    def setattr_ops(self):
        """
        total 'setattr' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._setattr_ops
    @setattr_ops.setter
    def setattr_ops(self, val):
        if val != None:
            self.validate('setattr_ops', val)
        self._setattr_ops = val
    
    _lookup_ops = None
    @property
    def lookup_ops(self):
        """
        total 'lookup' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._lookup_ops
    @lookup_ops.setter
    def lookup_ops(self, val):
        if val != None:
            self.validate('lookup_ops', val)
        self._lookup_ops = val
    
    _getattr_ops = None
    @property
    def getattr_ops(self):
        """
        total 'getattr' NFSv2 operation
        Range : [0..2^64-1].
        """
        return self._getattr_ops
    @getattr_ops.setter
    def getattr_ops(self, val):
        if val != None:
            self.validate('getattr_ops', val)
        self._getattr_ops = val
    
    _link_ops = None
    @property
    def link_ops(self):
        """
        total 'link' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._link_ops
    @link_ops.setter
    def link_ops(self, val):
        if val != None:
            self.validate('link_ops', val)
        self._link_ops = val
    
    _readlink_ops = None
    @property
    def readlink_ops(self):
        """
        total 'readlink' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._readlink_ops
    @readlink_ops.setter
    def readlink_ops(self, val):
        if val != None:
            self.validate('readlink_ops', val)
        self._readlink_ops = val
    
    _rename_ops = None
    @property
    def rename_ops(self):
        """
        total 'rename' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._rename_ops
    @rename_ops.setter
    def rename_ops(self, val):
        if val != None:
            self.validate('rename_ops', val)
        self._rename_ops = val
    
    _statfs_ops = None
    @property
    def statfs_ops(self):
        """
        total 'statfs' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._statfs_ops
    @statfs_ops.setter
    def statfs_ops(self, val):
        if val != None:
            self.validate('statfs_ops', val)
        self._statfs_ops = val
    
    _symlink_ops = None
    @property
    def symlink_ops(self):
        """
        total 'symlink' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._symlink_ops
    @symlink_ops.setter
    def symlink_ops(self, val):
        if val != None:
            self.validate('symlink_ops', val)
        self._symlink_ops = val
    
    _wrcache_ops = None
    @property
    def wrcache_ops(self):
        """
        total 'wrcache' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._wrcache_ops
    @wrcache_ops.setter
    def wrcache_ops(self, val):
        if val != None:
            self.validate('wrcache_ops', val)
        self._wrcache_ops = val
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        total 'write' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _rmdir_ops = None
    @property
    def rmdir_ops(self):
        """
        total 'rmdir' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._rmdir_ops
    @rmdir_ops.setter
    def rmdir_ops(self, val):
        if val != None:
            self.validate('rmdir_ops', val)
        self._rmdir_ops = val
    
    _remove_ops = None
    @property
    def remove_ops(self):
        """
        total 'remove' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._remove_ops
    @remove_ops.setter
    def remove_ops(self, val):
        if val != None:
            self.validate('remove_ops', val)
        self._remove_ops = val
    
    _mkdir_ops = None
    @property
    def mkdir_ops(self):
        """
        total 'mkdir' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._mkdir_ops
    @mkdir_ops.setter
    def mkdir_ops(self, val):
        if val != None:
            self.validate('mkdir_ops', val)
        self._mkdir_ops = val
    
    _null_ops = None
    @property
    def null_ops(self):
        """
        total 'null' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._null_ops
    @null_ops.setter
    def null_ops(self, val):
        if val != None:
            self.validate('null_ops', val)
        self._null_ops = val
    
    _create_ops = None
    @property
    def create_ops(self):
        """
        total 'create' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._create_ops
    @create_ops.setter
    def create_ops(self, val):
        if val != None:
            self.validate('create_ops', val)
        self._create_ops = val
    
    _read_ops = None
    @property
    def read_ops(self):
        """
        total 'read' NFSv2 operations
        Range : [0..2^64-1].
        """
        return self._read_ops
    @read_ops.setter
    def read_ops(self, val):
        if val != None:
            self.validate('read_ops', val)
        self._read_ops = val
    
    @staticmethod
    def get_api_name():
          return "nfsv2-client-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'readdir-ops',
            'root-ops',
            'setattr-ops',
            'lookup-ops',
            'getattr-ops',
            'link-ops',
            'readlink-ops',
            'rename-ops',
            'statfs-ops',
            'symlink-ops',
            'wrcache-ops',
            'write-ops',
            'rmdir-ops',
            'remove-ops',
            'mkdir-ops',
            'null-ops',
            'create-ops',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'readdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'root_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'setattr_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'lookup_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'getattr_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'link_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readlink_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'rename_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'statfs_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'symlink_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'wrcache_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'write_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'rmdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'remove_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'mkdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'null_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'create_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'required' },
        }
