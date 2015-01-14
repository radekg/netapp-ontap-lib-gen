from netapp.netapp_object import NetAppObject

class EventLogInfo(NetAppObject):
    """
    auto generated
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
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _event_xml_len = None
    @property
    def event_xml_len(self):
        """
        EMS Event XML Length
        Attributes: non-creatable, non-modifiable
        """
        return self._event_xml_len
    @event_xml_len.setter
    def event_xml_len(self, val):
        if val != None:
            self.validate('event_xml_len', val)
        self._event_xml_len = val
    
    _severity = None
    @property
    def severity(self):
        """
        Severity
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
    
    _ems_severity = None
    @property
    def ems_severity(self):
        """
        EMS Severity
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
        return self._ems_severity
    @ems_severity.setter
    def ems_severity(self, val):
        if val != None:
            self.validate('ems_severity', val)
        self._ems_severity = val
    
    _kernelseqnum = None
    @property
    def kernelseqnum(self):
        """
        Kernel Sequence Number
        Attributes: non-creatable, non-modifiable
        """
        return self._kernelseqnum
    @kernelseqnum.setter
    def kernelseqnum(self, val):
        if val != None:
            self.validate('kernelseqnum', val)
        self._kernelseqnum = val
    
    _seqnum = None
    @property
    def seqnum(self):
        """
        Sequence#
        Attributes: key, non-creatable, non-modifiable
        """
        return self._seqnum
    @seqnum.setter
    def seqnum(self, val):
        if val != None:
            self.validate('seqnum', val)
        self._seqnum = val
    
    _messagename = None
    @property
    def messagename(self):
        """
        Message Name
        Attributes: non-creatable, non-modifiable
        """
        return self._messagename
    @messagename.setter
    def messagename(self, val):
        if val != None:
            self.validate('messagename', val)
        self._messagename = val
    
    _source = None
    @property
    def source(self):
        """
        Source
        Attributes: non-creatable, non-modifiable
        """
        return self._source
    @source.setter
    def source(self, val):
        if val != None:
            self.validate('source', val)
        self._source = val
    
    _num_suppressed_since_last = None
    @property
    def num_suppressed_since_last(self):
        """
        Number of Times Suppressed Since Last Time Logged
        Attributes: non-creatable, non-modifiable
        """
        return self._num_suppressed_since_last
    @num_suppressed_since_last.setter
    def num_suppressed_since_last(self, val):
        if val != None:
            self.validate('num_suppressed_since_last', val)
        self._num_suppressed_since_last = val
    
    _time = None
    @property
    def time(self):
        """
        Time
        Attributes: non-creatable, non-modifiable
        """
        return self._time
    @time.setter
    def time(self, val):
        if val != None:
            self.validate('time', val)
        self._time = val
    
    _action = None
    @property
    def action(self):
        """
        Corrective Action
        Attributes: non-creatable, non-modifiable
        """
        return self._action
    @action.setter
    def action(self, val):
        if val != None:
            self.validate('action', val)
        self._action = val
    
    _event = None
    @property
    def event(self):
        """
        Event
        Attributes: non-creatable, non-modifiable
        """
        return self._event
    @event.setter
    def event(self, val):
        if val != None:
            self.validate('event', val)
        self._event = val
    
    _kernelgen = None
    @property
    def kernelgen(self):
        """
        Kernel Generation Number
        Attributes: non-creatable, non-modifiable
        """
        return self._kernelgen
    @kernelgen.setter
    def kernelgen(self, val):
        if val != None:
            self.validate('kernelgen', val)
        self._kernelgen = val
    
    _description = None
    @property
    def description(self):
        """
        Description
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    @staticmethod
    def get_api_name():
          return "event-log-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'event-xml-len',
            'severity',
            'ems-severity',
            'kernelseqnum',
            'seqnum',
            'messagename',
            'source',
            'num-suppressed-since-last',
            'time',
            'action',
            'event',
            'kernelgen',
            'description',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'event_xml_len': { 'class': int, 'is_list': False, 'required': 'optional' },
            'severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ems_severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kernelseqnum': { 'class': int, 'is_list': False, 'required': 'optional' },
            'seqnum': { 'class': int, 'is_list': False, 'required': 'optional' },
            'messagename': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'num_suppressed_since_last': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'action': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'event': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kernelgen': { 'class': int, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
