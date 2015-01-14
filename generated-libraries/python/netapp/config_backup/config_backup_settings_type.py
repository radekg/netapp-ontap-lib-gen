from netapp.netapp_object import NetAppObject

class ConfigBackupSettingsType(NetAppObject):
    """
    Configuration Backup Settings
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _job_schedule2 = None
    @property
    def job_schedule2(self):
        """
        The name of the second job schedule for generating
        configuration backups. It is pre-programmed to be
        'daily'.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_schedule2
    @job_schedule2.setter
    def job_schedule2(self, val):
        if val != None:
            self.validate('job_schedule2', val)
        self._job_schedule2 = val
    
    _job_schedule3 = None
    @property
    def job_schedule3(self):
        """
        The name of the third job schedule for generating
        configuration backups. It is pre-programmed to be
        'weekly'.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_schedule3
    @job_schedule3.setter
    def job_schedule3(self, val):
        if val != None:
            self.validate('job_schedule3', val)
        self._job_schedule3 = val
    
    _job_schedule1 = None
    @property
    def job_schedule1(self):
        """
        The name of the first job schedule for generating
        configuration backups. It is pre-programmed to be
        '8hour'.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_schedule1
    @job_schedule1.setter
    def job_schedule1(self, val):
        if val != None:
            self.validate('job_schedule1', val)
        self._job_schedule1 = val
    
    _destination_url = None
    @property
    def destination_url(self):
        """
        The destination URL for uploading the configuration
        backups. URL is specified following the syntax described
        in RFC 3986. Only 'ftp', 'http' and 'https' protocols are
        supported.
        Attributes: non-creatable, modifiable
        """
        return self._destination_url
    @destination_url.setter
    def destination_url(self, val):
        if val != None:
            self.validate('destination_url', val)
        self._destination_url = val
    
    _username_for_destination_url = None
    @property
    def username_for_destination_url(self):
        """
        The username for the destination URL.
        Attributes: non-creatable, modifiable
        """
        return self._username_for_destination_url
    @username_for_destination_url.setter
    def username_for_destination_url(self, val):
        if val != None:
            self.validate('username_for_destination_url', val)
        self._username_for_destination_url = val
    
    _backup_count1 = None
    @property
    def backup_count1(self):
        """
        The number of configuration backups to keep in the
        cluster for schedule 1.
        Attributes: non-creatable, modifiable
        """
        return self._backup_count1
    @backup_count1.setter
    def backup_count1(self, val):
        if val != None:
            self.validate('backup_count1', val)
        self._backup_count1 = val
    
    _backup_count3 = None
    @property
    def backup_count3(self):
        """
        The number of configuration backups to keep in the
        cluster for schedule 3.
        Attributes: non-creatable, modifiable
        """
        return self._backup_count3
    @backup_count3.setter
    def backup_count3(self, val):
        if val != None:
            self.validate('backup_count3', val)
        self._backup_count3 = val
    
    _backup_count2 = None
    @property
    def backup_count2(self):
        """
        The number of configuration backups to keep in the
        cluster for schedule 2.
        Attributes: non-creatable, modifiable
        """
        return self._backup_count2
    @backup_count2.setter
    def backup_count2(self, val):
        if val != None:
            self.validate('backup_count2', val)
        self._backup_count2 = val
    
    @staticmethod
    def get_api_name():
          return "config-backup-settings-type"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-schedule2',
            'job-schedule3',
            'job-schedule1',
            'destination-url',
            'username-for-destination-url',
            'backup-count1',
            'backup-count3',
            'backup-count2',
        ]
    
    def describe_properties(self):
        return {
            'job_schedule2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'username_for_destination_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backup_count1': { 'class': int, 'is_list': False, 'required': 'optional' },
            'backup_count3': { 'class': int, 'is_list': False, 'required': 'optional' },
            'backup_count2': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
