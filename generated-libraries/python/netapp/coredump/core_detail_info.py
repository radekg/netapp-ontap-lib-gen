from netapp.netapp_object import NetAppObject

class CoreDetailInfo(NetAppObject):
    """
    All important information about a single core in the
    system.
    """
    
    _is_saved = None
    @property
    def is_saved(self):
        """
        True if this core has already been saved.
        """
        return self._is_saved
    @is_saved.setter
    def is_saved(self, val):
        if val != None:
            self.validate('is_saved', val)
        self._is_saved = val
    
    _is_partial = None
    @property
    def is_partial(self):
        """
        True if the core is a partial core.  Partial
        cores are missing disks.  This is only
        returned if saved is false.
        """
        return self._is_partial
    @is_partial.setter
    def is_partial(self, val):
        if val != None:
            self.validate('is_partial', val)
        self._is_partial = val
    
    _corename = None
    @property
    def corename(self):
        """
        The name of the core file.  For unsaved cores,
        this is the name the core file will have once
        the core is saved.
        """
        return self._corename
    @corename.setter
    def corename(self, val):
        if val != None:
            self.validate('corename', val)
        self._corename = val
    
    _coreid = None
    @property
    def coreid(self):
        """
        A handle that can be used with coredump-remove
        or coredump-save to remove/save specific cores.
        Range : [0..2^63-1].
        """
        return self._coreid
    @coreid.setter
    def coreid(self, val):
        if val != None:
            self.validate('coreid', val)
        self._coreid = val
    
    _sysid = None
    @property
    def sysid(self):
        """
        The system id of the system that generated
        this core.  Range : [0..2^31-1].
        """
        return self._sysid
    @sysid.setter
    def sysid(self, val):
        if val != None:
            self.validate('sysid', val)
        self._sysid = val
    
    _attempts = None
    @property
    def attempts(self):
        """
        The number of attempts that have been made to
        save an unsaved core.  This is only returned
        if saved is false.  Range : [0..2^31-1].
        """
        return self._attempts
    @attempts.setter
    def attempts(self, val):
        if val != None:
            self.validate('attempts', val)
        self._attempts = val
    
    _fs_bytes_needed = None
    @property
    def fs_bytes_needed(self):
        """
        The maximum number of bytes needed in the
        root filesystem to save	this core.  This is
        only returned if saved is false.
        Range : [0..2^63-1].
        """
        return self._fs_bytes_needed
    @fs_bytes_needed.setter
    def fs_bytes_needed(self, val):
        if val != None:
            self.validate('fs_bytes_needed', val)
        self._fs_bytes_needed = val
    
    _panic_string = None
    @property
    def panic_string(self):
        """
        The panic string for the panic that generated
        this core.
        """
        return self._panic_string
    @panic_string.setter
    def panic_string(self, val):
        if val != None:
            self.validate('panic_string', val)
        self._panic_string = val
    
    _os_version = None
    @property
    def os_version(self):
        """
        The version of Data ONTAP that generated this core.
        """
        return self._os_version
    @os_version.setter
    def os_version(self, val):
        if val != None:
            self.validate('os_version', val)
        self._os_version = val
    
    _panic_time = None
    @property
    def panic_time(self):
        """
        The time of the panic that generated this core.
        It is specified in seconds since the epoch.
        Range : [0..2^31-1].
        """
        return self._panic_time
    @panic_time.setter
    def panic_time(self, val):
        if val != None:
            self.validate('panic_time', val)
        self._panic_time = val
    
    @staticmethod
    def get_api_name():
          return "core-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-saved',
            'is-partial',
            'corename',
            'coreid',
            'sysid',
            'attempts',
            'fs-bytes-needed',
            'panic-string',
            'os-version',
            'panic-time',
        ]
    
    def describe_properties(self):
        return {
            'is_saved': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_partial': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'corename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'coreid': { 'class': int, 'is_list': False, 'required': 'required' },
            'sysid': { 'class': int, 'is_list': False, 'required': 'required' },
            'attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fs_bytes_needed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'panic_string': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'os_version': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'panic_time': { 'class': int, 'is_list': False, 'required': 'required' },
        }
