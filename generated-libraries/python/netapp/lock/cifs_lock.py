from netapp.netapp_object import NetAppObject

class CifsLock(NetAppObject):
    """
    Information about a single CIFS lock.
    """
    
    _oplock_level = None
    @property
    def oplock_level(self):
        """
        Oplock level (for non-Delete-on-close lock), which is
        "Excl" (Exclusive Oplock), "lvl2" (Level-II Oplock), "RWH"
        (Read-Write-Handle Lease), "RW" (Read-Write Lease),
        "RH" (Read-Handle Lease), "R" (Read Lease), or "None"
        (No oplock).
        """
        return self._oplock_level
    @oplock_level.setter
    def oplock_level(self, val):
        if val != None:
            self.validate('oplock_level', val)
        self._oplock_level = val
    
    _lock_error = None
    @property
    def lock_error(self):
        """
        Error messages issued, e.g., low system memory or
        if the input syntax is not applicable to this
        protocol (but maybe applicable to other protocols), or
        else if this protocol is specified by the "protocol"
        input but the syntax of host, owner, or file
        parameters is wrong.<br>
        NOTE: New error messages may be added in the future.
        """
        return self._lock_error
    @lock_error.setter
    def lock_error(self, val):
        if val != None:
            self.validate('lock_error', val)
        self._lock_error = val
    
    _pid = None
    @property
    def pid(self):
        """
        Process-ID of SMB client holding the lock.
        """
        return self._pid
    @pid.setter
    def pid(self, val):
        if val != None:
            self.validate('pid', val)
        self._pid = val
    
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
    
    _absolute_path = None
    @property
    def absolute_path(self):
        """
        Name of the absolute ("/vol/volX" style) path
        corresponding to the CIFS path present in
        the ONTAPI output element, <b>path</b>.  <br>
        NOTE: In certain cases, the absolute path is unavailable
        (e.g., due to insufficient memory or if the lock is a
        Delete-on-close lock.)
        """
        return self._absolute_path
    @absolute_path.setter
    def absolute_path(self, val):
        if val != None:
            self.validate('absolute_path', val)
        self._absolute_path = val
    
    _state = None
    @property
    def state(self):
        """
        State of the lock, being one of:<br>
        GRANTED: The lock is granted and is not being revoked.
        Locks in this state are on the share-grant or
        byte-grant lists, depending on the lock type.
        <br>
        REVOKING: The lock has just begun revocation. Locks in
        this state are also on share-grant or
        byte-grant lists, depending on the lock type.
        <br>
        REVOKED: The lock is undergoing revocation and the
        protocol has marked it to be released. This is
        a transient state whereby the protocol
        indicates the results of lock revocation to the
        generic lock manager code. Locks in this state
        are on the share-grant or byte-grants lists,
        but are removed immediately.<br>
        GWAITING: The lock is waiting to be granted. Locks in
        this state are on the share-wait list or one
        of the wait lists associated with a granted
        byte lock. Locks enter this state when they
        can't be granted because of a conflict and the
        lock parameters indicate that the caller is
        prepared to wait.<br>
        EWAITING: The lock is waiting either to be granted or
        denied. Locks in this state are on the
        share-wait list or one of the wait lists
        associated with a granted byte lock. Locks
        enter this state when they can't be granted
        because of a conflict with a soft lock and
        lock parameters indicate they the caller is
        not prepared to wait. Generally, in this
        situation, the protocol is prepared to wait
        for a limited time to allow the revocation to
        be resolved so that it can be determined
        whether the lock is to be granted or denied.
        <br>
        ADJUSTED: The lock is undergoing revocation and the
        protocol has marked it to be replaced by a
        hard lock which is equal to it or weaker. This
        is a transient state whereby the protocol
        indicates the results of lock revocation to
        the generic lock manager code. Locks in this
        state are on the share-grant or byte-grant
        lists, but are transitioned back to the
        granted state once the changes in the lock
        have been dealt with.<br>
        DENIED: The lock has been denied. This is a temporary
        state used to mark locks that have, after
        waiting, been denied. This is so that when the
        lock state is noticed by a WAFL operation,
        appropriate information about the state of the
        request, including the denial status, will be
        available. Locks in this state are not in any
        of the per-file lists.<br>
        TIMEDOUT: The wait for the lock has timed out. This is a
        temporary state used to mark locks that have,
        after waiting, had the wait timed out. This
        is so that when the lock state is noticed by
        a WAFL operation, appropriate information
        about the state of the request, including the
        fact that it could not be granted due to a
        timeout, will be available. Locks in this
        state are not in any of the per-file lists.
        <br>
        SUBSUMED: Kept in reserve by protocol while protected
        by an encompassing soft lock. This is a
        transient state used for locks which are one
        of a set of locks that will take the place of
        a lock being revoked. Locks in this state are
        in an internal list and not in any of the
        per-file lists. They are converted to the
        GRANTED state and put in the share-grant list
        as part of completing the revocation operation
        .<br>
        GONE: About to be returned. This is a temporary state
        for lock objects that are to be freed as soon as
        any potential references to them are gone. Locks
        in this state are not on any of the per-file lists
        .<br>
        UNUSED: The lock was just allocated. This is a
        temporary state for lock objects that have been
        allocated but have not yet been dealt with (i.e.
        granted, denied, set up to wait).  Locks in this
        state are not on any of the per-file lists.<br>
        <br>
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
        NetBios name of the CIFS client. This may be unavailable
        in certain situations. In such cases, the ONTAPI element
        'host-ip' alone provides identity of the host.
        """
        return self._host_name
    @host_name.setter
    def host_name(self, val):
        if val != None:
            self.validate('host_name', val)
        self._host_name = val
    
    _dh_state = None
    @property
    def dh_state(self):
        """
        Durable state of the lock, which can be "DH_GRANTED"
        (durability granted), "DH_ACTIVE" (lock is currently
        durable), "DH_PURGED" (lock has been purged), or
        "DH_NONE" (durability is not granted). For lease locks,
        dh-state is unavailable.
        """
        return self._dh_state
    @dh_state.setter
    def dh_state(self, val):
        if val != None:
            self.validate('dh_state', val)
        self._dh_state = val
    
    _mode = None
    @property
    def mode(self):
        """
        File access mode that can be one of the following:<br>
        DelOnClose: Delete-on-close lock<br>
        DelOnCloseWait: Waiting Delete-on-close lock<br>
        SuperLock: Super lock, eg, used by antivirus scanner<br>
        Oplock-Excl: Exclusive Oplock<br>
        Oplock-Lvl2: Level-II Oplock<br>
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
        Name of the lock owner: a username prefixed by an
        optional domain (and a backslash) for CIFS protocol
        ([domain\]username).
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
        Name of the path for a file or directory or NT stream.<br>
        NOTE: In certain cases, the path is unavailable
        (e.g., due to insufficient memory)
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
        IP address, in dotted-decimal format, of the CIFS client.
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
          return "cifs-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'oplock-level',
            'lock-error',
            'pid',
            'is-bytelock-exclusive',
            'bytelock-length',
            'absolute-path',
            'state',
            'host-name',
            'dh-state',
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
            'oplock_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lock_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_bytelock_exclusive': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'bytelock_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'absolute_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'host_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dh_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bytelock_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'host_ip': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
