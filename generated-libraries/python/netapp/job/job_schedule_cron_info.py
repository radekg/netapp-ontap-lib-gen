from netapp.netapp_object import NetAppObject

class JobScheduleCronInfo(NetAppObject):
    """
    Contains detail information about cron job schedules.
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
    
    _job_schedule_cron_day = None
    @property
    def job_schedule_cron_day(self):
        """
        The day(s) of the month when the job should be run.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_cron_day
    @job_schedule_cron_day.setter
    def job_schedule_cron_day(self, val):
        if val != None:
            self.validate('job_schedule_cron_day', val)
        self._job_schedule_cron_day = val
    
    _job_schedule_cron_minute = None
    @property
    def job_schedule_cron_minute(self):
        """
        The minute(s) of each hour when the job should be run.
        Attributes: required-for-create, modifiable
        """
        return self._job_schedule_cron_minute
    @job_schedule_cron_minute.setter
    def job_schedule_cron_minute(self, val):
        if val != None:
            self.validate('job_schedule_cron_minute', val)
        self._job_schedule_cron_minute = val
    
    _job_schedule_cron_month = None
    @property
    def job_schedule_cron_month(self):
        """
        The month(s) when the job should be run.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_cron_month
    @job_schedule_cron_month.setter
    def job_schedule_cron_month(self, val):
        if val != None:
            self.validate('job_schedule_cron_month', val)
        self._job_schedule_cron_month = val
    
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
    
    _job_schedule_cron_hour = None
    @property
    def job_schedule_cron_hour(self):
        """
        The hour(s) of the day when the job should be run.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_cron_hour
    @job_schedule_cron_hour.setter
    def job_schedule_cron_hour(self, val):
        if val != None:
            self.validate('job_schedule_cron_hour', val)
        self._job_schedule_cron_hour = val
    
    _job_schedule_cron_day_of_week = None
    @property
    def job_schedule_cron_day_of_week(self):
        """
        The day(s) in the week when the job should be run.
        Attributes: optional-for-create, modifiable
        """
        return self._job_schedule_cron_day_of_week
    @job_schedule_cron_day_of_week.setter
    def job_schedule_cron_day_of_week(self, val):
        if val != None:
            self.validate('job_schedule_cron_day_of_week', val)
        self._job_schedule_cron_day_of_week = val
    
    @staticmethod
    def get_api_name():
          return "job-schedule-cron-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-schedule-description',
            'job-schedule-cron-day',
            'job-schedule-cron-minute',
            'job-schedule-cron-month',
            'job-schedule-name',
            'job-schedule-cron-hour',
            'job-schedule-cron-day-of-week',
        ]
    
    def describe_properties(self):
        return {
            'job_schedule_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_cron_day': { 'class': int, 'is_list': True, 'required': 'optional' },
            'job_schedule_cron_minute': { 'class': int, 'is_list': True, 'required': 'optional' },
            'job_schedule_cron_month': { 'class': int, 'is_list': True, 'required': 'optional' },
            'job_schedule_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_cron_hour': { 'class': int, 'is_list': True, 'required': 'optional' },
            'job_schedule_cron_day_of_week': { 'class': int, 'is_list': True, 'required': 'optional' },
        }
