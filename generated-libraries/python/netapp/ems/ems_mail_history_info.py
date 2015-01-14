from netapp.netapp_object import NetAppObject

class EmsMailHistoryInfo(NetAppObject):
    """
    EMS Mail History Info
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
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _drops_since_previous_time = None
    @property
    def drops_since_previous_time(self):
        """
        Number of drops since previous transmission.
        Attributes: non-creatable, non-modifiable
        """
        return self._drops_since_previous_time
    @drops_since_previous_time.setter
    def drops_since_previous_time(self, val):
        if val != None:
            self.validate('drops_since_previous_time', val)
        self._drops_since_previous_time = val
    
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
    
    _seq_num = None
    @property
    def seq_num(self):
        """
        The message sequence number.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._seq_num
    @seq_num.setter
    def seq_num(self, val):
        if val != None:
            self.validate('seq_num', val)
        self._seq_num = val
    
    _previous_time = None
    @property
    def previous_time(self):
        """
        Previous transmission time.
        Attributes: non-creatable, non-modifiable
        """
        return self._previous_time
    @previous_time.setter
    def previous_time(self, val):
        if val != None:
            self.validate('previous_time', val)
        self._previous_time = val
    
    _time = None
    @property
    def time(self):
        """
        The mail transmission time.
        Attributes: non-creatable, non-modifiable
        """
        return self._time
    @time.setter
    def time(self, val):
        if val != None:
            self.validate('time', val)
        self._time = val
    
    _message = None
    @property
    def message(self):
        """
        The alert message.
        Attributes: non-creatable, non-modifiable
        """
        return self._message
    @message.setter
    def message(self, val):
        if val != None:
            self.validate('message', val)
        self._message = val
    
    _mail_address = None
    @property
    def mail_address(self):
        """
        The mail address.
        Attributes: non-creatable, non-modifiable
        """
        return self._mail_address
    @mail_address.setter
    def mail_address(self, val):
        if val != None:
            self.validate('mail_address', val)
        self._mail_address = val
    
    @staticmethod
    def get_api_name():
          return "ems-mail-history-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'drops-since-previous-time',
            'message-name',
            'seq-num',
            'previous-time',
            'time',
            'message',
            'mail-address',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'drops_since_previous_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'message_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'seq_num': { 'class': int, 'is_list': False, 'required': 'optional' },
            'previous_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mail_address': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
