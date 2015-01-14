from netapp.netapp_object import NetAppObject

class MaintAbortStatusInfo(NetAppObject):
    """
    Maintenance Center abort test information.
    """
    
    _status = None
    @property
    def status(self):
        """
        status
        Possible values are: "aborting", "not-testing",
        "disk-not-found", and "abort-failed".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        name of disk.
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    @staticmethod
    def get_api_name():
          return "maint-abort-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'disk-name',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
