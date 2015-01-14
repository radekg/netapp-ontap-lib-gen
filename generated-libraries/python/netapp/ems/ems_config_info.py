from netapp.netapp_object import NetAppObject

class EmsConfigInfo(NetAppObject):
    """
    EMS Configuration Info
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
    
    _max_target_log_size = None
    @property
    def max_target_log_size(self):
        """
        The target upper limit of the event log file size in
        bytes. Used by autosuppression to control growth of log
        file size.
        Attributes: non-creatable, modifiable
        """
        return self._max_target_log_size
    @max_target_log_size.setter
    def max_target_log_size(self, val):
        if val != None:
            self.validate('max_target_log_size', val)
        self._max_target_log_size = val
    
    _console = None
    @property
    def console(self):
        """
        Whether console logging should be used.
        Attributes: non-creatable, modifiable
        """
        return self._console
    @console.setter
    def console(self, val):
        if val != None:
            self.validate('console', val)
        self._console = val
    
    _suppression = None
    @property
    def suppression(self):
        """
        Whether suppression should be used.
        Attributes: non-creatable, modifiable
        """
        return self._suppression
    @suppression.setter
    def suppression(self, val):
        if val != None:
            self.validate('suppression', val)
        self._suppression = val
    
    _max_target_event_bytes = None
    @property
    def max_target_event_bytes(self):
        """
        Maximum bytes per event per week. Used by autosuppression
        to control growth of log file size.
        Attributes: non-creatable, modifiable
        """
        return self._max_target_event_bytes
    @max_target_event_bytes.setter
    def max_target_event_bytes(self, val):
        if val != None:
            self.validate('max_target_event_bytes', val)
        self._max_target_event_bytes = val
    
    _max_log_show_size = None
    @property
    def max_log_show_size(self):
        """
        Maximum number of events to show.
        Attributes: non-creatable, modifiable
        """
        return self._max_log_show_size
    @max_log_show_size.setter
    def max_log_show_size(self, val):
        if val != None:
            self.validate('max_log_show_size', val)
        self._max_log_show_size = val
    
    _trace_log_size = None
    @property
    def trace_log_size(self):
        """
        Maximum number of traces kept.
        Attributes: non-creatable, modifiable
        """
        return self._trace_log_size
    @trace_log_size.setter
    def trace_log_size(self, val):
        if val != None:
            self.validate('trace_log_size', val)
        self._trace_log_size = val
    
    _mail_from = None
    @property
    def mail_from(self):
        """
        The from address of ems mail.
        Attributes: non-creatable, modifiable
        """
        return self._mail_from
    @mail_from.setter
    def mail_from(self, val):
        if val != None:
            self.validate('mail_from', val)
        self._mail_from = val
    
    _mail_server = None
    @property
    def mail_server(self):
        """
        The mail server to use when sending mail.
        Attributes: non-creatable, modifiable
        """
        return self._mail_server
    @mail_server.setter
    def mail_server(self, val):
        if val != None:
            self.validate('mail_server', val)
        self._mail_server = val
    
    _console_log_level = None
    @property
    def console_log_level(self):
        """
        Console logging level.
        Attributes: non-creatable, modifiable
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
        return self._console_log_level
    @console_log_level.setter
    def console_log_level(self, val):
        if val != None:
            self.validate('console_log_level', val)
        self._console_log_level = val
    
    @staticmethod
    def get_api_name():
          return "ems-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'max-target-log-size',
            'console',
            'suppression',
            'max-target-event-bytes',
            'max-log-show-size',
            'trace-log-size',
            'mail-from',
            'mail-server',
            'console-log-level',
        ]
    
    def describe_properties(self):
        return {
            'max_target_log_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'console': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'suppression': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_target_event_bytes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_log_show_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'trace_log_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mail_from': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mail_server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'console_log_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
