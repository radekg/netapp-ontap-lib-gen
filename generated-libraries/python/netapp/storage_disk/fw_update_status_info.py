from netapp.netapp_object import NetAppObject

class FwUpdateStatusInfo(NetAppObject):
    """
    List of disks that are pending updates, but not
    able to be updated.
    """
    
    _update_completion = None
    @property
    def update_completion(self):
        """
        Estimate for background firmware download
        completion in minutes.
        """
        return self._update_completion
    @update_completion.setter
    def update_completion(self, val):
        if val != None:
            self.validate('update_completion', val)
        self._update_completion = val
    
    _update_unable = None
    @property
    def update_unable(self):
        """
        Name of disk that cannot be updated.
        """
        return self._update_unable
    @update_unable.setter
    def update_unable(self, val):
        if val != None:
            self.validate('update_unable', val)
        self._update_unable = val
    
    _waiting_disks = None
    @property
    def waiting_disks(self):
        """
        The number of disks waiting for firmware update.
        """
        return self._waiting_disks
    @waiting_disks.setter
    def waiting_disks(self, val):
        if val != None:
            self.validate('waiting_disks', val)
        self._waiting_disks = val
    
    _avg_duration = None
    @property
    def avg_duration(self):
        """
        Average firmware update duration per disk
        in seconds.
        """
        return self._avg_duration
    @avg_duration.setter
    def avg_duration(self, val):
        if val != None:
            self.validate('avg_duration', val)
        self._avg_duration = val
    
    @staticmethod
    def get_api_name():
          return "fw-update-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'update-completion',
            'update-unable',
            'waiting-disks',
            'avg-duration',
        ]
    
    def describe_properties(self):
        return {
            'update_completion': { 'class': int, 'is_list': False, 'required': 'optional' },
            'update_unable': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'waiting_disks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'avg_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
