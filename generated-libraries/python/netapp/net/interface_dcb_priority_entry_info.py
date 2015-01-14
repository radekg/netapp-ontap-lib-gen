from netapp.netapp_object import NetAppObject

class InterfaceDcbPriorityEntryInfo(NetAppObject):
    """
    DCB configuration information about a priority.
    """
    
    _priority = None
    @property
    def priority(self):
        """
        The DCB priority.
        Range: [0..7]
        """
        return self._priority
    @priority.setter
    def priority(self, val):
        if val != None:
            self.validate('priority', val)
        self._priority = val
    
    _application = None
    @property
    def application(self):
        """
        Application assigned to a specified priority group.
        """
        return self._application
    @application.setter
    def application(self, val):
        if val != None:
            self.validate('application', val)
        self._application = val
    
    _priority_group_id = None
    @property
    def priority_group_id(self):
        """
        The priority group ID. A priority group is a group of
        priorities bound together by management for the purpose of
        bandwidth allocation. All priorities in a single group are
        expected to have similar traffic handling requirements
        (e.g. latency or frame loss).
        Range: [0..15]
        """
        return self._priority_group_id
    @priority_group_id.setter
    def priority_group_id(self, val):
        if val != None:
            self.validate('priority_group_id', val)
        self._priority_group_id = val
    
    _is_flow_control_enabled = None
    @property
    def is_flow_control_enabled(self):
        """
        TRUE: the flow control is enabled on a specific priority.
        """
        return self._is_flow_control_enabled
    @is_flow_control_enabled.setter
    def is_flow_control_enabled(self, val):
        if val != None:
            self.validate('is_flow_control_enabled', val)
        self._is_flow_control_enabled = val
    
    @staticmethod
    def get_api_name():
          return "interface-dcb-priority-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'priority',
            'application',
            'priority-group-id',
            'is-flow-control-enabled',
        ]
    
    def describe_properties(self):
        return {
            'priority': { 'class': int, 'is_list': False, 'required': 'required' },
            'application': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'priority_group_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_flow_control_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
