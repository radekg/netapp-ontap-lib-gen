from netapp.netapp_object import NetAppObject

class JobTypeInfo(NetAppObject):
    """
    Contains information about a specific job type.
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
    
    _job_type_is_pausible = None
    @property
    def job_type_is_pausible(self):
        """
        True means that the job may be paused during execution.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_pausible
    @job_type_is_pausible.setter
    def job_type_is_pausible(self, val):
        if val != None:
            self.validate('job_type_is_pausible', val)
        self._job_type_is_pausible = val
    
    _job_type_is_restartable = None
    @property
    def job_type_is_restartable(self):
        """
        True means that the job may be restarted following a
        failure or reboot.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_restartable
    @job_type_is_restartable.setter
    def job_type_is_restartable(self, val):
        if val != None:
            self.validate('job_type_is_restartable', val)
        self._job_type_is_restartable = val
    
    _job_type_is_auditable = None
    @property
    def job_type_is_auditable(self):
        """
        True means that the job execution requires audit
        records.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_auditable
    @job_type_is_auditable.setter
    def job_type_is_auditable(self, val):
        if val != None:
            self.validate('job_type_is_auditable', val)
        self._job_type_is_auditable = val
    
    _job_type_is_quittable = None
    @property
    def job_type_is_quittable(self):
        """
        Quittable?
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_quittable
    @job_type_is_quittable.setter
    def job_type_is_quittable(self, val):
        if val != None:
            self.validate('job_type_is_quittable', val)
        self._job_type_is_quittable = val
    
    _job_type_is_hidden = None
    @property
    def job_type_is_hidden(self):
        """
        True means that the job is hidden from the CLI for
        admin-level users.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_hidden
    @job_type_is_hidden.setter
    def job_type_is_hidden(self, val):
        if val != None:
            self.validate('job_type_is_hidden', val)
        self._job_type_is_hidden = val
    
    _job_type_is_deletable = None
    @property
    def job_type_is_deletable(self):
        """
        True means that jobs may be deleted from their queue.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_deletable
    @job_type_is_deletable.setter
    def job_type_is_deletable(self, val):
        if val != None:
            self.validate('job_type_is_deletable', val)
        self._job_type_is_deletable = val
    
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
    
    _job_type_id = None
    @property
    def job_type_id(self):
        """
        Job type's universally unique identifier (UUID).
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_id
    @job_type_id.setter
    def job_type_id(self, val):
        if val != None:
            self.validate('job_type_id', val)
        self._job_type_id = val
    
    _job_type_has_progress = None
    @property
    def job_type_has_progress(self):
        """
        True means the that job supports in-flight queries of its
        status.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_has_progress
    @job_type_has_progress.setter
    def job_type_has_progress(self, val):
        if val != None:
            self.validate('job_type_has_progress', val)
        self._job_type_has_progress = val
    
    _job_type_check_interval = None
    @property
    def job_type_check_interval(self):
        """
        The number of seconds that must elapse before pending
        jobs are reevaluated.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_check_interval
    @job_type_check_interval.setter
    def job_type_check_interval(self, val):
        if val != None:
            self.validate('job_type_check_interval', val)
        self._job_type_check_interval = val
    
    _job_type_run_if_did_not = None
    @property
    def job_type_run_if_did_not(self):
        """
        True means that jobs that are not scheduled because of
        outages should be run.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_run_if_did_not
    @job_type_run_if_did_not.setter
    def job_type_run_if_did_not(self, val):
        if val != None:
            self.validate('job_type_run_if_did_not', val)
        self._job_type_run_if_did_not = val
    
    _job_type = None
    @property
    def job_type(self):
        """
        Job type. For example, 'AggrCreate', 'VOL_CREATE'.  These
        are pre-defined in the system binaries. You can get an
        up-to-date list call job-type-get-iter without a query.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_type
    @job_type.setter
    def job_type(self, val):
        if val != None:
            self.validate('job_type', val)
        self._job_type = val
    
    _job_type_is_unique = None
    @property
    def job_type_is_unique(self):
        """
        True means that two jobs operating on the same task may
        not exist concurrently.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_unique
    @job_type_is_unique.setter
    def job_type_is_unique(self, val):
        if val != None:
            self.validate('job_type_is_unique', val)
        self._job_type_is_unique = val
    
    _job_type_replicate_local = None
    @property
    def job_type_replicate_local(self):
        """
        True means that server-affinity jobs must have their
        stateful data replicated.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_replicate_local
    @job_type_replicate_local.setter
    def job_type_replicate_local(self, val):
        if val != None:
            self.validate('job_type_replicate_local', val)
        self._job_type_replicate_local = val
    
    _job_type_run_if_would_have = None
    @property
    def job_type_run_if_would_have(self):
        """
        True means that jobs that are not scheduled because one
        of the same type was outsanding should be rescheduled.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_run_if_would_have
    @job_type_run_if_would_have.setter
    def job_type_run_if_would_have(self, val):
        if val != None:
            self.validate('job_type_run_if_would_have', val)
        self._job_type_run_if_would_have = val
    
    _job_type_is_exclusive = None
    @property
    def job_type_is_exclusive(self):
        """
        True means that the job type only allows one to be
        scheduled at a time.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_type_is_exclusive
    @job_type_is_exclusive.setter
    def job_type_is_exclusive(self, val):
        if val != None:
            self.validate('job_type_is_exclusive', val)
        self._job_type_is_exclusive = val
    
    @staticmethod
    def get_api_name():
          return "job-type-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-type-is-pausible',
            'job-type-is-restartable',
            'job-type-is-auditable',
            'job-type-is-quittable',
            'job-type-is-hidden',
            'job-type-is-deletable',
            'job-category',
            'job-type-id',
            'job-type-has-progress',
            'job-type-check-interval',
            'job-type-run-if-did-not',
            'job-type',
            'job-type-is-unique',
            'job-type-replicate-local',
            'job-type-run-if-would-have',
            'job-type-is-exclusive',
        ]
    
    def describe_properties(self):
        return {
            'job_type_is_pausible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_restartable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_auditable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_quittable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_hidden': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_deletable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_category': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_type_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_type_has_progress': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_check_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_type_run_if_did_not': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_type_is_unique': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_replicate_local': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_run_if_would_have': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_type_is_exclusive': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
