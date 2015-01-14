from netapp.netapp_object import NetAppObject

class JobHistoryInfo(NetAppObject):
    """
    Job history log event
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
    
    _job_end_time = None
    @property
    def job_end_time(self):
        """
        When the job last completed. The time value is in seconds
        since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_end_time
    @job_end_time.setter
    def job_end_time(self, val):
        if val != None:
            self.validate('job_end_time', val)
        self._job_end_time = val
    
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
    
    _job_event_time = None
    @property
    def job_event_time(self):
        """
        The time when this event was logged.  The time value is
        in seconds since January 1, 1970.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_event_time
    @job_event_time.setter
    def job_event_time(self, val):
        if val != None:
            self.validate('job_event_time', val)
        self._job_event_time = val
    
    _job_event_type = None
    @property
    def job_event_type(self):
        """
        The type of this history event.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "idle"      - The job has become idle,
        <li> "running"   - The job has started running,
        <li> "succeeded" - The job has completed successfully,
        <li> "failed"    - The job has completed with a
        failure,
        <li> "paused"    - The job has been paused,
        <li> "stopped"   - The job has been stopped,
        <li> "deleted"   - The job has been deleted,
        <li> "error"     - Job Manager experienced an error
        while processing the job
        </ul>
        """
        return self._job_event_type
    @job_event_type.setter
    def job_event_type(self, val):
        if val != None:
            self.validate('job_event_type', val)
        self._job_event_type = val
    
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
    
    _job_start_time = None
    @property
    def job_start_time(self):
        """
        When the job last started.  The time value is in seconds
        since January 1, 1970.
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
        Human-readable job progress message.
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
        Human-readable job completion message.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_completion
    @job_completion.setter
    def job_completion(self, val):
        if val != None:
            self.validate('job_completion', val)
        self._job_completion = val
    
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
    
    _job_manager_error_code = None
    @property
    def job_manager_error_code(self):
        """
        The error code, if any, that the Job Manager associated
        with this event. If set, 'job-error-text' will contain
        human-readable information about the error.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_manager_error_code
    @job_manager_error_code.setter
    def job_manager_error_code(self, val):
        if val != None:
            self.validate('job_manager_error_code', val)
        self._job_manager_error_code = val
    
    _job_manager_error_text = None
    @property
    def job_manager_error_text(self):
        """
        The human-readable text for the error code, if any, that
        the Job Manager associated with this event.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_manager_error_text
    @job_manager_error_text.setter
    def job_manager_error_text(self, val):
        if val != None:
            self.validate('job_manager_error_text', val)
        self._job_manager_error_text = val
    
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
    
    _job_node = None
    @property
    def job_node(self):
        """
        The name of the node where the job ran, or the node that
        changed the job's state.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_node
    @job_node.setter
    def job_node(self, val):
        if val != None:
            self.validate('job_node', val)
        self._job_node = val
    
    _job_id = None
    @property
    def job_id(self):
        """
        The identifier associated with this job by the Job
        Manager. This identifier is unique within a cluster. The
        'job-history-get-iter' API can return multiple records
        for a given job identifier because it logs the state
        transitions that the job has been through.  Records in
        the 'job-history-get-iter' API are returned in reverse
        chronological order.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
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
    
    _log_id = None
    @property
    def log_id(self):
        """
        The internal identifier of this job history event.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._log_id
    @log_id.setter
    def log_id(self, val):
        if val != None:
            self.validate('log_id', val)
        self._log_id = val
    
    @staticmethod
    def get_api_name():
          return "job-history-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-end-time',
            'job-name',
            'job-event-time',
            'job-event-type',
            'job-status-code',
            'job-start-time',
            'job-progress',
            'job-completion',
            'job-uuid',
            'job-manager-error-code',
            'job-manager-error-text',
            'job-vserver',
            'job-username',
            'job-node',
            'job-id',
            'job-description',
            'log-id',
        ]
    
    def describe_properties(self):
        return {
            'job_end_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_event_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_event_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_status_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_start_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_completion': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_manager_error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_manager_error_text': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_username': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'log_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
