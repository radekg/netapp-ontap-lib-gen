from netapp.netapp_object import NetAppObject

class Volume64BitUpgradeCheckAttributes(NetAppObject):
    """
    Information returned when 'upgrade-64bit-mode' in 'aggr-add' is
    'check'.
    """
    
    _used_space = None
    @property
    def used_space(self):
        """
        Amount of space (in bytes) that would be used in the
        volume after it is upgraded to 64-bit.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._used_space
    @used_space.setter
    def used_space(self, val):
        if val != None:
            self.validate('used_space', val)
        self._used_space = val
    
    _capacity = None
    @property
    def capacity(self):
        """
        Percentage of space that would be used in the volume
        after it is upgraded to 64-bit.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._capacity
    @capacity.setter
    def capacity(self, val):
        if val != None:
            self.validate('capacity', val)
        self._capacity = val
    
    _age = None
    @property
    def age(self):
        """
        The age in seconds of the space check results.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._age
    @age.setter
    def age(self, val):
        if val != None:
            self.validate('age', val)
        self._age = val
    
    _grow_space = None
    @property
    def grow_space(self):
        """
        Amount of space (in bytes) the volume must be grown by
        before successfully upgrading its current data.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._grow_space
    @grow_space.setter
    def grow_space(self, val):
        if val != None:
            self.validate('grow_space', val)
        self._grow_space = val
    
    _check_last_errno = None
    @property
    def check_last_errno(self):
        """
        The error code of the last attempt to check for space
        usage on the specific volume. This field is present only
        if a 64-bit upgrade check was previously attempted.
        Possible values:
        0 - indicates success
        EVOLUME_64BIT_UPGRADE_KIREETI_NOT_AVAIL
        Upgrade check results may be out of date if
        check-last-errno is not 0.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._check_last_errno
    @check_last_errno.setter
    def check_last_errno(self, val):
        if val != None:
            self.validate('check_last_errno', val)
        self._check_last_errno = val
    
    _available_space = None
    @property
    def available_space(self):
        """
        Amount of space (in bytes) that would be available in the
        volume after it is upgraded to 64-bit.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._available_space
    @available_space.setter
    def available_space(self, val):
        if val != None:
            self.validate('available_space', val)
        self._available_space = val
    
    @staticmethod
    def get_api_name():
          return "volume-64bit-upgrade-check-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'used-space',
            'capacity',
            'age',
            'grow-space',
            'check-last-errno',
            'available-space',
        ]
    
    def describe_properties(self):
        return {
            'used_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'grow_space': { 'class': int, 'is_list': False, 'required': 'optional' },
            'check_last_errno': { 'class': int, 'is_list': False, 'required': 'optional' },
            'available_space': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
