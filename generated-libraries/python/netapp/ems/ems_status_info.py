from netapp.netapp_object import NetAppObject

class EmsStatusInfo(NetAppObject):
    """
    EMS Message Info
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
        Node emitting the EMS message.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _num_autosuppressed = None
    @property
    def num_autosuppressed(self):
        """
        Number of times the event has been autosuppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_autosuppressed
    @num_autosuppressed.setter
    def num_autosuppressed(self, val):
        if val != None:
            self.validate('num_autosuppressed', val)
        self._num_autosuppressed = val
    
    _indications = None
    @property
    def indications(self):
        """
        Number of times the event has been posted.
        Attributes: non-creatable, non-modifiable
        """
        return self._indications
    @indications.setter
    def indications(self, val):
        if val != None:
            self.validate('indications', val)
        self._indications = val
    
    _message_name = None
    @property
    def message_name(self):
        """
        The message name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._message_name
    @message_name.setter
    def message_name(self, val):
        if val != None:
            self.validate('message_name', val)
        self._message_name = val
    
    _num_rate_limited = None
    @property
    def num_rate_limited(self):
        """
        Number of times the event has been rate limited.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_rate_limited
    @num_rate_limited.setter
    def num_rate_limited(self, val):
        if val != None:
            self.validate('num_rate_limited', val)
        self._num_rate_limited = val
    
    _last_time_processed = None
    @property
    def last_time_processed(self):
        """
        Time the event was most recently posted and not
        suppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_time_processed
    @last_time_processed.setter
    def last_time_processed(self, val):
        if val != None:
            self.validate('last_time_processed', val)
        self._last_time_processed = val
    
    _last_hour_histogram = None
    @property
    def last_hour_histogram(self):
        """
        60-minute histogram. Number of times the event was posted
        in the last hour. The histogram is divided into sixty
        buckets, each bucket collecting one minute. The buckets
        are displayed in reverse chronological order (most recent
        first).
        Attributes: non-creatable, non-modifiable
        """
        return self._last_hour_histogram
    @last_hour_histogram.setter
    def last_hour_histogram(self, val):
        if val != None:
            self.validate('last_hour_histogram', val)
        self._last_hour_histogram = val
    
    _last_day_histogram = None
    @property
    def last_day_histogram(self):
        """
        24-hour histogram. Number of times the event was posted
        in the last day. The histogram is divided into 24
        buckets, each bucket collecting one hour. The buckets are
        displayed in reverse chronological order (most recent
        first).
        Attributes: non-creatable, non-modifiable
        """
        return self._last_day_histogram
    @last_day_histogram.setter
    def last_day_histogram(self, val):
        if val != None:
            self.validate('last_day_histogram', val)
        self._last_day_histogram = val
    
    _last_time_dropped = None
    @property
    def last_time_dropped(self):
        """
        Time the event was most recently posted and suppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_time_dropped
    @last_time_dropped.setter
    def last_time_dropped(self, val):
        if val != None:
            self.validate('last_time_dropped', val)
        self._last_time_dropped = val
    
    _last_week_histogram = None
    @property
    def last_week_histogram(self):
        """
        7-day histogram. Number of times the event was posted in
        the last week. The histogram is divided into 7 buckets,
        each bucket collecting one day. The buckets are displayed
        in reverse chronological order (most recent first).
        Attributes: non-creatable, non-modifiable
        """
        return self._last_week_histogram
    @last_week_histogram.setter
    def last_week_histogram(self, val):
        if val != None:
            self.validate('last_week_histogram', val)
        self._last_week_histogram = val
    
    _last_time_occurred = None
    @property
    def last_time_occurred(self):
        """
        Time the event was most recently posted.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_time_occurred
    @last_time_occurred.setter
    def last_time_occurred(self, val):
        if val != None:
            self.validate('last_time_occurred', val)
        self._last_time_occurred = val
    
    _change_since = None
    @property
    def change_since(self):
        """
        The algorithm to determine which events are considered
        chatter is run periodically. The change-since parameter
        indicates whether the event has been posted since the
        last time the chatter determination algorithm has run.
        Attributes: non-creatable, non-modifiable
        """
        return self._change_since
    @change_since.setter
    def change_since(self, val):
        if val != None:
            self.validate('change_since', val)
        self._change_since = val
    
    _probability = None
    @property
    def probability(self):
        """
        Probability of an event being suppressed via
        autosuppress.
        Attributes: non-creatable, non-modifiable
        """
        return self._probability
    @probability.setter
    def probability(self, val):
        if val != None:
            self.validate('probability', val)
        self._probability = val
    
    _num_timer_suppressed = None
    @property
    def num_timer_suppressed(self):
        """
        Number of times the event has been timer suppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_timer_suppressed
    @num_timer_suppressed.setter
    def num_timer_suppressed(self, val):
        if val != None:
            self.validate('num_timer_suppressed', val)
        self._num_timer_suppressed = val
    
    _stat_starting_time = None
    @property
    def stat_starting_time(self):
        """
        Time the event was first posted.
        Attributes: non-creatable, non-modifiable
        """
        return self._stat_starting_time
    @stat_starting_time.setter
    def stat_starting_time(self, val):
        if val != None:
            self.validate('stat_starting_time', val)
        self._stat_starting_time = val
    
    _is_chatter = None
    @property
    def is_chatter(self):
        """
        Whether the event is considered chatter, and therefore
        subject to autosuppression.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_chatter
    @is_chatter.setter
    def is_chatter(self, val):
        if val != None:
            self.validate('is_chatter', val)
        self._is_chatter = val
    
    _accumulated_bytes = None
    @property
    def accumulated_bytes(self):
        """
        The total number of bytes the event has accumulated in
        the log file.
        Attributes: non-creatable, non-modifiable
        """
        return self._accumulated_bytes
    @accumulated_bytes.setter
    def accumulated_bytes(self, val):
        if val != None:
            self.validate('accumulated_bytes', val)
        self._accumulated_bytes = val
    
    _drops = None
    @property
    def drops(self):
        """
        Number of times the event has been suppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._drops
    @drops.setter
    def drops(self, val):
        if val != None:
            self.validate('drops', val)
        self._drops = val
    
    _num_dup_suppressed = None
    @property
    def num_dup_suppressed(self):
        """
        Number of times the event has been duplicate suppressed.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_dup_suppressed
    @num_dup_suppressed.setter
    def num_dup_suppressed(self, val):
        if val != None:
            self.validate('num_dup_suppressed', val)
        self._num_dup_suppressed = val
    
    _num_suppressed_since_last = None
    @property
    def num_suppressed_since_last(self):
        """
        Number of times suppressed since last time logged.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_suppressed_since_last
    @num_suppressed_since_last.setter
    def num_suppressed_since_last(self, val):
        if val != None:
            self.validate('num_suppressed_since_last', val)
        self._num_suppressed_since_last = val
    
    _severity = None
    @property
    def severity(self):
        """
        The severity of the event.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "node_fault"     - A data corruption has been
        detected or the node is unable to provide client
        service,
        <li> "svc_fault"      - A temporary loss of service has
        been detected, typically a transient software fault,
        <li> "node_error"     - A hardware error has been
        detected which is not immediately fatal,
        <li> "svc_error"      - A software error has been
        detected which is not immediately fatal,
        <li> "warning"        - A high-priority message, does
        not indicate a fault,
        <li> "notice"         - A normal-priority message, does
        not indicate a fault,
        <li> "info"           - A low-priority message, does
        not indicate a fault,
        <li> "debug"          - A debugging message, typically
        suppressed from customer,
        <li> "var"            - Message has variable severity,
        selected at runtime
        </ul>
        """
        return self._severity
    @severity.setter
    def severity(self, val):
        if val != None:
            self.validate('severity', val)
        self._severity = val
    
    @staticmethod
    def get_api_name():
          return "ems-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'num-autosuppressed',
            'indications',
            'message-name',
            'num-rate-limited',
            'last-time-processed',
            'last-hour-histogram',
            'last-day-histogram',
            'last-time-dropped',
            'last-week-histogram',
            'last-time-occurred',
            'change-since',
            'probability',
            'num-timer-suppressed',
            'stat-starting-time',
            'is-chatter',
            'accumulated-bytes',
            'drops',
            'num-dup-suppressed',
            'num-suppressed-since-last',
            'severity',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'num_autosuppressed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'indications': { 'class': int, 'is_list': False, 'required': 'optional' },
            'message_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'num_rate_limited': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_time_processed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_hour_histogram': { 'class': int, 'is_list': True, 'required': 'optional' },
            'last_day_histogram': { 'class': int, 'is_list': True, 'required': 'optional' },
            'last_time_dropped': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_week_histogram': { 'class': int, 'is_list': True, 'required': 'optional' },
            'last_time_occurred': { 'class': int, 'is_list': False, 'required': 'optional' },
            'change_since': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'probability': { 'class': int, 'is_list': False, 'required': 'optional' },
            'num_timer_suppressed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'stat_starting_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_chatter': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'accumulated_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'drops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'num_dup_suppressed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'num_suppressed_since_last': { 'class': int, 'is_list': False, 'required': 'optional' },
            'severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
