from netapp.netapp_object import NetAppObject

class EmsRoutingInfo(NetAppObject):
    """
    EMS Routing Info
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
    
    _snmp_support = None
    @property
    def snmp_support(self):
        """
        Indicates whether or not the event supports SNMP traps.
        Attributes: non-creatable, non-modifiable
        """
        return self._snmp_support
    @snmp_support.setter
    def snmp_support(self, val):
        if val != None:
            self.validate('snmp_support', val)
        self._snmp_support = val
    
    _message_name = None
    @property
    def message_name(self):
        """
        The name of the EMS message.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._message_name
    @message_name.setter
    def message_name(self, val):
        if val != None:
            self.validate('message_name', val)
        self._message_name = val
    
    _severity = None
    @property
    def severity(self):
        """
        The event severity.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "emergency"      - System is unusable,
        <li> "alert"          - Action must be taken
        immediately,
        <li> "critical"       - Critical condition,
        <li> "error"          - Error condition,
        <li> "warning"        - Warning condition,
        <li> "notice"         - Normal but significant
        condition,
        <li> "informational"  - Information message,
        <li> "debug"          - A debugging message
        </ul>
        """
        return self._severity
    @severity.setter
    def severity(self, val):
        if val != None:
            self.validate('severity', val)
        self._severity = val
    
    _frequency_threshold = None
    @property
    def frequency_threshold(self):
        """
        Number of times an event occurs before a repeat
        notification of the event is sent.
        Attributes: non-creatable, modifiable
        """
        return self._frequency_threshold
    @frequency_threshold.setter
    def frequency_threshold(self, val):
        if val != None:
            self.validate('frequency_threshold', val)
        self._frequency_threshold = val
    
    _description = None
    @property
    def description(self):
        """
        The event description.
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _action = None
    @property
    def action(self):
        """
        The corrective action.
        Attributes: non-creatable, non-modifiable
        """
        return self._action
    @action.setter
    def action(self, val):
        if val != None:
            self.validate('action', val)
        self._action = val
    
    _time_threshold = None
    @property
    def time_threshold(self):
        """
        Minimum number of seconds between repeat notifications of
        an event.
        Attributes: non-creatable, modifiable
        """
        return self._time_threshold
    @time_threshold.setter
    def time_threshold(self, val):
        if val != None:
            self.validate('time_threshold', val)
        self._time_threshold = val
    
    _destinations = None
    @property
    def destinations(self):
        """
        The event destinations.
        Attributes: non-creatable, modifiable
        """
        return self._destinations
    @destinations.setter
    def destinations(self, val):
        if val != None:
            self.validate('destinations', val)
        self._destinations = val
    
    @staticmethod
    def get_api_name():
          return "ems-routing-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snmp-support',
            'message-name',
            'severity',
            'frequency-threshold',
            'description',
            'action',
            'time-threshold',
            'destinations',
        ]
    
    def describe_properties(self):
        return {
            'snmp_support': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'message_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'frequency_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'action': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destinations': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
