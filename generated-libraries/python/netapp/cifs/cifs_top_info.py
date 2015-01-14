from netapp.netapp_object import NetAppObject

class CifsTopInfo(NetAppObject):
    """
    Information about a single cifs top.
    """
    
    _ops_per_sec = None
    @property
    def ops_per_sec(self):
        """
        The number of operations of any type per second.
        """
        return self._ops_per_sec
    @ops_per_sec.setter
    def ops_per_sec(self, val):
        if val != None:
            self.validate('ops_per_sec', val)
        self._ops_per_sec = val
    
    _read_size = None
    @property
    def read_size(self):
        """
        The size in kbytes per second of data of read requests.
        """
        return self._read_size
    @read_size.setter
    def read_size(self, val):
        if val != None:
            self.validate('read_size', val)
        self._read_size = val
    
    _suspicious_per_sec = None
    @property
    def suspicious_per_sec(self):
        """
        The number of "suspicious" events per second due to the
        following conditions:
        ACCESS-DENIED returned for FindFirst
        ACCESS-DENIED returned for Open/CreateFile
        ACCESS-DENIED returned for DeleteFile
        SUCCESS returned for DeleteFile
        SUCCESS returned for TruncateFile
        """
        return self._suspicious_per_sec
    @suspicious_per_sec.setter
    def suspicious_per_sec(self, val):
        if val != None:
            self.validate('suspicious_per_sec', val)
        self._suspicious_per_sec = val
    
    _write_ops = None
    @property
    def write_ops(self):
        """
        The number of write requests.
        """
        return self._write_ops
    @write_ops.setter
    def write_ops(self, val):
        if val != None:
            self.validate('write_ops', val)
        self._write_ops = val
    
    _user_info = None
    @property
    def user_info(self):
        """
        Information on the client with its IP address and user
        account.
        """
        return self._user_info
    @user_info.setter
    def user_info(self, val):
        if val != None:
            self.validate('user_info', val)
        self._user_info = val
    
    _write_size = None
    @property
    def write_size(self):
        """
        The size in kbytes per second of data of write requests.
        """
        return self._write_size
    @write_size.setter
    def write_size(self, val):
        if val != None:
            self.validate('write_size', val)
        self._write_size = val
    
    _read_ops = None
    @property
    def read_ops(self):
        """
        The number of read requests.
        """
        return self._read_ops
    @read_ops.setter
    def read_ops(self, val):
        if val != None:
            self.validate('read_ops', val)
        self._read_ops = val
    
    @staticmethod
    def get_api_name():
          return "cifs-top-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ops-per-sec',
            'read-size',
            'suspicious-per-sec',
            'write-ops',
            'user-info',
            'write-size',
            'read-ops',
        ]
    
    def describe_properties(self):
        return {
            'ops_per_sec': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'suspicious_per_sec': { 'class': int, 'is_list': False, 'required': 'required' },
            'write_ops': { 'class': int, 'is_list': False, 'required': 'required' },
            'user_info': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'write_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_ops': { 'class': int, 'is_list': False, 'required': 'required' },
        }
