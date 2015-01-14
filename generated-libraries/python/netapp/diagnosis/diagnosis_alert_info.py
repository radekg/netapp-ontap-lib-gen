from netapp.netapp_object import NetAppObject

class DiagnosisAlertInfo(NetAppObject):
    """
    System Health Alert
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
        Node hosting this health monitor.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _subsystem = None
    @property
    def subsystem(self):
        """
        Type of subsystem being monitored (e.g. sas_connect).
        Attributes: non-creatable, non-modifiable
        """
        return self._subsystem
    @subsystem.setter
    def subsystem(self, val):
        if val != None:
            self.validate('subsystem', val)
        self._subsystem = val
    
    _additional_info = None
    @property
    def additional_info(self):
        """
        Additional information from the resource that generated
        this alert
        Attributes: non-creatable, non-modifiable
        """
        return self._additional_info
    @additional_info.setter
    def additional_info(self, val):
        if val != None:
            self.validate('additional_info', val)
        self._additional_info = val
    
    _indication_time = None
    @property
    def indication_time(self):
        """
        Time of alert generation.
        Attributes: non-creatable, non-modifiable
        """
        return self._indication_time
    @indication_time.setter
    def indication_time(self, val):
        if val != None:
            self.validate('indication_time', val)
        self._indication_time = val
    
    _monitor = None
    @property
    def monitor(self):
        """
        Type of health monitor (e.g. node_connect,
        system_connect, system).
        Attributes: key, non-creatable, non-modifiable
        """
        return self._monitor
    @monitor.setter
    def monitor(self, val):
        if val != None:
            self.validate('monitor', val)
        self._monitor = val
    
    _acknowledge = None
    @property
    def acknowledge(self):
        """
        Acknowledge the alert condition.
        Attributes: non-creatable, modifiable
        """
        return self._acknowledge
    @acknowledge.setter
    def acknowledge(self, val):
        if val != None:
            self.validate('acknowledge', val)
        self._acknowledge = val
    
    _probable_cause = None
    @property
    def probable_cause(self):
        """
        Probable cause for alert generation.
        Attributes: non-creatable, non-modifiable
        """
        return self._probable_cause
    @probable_cause.setter
    def probable_cause(self, val):
        if val != None:
            self.validate('probable_cause', val)
        self._probable_cause = val
    
    _perceived_severity = None
    @property
    def perceived_severity(self):
        """
        Severity of alert.
        Attributes: non-creatable, non-modifiable
        """
        return self._perceived_severity
    @perceived_severity.setter
    def perceived_severity(self, val):
        if val != None:
            self.validate('perceived_severity', val)
        self._perceived_severity = val
    
    _probable_cause_description = None
    @property
    def probable_cause_description(self):
        """
        Detailed description of probable cause for alert
        generation.
        Attributes: non-creatable, non-modifiable
        """
        return self._probable_cause_description
    @probable_cause_description.setter
    def probable_cause_description(self, val):
        if val != None:
            self.validate('probable_cause_description', val)
        self._probable_cause_description = val
    
    _policy = None
    @property
    def policy(self):
        """
        Policy rule responsible for creating this alert.
        Attributes: non-creatable, non-modifiable
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    _alerting_resource_name = None
    @property
    def alerting_resource_name(self):
        """
        Display name of resource that generated the alert.
        Attributes: non-creatable, non-modifiable
        """
        return self._alerting_resource_name
    @alerting_resource_name.setter
    def alerting_resource_name(self, val):
        if val != None:
            self.validate('alerting_resource_name', val)
        self._alerting_resource_name = val
    
    _possible_effect = None
    @property
    def possible_effect(self):
        """
        Possible effect seen due to this problem.
        Attributes: non-creatable, non-modifiable
        """
        return self._possible_effect
    @possible_effect.setter
    def possible_effect(self, val):
        if val != None:
            self.validate('possible_effect', val)
        self._possible_effect = val
    
    _suppress = None
    @property
    def suppress(self):
        """
        Suppress this alert.
        Attributes: non-creatable, modifiable
        """
        return self._suppress
    @suppress.setter
    def suppress(self, val):
        if val != None:
            self.validate('suppress', val)
        self._suppress = val
    
    _corrective_actions = None
    @property
    def corrective_actions(self):
        """
        Recommended actions to correct the problem reported by
        alert.
        Attributes: non-creatable, non-modifiable
        """
        return self._corrective_actions
    @corrective_actions.setter
    def corrective_actions(self, val):
        if val != None:
            self.validate('corrective_actions', val)
        self._corrective_actions = val
    
    _acknowledger = None
    @property
    def acknowledger(self):
        """
        Person who acknowledged this alert
        Attributes: non-creatable, modifiable
        """
        return self._acknowledger
    @acknowledger.setter
    def acknowledger(self, val):
        if val != None:
            self.validate('acknowledger', val)
        self._acknowledger = val
    
    _alert_id = None
    @property
    def alert_id(self):
        """
        Alert identification.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._alert_id
    @alert_id.setter
    def alert_id(self, val):
        if val != None:
            self.validate('alert_id', val)
        self._alert_id = val
    
    _alerting_resource = None
    @property
    def alerting_resource(self):
        """
        Unique name of resource that generated the alert.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._alerting_resource
    @alerting_resource.setter
    def alerting_resource(self, val):
        if val != None:
            self.validate('alerting_resource', val)
        self._alerting_resource = val
    
    _suppressor = None
    @property
    def suppressor(self):
        """
        Person who suppressed this alert
        Attributes: non-creatable, modifiable
        """
        return self._suppressor
    @suppressor.setter
    def suppressor(self, val):
        if val != None:
            self.validate('suppressor', val)
        self._suppressor = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-alert-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'subsystem',
            'additional-info',
            'indication-time',
            'monitor',
            'acknowledge',
            'probable-cause',
            'perceived-severity',
            'probable-cause-description',
            'policy',
            'alerting-resource-name',
            'possible-effect',
            'suppress',
            'corrective-actions',
            'acknowledger',
            'alert-id',
            'alerting-resource',
            'suppressor',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'subsystem': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'additional_info': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'indication_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'monitor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'acknowledge': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'probable_cause': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'perceived_severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'probable_cause_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alerting_resource_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'possible_effect': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'suppress': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'corrective_actions': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'acknowledger': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alert_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alerting_resource': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'suppressor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
