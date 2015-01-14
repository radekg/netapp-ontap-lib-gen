from netapp.netapp_object import NetAppObject

class DiagnosisPolicyDefinitionInfo(NetAppObject):
    """
    System Health Policy Definition
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
    
    _creation_time = None
    @property
    def creation_time(self):
        """
        Time when the previous alert was created due to this
        policy.
        Attributes: non-creatable, non-modifiable
        """
        return self._creation_time
    @creation_time.setter
    def creation_time(self, val):
        if val != None:
            self.validate('creation_time', val)
        self._creation_time = val
    
    _enable = None
    @property
    def enable(self):
        """
        Enable/disable this policy.
        Attributes: non-creatable, modifiable
        """
        return self._enable
    @enable.setter
    def enable(self, val):
        if val != None:
            self.validate('enable', val)
        self._enable = val
    
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
    
    _policy_id = None
    @property
    def policy_id(self):
        """
        Policy identifier.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._policy_id
    @policy_id.setter
    def policy_id(self, val):
        if val != None:
            self.validate('policy_id', val)
        self._policy_id = val
    
    _rule_expression = None
    @property
    def rule_expression(self):
        """
        Arithmetic expression which defines alerts to be created
        as a result of this policy.
        Attributes: non-creatable, non-modifiable
        """
        return self._rule_expression
    @rule_expression.setter
    def rule_expression(self, val):
        if val != None:
            self.validate('rule_expression', val)
        self._rule_expression = val
    
    _responsible_resource_info = None
    @property
    def responsible_resource_info(self):
        """
        The resource responsible for creating this alert
        Attributes: non-creatable, non-modifiable
        """
        return self._responsible_resource_info
    @responsible_resource_info.setter
    def responsible_resource_info(self, val):
        if val != None:
            self.validate('responsible_resource_info', val)
        self._responsible_resource_info = val
    
    _alert_id = None
    @property
    def alert_id(self):
        """
        Alert identifier for alert to be generated on policy rule
        match.
        Attributes: non-creatable, non-modifiable
        """
        return self._alert_id
    @alert_id.setter
    def alert_id(self, val):
        if val != None:
            self.validate('alert_id', val)
        self._alert_id = val
    
    _alert_count = None
    @property
    def alert_count(self):
        """
        Count of alerts created as a result of this policy.
        Attributes: non-creatable, non-modifiable
        """
        return self._alert_count
    @alert_count.setter
    def alert_count(self, val):
        if val != None:
            self.validate('alert_count', val)
        self._alert_count = val
    
    _where = None
    @property
    def where(self):
        """
        Where clause of Arithmetic expression.
        Attributes: non-creatable, non-modifiable
        """
        return self._where
    @where.setter
    def where(self, val):
        if val != None:
            self.validate('where', val)
        self._where = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-policy-definition-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'creation-time',
            'enable',
            'monitor',
            'policy-id',
            'rule-expression',
            'responsible-resource-info',
            'alert-id',
            'alert-count',
            'where',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creation_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'monitor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rule_expression': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'responsible_resource_info': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alert_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alert_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'where': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
