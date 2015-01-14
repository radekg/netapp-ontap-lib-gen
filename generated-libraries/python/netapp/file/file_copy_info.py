from netapp.netapp_object import NetAppObject

class FileCopyInfo(NetAppObject):
    """
    File Copy Status
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
    
    _source_file_generation_id = None
    @property
    def source_file_generation_id(self):
        """
        Generation number for the source file handle
        Attributes: non-creatable, non-modifiable
        """
        return self._source_file_generation_id
    @source_file_generation_id.setter
    def source_file_generation_id(self, val):
        if val != None:
            self.validate('source_file_generation_id', val)
        self._source_file_generation_id = val
    
    _scanner_total_size = None
    @property
    def scanner_total_size(self):
        """
        Total bytes to be scanned.
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_total_size
    @scanner_total_size.setter
    def scanner_total_size(self, val):
        if val != None:
            self.validate('scanner_total_size', val)
        self._scanner_total_size = val
    
    _is_scanner_paused = None
    @property
    def is_scanner_paused(self):
        """
        Indicates whether the scanner is paused or not.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_scanner_paused
    @is_scanner_paused.setter
    def is_scanner_paused(self, val):
        if val != None:
            self.validate('is_scanner_paused', val)
        self._is_scanner_paused = val
    
    _source_fileid = None
    @property
    def source_fileid(self):
        """
        A unique number within the filesystem identifying the
        source file
        Attributes: non-creatable, non-modifiable
        """
        return self._source_fileid
    @source_fileid.setter
    def source_fileid(self, val):
        if val != None:
            self.validate('source_fileid', val)
        self._source_fileid = val
    
    _destination_path = None
    @property
    def destination_path(self):
        """
        Full path of the destination file, in the format
        <vserver>:<volume>/<path>/<filename>
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_path
    @destination_path.setter
    def destination_path(self, val):
        if val != None:
            self.validate('destination_path', val)
        self._destination_path = val
    
    _destination_volume_dsid = None
    @property
    def destination_volume_dsid(self):
        """
        Destination Data Set ID
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_volume_dsid
    @destination_volume_dsid.setter
    def destination_volume_dsid(self, val):
        if val != None:
            self.validate('destination_volume_dsid', val)
        self._destination_volume_dsid = val
    
    _file_index = None
    @property
    def file_index(self):
        """
        An additional unique element identifying one file among
        many that could be possibly copied as part of a job. For
        file copy operations that involve only one file, the
        file-index value of zero is always correct.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_index
    @file_index.setter
    def file_index(self, val):
        if val != None:
            self.validate('file_index', val)
        self._file_index = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the vserver.
        Attributes: non-creatable, non-modifiable
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
        Indicates whether the snapshot is fenced or not.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_snapshot_fenced
    @is_snapshot_fenced.setter
    def is_snapshot_fenced(self, val):
        if val != None:
            self.validate('is_snapshot_fenced', val)
        self._is_snapshot_fenced = val
    
    _last_failure_reason = None
    @property
    def last_failure_reason(self):
        """
        Contains the most recent failure reason.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_failure_reason
    @last_failure_reason.setter
    def last_failure_reason(self, val):
        if val != None:
            self.validate('last_failure_reason', val)
        self._last_failure_reason = val
    
    _scanner_progress_bytes = None
    @property
    def scanner_progress_bytes(self):
        """
        Scanner progress in bytes scanned.
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
        Status of the file copy scanner.
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
    
    _is_scanner_active = None
    @property
    def is_scanner_active(self):
        """
        Indicates whether the scanner is active or not.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_scanner_active
    @is_scanner_active.setter
    def is_scanner_active(self, val):
        if val != None:
            self.validate('is_scanner_active', val)
        self._is_scanner_active = val
    
    _destination_fileid = None
    @property
    def destination_fileid(self):
        """
        A unique number within the filesystem identifying the
        destination file
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_fileid
    @destination_fileid.setter
    def destination_fileid(self, val):
        if val != None:
            self.validate('destination_fileid', val)
        self._destination_fileid = val
    
    _report_time = None
    @property
    def report_time(self):
        """
        Amount of time in seconds that the job will remain
        visible for reporting purposes.
        Attributes: non-creatable, non-modifiable
        """
        return self._report_time
    @report_time.setter
    def report_time(self, val):
        if val != None:
            self.validate('report_time', val)
        self._report_time = val
    
    _destination_file_path = None
    @property
    def destination_file_path(self):
        """
        The destination file being copied into, in the format
        /<path>/<file>
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_file_path
    @destination_file_path.setter
    def destination_file_path(self, val):
        if val != None:
            self.validate('destination_file_path', val)
        self._destination_file_path = val
    
    _source_volume_dsid = None
    @property
    def source_volume_dsid(self):
        """
        Source volume Data Set ID
        Attributes: non-creatable, non-modifiable
        """
        return self._source_volume_dsid
    @source_volume_dsid.setter
    def source_volume_dsid(self, val):
        if val != None:
            self.validate('source_volume_dsid', val)
        self._source_volume_dsid = val
    
    _is_destination_ready = None
    @property
    def is_destination_ready(self):
        """
        Indicates whether the destination file is ready for use
        or not.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_destination_ready
    @is_destination_ready.setter
    def is_destination_ready(self, val):
        if val != None:
            self.validate('is_destination_ready', val)
        self._is_destination_ready = val
    
    _destination_file_generation_id = None
    @property
    def destination_file_generation_id(self):
        """
        Generation number for the destination file handle
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_file_generation_id
    @destination_file_generation_id.setter
    def destination_file_generation_id(self, val):
        if val != None:
            self.validate('destination_file_generation_id', val)
        self._destination_file_generation_id = val
    
    _source_file_path = None
    @property
    def source_file_path(self):
        """
        The source file being copied in the format
        /<path>/<file>
        Attributes: non-creatable, non-modifiable
        """
        return self._source_file_path
    @source_file_path.setter
    def source_file_path(self, val):
        if val != None:
            self.validate('source_file_path', val)
        self._source_file_path = val
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        UUID which uniquely identifies the job that started this
        copy operation.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    _scanner_progress_percentage = None
    @property
    def scanner_progress_percentage(self):
        """
        Scanner progress as percentage.
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_progress_percentage
    @scanner_progress_percentage.setter
    def scanner_progress_percentage(self, val):
        if val != None:
            self.validate('scanner_progress_percentage', val)
        self._scanner_progress_percentage = val
    
    _source_volume_msid = None
    @property
    def source_volume_msid(self):
        """
        Source volume Master Data Set ID
        Attributes: non-creatable, non-modifiable
        """
        return self._source_volume_msid
    @source_volume_msid.setter
    def source_volume_msid(self, val):
        if val != None:
            self.validate('source_volume_msid', val)
        self._source_volume_msid = val
    
    @staticmethod
    def get_api_name():
          return "file-copy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'source-file-generation-id',
            'scanner-total-size',
            'is-scanner-paused',
            'source-fileid',
            'destination-path',
            'destination-volume-dsid',
            'file-index',
            'vserver',
            'is-snapshot-fenced',
            'last-failure-reason',
            'scanner-progress-bytes',
            'scanner-status',
            'is-scanner-active',
            'destination-fileid',
            'report-time',
            'destination-file-path',
            'source-volume-dsid',
            'is-destination-ready',
            'destination-file-generation-id',
            'source-file-path',
            'job-uuid',
            'scanner-progress-percentage',
            'source-volume-msid',
        ]
    
    def describe_properties(self):
        return {
            'source_file_generation_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_total_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_scanner_paused': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'source_fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_volume_dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'file_index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_snapshot_fenced': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_failure_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scanner_progress_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scanner_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_scanner_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'destination_fileid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'report_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_file_path': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'source_volume_dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_destination_ready': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'destination_file_generation_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_file_path': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scanner_progress_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_volume_msid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
