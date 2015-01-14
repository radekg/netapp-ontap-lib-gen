from netapp.netapp_object import NetAppObject

class DiagnosisAlertDefinitionInfo(NetAppObject):
    """
    System Health Alert Definition
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
        Severity of alert
        (Unknown,Other,Information,Degraded,Minor,Major,Critical,Fatal).
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
    
    _additional_information = None
    @property
    def additional_information(self):
        """
        Additional information about the alert.
        Attributes: non-creatable, non-modifiable
        """
        return self._additional_information
    @additional_information.setter
    def additional_information(self, val):
        if val != None:
            self.validate('additional_information', val)
        self._additional_information = val
    
    _alert_type = None
    @property
    def alert_type(self):
        """
        Type of alert
        (other,communications,quality-of-service,processing-error,device,environmental,model-change,security).
        Attributes: non-creatable, non-modifiable
        """
        return self._alert_type
    @alert_type.setter
    def alert_type(self, val):
        if val != None:
            self.validate('alert_type', val)
        self._alert_type = val
    
    _possible_effect = None
    @property
    def possible_effect(self):
        """
        Detailed description of the possible effect of the
        condition.
        Attributes: non-creatable, non-modifiable
        """
        return self._possible_effect
    @possible_effect.setter
    def possible_effect(self, val):
        if val != None:
            self.validate('possible_effect', val)
        self._possible_effect = val
    
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
    
    @staticmethod
    def get_api_name():
          return "diagnosis-alert-definition-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'subsystem',
            'monitor',
            'probable-cause',
            'perceived-severity',
            'probable-cause-description',
            'additional-information',
            'alert-type',
            'possible-effect',
            'corrective-actions',
            'alert-id',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'subsystem': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'monitor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'probable_cause': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'perceived_severity': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'probable_cause_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'additional_information': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alert_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'possible_effect': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'corrective_actions': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alert_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
