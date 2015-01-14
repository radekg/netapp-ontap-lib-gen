from netapp.netapp_object import NetAppObject

class AutosupportHistoryInfo(NetAppObject):
    """
    AutoSupport history data
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
    
    _status = None
    @property
    def status(self):
        """
        The delivery status for this AutoSupport message.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "initializing"             - ASUP request is being
        processed,
        <li> "collection_failed"        - The AutoSupport
        Collection failed. See 'Last Error' for more
        information,
        <li> "collection_in_progress"   - The AutoSupport
        Collection is in progress,
        <li> "queued"                   - ASUP is queued for
        delivery,
        <li> "transmitting"             - ASUP transmission is
        in progress,
        <li> "sent_successful"          - ASUP was successfully
        sent,
        <li> "ignore"                   - ASUP was processed
        successfully but has no destinations configured,
        <li> "re_queued"                - ASUP transmission
        failed and has been re-queued,
        <li> "transmission_failed"      - ASUP transmission has
        failed and the retry limit has been exceeded,
        <li> "ondemand_ignore"          - ASUP was processed
        successfully but ASUP OnDemand has declined delivery
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _generation_timestamp = None
    @property
    def generation_timestamp(self):
        """
        The timestamp of the original generation (collection) of
        this AutoSupport message.  The time value is in seconds
        since January 1, 1970 UTC.
        Attributes: non-creatable, non-modifiable
        """
        return self._generation_timestamp
    @generation_timestamp.setter
    def generation_timestamp(self, val):
        if val != None:
            self.validate('generation_timestamp', val)
        self._generation_timestamp = val
    
    _destination = None
    @property
    def destination(self):
        """
        The transport protocol for this AutoSupport message's
        destination.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "smtp"           ,
        <li> "http"           ,
        <li> "noteto"         ,
        <li> "retransmit"
        </ul>
        """
        return self._destination
    @destination.setter
    def destination(self, val):
        if val != None:
            self.validate('destination', val)
        self._destination = val
    
    _seq_num = None
    @property
    def seq_num(self):
        """
        The AutoSupport message sequence number.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._seq_num
    @seq_num.setter
    def seq_num(self, val):
        if val != None:
            self.validate('seq_num', val)
        self._seq_num = val
    
    _uri = None
    @property
    def uri(self):
        """
        The URI used to deliver this AutoSupport message.
        Attributes: non-creatable, non-modifiable
        """
        return self._uri
    @uri.setter
    def uri(self, val):
        if val != None:
            self.validate('uri', val)
        self._uri = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The name of the filer where the AutoSupport message was
        previously generated.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _trigger = None
    @property
    def trigger(self):
        """
        The name of the EMS event that triggered this AutoSupport
        message.
        Attributes: non-creatable, non-modifiable
        """
        return self._trigger
    @trigger.setter
    def trigger(self, val):
        if val != None:
            self.validate('trigger', val)
        self._trigger = val
    
    _last_modification_timestamp = None
    @property
    def last_modification_timestamp(self):
        """
        The timestamp of the last update to this history record.
        The time value is in seconds since January 1, 1970 UTC.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_modification_timestamp
    @last_modification_timestamp.setter
    def last_modification_timestamp(self, val):
        if val != None:
            self.validate('last_modification_timestamp', val)
        self._last_modification_timestamp = val
    
    _attempt_count = None
    @property
    def attempt_count(self):
        """
        The number of attempted deliveries for this AutoSupport
        message.
        Attributes: non-creatable, non-modifiable
        """
        return self._attempt_count
    @attempt_count.setter
    def attempt_count(self, val):
        if val != None:
            self.validate('attempt_count', val)
        self._attempt_count = val
    
    _subject = None
    @property
    def subject(self):
        """
        The subject field of this AutoSupport message.
        Attributes: non-creatable, non-modifiable
        """
        return self._subject
    @subject.setter
    def subject(self, val):
        if val != None:
            self.validate('subject', val)
        self._subject = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-history-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'generation-timestamp',
            'destination',
            'seq-num',
            'uri',
            'node-name',
            'trigger',
            'last-modification-timestamp',
            'attempt-count',
            'subject',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'generation_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'seq_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'uri': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trigger': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_modification_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'attempt_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'subject': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
