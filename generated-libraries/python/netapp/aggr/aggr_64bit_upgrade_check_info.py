from netapp.netapp_object import NetAppObject

class Aggr64BitUpgradeCheckInfo(NetAppObject):
    """
    Information returned when upgrade-64bit-mode in
    aggr-add or aggr-64bit-upgrade-start is "check".
    """
    
    _added_space = None
    @property
    def added_space(self):
        """
        The effective total space to be added
        (in bytes), not including blocks used
        by the 64-bit upgrade of the aggregate
        and its contained flexible volumes.
        Range: [0..2^64-1].
        """
        return self._added_space
    @added_space.setter
    def added_space(self, val):
        if val != None:
            self.validate('added_space', val)
        self._added_space = val
    
    _cookie = None
    @property
    def cookie(self):
        """
        The opaque cookie to uniquely identify
        a 64-bit upgrade transaction previously
        triggered on the aggregate.
        Range: [0..2^64-1].
        """
        return self._cookie
    @cookie.setter
    def cookie(self, val):
        if val != None:
            self.validate('cookie', val)
        self._cookie = val
    
    _space_estimate_complete = None
    @property
    def space_estimate_complete(self):
        """
        True if the space estimate has
        completed. Check "last-errno" to find
        out whether the space estimate was
        successful.
        """
        return self._space_estimate_complete
    @space_estimate_complete.setter
    def space_estimate_complete(self, val):
        if val != None:
            self.validate('space_estimate_complete', val)
        self._space_estimate_complete = val
    
    _last_errno = None
    @property
    def last_errno(self):
        """
        The error code of the last attempt to
        check for space usage on the specific
        aggregate. This field is present only
        if a 64-bit upgrade check was previously
        attempted. Possible values:
        0 - indicates success
        EVOLUME_64BIT_UPGRADE_KIREETI_NOT_AVAIL
        Per-volume upgrade check results may be
        out of date if last-errno is not 0.
        """
        return self._last_errno
    @last_errno.setter
    def last_errno(self, val):
        if val != None:
            self.validate('last_errno', val)
        self._last_errno = val
    
    @staticmethod
    def get_api_name():
          return "aggr-64bit-upgrade-check-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'added-space',
            'cookie',
            'space-estimate-complete',
            'last-errno',
        ]
    
    def describe_properties(self):
        return {
            'added_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cookie': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_estimate_complete': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_errno': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
