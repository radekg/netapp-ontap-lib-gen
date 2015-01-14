from netapp.netapp_object import NetAppObject

class JobInfo(NetAppObject):
    """
    Contains information about a specific job.
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
    
    _job_status_code = None
    @property
    def job_status_code(self):
        """
        Status code. Value other than 0 indicates an error in the
        job execution, in which case 'job-completion' will
        contain human-readable information about the error.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_status_code
    @job_status_code.setter
    def job_status_code(self, val):
        if val != None:
            self.validate('job_status_code', val)
        self._job_status_code = val
    
    _job_dropdead_time = None
    @property
    def job_dropdead_time(self):
        """
        Discard the job if not started by this time.  The time
        value is in seconds since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_dropdead_time
    @job_dropdead_time.setter
    def job_dropdead_time(self, val):
        if val != None:
            self.validate('job_dropdead_time', val)
        self._job_dropdead_time = val
    
    _job_type = None
    @property
    def job_type(self):
        """
        Job type. For example, 'AggrCreate', 'VOL_CREATE'.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type
    @job_type.setter
    def job_type(self, val):
        if val != None:
            self.validate('job_type', val)
        self._job_type = val
    
    _job_end_time = None
    @property
    def job_end_time(self):
        """
        When the job finished running.  The time value is in
        seconds since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_end_time
    @job_end_time.setter
    def job_end_time(self, val):
        if val != None:
            self.validate('job_end_time', val)
        self._job_end_time = val
    
    _job_affinity = None
    @property
    def job_affinity(self):
        """
        Job affinity indicates whether this job is tied to a
        specific node or not.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "cluster"   - Cluster Affinity,
        <li> "node"      - Node Affinity
        </ul>
        """
        return self._job_affinity
    @job_affinity.setter
    def job_affinity(self, val):
        if val != None:
            self.validate('job_affinity', val)
        self._job_affinity = val
    
    _job_queue_time = None
    @property
    def job_queue_time(self):
        """
        When the job was queued.  The time value is in seconds
        since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_queue_time
    @job_queue_time.setter
    def job_queue_time(self, val):
        if val != None:
            self.validate('job_queue_time', val)
        self._job_queue_time = val
    
    _job_username = None
    @property
    def job_username(self):
        """
        The name of the user that created the job.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_username
    @job_username.setter
    def job_username(self, val):
        if val != None:
            self.validate('job_username', val)
        self._job_username = val
    
    _job_description = None
    @property
    def job_description(self):
        """
        Job description.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_description
    @job_description.setter
    def job_description(self, val):
        if val != None:
            self.validate('job_description', val)
        self._job_description = val
    
    _job_category = None
    @property
    def job_category(self):
        """
        Job category. For example, 'Aggregate', 'VOPL'.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_category
    @job_category.setter
    def job_category(self, val):
        if val != None:
            self.validate('job_category', val)
        self._job_category = val
    
    _job_vserver = None
    @property
    def job_vserver(self):
        """
        Vserver from which the job was created.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_vserver
    @job_vserver.setter
    def job_vserver(self, val):
        if val != None:
            self.validate('job_vserver', val)
        self._job_vserver = val
    
    _is_restarted = None
    @property
    def is_restarted(self):
        """
        Whether the job has been re-started.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_restarted
    @is_restarted.setter
    def is_restarted(self, val):
        if val != None:
            self.validate('is_restarted', val)
        self._is_restarted = val
    
    _job_start_time = None
    @property
    def job_start_time(self):
        """
        When the job started running.  The time value is in
        seconds since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_start_time
    @job_start_time.setter
    def job_start_time(self, val):
        if val != None:
            self.validate('job_start_time', val)
        self._job_start_time = val
    
    _job_progress = None
    @property
    def job_progress(self):
        """
        Information about the progress of this job.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_progress
    @job_progress.setter
    def job_progress(self, val):
        if val != None:
            self.validate('job_progress', val)
        self._job_progress = val
    
    _job_completion = None
    @property
    def job_completion(self):
        """
        Human-readable job completion text.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_completion
    @job_completion.setter
    def job_completion(self, val):
        if val != None:
            self.validate('job_completion', val)
        self._job_completion = val
    
    _job_node = None
    @property
    def job_node(self):
        """
        The id of the node where the job is run.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_node
    @job_node.setter
    def job_node(self, val):
        if val != None:
            self.validate('job_node', val)
        self._job_node = val
    
    _job_state = None
    @property
    def job_state(self):
        """
        Job state. See the category discussion section for a
        detailed description of job states.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "initial"        - Initializing,
        <li> "queued"         - Queued,
        <li> "running"        - Running,
        <li> "waiting"        - Waiting For Another Job,
        <li> "pausing"        - Entering Paused State,
        <li> "paused"         - Paused,
        <li> "quitting"       - Entering Quit State,
        <li> "success"        - Succeeded,
        <li> "failure"        - Failed,
        <li> "reschedule"     - Forcing Reschedule,
        <li> "error"          - Internal Error,
        <li> "quit"           - Quit,
        <li> "dead"           - Died,
        <li> "unknown"        - Unknown,
        <li> "restart"        - Forcing Restart,
        <li> "dormant"        - Waiting For External Event
        </ul>
        """
        return self._job_state
    @job_state.setter
    def job_state(self, val):
        if val != None:
            self.validate('job_state', val)
        self._job_state = val
    
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
    
    _job_name = None
    @property
    def job_name(self):
        """
        Name of the job.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_name
    @job_name.setter
    def job_name(self, val):
        if val != None:
            self.validate('job_name', val)
        self._job_name = val
    
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
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        Job's universally unique identifier (UUID).
        Attributes: non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    _job_process = None
    @property
    def job_process(self):
        """
        The name of the process responsible for running the job.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_process
    @job_process.setter
    def job_process(self, val):
        if val != None:
            self.validate('job_process', val)
        self._job_process = val
    
    _job_schedule = None
    @property
    def job_schedule(self):
        """
        The name of the job schedule.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_schedule
    @job_schedule.setter
    def job_schedule(self, val):
        if val != None:
            self.validate('job_schedule', val)
        self._job_schedule = val
    
    @staticmethod
    def get_api_name():
          return "job-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-status-code',
            'job-dropdead-time',
            'job-type',
            'job-end-time',
            'job-affinity',
            'job-queue-time',
            'job-username',
            'job-description',
            'job-category',
            'job-vserver',
            'is-restarted',
            'job-start-time',
            'job-progress',
            'job-completion',
            'job-node',
            'job-state',
            'job-id',
            'job-name',
            'job-priority',
            'job-uuid',
            'job-process',
            'job-schedule',
        ]
    
    def describe_properties(self):
        return {
            'job_status_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_dropdead_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_end_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_affinity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_queue_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_username': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_category': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_restarted': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_start_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_completion': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_priority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_process': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
