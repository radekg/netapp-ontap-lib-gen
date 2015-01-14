from netapp.netapp_object import NetAppObject

class SnapshotScheduleInfo(NetAppObject):
    """
    Information about individual snapshot schedules
    """
    
    _count = None
    @property
    def count(self):
        """
        Maximum number of snapshots to retain for the schedule
        present in the snapshot policy.
        Attributes: non-creatable, non-modifiable
        """
        return self._count
    @count.setter
    def count(self, val):
        if val != None:
            self.validate('count', val)
        self._count = val
    
    _prefix = None
    @property
    def prefix(self):
        """
        Snapshot name prefix for the schedule present in the
        snapshot policy. Prefix will be used in the snapshot name
        instead of the schedule name. If prefix is not provided,
        schedule name will be used in the snapshot name. For eg,
        if the prefix name 'hourly-even' is assigned to the
        schedule name 'hourly' then the snapshot name will look
        like 'hourly-even.2010-05-10_0205'. If no prefix is
        associated with the schedule 'hourly' then prefix will be
        set to 'hourly' as the default value.
        Attributes: non-creatable, non-modifiable
        """
        return self._prefix
    @prefix.setter
    def prefix(self, val):
        if val != None:
            self.validate('prefix', val)
        self._prefix = val
    
    _snapmirror_label = None
    @property
    def snapmirror_label(self):
        """
        Snapshot SnapMirror Label for the schedule present in the
        snapshot policy. The value specified will be added as an
        attribute to the snapshot created by the schedule. The
        maximum length of this field is 31 characters
        Attributes: required-for-create, modifiable
        """
        return self._snapmirror_label
    @snapmirror_label.setter
    def snapmirror_label(self, val):
        if val != None:
            self.validate('snapmirror_label', val)
        self._snapmirror_label = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        A human readable string describing the name of a schedule
        present in the snapshot policy. Maximum length of this
        field can be 255 characters. The schedule name can be any
        one of the reserved schedules like 'hourly',
        'weekly','daily' or it can be a user created schedule.
        Attributes: non-creatable, non-modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'count',
            'prefix',
            'snapmirror-label',
            'schedule',
        ]
    
    def describe_properties(self):
        return {
            'count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'prefix': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapmirror_label': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
