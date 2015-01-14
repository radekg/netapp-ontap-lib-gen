from netapp.netapp_object import NetAppObject

class SnapvaultStatusInfo(NetAppObject):
    """
    Format of each status entry.
    """
    
    _transfer_progress = None
    @property
    def transfer_progress(self):
        """
        Number of kilobytes (1024 bytes) transferred so far. This
        field is valid only for active transfers. If there is no
        active transfer in progress, this field is absent.
        Range:[0..2^32-1]
        """
        return self._transfer_progress
    @transfer_progress.setter
    def transfer_progress(self, val):
        if val != None:
            self.validate('transfer_progress', val)
        self._transfer_progress = val
    
    _compressed_bytes = None
    @property
    def compressed_bytes(self):
        """
        Number of compressed bytes transferred if QSM compression
        is being used. This field is absent if the transfer is not
        compressed.
        Range:[0..2^64-1]
        """
        return self._compressed_bytes
    @compressed_bytes.setter
    def compressed_bytes(self, val):
        if val != None:
            self.validate('compressed_bytes', val)
        self._compressed_bytes = val
    
    _last_transfer_type = None
    @property
    def last_transfer_type(self):
        """
        Last transfer type. Possible values are: "initialize",
        "update", "retry", "resync".
        """
        return self._last_transfer_type
    @last_transfer_type.setter
    def last_transfer_type(self, val):
        if val != None:
            self.validate('last_transfer_type', val)
        self._last_transfer_type = val
    
    _last_transfer_size = None
    @property
    def last_transfer_size(self):
        """
        Size in kilobytes (1024 bytes) of the last transfer.
        Range:[0..2^32-1]
        """
        return self._last_transfer_size
    @last_transfer_size.setter
    def last_transfer_size(self, val):
        if val != None:
            self.validate('last_transfer_size', val)
        self._last_transfer_size = val
    
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
    
    _contents = None
    @property
    def contents(self):
        """
        State of the active file system of the snapvault
        path on this system. Possible values are: "replica",
        "transitioning" and "original". This field is present only
        on the destination.
        """
        return self._contents
    @contents.setter
    def contents(self, val):
        if val != None:
            self.validate('contents', val)
        self._contents = val
    
    _current_transfer_type = None
    @property
    def current_transfer_type(self):
        """
        Type of the current transfer. Possible values are:
        "initialize", "update", "retry", "resync". Only
        available for active transfers.
        """
        return self._current_transfer_type
    @current_transfer_type.setter
    def current_transfer_type(self, val):
        if val != None:
            self.validate('current_transfer_type', val)
        self._current_transfer_type = val
    
    _destination_path = None
    @property
    def destination_path(self):
        """
        Destination path.
        """
        return self._destination_path
    @destination_path.setter
    def destination_path(self, val):
        if val != None:
            self.validate('destination_path', val)
        self._destination_path = val
    
    _state = None
    @property
    def state(self):
        """
        State of this relationship. Possible values are:
        "uninitialized","snapvaulted","broken-off","unknown",
        "source","restoring","quiesced".
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _last_transfer_from_path = None
    @property
    def last_transfer_from_path(self):
        """
        Source path used for the last transfer.
        """
        return self._last_transfer_from_path
    @last_transfer_from_path.setter
    def last_transfer_from_path(self, val):
        if val != None:
            self.validate('last_transfer_from_path', val)
        self._last_transfer_from_path = val
    
    _uncompressed_bytes = None
    @property
    def uncompressed_bytes(self):
        """
        Number of uncompressed bytes transferred if QSM compression
        is being used. This field is absent if the transfer is not
        compressed.
        Range:[0..2^64-1]
        """
        return self._uncompressed_bytes
    @uncompressed_bytes.setter
    def uncompressed_bytes(self, val):
        if val != None:
            self.validate('uncompressed_bytes', val)
        self._uncompressed_bytes = val
    
    _source_system = None
    @property
    def source_system(self):
        """
        Source hostname.
        """
        return self._source_system
    @source_system.setter
    def source_system(self, val):
        if val != None:
            self.validate('source_system', val)
        self._source_system = val
    
    _status = None
    @property
    def status(self):
        """
        Transfer status for this relationship. Possible values
        are: "idle", "transferring", "pending", "aborting",
        "quiescing", "resyncing", "restoring".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _last_transfer_duration = None
    @property
    def last_transfer_duration(self):
        """
        Duration of last transfer in seconds.
        Range:[0..2^32-1]
        """
        return self._last_transfer_duration
    @last_transfer_duration.setter
    def last_transfer_duration(self, val):
        if val != None:
            self.validate('last_transfer_duration', val)
        self._last_transfer_duration = val
    
    _destination_system = None
    @property
    def destination_system(self):
        """
        Destination hostname.
        """
        return self._destination_system
    @destination_system.setter
    def destination_system(self, val):
        if val != None:
            self.validate('destination_system', val)
        self._destination_system = val
    
    _lag_time = None
    @property
    def lag_time(self):
        """
        Amount of time in seconds since the beginning of the
        most recently successful transfer from source. This field
        is present only when there has been a successful baseline
        transfer.
        Range:[1..2^32-1]
        """
        return self._lag_time
    @lag_time.setter
    def lag_time(self, val):
        if val != None:
            self.validate('lag_time', val)
        self._lag_time = val
    
    _base_snapshot = None
    @property
    def base_snapshot(self):
        """
        Snapshot the relationship is currently based upon.
        """
        return self._base_snapshot
    @base_snapshot.setter
    def base_snapshot(self, val):
        if val != None:
            self.validate('base_snapshot', val)
        self._base_snapshot = val
    
    _current_transfer_error = None
    @property
    def current_transfer_error(self):
        """
        A human readable error string for the current transfer.
        """
        return self._current_transfer_error
    @current_transfer_error.setter
    def current_transfer_error(self, val):
        if val != None:
            self.validate('current_transfer_error', val)
        self._current_transfer_error = val
    
    _source_path = None
    @property
    def source_path(self):
        """
        Source path.
        """
        return self._source_path
    @source_path.setter
    def source_path(self, val):
        if val != None:
            self.validate('source_path', val)
        self._source_path = val
    
    _inodes_replicated = None
    @property
    def inodes_replicated(self):
        """
        Shows the number of inodes replicated. Present
        during directory processing phase.
        """
        return self._inodes_replicated
    @inodes_replicated.setter
    def inodes_replicated(self, val):
        if val != None:
            self.validate('inodes_replicated', val)
        self._inodes_replicated = val
    
    _last_transfer_from_system = None
    @property
    def last_transfer_from_system(self):
        """
        Source system used for the last transfer.
        """
        return self._last_transfer_from_system
    @last_transfer_from_system.setter
    def last_transfer_from_system(self, val):
        if val != None:
            self.validate('last_transfer_from_system', val)
        self._last_transfer_from_system = val
    
    _mirror_timestamp = None
    @property
    def mirror_timestamp(self):
        """
        Creation time of the snapshot used for the most recent
        successful transfer. Specified in seconds since Jan 1,
        1970. This field is present only when there has been a
        successful baseline transfer.
        Range:[1..2^32-1]
        """
        return self._mirror_timestamp
    @mirror_timestamp.setter
    def mirror_timestamp(self, val):
        if val != None:
            self.validate('mirror_timestamp', val)
        self._mirror_timestamp = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'transfer-progress',
            'compressed-bytes',
            'last-transfer-type',
            'last-transfer-size',
            'replication-ops',
            'contents',
            'current-transfer-type',
            'destination-path',
            'state',
            'last-transfer-from-path',
            'uncompressed-bytes',
            'source-system',
            'status',
            'last-transfer-duration',
            'destination-system',
            'lag-time',
            'base-snapshot',
            'current-transfer-error',
            'source-path',
            'inodes-replicated',
            'last-transfer-from-system',
            'mirror-timestamp',
        ]
    
    def describe_properties(self):
        return {
            'transfer_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'compressed_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_transfer_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'replication_ops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'contents': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_transfer_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_transfer_from_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uncompressed_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_system': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_transfer_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_system': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lag_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'base_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_transfer_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'inodes_replicated': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_from_system': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mirror_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
