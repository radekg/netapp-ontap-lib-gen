from netapp.netapp_object import NetAppObject

class MaintStartStatusInfo(NetAppObject):
    """
    Status of starting Maintenance Center tests.
    """
    
    _status = None
    @property
    def status(self):
        """
        status
        Possible values are: "starting", "disk-not-found",
        "already-degraded", "disk-not-available",
        "disk-already-prefailed", and "max-disks-testing".
        "starting" means that the disk is starting maintenance testing or that
        a filesystem disk has been marked for copying and testing will begin when
        the copy completes.
        "already degraded" is returned for a filesystem disk if is-immediate is
        selected and the disk can't be removed from the RAID group because removing
        it would cause the volume to fail.
        "disk-already-prefailed" is returned for a filesystem disk that is already
        marked for copy if is-immediate is not selected. If is-immediate is selected
        the copy will be aborted, the disk will start testing, and "starting" will be
        returned.
        "disk-not-available" is returned if the disk is not available for testing.
        Filesystem disks and Spare disks may be tested. Failed disks and disks already
        being tested will return "disk-not-available".
        "disk-not-found" is returned if the disk name is not found.
        "max-disks-testing" is returned if the maximum number of disks allowed to be
        testing is reached. More disks may start testing when some currently testing
        disks finish.
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
          return "maint-start-status-info"
    
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
