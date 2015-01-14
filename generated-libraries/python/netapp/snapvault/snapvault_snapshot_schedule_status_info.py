from netapp.netapp_object import NetAppObject

class SnapvaultSnapshotScheduleStatusInfo(NetAppObject):
    """
    Structure of the snapshot schedule status entry.
    """
    
    _status = None
    @property
    def status(self):
        """
        Status of this schedule. Possible values are: "Idle",
        "Active", "Aborting", "Queued", "Saving".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        Volume for which this schedule is configured.
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _schedule_name = None
    @property
    def schedule_name(self):
        """
        Uniquely identifies schedule within a volume.
        """
        return self._schedule_name
    @schedule_name.setter
    def schedule_name(self, val):
        if val != None:
            self.validate('schedule_name', val)
        self._schedule_name = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-snapshot-schedule-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'volume-name',
            'schedule-name',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'schedule_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
