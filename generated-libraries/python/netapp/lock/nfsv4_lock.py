from netapp.netapp_object import NetAppObject

class Nfsv4Lock(NetAppObject):
    """
    Information about a single NFSv4 lock.
    """
    
    _lock_error = None
    @property
    def lock_error(self):
        """
        Error messages issued, e.g., if the input syntax
        is not applicable to this protocol (but maybe applicable
        to other protocols), or else if this protocol is
        specified by the "protocol" input but the syntax of
        host, owner, or file is wrong.
        """
        return self._lock_error
    @lock_error.setter
    def lock_error(self, val):
        if val != None:
            self.validate('lock_error', val)
        self._lock_error = val
    
    _is_bytelock_exclusive = None
    @property
    def is_bytelock_exclusive(self):
        """
        Is true for exclusive bytelock, else false.
        """
        return self._is_bytelock_exclusive
    @is_bytelock_exclusive.setter
    def is_bytelock_exclusive(self, val):
        if val != None:
            self.validate('is_bytelock_exclusive', val)
        self._is_bytelock_exclusive = val
    
    _pid = None
    @property
    def pid(self):
        """
        Process-ID of NFSv4 client.
        """
        return self._pid
    @pid.setter
    def pid(self, val):
        if val != None:
            self.validate('pid', val)
        self._pid = val
    
    _state_index_table = None
    @property
    def state_index_table(self):
        """
        This is an index into a state table that contains
        entire NFSv4 state information of the filer.
        """
        return self._state_index_table
    @state_index_table.setter
    def state_index_table(self, val):
        if val != None:
            self.validate('state_index_table', val)
        self._state_index_table = val
    
    _state = None
    @property
    def state(self):
        """
        State of the lock. See cifs-lock for
        description of all state values.<br>
        NOTE: Future releases may have new lock states.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _bytelock_length = None
    @property
    def bytelock_length(self):
        """
        Number of bytes (from bytelock-offset) that are locked.
        """
        return self._bytelock_length
    @bytelock_length.setter
    def bytelock_length(self, val):
        if val != None:
            self.validate('bytelock_length', val)
        self._bytelock_length = val
    
    _mode = None
    @property
    def mode(self):
        """
        File access mode that can be one of the following:<br>
        Deleg-Read: Read delegation<br>
        Deleg-Wrt:  Write delegation<br>
        or a string of form "AccessMode-ShareMode" with:
        AccessMode: RdWr(Read-Write), Read(Read-only)
        Writ(Write), None(No access)<br>
        ShareMode: denyA(deny all), denyR(deny Read access)
        denyW(deny Write access), denyN(deny none)
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _bytelock_offset = None
    @property
    def bytelock_offset(self):
        """
        Starting offset in file that gets bytelocked.
        """
        return self._bytelock_offset
    @bytelock_offset.setter
    def bytelock_offset(self, val):
        if val != None:
            self.validate('bytelock_offset', val)
        self._bytelock_offset = val
    
    _owner = None
    @property
    def owner(self):
        """
        Name of the owner.
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _path = None
    @property
    def path(self):
        """
        Name of the path for a file or directory.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _host_ip = None
    @property
    def host_ip(self):
        """
        IP address, in dotted-decimal format, of the NFSv4 host.
        """
        return self._host_ip
    @host_ip.setter
    def host_ip(self, val):
        if val != None:
            self.validate('host_ip', val)
        self._host_ip = val
    
    _type = None
    @property
    def type(self):
        """
        Type of lock, either "share-level" or "byte-range".<br>
        NOTE: Future releases might have new values.
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _fsid = None
    @property
    def fsid(self):
        """
        Filesystem ID.
        """
        return self._fsid
    @fsid.setter
    def fsid(self, val):
        if val != None:
            self.validate('fsid', val)
        self._fsid = val
    
    _fileid = None
    @property
    def fileid(self):
        """
        A unique number (withing filesystem) identifying the
        file associated with the lock.
        """
        return self._fileid
    @fileid.setter
    def fileid(self, val):
        if val != None:
            self.validate('fileid', val)
        self._fileid = val
    
    @staticmethod
    def get_api_name():
          return "nfsv4-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'lock-error',
            'is-bytelock-exclusive',
            'pid',
            'state-index-table',
            'state',
            'bytelock-length',
            'mode',
            'bytelock-offset',
            'owner',
            'path',
            'host-ip',
            'type',
            'fsid',
            'fileid',
        ]
    
    def describe_properties(self):
        return {
            'lock_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_bytelock_exclusive': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'pid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state_index_table': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'bytelock_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bytelock_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'host_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
