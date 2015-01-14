from netapp.netapp_object import NetAppObject

class CoreSegmentStatusInfo(NetAppObject):
    """
    Core Segmentation Job Status
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
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _status = None
    @property
    def status(self):
        """
        Status of Core Segmentation Job.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "queued"    - Queued,
        <li> "running"   - Running,
        <li> "stopping"  - Stopping,
        <li> "finished"  - Completed
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _job_id = None
    @property
    def job_id(self):
        """
        Core Segmentation Job Id.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
    _percent_completed = None
    @property
    def percent_completed(self):
        """
        Percentage of Core Segmentation Completed. For queued
        jobs, the percentage is 0. For jobs running or stopping,
        the percentage is the percentage of the core segmenting
        job completed. For finished jobs, the percentage is 100.
        Attributes: non-creatable, non-modifiable
        """
        return self._percent_completed
    @percent_completed.setter
    def percent_completed(self, val):
        if val != None:
            self.validate('percent_completed', val)
        self._percent_completed = val
    
    _core_name = None
    @property
    def core_name(self):
        """
        Full Core to be segmented.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._core_name
    @core_name.setter
    def core_name(self, val):
        if val != None:
            self.validate('core_name', val)
        self._core_name = val
    
    @staticmethod
    def get_api_name():
          return "core-segment-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'status',
            'job-id',
            'percent-completed',
            'core-name',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_completed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'core_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
