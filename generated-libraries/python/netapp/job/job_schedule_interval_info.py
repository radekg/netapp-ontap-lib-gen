from netapp.netapp_object import NetAppObject

class JobScheduleIntervalInfo(NetAppObject):
    """
    Contains detail information about interval job schedules.
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
    
    _job_schedule_description = None
    @property
    def job_schedule_description(self):
        """
        The description of the job schedule.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_schedule_description
    @job_schedule_description.setter
    def job_schedule_description(self, val):
        if val != None:
            self.validate('job_schedule_description', val)
        self._job_schedule_description = val
    
    _job_schedule_interval_minutes = None
    @property
    def job_schedule_interval_minutes(self):
        """
        The number of minutes between jobs.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_interval_minutes
    @job_schedule_interval_minutes.setter
    def job_schedule_interval_minutes(self, val):
        if val != None:
            self.validate('job_schedule_interval_minutes', val)
        self._job_schedule_interval_minutes = val
    
    _job_schedule_interval_seconds = None
    @property
    def job_schedule_interval_seconds(self):
        """
        The number of seconds between jobs.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_interval_seconds
    @job_schedule_interval_seconds.setter
    def job_schedule_interval_seconds(self, val):
        if val != None:
            self.validate('job_schedule_interval_seconds', val)
        self._job_schedule_interval_seconds = val
    
    _job_schedule_interval_hours = None
    @property
    def job_schedule_interval_hours(self):
        """
        The number of hours between jobs.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_interval_hours
    @job_schedule_interval_hours.setter
    def job_schedule_interval_hours(self, val):
        if val != None:
            self.validate('job_schedule_interval_hours', val)
        self._job_schedule_interval_hours = val
    
    _job_schedule_interval_days = None
    @property
    def job_schedule_interval_days(self):
        """
        The number of days between jobs.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_interval_days
    @job_schedule_interval_days.setter
    def job_schedule_interval_days(self, val):
        if val != None:
            self.validate('job_schedule_interval_days', val)
        self._job_schedule_interval_days = val
    
    _job_schedule_name = None
    @property
    def job_schedule_name(self):
        """
        The name of the job schedule.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._job_schedule_name
    @job_schedule_name.setter
    def job_schedule_name(self, val):
        if val != None:
            self.validate('job_schedule_name', val)
        self._job_schedule_name = val
    
    @staticmethod
    def get_api_name():
          return "job-schedule-interval-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-schedule-description',
            'job-schedule-interval-minutes',
            'job-schedule-interval-seconds',
            'job-schedule-interval-hours',
            'job-schedule-interval-days',
            'job-schedule-name',
        ]
    
    def describe_properties(self):
        return {
            'job_schedule_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_interval_minutes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_schedule_interval_seconds': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_schedule_interval_hours': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_schedule_interval_days': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_schedule_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
