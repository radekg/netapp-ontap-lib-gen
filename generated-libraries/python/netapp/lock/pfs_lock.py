from netapp.netapp_object import NetAppObject

class PfsLock(NetAppObject):
    """
    Information about a single PFS lock.
    """
    
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
    
    _host_name = None
    @property
    def host_name(self):
        """
        Fully qualified domain name of PFS host holding the lock.
        """
        return self._host_name
    @host_name.setter
    def host_name(self, val):
        if val != None:
            self.validate('host_name', val)
        self._host_name = val
    
    _mode = None
    @property
    def mode(self):
        """
        File access mode that can be one of the following:<br>
        Deleg-PfsRead: Read delegation<br>
        or a string of form "AccessMode-ShareMode" with:<br>
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
    
    _owner = None
    @property
    def owner(self):
        """
        Name of the lock owner: IP address (of the caching filer
        holding the PFS lock), suffixed by a colon, and
        filesystem ID (of the caching filesystem holding the
        PFS lock). Syntax is: "IP:fsid".
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
        IP address, in dotted-decimal format, of the PFS host.
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
        Type of lock, which can only be "share-level".<br>
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
        Filesystem ID of the filesystem on the origin filier
        holding the PFS	lock.
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
        file, associated with the lock, on the origin
        filer.
        """
        return self._fileid
    @fileid.setter
    def fileid(self, val):
        if val != None:
            self.validate('fileid', val)
        self._fileid = val
    
    @staticmethod
    def get_api_name():
          return "pfs-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'lock-error',
            'state',
            'host-name',
            'mode',
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
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'host_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'host_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
