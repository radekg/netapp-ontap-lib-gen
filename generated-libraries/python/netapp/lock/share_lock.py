from netapp.netapp_object import NetAppObject

class ShareLock(NetAppObject):
    """
    Description of share-locks
    """
    
    _smb2_open_type = None
    @property
    def smb2_open_type(self):
        """
        Indicates the type of smb2 open.
        Possible values are:
        <ul>
        <li>"durable",</li>
        <li>"none".</li>
        </ul>
        """
        return self._smb2_open_type
    @smb2_open_type.setter
    def smb2_open_type(self, val):
        if val != None:
            self.validate('smb2_open_type', val)
        self._smb2_open_type = val
    
    _smb2_lock_time_remaining = None
    @property
    def smb2_lock_time_remaining(self):
        """
        Indicates the time remaining in seconds for a
        smb2 lock after it is disconnected.
        """
        return self._smb2_lock_time_remaining
    @smb2_lock_time_remaining.setter
    def smb2_lock_time_remaining(self, val):
        if val != None:
            self.validate('smb2_lock_time_remaining', val)
        self._smb2_lock_time_remaining = val
    
    _smb2_connect_state = None
    @property
    def smb2_connect_state(self):
        """
        Indicates the connection state of smb2 lock.
        Possible values are:
        <ul>
        <li>"connected",</li>
        <li>"disconnected",</li>
        <li>"reconnecting",</li>
        <li>"reconnected",</li>
        <li>"timedout".</li>
        </ul>
        """
        return self._smb2_connect_state
    @smb2_connect_state.setter
    def smb2_connect_state(self, val):
        if val != None:
            self.validate('smb2_connect_state', val)
        self._smb2_connect_state = val
    
    _is_sharelock_soft = None
    @property
    def is_sharelock_soft(self):
        """
        is true for soft sharelocks,
        A sharelock is marked soft after lease expiration.
        """
        return self._is_sharelock_soft
    @is_sharelock_soft.setter
    def is_sharelock_soft(self, val):
        if val != None:
            self.validate('is_sharelock_soft', val)
        self._is_sharelock_soft = val
    
    _is_sharelock_super = None
    @property
    def is_sharelock_super(self):
        """
        is true for super sharelocks,
        A superlock preempts existing locks on a given file.
        """
        return self._is_sharelock_super
    @is_sharelock_super.setter
    def is_sharelock_super(self, val):
        if val != None:
            self.validate('is_sharelock_super', val)
        self._is_sharelock_super = val
    
    _mode = None
    @property
    def mode(self):
        """
        Access mode. Various values are
        "delete-on-close"
        or a string of of type "Accessmode-Denymode"
        Possible values for Accessmode are:
        <ul>
        <li>"read",</li>
        <li>"write"</li>
        <li>"read_write".</li>
        </ul>
        Possible values for Denymode are:
        <ul>
        <li>"deny_read",</li>
        <li>"deny_write",</li>
        <li>"deny_all",</li>
        <li>"deny_delete",</li>
        <li>"deny_none".</li>
        </ul>
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _smb2_open_group_id = None
    @property
    def smb2_open_group_id(self):
        """
        Indicates the open group id for the smb2 lock.
        This is a byte string provided by the CIFS
        client and opaque to the d-blade.
        """
        return self._smb2_open_group_id
    @smb2_open_group_id.setter
    def smb2_open_group_id(self, val):
        if val != None:
            self.validate('smb2_open_group_id', val)
        self._smb2_open_group_id = val
    
    @staticmethod
    def get_api_name():
          return "share-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'smb2-open-type',
            'smb2-lock-time-remaining',
            'smb2-connect-state',
            'is-sharelock-soft',
            'is-sharelock-super',
            'mode',
            'smb2-open-group-id',
        ]
    
    def describe_properties(self):
        return {
            'smb2_open_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'smb2_lock_time_remaining': { 'class': int, 'is_list': False, 'required': 'optional' },
            'smb2_connect_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_sharelock_soft': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_sharelock_super': { 'class': bool, 'is_list': False, 'required': 'required' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'smb2_open_group_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
