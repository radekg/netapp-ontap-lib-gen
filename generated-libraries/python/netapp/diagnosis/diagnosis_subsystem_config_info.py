from netapp.netapp_object import NetAppObject

class DiagnosisSubsystemConfigInfo(NetAppObject):
    """
    System Health Subsystem Status
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
    
    _subsystem = None
    @property
    def subsystem(self):
        """
        Type of subsystem being monitored
        <p>
        Possible values:
        <ul>
        <li> 'sas_connect',
        <li> 'ha_health',
        </ul>
        Attributes: key, non-creatable, non-modifiable
        """
        return self._subsystem
    @subsystem.setter
    def subsystem(self, val):
        if val != None:
            self.validate('subsystem', val)
        self._subsystem = val
    
    _init_state = None
    @property
    def init_state(self):
        """
        Initialization State of Subsystem.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "invalid"                  ,
        <li> "initializing"             ,
        <li> "initialized"              ,
        <li> "start_discovery"          ,
        <li> "start_rediscovery"        ,
        <li> "discovered_partially"     ,
        <li> "discovery_done"           ,
        <li> "discovery_max"
        </ul>
        """
        return self._init_state
    @init_state.setter
    def init_state(self, val):
        if val != None:
            self.validate('init_state', val)
        self._init_state = val
    
    _outstanding_alert_count = None
    @property
    def outstanding_alert_count(self):
        """
        Number of outstanding alerts.
        Attributes: non-creatable, non-modifiable
        """
        return self._outstanding_alert_count
    @outstanding_alert_count.setter
    def outstanding_alert_count(self, val):
        if val != None:
            self.validate('outstanding_alert_count', val)
        self._outstanding_alert_count = val
    
    _health = None
    @property
    def health(self):
        """
        Health of Subsystem.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ok"                  ,
        <li> "ok_with_suppressed"  ,
        <li> "degraded"            ,
        <li> "unreachable"         ,
        <li> "unknown"
        </ul>
        """
        return self._health
    @health.setter
    def health(self, val):
        if val != None:
            self.validate('health', val)
        self._health = val
    
    _suppressed_alert_count = None
    @property
    def suppressed_alert_count(self):
        """
        Number of suppressed alerts.
        Attributes: non-creatable, non-modifiable
        """
        return self._suppressed_alert_count
    @suppressed_alert_count.setter
    def suppressed_alert_count(self, val):
        if val != None:
            self.validate('suppressed_alert_count', val)
        self._suppressed_alert_count = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-subsystem-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'subsystem',
            'init-state',
            'outstanding-alert-count',
            'health',
            'suppressed-alert-count',
        ]
    
    def describe_properties(self):
        return {
            'subsystem': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'init_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'outstanding_alert_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'health': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'suppressed_alert_count': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
