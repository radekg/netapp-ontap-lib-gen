from netapp.netapp_object import NetAppObject

class SnapmirrorStatusInfo(NetAppObject):
    """
    The SnapMirror pair status.
    """
    
    _status = None
    @property
    def status(self):
        """
        SnapMirror pair transfer status.  Possible values are:
        "Idle, "Transferring", "Pending", "Aborting",
        "Migrating", "Quiescing", "Resyncing", "Waiting",
        "Syncing", "In-sync" and "Paused". In case the previous
        transfer was failed/aborted and had a restart checkpoint
        set, the status could be "Idle with restart checkpoint"
        or "Pending with restart checkpoint". In addition
        the status could be "Checking", "Fixing" and
        "Transferring, Checking" when "snapmirror check" command
        is being run on the destination volume.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _last_transfer_size = None
    @property
    def last_transfer_size(self):
        """
        The size in kilo bytes (1024) of the last SnapMirror
        transfer.
        """
        return self._last_transfer_size
    @last_transfer_size.setter
    def last_transfer_size(self, val):
        if val != None:
            self.validate('last_transfer_size', val)
        self._last_transfer_size = val
    
    _current_transfer_type = None
    @property
    def current_transfer_type(self):
        """
        Type of the current SnapMirror transfer.  Possible
        values are: initialize, store, schedule, retry,
        retrieve, resync, and migrate.  Only present when
        there is a transfer.
        """
        return self._current_transfer_type
    @current_transfer_type.setter
    def current_transfer_type(self, val):
        if val != None:
            self.validate('current_transfer_type', val)
        self._current_transfer_type = val
    
    _mirror_timestamp = None
    @property
    def mirror_timestamp(self):
        """
        Access time in seconds since Jan 1, 1970.
        """
        return self._mirror_timestamp
    @mirror_timestamp.setter
    def mirror_timestamp(self, val):
        if val != None:
            self.validate('mirror_timestamp', val)
        self._mirror_timestamp = val
    
    _transfer_progress = None
    @property
    def transfer_progress(self):
        """
        Number of kilo bytes (1024) transfered in a current
        on-going transfer.
        """
        return self._transfer_progress
    @transfer_progress.setter
    def transfer_progress(self, val):
        if val != None:
            self.validate('transfer_progress', val)
        self._transfer_progress = val
    
    _last_transfer_from = None
    @property
    def last_transfer_from(self):
        """
        Source location of the last SnapMirror transfer.
        """
        return self._last_transfer_from
    @last_transfer_from.setter
    def last_transfer_from(self, val):
        if val != None:
            self.validate('last_transfer_from', val)
        self._last_transfer_from = val
    
    _last_transfer_type = None
    @property
    def last_transfer_type(self):
        """
        Last SnapMirror transfer type.  Possible values are:
        "initialize", "store", "schedule", "retry", "retrieve",
        "resync", and "migrate".  Only present when there was a
        last transfer.
        """
        return self._last_transfer_type
    @last_transfer_type.setter
    def last_transfer_type(self, val):
        if val != None:
            self.validate('last_transfer_type', val)
        self._last_transfer_type = val
    
    _state = None
    @property
    def state(self):
        """
        SnapMirror pair state.  Possible values are:
        "uninitialized", "snapmirrored", "broken-off",
        "quiesced", "source", and "unknown".
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _replication_ops = None
    @property
    def replication_ops(self):
        """
        Counter that is incremented for every replication
        operation. Present during directory processing phase.
        """
        return self._replication_ops
    @replication_ops.setter
    def replication_ops(self, val):
        if val != None:
            self.validate('replication_ops', val)
        self._replication_ops = val
    
    _lag_time = None
    @property
    def lag_time(self):
        """
        Amount of time since the last snapmirror transfer
        in seconds.
        """
        return self._lag_time
    @lag_time.setter
    def lag_time(self, val):
        if val != None:
            self.validate('lag_time', val)
        self._lag_time = val
    
    _destination_location = None
    @property
    def destination_location(self):
        """
        The destination location of the SnapMirror pair.  The
        form is &lt;filer&gt;:&lt;volume&gt; or
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self._destination_location
    @destination_location.setter
    def destination_location(self, val):
        if val != None:
            self.validate('destination_location', val)
        self._destination_location = val
    
    _base_snapshot = None
    @property
    def base_snapshot(self):
        """
        Base snapshot name.  Only present if available.
        """
        return self._base_snapshot
    @base_snapshot.setter
    def base_snapshot(self, val):
        if val != None:
            self.validate('base_snapshot', val)
        self._base_snapshot = val
    
    _source_location = None
    @property
    def source_location(self):
        """
        The source location of the SnapMirror pair.  The form
        is &lt;filer&gt;:&lt;volume&gt; or
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self._source_location
    @source_location.setter
    def source_location(self, val):
        if val != None:
            self.validate('source_location', val)
        self._source_location = val
    
    _last_transfer_duration = None
    @property
    def last_transfer_duration(self):
        """
        Duration of the last SnapMirror transfer in seconds.
        """
        return self._last_transfer_duration
    @last_transfer_duration.setter
    def last_transfer_duration(self, val):
        if val != None:
            self.validate('last_transfer_duration', val)
        self._last_transfer_duration = val
    
    _current_transfer_error = None
    @property
    def current_transfer_error(self):
        """
        A human readable transfer error of the current
        snapmirror transfer.  Present when there is a
        current error.
        """
        return self._current_transfer_error
    @current_transfer_error.setter
    def current_transfer_error(self, val):
        if val != None:
            self.validate('current_transfer_error', val)
        self._current_transfer_error = val
    
    _contents = None
    @property
    def contents(self):
        """
        State of the active file system of snapmirror
        destinations.  Possible values are: "replica",
        "transitioning", and "original".
        """
        return self._contents
    @contents.setter
    def contents(self, val):
        if val != None:
            self.validate('contents', val)
        self._contents = val
    
    _inodes_replicated = None
    @property
    def inodes_replicated(self):
        """
        Shows the number of inodes replicated. Present during
        directory processing phase.
        """
        return self._inodes_replicated
    @inodes_replicated.setter
    def inodes_replicated(self, val):
        if val != None:
            self.validate('inodes_replicated', val)
        self._inodes_replicated = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'last-transfer-size',
            'current-transfer-type',
            'mirror-timestamp',
            'transfer-progress',
            'last-transfer-from',
            'last-transfer-type',
            'state',
            'replication-ops',
            'lag-time',
            'destination-location',
            'base-snapshot',
            'source-location',
            'last-transfer-duration',
            'current-transfer-error',
            'contents',
            'inodes-replicated',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_transfer_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'current_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mirror_timestamp': { 'class': int, 'is_list': False, 'required': 'required' },
            'transfer_progress': { 'class': int, 'is_list': False, 'required': 'required' },
            'last_transfer_from': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'replication_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lag_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'base_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_transfer_duration': { 'class': int, 'is_list': False, 'required': 'required' },
            'current_transfer_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'contents': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'inodes_replicated': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
