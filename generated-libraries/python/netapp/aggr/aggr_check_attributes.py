from netapp.netapp_object import NetAppObject

class AggrCheckAttributes(NetAppObject):
    """
    Information returned when upgrade-64bit-mode in
    aggr-add API is "check".
    """
    
    _cookie = None
    @property
    def cookie(self):
        """
        The opaque cookie to uniquely identify
        a 64-bit upgrade transaction previously
        triggered on the aggregate using aggr-add API.
        Range: [0..2^64-1].
        """
        return self._cookie
    @cookie.setter
    def cookie(self, val):
        if val != None:
            self.validate('cookie', val)
        self._cookie = val
    
    _check_last_errno = None
    @property
    def check_last_errno(self):
        """
        The error code of the last attempt to
        check for space usage on the specific
        aggregate. This field is present only
        if a previous 64-bit upgrade check
        failed. Possible values:
        0 - indicates success
        EVOLUME_64BIT_UPGRADE_KIREETI_NOT_AVAIL
        Per-volume upgrade check results may be
        out of date if last-errno is not 0.
        """
        return self._check_last_errno
    @check_last_errno.setter
    def check_last_errno(self, val):
        if val != None:
            self.validate('check_last_errno', val)
        self._check_last_errno = val
    
    _added_space = None
    @property
    def added_space(self):
        """
        The effective total space that would be added
        (in bytes) to the aggregate. This would not include
        the blocks used by the 64-bit upgrade of the aggregate
        and its contained flexible volumes.
        Range: [0..2^64-1].
        """
        return self._added_space
    @added_space.setter
    def added_space(self, val):
        if val != None:
            self.validate('added_space', val)
        self._added_space = val
    
    _is_space_estimate_complete = None
    @property
    def is_space_estimate_complete(self):
        """
        True if the space estimate has completed.
        Check "check-last-errno" to find out whether
        the space estimate was successful.
        """
        return self._is_space_estimate_complete
    @is_space_estimate_complete.setter
    def is_space_estimate_complete(self, val):
        if val != None:
            self.validate('is_space_estimate_complete', val)
        self._is_space_estimate_complete = val
    
    @staticmethod
    def get_api_name():
          return "aggr-check-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cookie',
            'check-last-errno',
            'added-space',
            'is-space-estimate-complete',
        ]
    
    def describe_properties(self):
        return {
            'cookie': { 'class': int, 'is_list': False, 'required': 'optional' },
            'check_last_errno': { 'class': int, 'is_list': False, 'required': 'optional' },
            'added_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_space_estimate_complete': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
