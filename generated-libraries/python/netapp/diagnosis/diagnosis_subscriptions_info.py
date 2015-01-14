from netapp.netapp_object import NetAppObject

class DiagnosisSubscriptionsInfo(NetAppObject):
    """
    System Health Subscriptions
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
        Node hosting this health monitor and sends out
        notifications
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _creation_time = None
    @property
    def creation_time(self):
        """
        Time at which this subscription was created.
        Attributes: non-creatable, non-modifiable
        """
        return self._creation_time
    @creation_time.setter
    def creation_time(self, val):
        if val != None:
            self.validate('creation_time', val)
        self._creation_time = val
    
    _monitor = None
    @property
    def monitor(self):
        """
        Type of source health monitor (e.g. node_connect,
        system_connect, system).
        Attributes: key, required-for-create, non-modifiable
        """
        return self._monitor
    @monitor.setter
    def monitor(self, val):
        if val != None:
            self.validate('monitor', val)
        self._monitor = val
    
    _notify_dest_hm = None
    @property
    def notify_dest_hm(self):
        """
        Health monitor subsribing for notification.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._notify_dest_hm
    @notify_dest_hm.setter
    def notify_dest_hm(self, val):
        if val != None:
            self.validate('notify_dest_hm', val)
        self._notify_dest_hm = val
    
    _time_gap_notify = None
    @property
    def time_gap_notify(self):
        """
        Time Period between two notifications.
        Attributes: optional-for-create, modifiable
        """
        return self._time_gap_notify
    @time_gap_notify.setter
    def time_gap_notify(self, val):
        if val != None:
            self.validate('time_gap_notify', val)
        self._time_gap_notify = val
    
    _notify_type = None
    @property
    def notify_type(self):
        """
        Type of notification (dsmf-type, fptr-type).
        Attributes: non-creatable, non-modifiable
        """
        return self._notify_type
    @notify_type.setter
    def notify_type(self, val):
        if val != None:
            self.validate('notify_type', val)
        self._notify_type = val
    
    _notify_table = None
    @property
    def notify_table(self):
        """
        Table name for DSMF notification.
        Attributes: optional-for-create, modifiable
        """
        return self._notify_table
    @notify_table.setter
    def notify_table(self, val):
        if val != None:
            self.validate('notify_table', val)
        self._notify_table = val
    
    _psc_option = None
    @property
    def psc_option(self):
        """
        Enable/Disable periodic status confirmation.
        Attributes: optional-for-create, modifiable
        """
        return self._psc_option
    @psc_option.setter
    def psc_option(self, val):
        if val != None:
            self.validate('psc_option', val)
        self._psc_option = val
    
    _class_name = None
    @property
    def class_name(self):
        """
        Class name of changed resource.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._class_name
    @class_name.setter
    def class_name(self, val):
        if val != None:
            self.validate('class_name', val)
        self._class_name = val
    
    _notify_fptr = None
    @property
    def notify_fptr(self):
        """
        Function pointer to be invoked.
        Attributes: non-creatable, non-modifiable
        """
        return self._notify_fptr
    @notify_fptr.setter
    def notify_fptr(self, val):
        if val != None:
            self.validate('notify_fptr', val)
        self._notify_fptr = val
    
    _subscription_id = None
    @property
    def subscription_id(self):
        """
        Subscription identifier.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._subscription_id
    @subscription_id.setter
    def subscription_id(self, val):
        if val != None:
            self.validate('subscription_id', val)
        self._subscription_id = val
    
    _event_type = None
    @property
    def event_type(self):
        """
        Type of event (rm-add, rm-del, rm-mod) for which
        notification is to be generated.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._event_type
    @event_type.setter
    def event_type(self, val):
        if val != None:
            self.validate('event_type', val)
        self._event_type = val
    
    _max_notify_period = None
    @property
    def max_notify_period(self):
        """
        Maximum expected time for Notification to complete.
        Attributes: optional-for-create, modifiable
        """
        return self._max_notify_period
    @max_notify_period.setter
    def max_notify_period(self, val):
        if val != None:
            self.validate('max_notify_period', val)
        self._max_notify_period = val
    
    _fail_thresh = None
    @property
    def fail_thresh(self):
        """
        Failure threshold for notification.
        Attributes: optional-for-create, modifiable
        """
        return self._fail_thresh
    @fail_thresh.setter
    def fail_thresh(self, val):
        if val != None:
            self.validate('fail_thresh', val)
        self._fail_thresh = val
    
    _instance_name = None
    @property
    def instance_name(self):
        """
        Instance name of changed resource.
        Attributes: optional-for-create, modifiable
        """
        return self._instance_name
    @instance_name.setter
    def instance_name(self, val):
        if val != None:
            self.validate('instance_name', val)
        self._instance_name = val
    
    _notify_dest_node = None
    @property
    def notify_dest_node(self):
        """
        Node hosting the health monitor that is subscribing for
        notification.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._notify_dest_node
    @notify_dest_node.setter
    def notify_dest_node(self, val):
        if val != None:
            self.validate('notify_dest_node', val)
        self._notify_dest_node = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-subscriptions-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'creation-time',
            'monitor',
            'notify-dest-hm',
            'time-gap-notify',
            'notify-type',
            'notify-table',
            'psc-option',
            'class-name',
            'notify-fptr',
            'subscription-id',
            'event-type',
            'max-notify-period',
            'fail-thresh',
            'instance-name',
            'notify-dest-node',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creation_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'monitor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'notify_dest_hm': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_gap_notify': { 'class': int, 'is_list': False, 'required': 'optional' },
            'notify_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'notify_table': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'psc_option': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'class_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'notify_fptr': { 'class': int, 'is_list': False, 'required': 'optional' },
            'subscription_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'event_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_notify_period': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fail_thresh': { 'class': int, 'is_list': False, 'required': 'optional' },
            'instance_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'notify_dest_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
