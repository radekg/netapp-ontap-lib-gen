from netapp.netapp_object import NetAppObject

class NlmLock(NetAppObject):
    """
    Information about a single NLM(Nfsv2/Nfsv3) lock.
    """
    
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
    
    _lock_error = None
    @property
    def lock_error(self):
        """
        Error messages issued, e.g., if the input syntax
        is not applicable to this protocol (but maybe applicable
        to other protocols), or else if this protocol is
        specified by the "protocol" input but the syntax of
        host, owner, or file parameters is wrong.
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
    
    _host = None
    @property
    def host(self):
        """
        IP address (in dotted decimal format) or a fully
        qualified domain name.
        """
        return self._host
    @host.setter
    def host(self, val):
        if val != None:
            self.validate('host', val)
        self._host = val
    
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
    
    _last_hop_caching_filer = None
    @property
    def last_hop_caching_filer(self):
        """
        Name of the last-hop downstream caching filer used to
        obtain this lock. Note that this filer is not the actual
        lock owner.
        """
        return self._last_hop_caching_filer
    @last_hop_caching_filer.setter
    def last_hop_caching_filer(self, val):
        if val != None:
            self.validate('last_hop_caching_filer', val)
        self._last_hop_caching_filer = val
    
    _mode = None
    @property
    def mode(self):
        """
        File access mode of form "AccessMode-denyN" with:<br>
        Access mode: RdWr(Read-Write), Read(Read-only)
        Writ(Write), None(No access)
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
          return "nlm-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bytelock-length',
            'lock-error',
            'is-bytelock-exclusive',
            'host',
            'state',
            'last-hop-caching-filer',
            'mode',
            'bytelock-offset',
            'owner',
            'path',
            'type',
            'fsid',
            'fileid',
        ]
    
    def describe_properties(self):
        return {
            'bytelock_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lock_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_bytelock_exclusive': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'host': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_hop_caching_filer': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bytelock_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': int, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
