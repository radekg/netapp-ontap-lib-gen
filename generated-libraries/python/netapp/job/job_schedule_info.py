from netapp.netapp_object import NetAppObject

class JobScheduleInfo(NetAppObject):
    """
    Contains overview information about a single job schedule.
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
    
    _job_schedule_type = None
    @property
    def job_schedule_type(self):
        """
        The type of job schedule.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "cron"      ,
        <li> "interval"  ,
        <li> "builtin"   ,
        <li> "unknown"
        </ul>
        """
        return self._job_schedule_type
    @job_schedule_type.setter
    def job_schedule_type(self, val):
        if val != None:
            self.validate('job_schedule_type', val)
        self._job_schedule_type = val
    
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
          return "job-schedule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-schedule-description',
            'job-schedule-type',
            'job-schedule-name',
        ]
    
    def describe_properties(self):
        return {
            'job_schedule_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
