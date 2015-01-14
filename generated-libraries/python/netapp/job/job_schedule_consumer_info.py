from netapp.netapp_object import NetAppObject

class JobScheduleConsumerInfo(NetAppObject):
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
    
    _job_id = None
    @property
    def job_id(self):
        """
        The job id.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
    _job_consumer_owner = None
    @property
    def job_consumer_owner(self):
        """
        The node where the job is scheduled.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_consumer_owner
    @job_consumer_owner.setter
    def job_consumer_owner(self, val):
        if val != None:
            self.validate('job_consumer_owner', val)
        self._job_consumer_owner = val
    
    _job_consumer_affinity = None
    @property
    def job_consumer_affinity(self):
        """
        The scheduling affinity of the job.  Affinity is used to
        indicate whether scheduling is independent (cluster) or
        specific (node) to a specific compute location in the
        cluster.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "cluster"   - Cluster Affinity,
        <li> "node"      - Node Affinity
        </ul>
        """
        return self._job_consumer_affinity
    @job_consumer_affinity.setter
    def job_consumer_affinity(self, val):
        if val != None:
            self.validate('job_consumer_affinity', val)
        self._job_consumer_affinity = val
    
    _job_schedule_name = None
    @property
    def job_schedule_name(self):
        """
        The name of the job schedule.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_schedule_name
    @job_schedule_name.setter
    def job_schedule_name(self, val):
        if val != None:
            self.validate('job_schedule_name', val)
        self._job_schedule_name = val
    
    _job_name = None
    @property
    def job_name(self):
        """
        Name of the job.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_name
    @job_name.setter
    def job_name(self, val):
        if val != None:
            self.validate('job_name', val)
        self._job_name = val
    
    @staticmethod
    def get_api_name():
          return "job-schedule-consumer-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-id',
            'job-consumer-owner',
            'job-consumer-affinity',
            'job-schedule-name',
            'job-name',
        ]
    
    def describe_properties(self):
        return {
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_consumer_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_consumer_affinity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
