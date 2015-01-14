from netapp.netapp_object import NetAppObject

class QosSettingsReadAheadInfo(NetAppObject):
    """
    QoS read-ahead setting typedef
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
    
    _jitter = None
    @property
    def jitter(self):
        """
        Threshold for detecting jitter (%)
        Attributes: optional-for-create, modifiable
        """
        return self._jitter
    @jitter.setter
    def jitter(self, val):
        if val != None:
            self.validate('jitter', val)
        self._jitter = val
    
    _min_disk_response_time = None
    @property
    def min_disk_response_time(self):
        """
        Minimum disk response time (ms)
        Attributes: optional-for-create, modifiable
        """
        return self._min_disk_response_time
    @min_disk_response_time.setter
    def min_disk_response_time(self, val):
        if val != None:
            self.validate('min_disk_response_time', val)
        self._min_disk_response_time = val
    
    _use_feedback = None
    @property
    def use_feedback(self):
        """
        Provide cache-miss feedback
        Attributes: optional-for-create, modifiable
        """
        return self._use_feedback
    @use_feedback.setter
    def use_feedback(self, val):
        if val != None:
            self.validate('use_feedback', val)
        self._use_feedback = val
    
    _overshoot = None
    @property
    def overshoot(self):
        """
        Allowable overshoot (%)
        Attributes: optional-for-create, modifiable
        """
        return self._overshoot
    @overshoot.setter
    def overshoot(self, val):
        if val != None:
            self.validate('overshoot', val)
        self._overshoot = val
    
    _max_range = None
    @property
    def max_range(self):
        """
        Maximum range used when aging streams (Blocks)
        Attributes: optional-for-create, modifiable
        """
        return self._max_range
    @max_range.setter
    def max_range(self, val):
        if val != None:
            self.validate('max_range', val)
        self._max_range = val
    
    _disk_response_weight = None
    @property
    def disk_response_weight(self):
        """
        Weight for disk response time aging (%)
        Attributes: optional-for-create, modifiable
        """
        return self._disk_response_weight
    @disk_response_weight.setter
    def disk_response_weight(self, val):
        if val != None:
            self.validate('disk_response_weight', val)
        self._disk_response_weight = val
    
    _min_retire_time = None
    @property
    def min_retire_time(self):
        """
        Minimum Time Before a Stream is Retired (us)
        Attributes: optional-for-create, modifiable
        """
        return self._min_retire_time
    @min_retire_time.setter
    def min_retire_time(self, val):
        if val != None:
            self.validate('min_retire_time', val)
        self._min_retire_time = val
    
    _read_ahead_class = None
    @property
    def read_ahead_class(self):
        """
        Readahead setting class
        Attributes: optional-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "preset"         - Preset,
        <li> "user_defined"   - User Defined,
        <li> "system_defined" - System Defined
        </ul>
        """
        return self._read_ahead_class
    @read_ahead_class.setter
    def read_ahead_class(self, val):
        if val != None:
            self.validate('read_ahead_class', val)
        self._read_ahead_class = val
    
    _interarrival_weight = None
    @property
    def interarrival_weight(self):
        """
        Weight for interarrival time aging (%)
        Attributes: optional-for-create, modifiable
        """
        return self._interarrival_weight
    @interarrival_weight.setter
    def interarrival_weight(self, val):
        if val != None:
            self.validate('interarrival_weight', val)
        self._interarrival_weight = val
    
    _use_async = None
    @property
    def use_async(self):
        """
        Use asynchronous speculation
        Attributes: optional-for-create, modifiable
        """
        return self._use_async
    @use_async.setter
    def use_async(self, val):
        if val != None:
            self.validate('use_async', val)
        self._use_async = val
    
    _smallfile_blocks = None
    @property
    def smallfile_blocks(self):
        """
        Maximum blocks for small-file handling
        Attributes: optional-for-create, modifiable
        """
        return self._smallfile_blocks
    @smallfile_blocks.setter
    def smallfile_blocks(self, val):
        if val != None:
            self.validate('smallfile_blocks', val)
        self._smallfile_blocks = val
    
    _max_blocks = None
    @property
    def max_blocks(self):
        """
        Maximum blocks to speculate
        Attributes: optional-for-create, modifiable
        """
        return self._max_blocks
    @max_blocks.setter
    def max_blocks(self, val):
        if val != None:
            self.validate('max_blocks', val)
        self._max_blocks = val
    
    _max_retire_time = None
    @property
    def max_retire_time(self):
        """
        Maximum Time Before a Stream is Retired (us)
        Attributes: optional-for-create, modifiable
        """
        return self._max_retire_time
    @max_retire_time.setter
    def max_retire_time(self, val):
        if val != None:
            self.validate('max_retire_time', val)
        self._max_retire_time = val
    
    _read_ahead_setting_name = None
    @property
    def read_ahead_setting_name(self):
        """
        Name of QoS Readahead Setting.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._read_ahead_setting_name
    @read_ahead_setting_name.setter
    def read_ahead_setting_name(self, val):
        if val != None:
            self.validate('read_ahead_setting_name', val)
        self._read_ahead_setting_name = val
    
    _max_disk_response_time = None
    @property
    def max_disk_response_time(self):
        """
        Maximum disk response time (ms)
        Attributes: optional-for-create, modifiable
        """
        return self._max_disk_response_time
    @max_disk_response_time.setter
    def max_disk_response_time(self, val):
        if val != None:
            self.validate('max_disk_response_time', val)
        self._max_disk_response_time = val
    
    _force_dump = None
    @property
    def force_dump(self):
        """
        Force DUMP-style readahead
        Attributes: optional-for-create, modifiable
        """
        return self._force_dump
    @force_dump.setter
    def force_dump(self, val):
        if val != None:
            self.validate('force_dump', val)
        self._force_dump = val
    
    _use_timing = None
    @property
    def use_timing(self):
        """
        Use timing algorithms
        Attributes: optional-for-create, modifiable
        """
        return self._use_timing
    @use_timing.setter
    def use_timing(self, val):
        if val != None:
            self.validate('use_timing', val)
        self._use_timing = val
    
    _min_range = None
    @property
    def min_range(self):
        """
        Minimum range used when aging streams (Blocks)
        Attributes: optional-for-create, modifiable
        """
        return self._min_range
    @min_range.setter
    def min_range(self, val):
        if val != None:
            self.validate('min_range', val)
        self._min_range = val
    
    _max_deadline = None
    @property
    def max_deadline(self):
        """
        Maximum deadline Offset (ms)
        Attributes: optional-for-create, modifiable
        """
        return self._max_deadline
    @max_deadline.setter
    def max_deadline(self, val):
        if val != None:
            self.validate('max_deadline', val)
        self._max_deadline = val
    
    _force_none = None
    @property
    def force_none(self):
        """
        Disable readahead
        Attributes: optional-for-create, modifiable
        """
        return self._force_none
    @force_none.setter
    def force_none(self, val):
        if val != None:
            self.validate('force_none', val)
        self._force_none = val
    
    _force_full = None
    @property
    def force_full(self):
        """
        Force full-file readahead
        Attributes: optional-for-create, modifiable
        """
        return self._force_full
    @force_full.setter
    def force_full(self, val):
        if val != None:
            self.validate('force_full', val)
        self._force_full = val
    
    _early_count = None
    @property
    def early_count(self):
        """
        Number of IO operations cautiously predicted
        Attributes: optional-for-create, modifiable
        """
        return self._early_count
    @early_count.setter
    def early_count(self, val):
        if val != None:
            self.validate('early_count', val)
        self._early_count = val
    
    _use_histogram = None
    @property
    def use_histogram(self):
        """
        Use Histogram-based predictions
        Attributes: optional-for-create, modifiable
        """
        return self._use_histogram
    @use_histogram.setter
    def use_histogram(self, val):
        if val != None:
            self.validate('use_histogram', val)
        self._use_histogram = val
    
    _min_file_histogram = None
    @property
    def min_file_histogram(self):
        """
        Minimum filesize for Histogram-based predictions
        (blocks)
        Attributes: optional-for-create, modifiable
        """
        return self._min_file_histogram
    @min_file_histogram.setter
    def min_file_histogram(self, val):
        if val != None:
            self.validate('min_file_histogram', val)
        self._min_file_histogram = val
    
    _max_gap = None
    @property
    def max_gap(self):
        """
        Maximum speculative blocks outstanding
        Attributes: optional-for-create, modifiable
        """
        return self._max_gap
    @max_gap.setter
    def max_gap(self, val):
        if val != None:
            self.validate('max_gap', val)
        self._max_gap = val
    
    _default = None
    @property
    def default(self):
        """
        Specifies whether this is the default readahead setting
        Attributes: optional-for-create, modifiable
        """
        return self._default
    @default.setter
    def default(self, val):
        if val != None:
            self.validate('default', val)
        self._default = val
    
    _align_blocks = None
    @property
    def align_blocks(self):
        """
        Block alignment
        Attributes: optional-for-create, modifiable
        """
        return self._align_blocks
    @align_blocks.setter
    def align_blocks(self, val):
        if val != None:
            self.validate('align_blocks', val)
        self._align_blocks = val
    
    _min_blocks = None
    @property
    def min_blocks(self):
        """
        Minimum blocks to speculate
        Attributes: optional-for-create, modifiable
        """
        return self._min_blocks
    @min_blocks.setter
    def min_blocks(self, val):
        if val != None:
            self.validate('min_blocks', val)
        self._min_blocks = val
    
    _metadata_blocks = None
    @property
    def metadata_blocks(self):
        """
        Minimum blocks for which metadata is predicted
        Attributes: optional-for-create, modifiable
        """
        return self._metadata_blocks
    @metadata_blocks.setter
    def metadata_blocks(self, val):
        if val != None:
            self.validate('metadata_blocks', val)
        self._metadata_blocks = val
    
    _disk_response_factor = None
    @property
    def disk_response_factor(self):
        """
        Disk response time factor
        Attributes: optional-for-create, modifiable
        """
        return self._disk_response_factor
    @disk_response_factor.setter
    def disk_response_factor(self, val):
        if val != None:
            self.validate('disk_response_factor', val)
        self._disk_response_factor = val
    
    @staticmethod
    def get_api_name():
          return "qos-settings-read-ahead-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'jitter',
            'min-disk-response-time',
            'use-feedback',
            'overshoot',
            'max-range',
            'disk-response-weight',
            'min-retire-time',
            'read-ahead-class',
            'interarrival-weight',
            'use-async',
            'smallfile-blocks',
            'max-blocks',
            'max-retire-time',
            'read-ahead-setting-name',
            'max-disk-response-time',
            'force-dump',
            'use-timing',
            'min-range',
            'max-deadline',
            'force-none',
            'force-full',
            'early-count',
            'use-histogram',
            'min-file-histogram',
            'max-gap',
            'default',
            'align-blocks',
            'min-blocks',
            'metadata-blocks',
            'disk-response-factor',
        ]
    
    def describe_properties(self):
        return {
            'jitter': { 'class': int, 'is_list': False, 'required': 'optional' },
            'min_disk_response_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'use_feedback': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'overshoot': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_range': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_response_weight': { 'class': int, 'is_list': False, 'required': 'optional' },
            'min_retire_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_ahead_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interarrival_weight': { 'class': int, 'is_list': False, 'required': 'optional' },
            'use_async': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'smallfile_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_retire_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_ahead_setting_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_disk_response_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'force_dump': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'use_timing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'min_range': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_deadline': { 'class': int, 'is_list': False, 'required': 'optional' },
            'force_none': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'force_full': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'early_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'use_histogram': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'min_file_histogram': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_gap': { 'class': int, 'is_list': False, 'required': 'optional' },
            'default': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'align_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'min_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'metadata_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_response_factor': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
