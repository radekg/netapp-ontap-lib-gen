from netapp.netapp_object import NetAppObject

class SisInfo(NetAppObject):
    """
    Status and statistics for the SIS volume.
    """
    
    _status = None
    @property
    def status(self):
        """
        Possible values: "idle", "active", "pending",
        or "undoing".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _size_shared = None
    @property
    def size_shared(self):
        """
        Number of bytes in the used space that is
        shared. This field appears if this SIS volume
        is online. Range : [0..2^64-1].
        """
        return self._size_shared
    @size_shared.setter
    def size_shared(self, val):
        if val != None:
            self.validate('size_shared', val)
        self._size_shared = val
    
    _percent_total_saved = None
    @property
    def percent_total_saved(self):
        """
        The percentage of disk space saved by compression &
        deduplication on the referenced file system.
        Range: [0 - 100]
        """
        return self._percent_total_saved
    @percent_total_saved.setter
    def percent_total_saved(self, val):
        if val != None:
            self.validate('percent_total_saved', val)
        self._percent_total_saved = val
    
    _dedup_saved = None
    @property
    def dedup_saved(self):
        """
        The total disk space saved due to deduplication
        in KB (1024 Bytes) on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._dedup_saved
    @dedup_saved.setter
    def dedup_saved(self, val):
        if val != None:
            self.validate('dedup_saved', val)
        self._dedup_saved = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        The schedule for SIS operation on the volume.
        See sis-set-config for the format of the
        schedule.
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _percent_compress_saved = None
    @property
    def percent_compress_saved(self):
        """
        The percentage of disk space saved by compression
        on the referenced file system.
        Range: [0 - 100]
        """
        return self._percent_compress_saved
    @percent_compress_saved.setter
    def percent_compress_saved(self, val):
        if val != None:
            self.validate('percent_compress_saved', val)
        self._percent_compress_saved = val
    
    _last_operation_end = None
    @property
    def last_operation_end(self):
        """
        End timestamp of the last SIS operation.
        """
        return self._last_operation_end
    @last_operation_end.setter
    def last_operation_end(self, val):
        if val != None:
            self.validate('last_operation_end', val)
        self._last_operation_end = val
    
    _total_saved = None
    @property
    def total_saved(self):
        """
        The total disk space saved by compression & deduplication
        in KB (1024 Bytes) on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._total_saved
    @total_saved.setter
    def total_saved(self, val):
        if val != None:
            self.validate('total_saved', val)
        self._total_saved = val
    
    _last_operation_size = None
    @property
    def last_operation_size(self):
        """
        The size in bytes of the last SIS operation.
        Range : [0..2^64-1].
        """
        return self._last_operation_size
    @last_operation_size.setter
    def last_operation_size(self, val):
        if val != None:
            self.validate('last_operation_size', val)
        self._last_operation_size = val
    
    _last_operation_begin = None
    @property
    def last_operation_begin(self):
        """
        Start timestamp of the last SIS operation.
        """
        return self._last_operation_begin
    @last_operation_begin.setter
    def last_operation_begin(self, val):
        if val != None:
            self.validate('last_operation_begin', val)
        self._last_operation_begin = val
    
    _state = None
    @property
    def state(self):
        """
        Possible values: "enabled", or "disabled".
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _percent_dedup_saved = None
    @property
    def percent_dedup_saved(self):
        """
        The percentage of disk space saved by deduplication
        on the referenced file system.
        Range: [0 - 100]
        """
        return self._percent_dedup_saved
    @percent_dedup_saved.setter
    def percent_dedup_saved(self, val):
        if val != None:
            self.validate('percent_dedup_saved', val)
        self._percent_dedup_saved = val
    
    _compress_saved = None
    @property
    def compress_saved(self):
        """
        The total disk space saved due to compression
        in KB (1024 Bytes) on the referenced file system.
        Range: [0 - 2^64-1]
        """
        return self._compress_saved
    @compress_saved.setter
    def compress_saved(self, val):
        if val != None:
            self.validate('compress_saved', val)
        self._compress_saved = val
    
    _last_operation_error = None
    @property
    def last_operation_error(self):
        """
        A human readable error message of the last
        SIS operation. Present when there was an
        error.
        """
        return self._last_operation_error
    @last_operation_error.setter
    def last_operation_error(self, val):
        if val != None:
            self.validate('last_operation_error', val)
        self._last_operation_error = val
    
    _percentage_saved = None
    @property
    def percentage_saved(self):
        """
        Percentage of space savings generated by the
        shared space. This is calculated as
        [size-saved / (size-saved + size-used)].
        This field appears if the SIS volume is
        online. Range : [0..100].
        """
        return self._percentage_saved
    @percentage_saved.setter
    def percentage_saved(self, val):
        if val != None:
            self.validate('percentage_saved', val)
        self._percentage_saved = val
    
    _progress = None
    @property
    def progress(self):
        """
        The progress of the current SIS operation.
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
        Possible values: "regular" or "snapvault".
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _size_saved = None
    @property
    def size_saved(self):
        """
        The disk space savings generated by the shared
        space. The size is in bytes.  The size-saved
        plus the size-used would be the total space
        usage, if no space is shared. This field
        appears if the SIS volume is online.
        Range : [0..2^64-1].
        """
        return self._size_saved
    @size_saved.setter
    def size_saved(self, val):
        if val != None:
            self.validate('size_saved', val)
        self._size_saved = val
    
    @staticmethod
    def get_api_name():
          return "sis-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'size-shared',
            'percent-total-saved',
            'dedup-saved',
            'schedule',
            'percent-compress-saved',
            'last-operation-end',
            'total-saved',
            'last-operation-size',
            'last-operation-begin',
            'state',
            'percent-dedup-saved',
            'compress-saved',
            'last-operation-error',
            'percentage-saved',
            'progress',
            'type',
            'size-saved',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'size_shared': { 'class': int, 'is_list': False, 'required': 'required' },
            'percent_total_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'dedup_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_compress_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'last_operation_end': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'total_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'last_operation_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'last_operation_begin': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_dedup_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'compress_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'last_operation_error': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percentage_saved': { 'class': int, 'is_list': False, 'required': 'required' },
            'progress': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'size_saved': { 'class': int, 'is_list': False, 'required': 'required' },
        }
