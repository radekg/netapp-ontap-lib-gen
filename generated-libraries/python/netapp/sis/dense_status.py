from netapp.sis.sis_logical_data import SisLogicalData
from netapp.netapp_object import NetAppObject

class DenseStatus(NetAppObject):
    """
    """
    
    _last_operation_state = None
    @property
    def last_operation_state(self):
        """
        Completion status for the last operation.
        Possible values:
        <ul>
        <li> "success",
        <li> "failure"
        </ul>
        Returned only if verbose option is set and when
        there is last completed operation.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_state
    @last_operation_state.setter
    def last_operation_state(self, val):
        if val != None:
            self.validate('last_operation_state', val)
        self._last_operation_state = val
    
    _last_operation_end_timestamp = None
    @property
    def last_operation_end_timestamp(self):
        """
        End timestamp of the last sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_end_timestamp
    @last_operation_end_timestamp.setter
    def last_operation_end_timestamp(self, val):
        if val != None:
            self.validate('last_operation_end_timestamp', val)
        self._last_operation_end_timestamp = val
    
    _is_compression_enabled = None
    @property
    def is_compression_enabled(self):
        """
        compression state of the volume
        Attributes: non-creatable, non-modifiable
        """
        return self._is_compression_enabled
    @is_compression_enabled.setter
    def is_compression_enabled(self, val):
        if val != None:
            self.validate('is_compression_enabled', val)
        self._is_compression_enabled = val
    
    _is_idd_enabled = None
    @property
    def is_idd_enabled(self):
        """
        Indicates incompressible data detection is enabled.
        Possible values:
        <ul>
        <li> "true",
        <li> "false"
        </ul>
        Once this set to 'true', inline compression will do a 4k
        compression quick check for large files before
        proceeding with full CG compression. If quick check
        finds a 4k within a CG as incompressible, inline
        compression won't attempt to compress the CG.
        Also indicates file level incompressible data
        detection is enabled for small files. Once this is
        enabled, when inline compression encounters a
        incompressible CG within a small file, it will mark
        the file with do not compress flag.
        As long as this flag is set on a small file, inline
        compression won't attempt to compress the file.
        This parameter is not supported on Infinite Volumes.
        """
        return self._is_idd_enabled
    @is_idd_enabled.setter
    def is_idd_enabled(self, val):
        if val != None:
            self.validate('is_idd_enabled', val)
        self._is_idd_enabled = val
    
    _is_content_available = None
    @property
    def is_content_available(self):
        """
        This indicates if the
        value of other elements in this dense-status object are valid.
        Attributes: non-creatable, non-modifiable
        This parameter is not supported on Infinite Volumes.
        <p>
        A "true" value for this field indicates a normal case when everything
        went fine while fetching the status values for this volume.
        All values returned are valid.
        A "false" value for this field indicates something went wrong while
        fetching the status values for this volume. Not all
        values returned are valid. The volume returned may
        not be a sis volume.
        """
        return self._is_content_available
    @is_content_available.setter
    def is_content_available(self, val):
        if val != None:
            self.validate('is_content_available', val)
        self._is_content_available = val
    
    _checkpoint_time = None
    @property
    def checkpoint_time(self):
        """
        Checkpoint creation timestamp.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set.
        This field is deprecated in Data ONTAP 8.1 and later.
        This parameter is not supported on Infinite Volumes.
        """
        return self._checkpoint_time
    @checkpoint_time.setter
    def checkpoint_time(self, val):
        if val != None:
            self.validate('checkpoint_time', val)
        self._checkpoint_time = val
    
    _checkpoint_progress = None
    @property
    def checkpoint_progress(self):
        """
        Checkpoint Stage Progress with information
        as to which stage of sis is checkpointed
        and how much data is processed for that stage.
        For example: 25 MB Scanned, 20 MB Searched,
        40 MB (20%) Done,
        30 MB Verified.
        Returned only if verbose option is set.
        This field is deprecated in Data ONTAP 8.1 and later.
        This parameter is not supported on Infinite Volumes.
        """
        return self._checkpoint_progress
    @checkpoint_progress.setter
    def checkpoint_progress(self, val):
        if val != None:
            self.validate('checkpoint_progress', val)
        self._checkpoint_progress = val
    
    _last_success_operation_begin_timestamp = None
    @property
    def last_success_operation_begin_timestamp(self):
        """
        Start timestamp of the last successful sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set and when
        there is last successfully completed operation.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_success_operation_begin_timestamp
    @last_success_operation_begin_timestamp.setter
    def last_success_operation_begin_timestamp(self, val):
        if val != None:
            self.validate('last_success_operation_begin_timestamp', val)
        self._last_success_operation_begin_timestamp = val
    
    _checkpoint_op_type = None
    @property
    def checkpoint_op_type(self):
        """
        Checkpoint Operation Type.
        Possible values:
        <ul>
        <li> "-",
        <li> "Scan",
        <li> "Start",
        <li> "Check",
        <li> "Undo",
        <li> "Downgrade"
        </ul>
        Returned only if verbose option is set.
        This field is deprecated in Data ONTAP 8.1 and later.
        This parameter is not supported on Infinite Volumes.
        """
        return self._checkpoint_op_type
    @checkpoint_op_type.setter
    def checkpoint_op_type(self, val):
        if val != None:
            self.validate('checkpoint_op_type', val)
        self._checkpoint_op_type = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _state = None
    @property
    def state(self):
        """
        Possible values:
        <ul>
        <li> "Enabled",
        <li> "Disabled"
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _policy = None
    @property
    def policy(self):
        """
        sis policy name.
        Returned only if verbose option is set.
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    _progress = None
    @property
    def progress(self):
        """
        The progress of the current sis operation
        with information as to which stage
        is currently in progress and how much data is
        processed for that stage.
        For example: 25 MB Scanned, 20 MB Searched,
        40 MB (20%) Done, 30 MB Verified.
        This parameter is not supported on Infinite Volumes.
        """
        return self._progress
    @progress.setter
    def progress(self, val):
        if val != None:
            self.validate('progress', val)
        self._progress = val
    
    _type = None
    @property
    def type(self):
        """
        Possible values:
        <ul>
        <li> "Regular",
        <li> "SnapVault"
        </ul>
        Any sis volume with Snapvault qtree in it
        would be marked as Snapvault and all others
        would be returned as type Regular.
        Returned only if verbose option is set.
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _quick_check_fsize = None
    @property
    def quick_check_fsize(self):
        """
        Quick check file size for Incompressible Data
        Detection. If Incompressible data detection is enabled
        and if the file size is >= quick-check-fsize,
        inline compression will do a 4k quick check
        before doing full CG compression.
        This parameter is not supported on Infinite Volumes.
        """
        return self._quick_check_fsize
    @quick_check_fsize.setter
    def quick_check_fsize(self, val):
        if val != None:
            self.validate('quick_check_fsize', val)
        self._quick_check_fsize = val
    
    _status = None
    @property
    def status(self):
        """
        Possible values:
        <ul>
        <li> "Idle"           - No sis
        operations are happening on this volume,
        <li> "Initializing"   - sis operation is
        being initialized,
        <li> "Active"         - sis operation
        is active on the volume,
        <li> "Undoing"        - sis is being
        undone on the volume,
        <li> "Pending"        - sis operations
        are scheduled for the volume,
        <li> "Downgrading"    - The sis operation
        necessary to downgrade the volume is active,
        <li> "Disabled"       - sis operation
        is disabled on the volume.
        </ul>
        This parameter is not supported on Infinite Volumes.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        The schedule for sis operation on the volume.
        See sis-set-config for the format of the
        schedule.
        Returned only if verbose option is set.
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _minimum_blocks_shared = None
    @property
    def minimum_blocks_shared(self):
        """
        The minimum number of contiguous blocks in a file
        that will be considered for block sharing.
        If the number of contiguous duplicate blocks is
        less than this number, then they won't be considered
        for sharing.
        Returned only if verbose option is set.
        """
        return self._minimum_blocks_shared
    @minimum_blocks_shared.setter
    def minimum_blocks_shared(self, val):
        if val != None:
            self.validate('minimum_blocks_shared', val)
        self._minimum_blocks_shared = val
    
    _checkpoint_stage = None
    @property
    def checkpoint_stage(self):
        """
        Checkpoint Stage information.
        Possible values:
        <ul>
        <li> "-",
        <li> "Gathering",
        <li> "Sorting",
        <li> "Saving_pass1",
        <li> "Saving_pass2",
        <li> "Checking",
        <li> "Checking_pass1",
        <li> "Checking_pass2",
        <li> "Compress_preproc",
        <li> "Compressing",
        <li> "Saving_sharing",
        <li> "Saving_end",
        <li> "Unknown_stage"
        </ul>
        Returned only if verbose option is set.
        This field is deprecated in Data ONTAP 8.1 and later.
        This parameter is not supported on Infinite Volumes.
        """
        return self._checkpoint_stage
    @checkpoint_stage.setter
    def checkpoint_stage(self, val):
        if val != None:
            self.validate('checkpoint_stage', val)
        self._checkpoint_stage = val
    
    _stale_fingerprint_percentage = None
    @property
    def stale_fingerprint_percentage(self):
        """
        Percentage of fingerprints that are stale in the
        fingerprint database.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._stale_fingerprint_percentage
    @stale_fingerprint_percentage.setter
    def stale_fingerprint_percentage(self, val):
        if val != None:
            self.validate('stale_fingerprint_percentage', val)
        self._stale_fingerprint_percentage = val
    
    _last_operation_error = None
    @property
    def last_operation_error(self):
        """
        A human readable error message of the last
        sis operation. Present when there was an
        error.
        Returned only if verbose option is set.
        and when there is a valid error.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_error
    @last_operation_error.setter
    def last_operation_error(self, val):
        if val != None:
            self.validate('last_operation_error', val)
        self._last_operation_error = val
    
    _path = None
    @property
    def path(self):
        """
        Volume for which sis information is returned.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _checkpoint_sub_stage = None
    @property
    def checkpoint_sub_stage(self):
        """
        Checkpoint Sub Stage information.
        Possible values:
        <ul>
        <li> "-",
        <li> "Sort_pass1",
        <li> "Sort_p1merge",
        <li> "Sort_pass2",
        <li> "Bucket_sort_init",
        <li> "Bucket_sort",
        <li> "Bucket_sort_done"
        </ul>
        Returned only if verbose option is set.
        This field is deprecated in Data ONTAP 8.1 and later.
        This parameter is not supported on Infinite Volumes.
        """
        return self._checkpoint_sub_stage
    @checkpoint_sub_stage.setter
    def checkpoint_sub_stage(self, val):
        if val != None:
            self.validate('checkpoint_sub_stage', val)
        self._checkpoint_sub_stage = val
    
    _logical_data = None
    @property
    def logical_data(self):
        """
        This contains logical size attributes of a volume.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._logical_data
    @logical_data.setter
    def logical_data(self, val):
        if val != None:
            self.validate('logical_data', val)
        self._logical_data = val
    
    _last_operation_size = None
    @property
    def last_operation_size(self):
        """
        The size of the last sis operation in human readable
        format. This output element is deprecated in Data
        ONTAP 8.1. Please use the
        last-operation-size-bytes output element instead.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_size
    @last_operation_size.setter
    def last_operation_size(self, val):
        if val != None:
            self.validate('last_operation_size', val)
        self._last_operation_size = val
    
    _last_success_operation_end_timestamp = None
    @property
    def last_success_operation_end_timestamp(self):
        """
        End timestamp of the last successful sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set and when
        there is last successfully completed operation.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_success_operation_end_timestamp
    @last_success_operation_end_timestamp.setter
    def last_success_operation_end_timestamp(self, val):
        if val != None:
            self.validate('last_success_operation_end_timestamp', val)
        self._last_success_operation_end_timestamp = val
    
    _changelog_used_percent = None
    @property
    def changelog_used_percent(self):
        """
        Percentage of changelog used.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._changelog_used_percent
    @changelog_used_percent.setter
    def changelog_used_percent(self, val):
        if val != None:
            self.validate('changelog_used_percent', val)
        self._changelog_used_percent = val
    
    _queued_job_type = None
    @property
    def queued_job_type(self):
        """
        Type of sis operation that is queued for the volume.
        Possible values:
        <ul>
        <li> "-" - No sis operation is queued for the volume,
        <li> "Scan",
        <li> "Start",
        <li> "Check",
        <li> "Downgrade"
        </ul>
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._queued_job_type
    @queued_job_type.setter
    def queued_job_type(self, val):
        if val != None:
            self.validate('queued_job_type', val)
        self._queued_job_type = val
    
    _last_operation_begin_timestamp = None
    @property
    def last_operation_begin_timestamp(self):
        """
        Start timestamp of the last sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_begin_timestamp
    @last_operation_begin_timestamp.setter
    def last_operation_begin_timestamp(self, val):
        if val != None:
            self.validate('last_operation_begin_timestamp', val)
        self._last_operation_begin_timestamp = val
    
    _blocks_skipped_sharing = None
    @property
    def blocks_skipped_sharing(self):
        """
        Number of blocks not considered for sharing because
        contiguous duplicate blocks were less than the value
        set for minimum-blocks-shared.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._blocks_skipped_sharing
    @blocks_skipped_sharing.setter
    def blocks_skipped_sharing(self, val):
        if val != None:
            self.validate('blocks_skipped_sharing', val)
        self._blocks_skipped_sharing = val
    
    _is_inline_compression_enabled = None
    @property
    def is_inline_compression_enabled(self):
        """
        inline compression state of the volume
        Attributes: non-creatable, non-modifiable
        """
        return self._is_inline_compression_enabled
    @is_inline_compression_enabled.setter
    def is_inline_compression_enabled(self, val):
        if val != None:
            self.validate('is_inline_compression_enabled', val)
        self._is_inline_compression_enabled = val
    
    _last_operation_size_bytes = None
    @property
    def last_operation_size_bytes(self):
        """
        The size in bytes of the last sis operation.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_operation_size_bytes
    @last_operation_size_bytes.setter
    def last_operation_size_bytes(self, val):
        if val != None:
            self.validate('last_operation_size_bytes', val)
        self._last_operation_size_bytes = val
    
    @staticmethod
    def get_api_name():
          return "dense-status"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'last-operation-state',
            'last-operation-end-timestamp',
            'is-compression-enabled',
            'is-idd-enabled',
            'is-content-available',
            'checkpoint-time',
            'checkpoint-progress',
            'last-success-operation-begin-timestamp',
            'checkpoint-op-type',
            'vserver',
            'state',
            'policy',
            'progress',
            'type',
            'quick-check-fsize',
            'status',
            'schedule',
            'minimum-blocks-shared',
            'checkpoint-stage',
            'stale-fingerprint-percentage',
            'last-operation-error',
            'path',
            'checkpoint-sub-stage',
            'logical-data',
            'last-operation-size',
            'last-success-operation-end-timestamp',
            'changelog-used-percent',
            'queued-job-type',
            'last-operation-begin-timestamp',
            'blocks-skipped-sharing',
            'is-inline-compression-enabled',
            'last-operation-size-bytes',
        ]
    
    def describe_properties(self):
        return {
            'last_operation_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_operation_end_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_compression_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_idd_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_content_available': { 'class': bool, 'is_list': False, 'required': 'required' },
            'checkpoint_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_success_operation_begin_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_op_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'progress': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quick_check_fsize': { 'class': int, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'minimum_blocks_shared': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_stage': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'stale_fingerprint_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_operation_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'checkpoint_sub_stage': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'logical_data': { 'class': SisLogicalData, 'is_list': False, 'required': 'optional' },
            'last_operation_size': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_success_operation_end_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'changelog_used_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'queued_job_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_operation_begin_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'blocks_skipped_sharing': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_inline_compression_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_operation_size_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
