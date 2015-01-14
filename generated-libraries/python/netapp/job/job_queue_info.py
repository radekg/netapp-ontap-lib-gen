from netapp.netapp_object import NetAppObject

class JobQueueInfo(NetAppObject):
    """
    Contains information about a single queued job.
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
    
    _job_priority = None
    @property
    def job_priority(self):
        """
        Job priority.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "low"       ,
        <li> "medium"    ,
        <li> "high"      ,
        <li> "exclusive"
        </ul>
        """
        return self._job_priority
    @job_priority.setter
    def job_priority(self, val):
        if val != None:
            self.validate('job_priority', val)
        self._job_priority = val
    
    _job_scheduled_time = None
    @property
    def job_scheduled_time(self):
        """
        Job schedule expiry.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_scheduled_time
    @job_scheduled_time.setter
    def job_scheduled_time(self, val):
        if val != None:
            self.validate('job_scheduled_time', val)
        self._job_scheduled_time = val
    
    _job_queue = None
    @property
    def job_queue(self):
        """
        Job queue name.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "queued"              ,
        <li> "runnable"            ,
        <li> "cluster_queued"      ,
        <li> "cluster_runnable"    ,
        <li> "pending"             ,
        <li> "paused"              ,
        <li> "cleanup"             ,
        <li> "startup"             ,
        <li> "shutdown"
        </ul>
        """
        return self._job_queue
    @job_queue.setter
    def job_queue(self, val):
        if val != None:
            self.validate('job_queue', val)
        self._job_queue = val
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        Job's universally unique identifier (UUID).
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    @staticmethod
    def get_api_name():
          return "job-queue-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-priority',
            'job-scheduled-time',
            'job-queue',
            'job-uuid',
        ]
    
    def describe_properties(self):
        return {
            'job_priority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_scheduled_time': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_queue': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
