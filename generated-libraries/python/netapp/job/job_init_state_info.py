from netapp.netapp_object import NetAppObject

class JobInitStateInfo(NetAppObject):
    """
    Contains initialization state for a job manager instance.
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
    
    _job_mgr_low_priority_threads = None
    @property
    def job_mgr_low_priority_threads(self):
        """
        Number of low priority threads.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_low_priority_threads
    @job_mgr_low_priority_threads.setter
    def job_mgr_low_priority_threads(self, val):
        if val != None:
            self.validate('job_mgr_low_priority_threads', val)
        self._job_mgr_low_priority_threads = val
    
    _job_mgr_is_recovery_enabled = None
    @property
    def job_mgr_is_recovery_enabled(self):
        """
        Is job failover enabled?
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_is_recovery_enabled
    @job_mgr_is_recovery_enabled.setter
    def job_mgr_is_recovery_enabled(self, val):
        if val != None:
            self.validate('job_mgr_is_recovery_enabled', val)
        self._job_mgr_is_recovery_enabled = val
    
    _job_mgr_excl_priority_threads = None
    @property
    def job_mgr_excl_priority_threads(self):
        """
        Number of exclusive priority threads.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_excl_priority_threads
    @job_mgr_excl_priority_threads.setter
    def job_mgr_excl_priority_threads(self, val):
        if val != None:
            self.validate('job_mgr_excl_priority_threads', val)
        self._job_mgr_excl_priority_threads = val
    
    _job_mgr_is_initialized = None
    @property
    def job_mgr_is_initialized(self):
        """
        Job Manager is initialized.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_is_initialized
    @job_mgr_is_initialized.setter
    def job_mgr_is_initialized(self, val):
        if val != None:
            self.validate('job_mgr_is_initialized', val)
        self._job_mgr_is_initialized = val
    
    _job_mgr_site_id = None
    @property
    def job_mgr_site_id(self):
        """
        Job Manager site's universally unique identifier (UUID).
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_site_id
    @job_mgr_site_id.setter
    def job_mgr_site_id(self, val):
        if val != None:
            self.validate('job_mgr_site_id', val)
        self._job_mgr_site_id = val
    
    _job_mgr_med_priority_threads = None
    @property
    def job_mgr_med_priority_threads(self):
        """
        Number of medium priority threads.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_med_priority_threads
    @job_mgr_med_priority_threads.setter
    def job_mgr_med_priority_threads(self, val):
        if val != None:
            self.validate('job_mgr_med_priority_threads', val)
        self._job_mgr_med_priority_threads = val
    
    _job_mgr_init_msg = None
    @property
    def job_mgr_init_msg(self):
        """
        Initialization message.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_init_msg
    @job_mgr_init_msg.setter
    def job_mgr_init_msg(self, val):
        if val != None:
            self.validate('job_mgr_init_msg', val)
        self._job_mgr_init_msg = val
    
    _job_mgr_cache_root = None
    @property
    def job_mgr_cache_root(self):
        """
        Full path to the root of the Job Manager local RDB
        cache.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_cache_root
    @job_mgr_cache_root.setter
    def job_mgr_cache_root(self, val):
        if val != None:
            self.validate('job_mgr_cache_root', val)
        self._job_mgr_cache_root = val
    
    _job_mgr_node = None
    @property
    def job_mgr_node(self):
        """
        The name of the node hosting a job manager instance.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_mgr_node
    @job_mgr_node.setter
    def job_mgr_node(self, val):
        if val != None:
            self.validate('job_mgr_node', val)
        self._job_mgr_node = val
    
    _job_mgr_high_priority_threads = None
    @property
    def job_mgr_high_priority_threads(self):
        """
        Number of high priority threads.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_high_priority_threads
    @job_mgr_high_priority_threads.setter
    def job_mgr_high_priority_threads(self, val):
        if val != None:
            self.validate('job_mgr_high_priority_threads', val)
        self._job_mgr_high_priority_threads = val
    
    _job_mgr_rdb_commit_interval = None
    @property
    def job_mgr_rdb_commit_interval(self):
        """
        Interval between RDB commits.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_rdb_commit_interval
    @job_mgr_rdb_commit_interval.setter
    def job_mgr_rdb_commit_interval(self, val):
        if val != None:
            self.validate('job_mgr_rdb_commit_interval', val)
        self._job_mgr_rdb_commit_interval = val
    
    _job_mgr_process = None
    @property
    def job_mgr_process(self):
        """
        Process using Job Manager
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_mgr_process
    @job_mgr_process.setter
    def job_mgr_process(self, val):
        if val != None:
            self.validate('job_mgr_process', val)
        self._job_mgr_process = val
    
    _job_mgr_thread_init_msg = None
    @property
    def job_mgr_thread_init_msg(self):
        """
        Thread initialization message.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_mgr_thread_init_msg
    @job_mgr_thread_init_msg.setter
    def job_mgr_thread_init_msg(self, val):
        if val != None:
            self.validate('job_mgr_thread_init_msg', val)
        self._job_mgr_thread_init_msg = val
    
    @staticmethod
    def get_api_name():
          return "job-init-state-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-mgr-low-priority-threads',
            'job-mgr-is-recovery-enabled',
            'job-mgr-excl-priority-threads',
            'job-mgr-is-initialized',
            'job-mgr-site-id',
            'job-mgr-med-priority-threads',
            'job-mgr-init-msg',
            'job-mgr-cache-root',
            'job-mgr-node',
            'job-mgr-high-priority-threads',
            'job-mgr-rdb-commit-interval',
            'job-mgr-process',
            'job-mgr-thread-init-msg',
        ]
    
    def describe_properties(self):
        return {
            'job_mgr_low_priority_threads': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_mgr_is_recovery_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_mgr_excl_priority_threads': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_mgr_is_initialized': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_mgr_site_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_mgr_med_priority_threads': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_mgr_init_msg': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_mgr_cache_root': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_mgr_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_mgr_high_priority_threads': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_mgr_rdb_commit_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_mgr_process': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_mgr_thread_init_msg': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
