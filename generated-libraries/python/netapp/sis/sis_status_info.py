from netapp.netapp_object import NetAppObject

class SisStatusInfo(NetAppObject):
    """
    <p>
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
    
    _logical_data_limit = None
    @property
    def logical_data_limit(self):
        """
        Dedupe logical data limit in bytes.
        This parameter is not supported on Infinite Volumes.
        """
        return self._logical_data_limit
    @logical_data_limit.setter
    def logical_data_limit(self, val):
        if val != None:
            self.validate('logical_data_limit', val)
        self._logical_data_limit = val
    
    _last_op_error = None
    @property
    def last_op_error(self):
        """
        A human readable error message of the last
        sis operation. Present when there was an error.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_op_error
    @last_op_error.setter
    def last_op_error(self, val):
        if val != None:
            self.validate('last_op_error', val)
        self._last_op_error = val
    
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
        When returned as part of the output, this indicates if the
        value of other elements in this sis-info object are valid.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        <p>
        A "true" value for this field indicates a normal case when everything
        went fine while fetching the status values for this volume.
        All values returned are valid.
        A "false" value for this field indicates something went wrong while
        fetching the status values for this volume. Not all
        values returned are valid. The volume returned may
        not be a sis volume.
        Default: true
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
        Checkpoint creation timestamp. The value is in seconds
        since January 1, 1970.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
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
        Checkpoint Stage Progress with information as to which
        stage of deduplication is checkpointed and how much data
        is processed for that stage. For ex: 25 MB Scanned, 20 MB
        Searched, 40 MB (20%) Done, 30 MB Verified.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._checkpoint_progress
    @checkpoint_progress.setter
    def checkpoint_progress(self, val):
        if val != None:
            self.validate('checkpoint_progress', val)
        self._checkpoint_progress = val
    
    _is_compression_enabled = None
    @property
    def is_compression_enabled(self):
        """
        Compression state of the volume
        Attributes: non-creatable, modifiable
        """
        return self._is_compression_enabled
    @is_compression_enabled.setter
    def is_compression_enabled(self, val):
        if val != None:
            self.validate('is_compression_enabled', val)
        self._is_compression_enabled = val
    
    _stale_fingerprint_percentage = None
    @property
    def stale_fingerprint_percentage(self):
        """
        Percentage of fingerprints that are stale in the
        fingerprint database.
        This parameter is not supported on Infinite Volumes.
        """
        return self._stale_fingerprint_percentage
    @stale_fingerprint_percentage.setter
    def stale_fingerprint_percentage(self, val):
        if val != None:
            self.validate('stale_fingerprint_percentage', val)
        self._stale_fingerprint_percentage = val
    
    _is_constituent = None
    @property
    def is_constituent(self):
        """
        True implies that the volume is a constituent of an
        Infinite Volume.
        """
        return self._is_constituent
    @is_constituent.setter
    def is_constituent(self, val):
        if val != None:
            self.validate('is_constituent', val)
        self._is_constituent = val
    
    _last_success_op_begin_timestamp = None
    @property
    def last_success_op_begin_timestamp(self):
        """
        Start timestamp of the last successful sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set and when
        there is last successfully completed operation.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_success_op_begin_timestamp
    @last_success_op_begin_timestamp.setter
    def last_success_op_begin_timestamp(self, val):
        if val != None:
            self.validate('last_success_op_begin_timestamp', val)
        self._last_success_op_begin_timestamp = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        A string identifying the Vserver
        Attributes: key, non-creatable, non-modifiable
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
        State of sis configured on the volume.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "Disabled",
        <li> "Enabled"
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _quick_check_fsize = None
    @property
    def quick_check_fsize(self):
        """
        Quick check file size for Incompressible Data Detection.
        If Incompressible data detection is enabled and if the
        file size is >= quick-check-fsize, inline compression
        will do a 4k quick check before doing full CG
        compression.
        This parameter is not supported on Infinite Volumes.
        """
        return self._quick_check_fsize
    @quick_check_fsize.setter
    def quick_check_fsize(self, val):
        if val != None:
            self.validate('quick_check_fsize', val)
        self._quick_check_fsize = val
    
    _policy = None
    @property
    def policy(self):
        """
        sis policy name.
        Attributes: non-creatable, modifiable
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
        with information as to which stage of sis process
        is currently in progress and how much data is processed
        for that stage. For ex: 25 MB Scanned, 20 MB Searched,
        40 MB (20%) Done, 30 MB Verified.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
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
        Any sis volume with Snapvault qtree in it
        would be marked as Snapvault and all others would be
        returned as type Regular.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "Regular"   ,
        <li> "Snapvault" </ul>
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _minimum_blocks_shared = None
    @property
    def minimum_blocks_shared(self):
        """
        The minimum number of contiguous blocks in a file
        that will be considered for block sharing.
        If the number of contiguous duplicate blocks is
        less than this number, then they won't be considered
        for sharing.
        """
        return self._minimum_blocks_shared
    @minimum_blocks_shared.setter
    def minimum_blocks_shared(self, val):
        if val != None:
            self.validate('minimum_blocks_shared', val)
        self._minimum_blocks_shared = val
    
    _last_op_size = None
    @property
    def last_op_size(self):
        """
        The amount of data processed in bytes for the last
        sis operation.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_op_size
    @last_op_size.setter
    def last_op_size(self, val):
        if val != None:
            self.validate('last_op_size', val)
        self._last_op_size = val
    
    _status = None
    @property
    def status(self):
        """
        Status of any sis operation running on the volume.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
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
        is disabled on the volume.</ul>
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
        The schedule for sis operation on the
        volume. See sis-set-config for the format of the
        schedule.
        Attributes: non-creatable, modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _changelog_size = None
    @property
    def changelog_size(self):
        """
        Size of changelog in bytes.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._changelog_size
    @changelog_size.setter
    def changelog_size(self, val):
        if val != None:
            self.validate('changelog_size', val)
        self._changelog_size = val
    
    _checkpoint_stage = None
    @property
    def checkpoint_stage(self):
        """
        Checkpoint stage information.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "Gathering"           - Scanning the volume for
        fingerprints,
        <li> "Sorting"             - Sorting the gathered
        fingerprints,
        <li> "Compress_preproc"    - Preprocessing volume data
        for compression,
        <li> "Compressing"         - Compressing the volume
        data,
        <li> "Saving_pass1"        - Creating duplicate list
        from the newly gathered fingerprints,
        <li> "Saving_pass2"        - Creating duplicate list
        from the fingerprint database,
        <li> "Saving_sharing"      - Creating shared data
        structures in the volume,
        <li> "Saving_end"          - Completing sis operations,
        <li> "Checking_pass0"      - Organizing data in the
        fingerprint database for block sharing,
        <li> "Checking_pass1"      - Organizing data in the
        fingerprint database for block sharing,
        <li> "Checking_pass2"      - Organizing data in the
        fingerprint database for block sharing,
        <li> "Unknown_stage"       - Invalid stage</ul>
        """
        return self._checkpoint_stage
    @checkpoint_stage.setter
    def checkpoint_stage(self, val):
        if val != None:
            self.validate('checkpoint_stage', val)
        self._checkpoint_stage = val
    
    _last_success_op_end_timestamp = None
    @property
    def last_success_op_end_timestamp(self):
        """
        End timestamp of the last successful sis operation.
        The value is in seconds since January 1, 1970.
        Returned only if verbose option is set and when
        there is last successfully completed operation.
        This parameter is not supported on Infinite Volumes.
        """
        return self._last_success_op_end_timestamp
    @last_success_op_end_timestamp.setter
    def last_success_op_end_timestamp(self, val):
        if val != None:
            self.validate('last_success_op_end_timestamp', val)
        self._last_success_op_end_timestamp = val
    
    _vault_transfer_log_size = None
    @property
    def vault_transfer_log_size(self):
        """
        Size of vault transfer log in bytes.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._vault_transfer_log_size
    @vault_transfer_log_size.setter
    def vault_transfer_log_size(self, val):
        if val != None:
            self.validate('vault_transfer_log_size', val)
        self._vault_transfer_log_size = val
    
    _logical_data_size = None
    @property
    def logical_data_size(self):
        """
        The size of logical data in the volume in bytes.
        This is calculated  as [size-saved + size-used +
        + compressed-data bytes].
        This parameter is not supported on Infinite Volumes.
        """
        return self._logical_data_size
    @logical_data_size.setter
    def logical_data_size(self, val):
        if val != None:
            self.validate('logical_data_size', val)
        self._logical_data_size = val
    
    _path = None
    @property
    def path(self):
        """
        Volume for which sis information is
        returned. Path is of the format /vol/&lt;vol_name&gt;.
        Attributes: key, non-creatable, non-modifiable
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
        Checkpoint sub-stage information.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "-"                - No sub stage check point
        present,
        <li> "Sort_pass1"       - Sorting the fingerprints for
        deduplication,
        <li> "Sort_p1merge"     - Merging the fingerprints for
        deduplication,
        <li> "Sort_pass2"       - Merging the fingerprints for
        deduplication,
        <li> "Bucket_sort_init" - Sorting the fingerprints for
        deduplication,
        <li> "Bucket_sort"      - Sorting the fingerprints for
        deduplication,
        <li> "Bucket_sort_done" - Sorting the fingerprints for
        deduplication completed</ul>
        """
        return self._checkpoint_sub_stage
    @checkpoint_sub_stage.setter
    def checkpoint_sub_stage(self, val):
        if val != None:
            self.validate('checkpoint_sub_stage', val)
        self._checkpoint_sub_stage = val
    
    _compression_changelog_size = None
    @property
    def compression_changelog_size(self):
        """
        Size of compression log in bytes.
        Returned only if verbose option is set.
        This parameter is not supported on Infinite Volumes.
        """
        return self._compression_changelog_size
    @compression_changelog_size.setter
    def compression_changelog_size(self, val):
        if val != None:
            self.validate('compression_changelog_size', val)
        self._compression_changelog_size = val
    
    _last_op_state = None
    @property
    def last_op_state(self):
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
        return self._last_op_state
    @last_op_state.setter
    def last_op_state(self, val):
        if val != None:
            self.validate('last_op_state', val)
        self._last_op_state = val
    
    _last_op_begin_timestamp = None
    @property
    def last_op_begin_timestamp(self):
        """
        Start timestamp of the last sis operation.
        The value is in seconds since January 1, 1970. Returned
        only if verbose option is requested.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_op_begin_timestamp
    @last_op_begin_timestamp.setter
    def last_op_begin_timestamp(self, val):
        if val != None:
            self.validate('last_op_begin_timestamp', val)
        self._last_op_begin_timestamp = val
    
    _checkpoint_op_type = None
    @property
    def checkpoint_op_type(self):
        """
        Checkpoint operation Type.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "Scan"      - Scanning volume for fingerprints,
        <li> "Start"     - Starting a sis
        operation,
        <li> "Check"     - Checking for stale data in the
        fingerprint database,
        <li> "Undo"      - Undoing sis on the volume,
        <li> "Downgrade" - Downgrading sis metafiles to a
        previous Data ONTAP release.</ul>
        """
        return self._checkpoint_op_type
    @checkpoint_op_type.setter
    def checkpoint_op_type(self, val):
        if val != None:
            self.validate('checkpoint_op_type', val)
        self._checkpoint_op_type = val
    
    _changelog_used_percent = None
    @property
    def changelog_used_percent(self):
        """
        Percentage of changelog used.
        This parameter is not supported on Infinite Volumes.
        """
        return self._changelog_used_percent
    @changelog_used_percent.setter
    def changelog_used_percent(self, val):
        if val != None:
            self.validate('changelog_used_percent', val)
        self._changelog_used_percent = val
    
    _last_op_end_timestamp = None
    @property
    def last_op_end_timestamp(self):
        """
        End timestamp of the last sis operation.
        This parameter is not supported on Infinite Volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_op_end_timestamp
    @last_op_end_timestamp.setter
    def last_op_end_timestamp(self, val):
        if val != None:
            self.validate('last_op_end_timestamp', val)
        self._last_op_end_timestamp = val
    
    _blocks_skipped_sharing = None
    @property
    def blocks_skipped_sharing(self):
        """
        Number of blocks not considered for sharing
        because contiguous duplicate blocks were less than the
        value
        set for minimum-blocks-shared.
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
        Inline compression state of the volume
        Attributes: non-creatable, modifiable
        """
        return self._is_inline_compression_enabled
    @is_inline_compression_enabled.setter
    def is_inline_compression_enabled(self, val):
        if val != None:
            self.validate('is_inline_compression_enabled', val)
        self._is_inline_compression_enabled = val
    
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
        This parameter is not supported on Infinite Volumes.
        """
        return self._queued_job_type
    @queued_job_type.setter
    def queued_job_type(self, val):
        if val != None:
            self.validate('queued_job_type', val)
        self._queued_job_type = val
    
    @staticmethod
    def get_api_name():
          return "sis-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'logical-data-limit',
            'last-op-error',
            'is-idd-enabled',
            'is-content-available',
            'checkpoint-time',
            'checkpoint-progress',
            'is-compression-enabled',
            'stale-fingerprint-percentage',
            'is-constituent',
            'last-success-op-begin-timestamp',
            'vserver',
            'state',
            'quick-check-fsize',
            'policy',
            'progress',
            'type',
            'minimum-blocks-shared',
            'last-op-size',
            'status',
            'schedule',
            'changelog-size',
            'checkpoint-stage',
            'last-success-op-end-timestamp',
            'vault-transfer-log-size',
            'logical-data-size',
            'path',
            'checkpoint-sub-stage',
            'compression-changelog-size',
            'last-op-state',
            'last-op-begin-timestamp',
            'checkpoint-op-type',
            'changelog-used-percent',
            'last-op-end-timestamp',
            'blocks-skipped-sharing',
            'is-inline-compression-enabled',
            'queued-job-type',
        ]
    
    def describe_properties(self):
        return {
            'logical_data_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_op_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_idd_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_content_available': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'checkpoint_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_compression_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'stale_fingerprint_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_constituent': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_success_op_begin_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quick_check_fsize': { 'class': int, 'is_list': False, 'required': 'optional' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'minimum_blocks_shared': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_op_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'changelog_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_stage': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_success_op_end_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vault_transfer_log_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'logical_data_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'checkpoint_sub_stage': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'compression_changelog_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_op_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_op_begin_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checkpoint_op_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'changelog_used_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_op_end_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'blocks_skipped_sharing': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_inline_compression_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'queued_job_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
