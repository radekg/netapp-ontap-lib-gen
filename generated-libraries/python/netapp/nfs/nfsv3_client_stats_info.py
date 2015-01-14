from netapp.netapp_object import NetAppObject

class Nfsv3ClientStatsInfo(NetAppObject):
    """
    structure containing statistics for NFSv3 operations
    """
    
    _setattr_ops = None
    @property
    def setattr_ops(self):
        """
        total 'setattr' NFSv3 operations
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
        total 'lookup' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._lookup_ops
    @lookup_ops.setter
    def lookup_ops(self, val):
        if val != None:
            self.validate('lookup_ops', val)
        self._lookup_ops = val
    
    _readlink_ops = None
    @property
    def readlink_ops(self):
        """
        total 'readlink' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._readlink_ops
    @readlink_ops.setter
    def readlink_ops(self, val):
        if val != None:
            self.validate('readlink_ops', val)
        self._readlink_ops = val
    
    _pathconf_ops = None
    @property
    def pathconf_ops(self):
        """
        total 'pathconf' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._pathconf_ops
    @pathconf_ops.setter
    def pathconf_ops(self, val):
        if val != None:
            self.validate('pathconf_ops', val)
        self._pathconf_ops = val
    
    _access_ops = None
    @property
    def access_ops(self):
        """
        total 'access' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._access_ops
    @access_ops.setter
    def access_ops(self, val):
        if val != None:
            self.validate('access_ops', val)
        self._access_ops = val
    
    _mkdir_ops = None
    @property
    def mkdir_ops(self):
        """
        total 'mkdir' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._mkdir_ops
    @mkdir_ops.setter
    def mkdir_ops(self, val):
        if val != None:
            self.validate('mkdir_ops', val)
        self._mkdir_ops = val
    
    _fsstat_ops = None
    @property
    def fsstat_ops(self):
        """
        total 'fsstat' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._fsstat_ops
    @fsstat_ops.setter
    def fsstat_ops(self, val):
        if val != None:
            self.validate('fsstat_ops', val)
        self._fsstat_ops = val
    
    _rename_ops = None
    @property
    def rename_ops(self):
        """
        total 'rename' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._rename_ops
    @rename_ops.setter
    def rename_ops(self, val):
        if val != None:
            self.validate('rename_ops', val)
        self._rename_ops = val
    
    _create_ops = None
    @property
    def create_ops(self):
        """
        total 'create' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._create_ops
    @create_ops.setter
    def create_ops(self, val):
        if val != None:
            self.validate('create_ops', val)
        self._create_ops = val
    
    _remove_ops = None
    @property
    def remove_ops(self):
        """
        total 'remove' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._remove_ops
    @remove_ops.setter
    def remove_ops(self, val):
        if val != None:
            self.validate('remove_ops', val)
        self._remove_ops = val
    
    _symlink_ops = None
    @property
    def symlink_ops(self):
        """
        total 'symlink' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._symlink_ops
    @symlink_ops.setter
    def symlink_ops(self, val):
        if val != None:
            self.validate('symlink_ops', val)
        self._symlink_ops = val
    
    _commit_ops = None
    @property
    def commit_ops(self):
        """
        total 'commit' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._commit_ops
    @commit_ops.setter
    def commit_ops(self, val):
        if val != None:
            self.validate('commit_ops', val)
        self._commit_ops = val
    
    _rmdir_ops = None
    @property
    def rmdir_ops(self):
        """
        total 'rmdir' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._rmdir_ops
    @rmdir_ops.setter
    def rmdir_ops(self, val):
        if val != None:
            self.validate('rmdir_ops', val)
        self._rmdir_ops = val
    
    _null_ops = None
    @property
    def null_ops(self):
        """
        total 'null' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._null_ops
    @null_ops.setter
    def null_ops(self, val):
        if val != None:
            self.validate('null_ops', val)
        self._null_ops = val
    
    _readdirplus_ops = None
    @property
    def readdirplus_ops(self):
        """
        total 'readdirplus' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._readdirplus_ops
    @readdirplus_ops.setter
    def readdirplus_ops(self, val):
        if val != None:
            self.validate('readdirplus_ops', val)
        self._readdirplus_ops = val
    
    _mknod_ops = None
    @property
    def mknod_ops(self):
        """
        total 'mknod' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._mknod_ops
    @mknod_ops.setter
    def mknod_ops(self, val):
        if val != None:
            self.validate('mknod_ops', val)
        self._mknod_ops = val
    
    _getattr_ops = None
    @property
    def getattr_ops(self):
        """
        total 'getattr' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._getattr_ops
    @getattr_ops.setter
    def getattr_ops(self, val):
        if val != None:
            self.validate('getattr_ops', val)
        self._getattr_ops = val
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        total 'write' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _fsinfo_ops = None
    @property
    def fsinfo_ops(self):
        """
        total 'fsinfo' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._fsinfo_ops
    @fsinfo_ops.setter
    def fsinfo_ops(self, val):
        if val != None:
            self.validate('fsinfo_ops', val)
        self._fsinfo_ops = val
    
    _link_ops = None
    @property
    def link_ops(self):
        """
        total 'link' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._link_ops
    @link_ops.setter
    def link_ops(self, val):
        if val != None:
            self.validate('link_ops', val)
        self._link_ops = val
    
    _readdir_ops = None
    @property
    def readdir_ops(self):
        """
        total 'readdir' NFSv3 operations
        Range : [0..2^64-1].
        """
        return self._readdir_ops
    @readdir_ops.setter
    def readdir_ops(self, val):
        if val != None:
            self.validate('readdir_ops', val)
        self._readdir_ops = val
    
    _read_ops = None
    @property
    def read_ops(self):
        """
        total 'read' NFSv3 operations
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
          return "nfsv3-client-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'setattr-ops',
            'lookup-ops',
            'readlink-ops',
            'pathconf-ops',
            'access-ops',
            'mkdir-ops',
            'fsstat-ops',
            'rename-ops',
            'create-ops',
            'remove-ops',
            'symlink-ops',
            'commit-ops',
            'rmdir-ops',
            'null-ops',
            'readdirplus-ops',
            'mknod-ops',
            'getattr-ops',
            'write-ops',
            'fsinfo-ops',
            'link-ops',
            'readdir-ops',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'setattr_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'lookup_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readlink_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'pathconf_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'access_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'mkdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'fsstat_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'rename_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'create_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'remove_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'symlink_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'commit_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'rmdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'null_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readdirplus_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'mknod_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'getattr_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'write_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'fsinfo_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'link_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'required' },
        }
