from netapp.netapp_object import NetAppObject

class AggrStartAttributes(NetAppObject):
    """
    Information returned when upgrade-64bit-mode in
    aggr-add API is "grow_all", "grow_none",
    or "grow_reserved".
    """
    
    _min_space_for_upgrade = None
    @property
    def min_space_for_upgrade(self):
        """
        The minimum additional disk space
        (in bytes) required to trigger 64-bit
        upgrade. This field is present when the
        specified disks do not have sufficient
        space to upgrade the aggregate and its
        contained flexible volumes to 64-bit.
        Range: [0..2^64-1].
        """
        return self._min_space_for_upgrade
    @min_space_for_upgrade.setter
    def min_space_for_upgrade(self, val):
        if val != None:
            self.validate('min_space_for_upgrade', val)
        self._min_space_for_upgrade = val
    
    _start_last_errno = None
    @property
    def start_last_errno(self):
        """
        The error code of the last attempt to
        start 64-bit upgrade on the specific
        aggregate. This field is present only
        if a previous 64-bit upgrade failed.
        Possible values include:
        EAGGR_64BIT_UPGRADE_ENOSPC
        EVOLUME_64BIT_UPGRADE_VVOL_ENOSPC
        EVOLUME_64BIT_UPGRADE_VVOL_ENOSPC_OVERWRITE
        EVOLUME_64BIT_UPGRADE_KIREETI_NOT_AVAIL
        EVOLUME_64BIT_UPGRADE_PREQUAL_NOT_AVAIL
        """
        return self._start_last_errno
    @start_last_errno.setter
    def start_last_errno(self, val):
        if val != None:
            self.validate('start_last_errno', val)
        self._start_last_errno = val
    
    @staticmethod
    def get_api_name():
          return "aggr-start-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'min-space-for-upgrade',
            'start-last-errno',
        ]
    
    def describe_properties(self):
        return {
            'min_space_for_upgrade': { 'class': int, 'is_list': False, 'required': 'optional' },
            'start_last_errno': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
