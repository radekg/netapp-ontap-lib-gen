from netapp.netapp_object import NetAppObject

class LunCopyInfo(NetAppObject):
    """
    Information of a LUN copy job
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
    
    _destination_path = None
    @property
    def destination_path(self):
        """
        Destination Path
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_path
    @destination_path.setter
    def destination_path(self, val):
        if val != None:
            self.validate('destination_path', val)
        self._destination_path = val
    
    _scanner_progress_percent = None
    @property
    def scanner_progress_percent(self):
        """
        LUN Copy Progress(%)
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_progress_percent
    @scanner_progress_percent.setter
    def scanner_progress_percent(self, val):
        if val != None:
            self.validate('scanner_progress_percent', val)
        self._scanner_progress_percent = val
    
    _scanner_total = None
    @property
    def scanner_total(self):
        """
        LUN Copy Total (bytes)
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_total
    @scanner_total.setter
    def scanner_total(self, val):
        if val != None:
            self.validate('scanner_total', val)
        self._scanner_total = val
    
    _promote_early = None
    @property
    def promote_early(self):
        """
        Promote Early
        Attributes: non-creatable, non-modifiable
        """
        return self._promote_early
    @promote_early.setter
    def promote_early(self, val):
        if val != None:
            self.validate('promote_early', val)
        self._promote_early = val
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        LUN Copy Job UUID
        Attributes: non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_snapshot_fenced = None
    @property
    def is_snapshot_fenced(self):
        """
        Is Snapshot Fenced
        Attributes: non-creatable, non-modifiable
        """
        return self._is_snapshot_fenced
    @is_snapshot_fenced.setter
    def is_snapshot_fenced(self, val):
        if val != None:
            self.validate('is_snapshot_fenced', val)
        self._is_snapshot_fenced = val
    
    _destination_ready = None
    @property
    def destination_ready(self):
        """
        Destination Ready
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_ready
    @destination_ready.setter
    def destination_ready(self, val):
        if val != None:
            self.validate('destination_ready', val)
        self._destination_ready = val
    
    _last_failure_reason = None
    @property
    def last_failure_reason(self):
        """
        Last Failure Reason
        Attributes: non-creatable, non-modifiable
        """
        return self._last_failure_reason
    @last_failure_reason.setter
    def last_failure_reason(self, val):
        if val != None:
            self.validate('last_failure_reason', val)
        self._last_failure_reason = val
    
    _elapsed_time = None
    @property
    def elapsed_time(self):
        """
        Elapsed Time
        Attributes: non-creatable, non-modifiable
        """
        return self._elapsed_time
    @elapsed_time.setter
    def elapsed_time(self, val):
        if val != None:
            self.validate('elapsed_time', val)
        self._elapsed_time = val
    
    _scanner_progress_bytes = None
    @property
    def scanner_progress_bytes(self):
        """
        LUN Copy Progress(bytes)
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_progress_bytes
    @scanner_progress_bytes.setter
    def scanner_progress_bytes(self, val):
        if val != None:
            self.validate('scanner_progress_bytes', val)
        self._scanner_progress_bytes = val
    
    _scanner_status = None
    @property
    def scanner_status(self):
        """
        Scanner Status
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "preparing"      - Preparing,
        <li> "allocation_map" - Allocating,
        <li> "data"           - Moving Data,
        <li> "destroy"        - Destroying,
        <li> "paused_admin"   - Paused by Admin,
        <li> "paused_error"   - Paused by Error,
        <li> "complete"       - Complete,
        <li> "failed"         - Failed
        </ul>
        """
        return self._scanner_status
    @scanner_status.setter
    def scanner_status(self, val):
        if val != None:
            self.validate('scanner_status', val)
        self._scanner_status = val
    
    _cutover_time = None
    @property
    def cutover_time(self):
        """
        Cutover Time (s)
        Attributes: non-creatable, non-modifiable
        """
        return self._cutover_time
    @cutover_time.setter
    def cutover_time(self, val):
        if val != None:
            self.validate('cutover_time', val)
        self._cutover_time = val
    
    _destination_node = None
    @property
    def destination_node(self):
        """
        Destination Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_node
    @destination_node.setter
    def destination_node(self, val):
        if val != None:
            self.validate('destination_node', val)
        self._destination_node = val
    
    _source_path = None
    @property
    def source_path(self):
        """
        Source Path
        Attributes: non-creatable, non-modifiable
        """
        return self._source_path
    @source_path.setter
    def source_path(self, val):
        if val != None:
            self.validate('source_path', val)
        self._source_path = val
    
    _max_throughput = None
    @property
    def max_throughput(self):
        """
        Maximum Scanner Speed
        Attributes: non-creatable, non-modifiable
        """
        return self._max_throughput
    @max_throughput.setter
    def max_throughput(self, val):
        if val != None:
            self.validate('max_throughput', val)
        self._max_throughput = val
    
    @staticmethod
    def get_api_name():
          return "lun-copy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'destination-path',
            'scanner-progress-percent',
            'scanner-total',
            'promote-early',
            'job-uuid',
            'vserver',
            'is-snapshot-fenced',
            'destination-ready',
            'last-failure-reason',
            'elapsed-time',
            'scanner-progress-bytes',
            'scanner-status',
            'cutover-time',
            'destination-node',
            'source-path',
            'max-throughput',
        ]
    
    def describe_properties(self):
        return {
            'destination_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scanner_progress_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'promote_early': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_snapshot_fenced': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'destination_ready': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_failure_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'elapsed_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_progress_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cutover_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_throughput': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
