from netapp.snapvault.snapvault_schedule_info import SnapvaultScheduleInfo
from netapp.snapvault.snapvault_schedule_options import SnapvaultScheduleOptions
from netapp.netapp_object import NetAppObject

class SnapvaultPrimarySnapshotScheduleInfo(NetAppObject):
    """
    Structure of each snapshot schedule.
    """
    
    _preserve_snapshots = None
    @property
    def preserve_snapshots(self):
        """
        Allowed values are on/off/default.
        It prevents SnapVault from auto-deleting older snapshots
        from this SnapVault snapshot schedule to create new
        snapshots when set to on.
        When unspecified, value is set to default.
        When set to default, the behaviour of preserving snapshots
        is guided by the global snapvault.preservesnap option.
        This setting is honoured only for the secondary schedules.
        It is ignored for the SnapVault primary schedules.
        """
        return self._preserve_snapshots
    @preserve_snapshots.setter
    def preserve_snapshots(self, val):
        if val != None:
            self.validate('preserve_snapshots', val)
        self._preserve_snapshots = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        Describes the actual schedule.
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _schedule_name = None
    @property
    def schedule_name(self):
        """
        Uniquely identifies this schedule within a primary
        volume. The schedule-name will be used as a prefix in
        the name of each snapshot created by this schedule.
        """
        return self._schedule_name
    @schedule_name.setter
    def schedule_name(self, val):
        if val != None:
            self.validate('schedule_name', val)
        self._schedule_name = val
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        The primary volume for which this schedule has been
        configured.
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _warn_at_count = None
    @property
    def warn_at_count(self):
        """
        On SnapVault secondary, when preserve-snapshots is set,
        SnapVault sends a warning message when the number of
        remaining snapshots for this backup schedule is less
        than this input. Setting this to zero turns off the
        same warning. Default value is 0.
        This setting is honoured only for the secondary schedules.
        It is ignored for the SnapVault primary schedules.
        Range:[0..retention-count - 1]
        """
        return self._warn_at_count
    @warn_at_count.setter
    def warn_at_count(self, val):
        if val != None:
            self.validate('warn_at_count', val)
        self._warn_at_count = val
    
    _is_auto_update = None
    @property
    def is_auto_update(self):
        """
        Schedules that have is-auto-update set to 'true' will
        initiate update transfers for all relationships in that
        volume before creating a new snapshot.
        Default value is 'false'.
        This setting is honoured only for the secondary schedules.
        It is ignored for the SnapVault primary schedules.
        """
        return self._is_auto_update
    @is_auto_update.setter
    def is_auto_update(self, val):
        if val != None:
            self.validate('is_auto_update', val)
        self._is_auto_update = val
    
    _retention_count = None
    @property
    def retention_count(self):
        """
        Denotes the maximum number of most recent snapshots
        that will be retained by this schedule.
        Range:[0..254]
        """
        return self._retention_count
    @retention_count.setter
    def retention_count(self, val):
        if val != None:
            self.validate('retention_count', val)
        self._retention_count = val
    
    _options = None
    @property
    def options(self):
        """
        Describes snapvault schedule options.
        """
        return self._options
    @options.setter
    def options(self, val):
        if val != None:
            self.validate('options', val)
        self._options = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-primary-snapshot-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'preserve-snapshots',
            'schedule',
            'schedule-name',
            'volume-name',
            'warn-at-count',
            'is-auto-update',
            'retention-count',
            'options',
        ]
    
    def describe_properties(self):
        return {
            'preserve_snapshots': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': SnapvaultScheduleInfo, 'is_list': False, 'required': 'optional' },
            'schedule_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'warn_at_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_auto_update': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'retention_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'options': { 'class': SnapvaultScheduleOptions, 'is_list': False, 'required': 'optional' },
        }
