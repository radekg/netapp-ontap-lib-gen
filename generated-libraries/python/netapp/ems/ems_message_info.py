from netapp.netapp_object import NetAppObject

class EmsMessageInfo(NetAppObject):
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
    
    _message_name = None
    @property
    def message_name(self):
        """
        The emitted message's name.
        Attributes: non-creatable, non-modifiable
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
        Message severity.
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
        Message EMS severity.
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
    
    _event_xml_len = None
    @property
    def event_xml_len(self):
        """
        EMS event XML length in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._event_xml_len
    @event_xml_len.setter
    def event_xml_len(self, val):
        if val != None:
            self.validate('event_xml_len', val)
        self._event_xml_len = val
    
    _kernel_seq_num = None
    @property
    def kernel_seq_num(self):
        """
        The emitted message's kernel sequence number.
        Attributes: non-creatable, non-modifiable
        """
        return self._kernel_seq_num
    @kernel_seq_num.setter
    def kernel_seq_num(self, val):
        if val != None:
            self.validate('kernel_seq_num', val)
        self._kernel_seq_num = val
    
    _seq_num = None
    @property
    def seq_num(self):
        """
        The message sequence number.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._seq_num
    @seq_num.setter
    def seq_num(self, val):
        if val != None:
            self.validate('seq_num', val)
        self._seq_num = val
    
    _source = None
    @property
    def source(self):
        """
        The emitted message's source.
        Attributes: non-creatable, non-modifiable
        """
        return self._source
    @source.setter
    def source(self, val):
        if val != None:
            self.validate('source', val)
        self._source = val
    
    _time = None
    @property
    def time(self):
        """
        The time of message emission.
        Attributes: non-creatable, non-modifiable
        """
        return self._time
    @time.setter
    def time(self, val):
        if val != None:
            self.validate('time', val)
        self._time = val
    
    _kernel_gen = None
    @property
    def kernel_gen(self):
        """
        The emitted message's kernel generation number.
        Attributes: non-creatable, non-modifiable
        """
        return self._kernel_gen
    @kernel_gen.setter
    def kernel_gen(self, val):
        if val != None:
            self.validate('kernel_gen', val)
        self._kernel_gen = val
    
    _event = None
    @property
    def event(self):
        """
        The EMS event.
        Attributes: non-creatable, non-modifiable
        """
        return self._event
    @event.setter
    def event(self, val):
        if val != None:
            self.validate('event', val)
        self._event = val
    
    _num_suppressed_since_last = None
    @property
    def num_suppressed_since_last(self):
        """
        Number of times suppressed since last time the event was
        logged.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_suppressed_since_last
    @num_suppressed_since_last.setter
    def num_suppressed_since_last(self, val):
        if val != None:
            self.validate('num_suppressed_since_last', val)
        self._num_suppressed_since_last = val
    
    @staticmethod
    def get_api_name():
          return "ems-message-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'message-name',
            'severity',
            'ems-severity',
            'event-xml-len',
            'kernel-seq-num',
            'seq-num',
            'source',
            'time',
            'kernel-gen',
            'event',
            'num-suppressed-since-last',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'message_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ems_severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'event_xml_len': { 'class': int, 'is_list': False, 'required': 'optional' },
            'kernel_seq_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'seq_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'kernel_gen': { 'class': int, 'is_list': False, 'required': 'optional' },
            'event': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'num_suppressed_since_last': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
