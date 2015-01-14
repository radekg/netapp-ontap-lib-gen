from netapp.netapp_object import NetAppObject

class TrapInfo(NetAppObject):
    """
    Information about a single user defined trap.
    """
    
    _edge_1_direction = None
    @property
    def edge_1_direction(self):
        """
        Sets the direction of travel across the edge-1
        threshold beyond which the trap is triggered.
        Possible values are "up", and "down".
        If not specified on input, the default value
        is "up".
        """
        return self._edge_1_direction
    @edge_1_direction.setter
    def edge_1_direction(self, val):
        if val != None:
            self.validate('edge_1_direction', val)
        self._edge_1_direction = val
    
    _trap_name = None
    @property
    def trap_name(self):
        """
        Name of the trap given by the user.  Note that
        trap-name may not contain embedded periods.
        """
        return self._trap_name
    @trap_name.setter
    def trap_name(self, val):
        if val != None:
            self.validate('trap_name', val)
        self._trap_name = val
    
    _interval = None
    @property
    def interval(self):
        """
        Time in seconds between evaluations of the trap.
        A trap can send data only as often as it
        is evaluated.
        If not specified on input, the default value
        is 3600 seconds (1-hour).  Range may be
        [0..31536000].
        """
        return self._interval
    @interval.setter
    def interval(self, val):
        if val != None:
            self.validate('interval', val)
        self._interval = val
    
    _backoff_calculator = None
    @property
    def backoff_calculator(self):
        """
        Specifies a method by which the frequency of
        trap evaluation may be modified.  Possible values
        are "step-backoff", "exponential-backoff", and
        "no-backoff"
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is "no-backoff".
        """
        return self._backoff_calculator
    @backoff_calculator.setter
    def backoff_calculator(self, val):
        if val != None:
            self.validate('backoff_calculator', val)
        self._backoff_calculator = val
    
    _backoff_step = None
    @property
    def backoff_step(self):
        """
        Time in seconds by which evaluation interval
        is increased when step-backoff method used.
        Used with "step-backoff" calculator.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is 0.  Range may
        be [0..2^31-1].
        """
        return self._backoff_step
    @backoff_step.setter
    def backoff_step(self, val):
        if val != None:
            self.validate('backoff_step', val)
        self._backoff_step = val
    
    _edge_2_direction = None
    @property
    def edge_2_direction(self):
        """
        Sets the direction of travel across the edge-2
        threshold beyond which the trap is triggered.
        Possible values are "up", and "down".
        Used with double-edge-trigger condition.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is "down".
        """
        return self._edge_2_direction
    @edge_2_direction.setter
    def edge_2_direction(self, val):
        if val != None:
            self.validate('edge_2_direction', val)
        self._edge_2_direction = val
    
    _OID = None
    @property
    def OID(self):
        """
        Specifies the OID of the MIB object that is
        queried to determine the trap's value.
        This attribute is set to "undefined" on output
        if not explicitly specified in trap definition.
        If absent on input, there is no default value,
        and trap definition is incomplete.
        """
        return self._OID
    @OID.setter
    def OID(self, val):
        if val != None:
            self.validate('OID', val)
        self._OID = val
    
    _edge_2 = None
    @property
    def edge_2(self):
        """
        Threshold value at which trap is triggered.
        Used with double-edge-trigger condition.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is 0.  Range may
        be [-2^31..2^31-1].
        """
        return self._edge_2
    @edge_2.setter
    def edge_2(self, val):
        if val != None:
            self.validate('edge_2', val)
        self._edge_2 = val
    
    _interval_offset = None
    @property
    def interval_offset(self):
        """
        Time in seconds until the first trap evaluation.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is 0.  Range may be
        [0..31536000].
        """
        return self._interval_offset
    @interval_offset.setter
    def interval_offset(self, val):
        if val != None:
            self.validate('interval_offset', val)
        self._interval_offset = val
    
    _rate_interval = None
    @property
    def rate_interval(self):
        """
        Time in seconds over which rate of change is
        calculated from sample data.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is 0.  Range may
        be [0..2^31-1].
        """
        return self._rate_interval
    @rate_interval.setter
    def rate_interval(self, val):
        if val != None:
            self.validate('rate_interval', val)
        self._rate_interval = val
    
    _priority = None
    @property
    def priority(self):
        """
        Priority level of trap.  Possible values (in
        descending order of severity) are "emergency",
        "alert", "critical", "error", "warning",
        "notification", "informational", or "debug".
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is "notification".
        """
        return self._priority
    @priority.setter
    def priority(self, val):
        if val != None:
            self.validate('priority', val)
        self._priority = val
    
    _trigger = None
    @property
    def trigger(self):
        """
        Sets the condition under which the trap will
        send a notification.  Possible values are
        "single-edge-trigger", "double-edge-trigger",
        or "level-trigger".
        This attribute is set to "undefined" on output
        if not explicitly specified in trap definition.
        If absent on input, there is no default value,
        and trap definition is incomplete.
        """
        return self._trigger
    @trigger.setter
    def trigger(self, val):
        if val != None:
            self.validate('trigger', val)
        self._trigger = val
    
    _current_value = None
    @property
    def current_value(self):
        """
        Value of trap at time of query.
        On input, this attribute is ignored.
        Range may be [-2^31..2^31-1].
        """
        return self._current_value
    @current_value.setter
    def current_value(self, val):
        if val != None:
            self.validate('current_value', val)
        self._current_value = val
    
    _active = None
    @property
    def active(self):
        """
        Notification state of trap.  Possible values
        are "on" indicating agent will deliver
        notification if triggered, "off" indicating
        trap is inactive, and "incomplete" indicating
        one or more of the required attributes have
        not been defined.
        The default value for a fully defined trap is "off".
        """
        return self._active
    @active.setter
    def active(self, val):
        if val != None:
            self.validate('active', val)
        self._active = val
    
    _message = None
    @property
    def message(self):
        """
        Message associated with trap.  May be either
        a literal string, or specifies an OID.
        This attribute is set to "undefined" on output
        if not explicitly specified in trap definition.
        If absent on input, there is no default value,
        and trap definition is incomplete.
        """
        return self._message
    @message.setter
    def message(self, val):
        if val != None:
            self.validate('message', val)
        self._message = val
    
    _edge_1 = None
    @property
    def edge_1(self):
        """
        Threshold value at which trap is triggered.
        If not specified on input, the default value
        is 2^31-1.  Range may be [-2^31..2^31-1].
        """
        return self._edge_1
    @edge_1.setter
    def edge_1(self, val):
        if val != None:
            self.validate('edge_1', val)
        self._edge_1 = val
    
    _backoff_multiplier = None
    @property
    def backoff_multiplier(self):
        """
        Factor by which interval is multiplied when
        exponential-backoff method used.
        Used with "exponential-backoff" calculator.
        This attribute may be absent on output if not
        explicitly specified in trap definition.  If
        absent on input, the default is 1.  Range may
        be [0..2^31-1].
        """
        return self._backoff_multiplier
    @backoff_multiplier.setter
    def backoff_multiplier(self, val):
        if val != None:
            self.validate('backoff_multiplier', val)
        self._backoff_multiplier = val
    
    @staticmethod
    def get_api_name():
          return "trap-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'edge-1-direction',
            'trap-name',
            'interval',
            'backoff-calculator',
            'backoff-step',
            'edge-2-direction',
            'OID',
            'edge-2',
            'interval-offset',
            'rate-interval',
            'priority',
            'trigger',
            'current-value',
            'active',
            'message',
            'edge-1',
            'backoff-multiplier',
        ]
    
    def describe_properties(self):
        return {
            'edge_1_direction': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trap_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'backoff_calculator': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backoff_step': { 'class': int, 'is_list': False, 'required': 'optional' },
            'edge_2_direction': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'OID': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'edge_2': { 'class': int, 'is_list': False, 'required': 'optional' },
            'interval_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
            'rate_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'priority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trigger': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_value': { 'class': int, 'is_list': False, 'required': 'optional' },
            'active': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'edge_1': { 'class': int, 'is_list': False, 'required': 'optional' },
            'backoff_multiplier': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
