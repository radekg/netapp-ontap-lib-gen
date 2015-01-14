from netapp.netapp_object import NetAppObject

class SnapvaultScheduleOptions(NetAppObject):
    """
    Describes snapvault schedule options.
    """
    
    _retention_period = None
    @property
    def retention_period(self):
        """
        This option is used to specify a retention period for
        snapshots, which are created by this schedule, for
        SnapLock volumes. The retention period is specified as a
        count followed by a suffix. the valid suffixes are
        d  - for days
        m  - for months
        y  - for years
        For example a value of 6m represents a retention period
        of 6 months. THe maximum valid retention period is 30
        years, or the maximum retention period set for the volume,
        whichever is shorter. The minimum valid retention period
        is 0 days, ir the minimum retention period set for the
        volume, whichever is longer. If the option value is
        default or the retention-period option is not specified,
        the snapshots will be created with retention period
        equal to the default retention period of the secondary
        SnapLock volume, or 30 years, whichever is shorter.
        """
        return self._retention_period
    @retention_period.setter
    def retention_period(self, val):
        if val != None:
            self.validate('retention_period', val)
        self._retention_period = val
    
    _tries_count = None
    @property
    def tries_count(self):
        """
        Number of times SnapVault should try creating each
        scheduled snapshot before giving up. If the snapshot
        creation fails due to transient errors such as the volume
        being out of space, SnapVault will keep trying to create
        the snapshot every minute untill the request is
        fulfilled. The allowed range is from 0 to 120. The
        default value is unlimited. If tries-count is not use,
        then the value will remain unchanged and the already
        configured value will be used.
        The default value for this option is -1.
        Range:[-1..120]
        """
        return self._tries_count
    @tries_count.setter
    def tries_count(self, val):
        if val != None:
            self.validate('tries_count', val)
        self._tries_count = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-schedule-options"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'retention-period',
            'tries-count',
        ]
    
    def describe_properties(self):
        return {
            'retention_period': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tries_count': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
