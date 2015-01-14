from netapp.netapp_object import NetAppObject

class NfsTopInfo(NetAppObject):
    """
    Information about a single nfs top.
    """
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        The number of nfs WRITE operations
        Range : [0..2^64-1].
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _lookup_ops = None
    @property
    def lookup_ops(self):
        """
        The number of nfs LOOKUP operations
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
        The number of nfs GETATTR operations
        Range : [0..2^64-1].
        """
        return self._getattr_ops
    @getattr_ops.setter
    def getattr_ops(self, val):
        if val != None:
            self.validate('getattr_ops', val)
        self._getattr_ops = val
    
    _readlink_ops = None
    @property
    def readlink_ops(self):
        """
        The number of nfs READLINK operations
        Range : [0..2^64-1].
        """
        return self._readlink_ops
    @readlink_ops.setter
    def readlink_ops(self, val):
        if val != None:
            self.validate('readlink_ops', val)
        self._readlink_ops = val
    
    _readdir_ops = None
    @property
    def readdir_ops(self):
        """
        The number of nfs READDIR and READIDRPLUS operations
        Range : [0..2^64-1].
        """
        return self._readdir_ops
    @readdir_ops.setter
    def readdir_ops(self, val):
        if val != None:
            self.validate('readdir_ops', val)
        self._readdir_ops = val
    
    _total_ops = None
    @property
    def total_ops(self):
        """
        The number of nfs operations
        Range : [0..2^64-1].
        """
        return self._total_ops
    @total_ops.setter
    def total_ops(self, val):
        if val != None:
            self.validate('total_ops', val)
        self._total_ops = val
    
    _remove_ops = None
    @property
    def remove_ops(self):
        """
        The number of nfs REMOVE operations
        Range : [0..2^64-1].
        """
        return self._remove_ops
    @remove_ops.setter
    def remove_ops(self, val):
        if val != None:
            self.validate('remove_ops', val)
        self._remove_ops = val
    
    _client_info = None
    @property
    def client_info(self):
        """
        Client IP address
        """
        return self._client_info
    @client_info.setter
    def client_info(self, val):
        if val != None:
            self.validate('client_info', val)
        self._client_info = val
    
    _create_ops = None
    @property
    def create_ops(self):
        """
        The number of nfs CREATE operations
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
        The number of nfs READ operations
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
          return "nfs-top-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'write-ops',
            'lookup-ops',
            'getattr-ops',
            'readlink-ops',
            'readdir-ops',
            'total-ops',
            'remove-ops',
            'client-info',
            'create-ops',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'write_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'lookup_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'getattr_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readlink_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'readdir_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'remove_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'client_info': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'create_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'required' },
        }
