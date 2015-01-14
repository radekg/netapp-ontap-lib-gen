from netapp.netapp_object import NetAppObject

class DiagnosisConfigInfo(NetAppObject):
    """
    System Health Config
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
        Possible values:
        <ul>
        <li> "sas_connect"        ,
        <li> "ha_health"          ,
        </ul>
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
        Type of health monitor.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "node_connect"   ...   node scope health monitor           ,
        <li> "system_connect" ...   cluster scope health monitor        ,
        <li> "system"         ...   aggregator of health monitor status ,
        </ul>
        """
        return self._monitor
    @monitor.setter
    def monitor(self, val):
        if val != None:
            self.validate('monitor', val)
        self._monitor = val
    
    _aggregator = None
    @property
    def aggregator(self):
        """
        Aggregating health monitor that aggregates status from
        this health monitor.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "node_connect"   ...   node scope health monitor           ,
        <li> "system_connect" ...   cluster scope health monitor        ,
        <li> "system"         ...   aggregator of health monitor status ,
        </ul>
        """
        return self._aggregator
    @aggregator.setter
    def aggregator(self, val):
        if val != None:
            self.validate('aggregator', val)
        self._aggregator = val
    
    _sub_pol_versions = None
    @property
    def sub_pol_versions(self):
        """
        Subordinate policy file versions.
        Attributes: non-creatable, non-modifiable
        """
        return self._sub_pol_versions
    @sub_pol_versions.setter
    def sub_pol_versions(self, val):
        if val != None:
            self.validate('sub_pol_versions', val)
        self._sub_pol_versions = val
    
    _init_state = None
    @property
    def init_state(self):
        """
        Subsystem initialization state of health monitor
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
    
    _health = None
    @property
    def health(self):
        """
        Status of health monitor (ok, ok-with-suppressed,
        degraded).
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ok"                 ,
        <li> "ok_with_suppressed" ,
        <li> "degraded"           ,
        <li> "unreachable"        ,
        <li> "unknown"
        </ul>
        """
        return self._health
    @health.setter
    def health(self, val):
        if val != None:
            self.validate('health', val)
        self._health = val
    
    _resources = None
    @property
    def resources(self):
        """
        Resources monitored by this health monitor.
        Attributes: non-creatable, non-modifiable
        """
        return self._resources
    @resources.setter
    def resources(self, val):
        if val != None:
            self.validate('resources', val)
        self._resources = val
    
    _context = None
    @property
    def context(self):
        """
        Scope of health monitor (node-context, cluster-context).
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "node_context"       ,
        <li> "cluster_context"
        </ul>
        """
        return self._context
    @context.setter
    def context(self, val):
        if val != None:
            self.validate('context', val)
        self._context = val
    
    _pol_version = None
    @property
    def pol_version(self):
        """
        Policy file version.
        Attributes: non-creatable, non-modifiable
        """
        return self._pol_version
    @pol_version.setter
    def pol_version(self, val):
        if val != None:
            self.validate('pol_version', val)
        self._pol_version = val
    
    _mon_version = None
    @property
    def mon_version(self):
        """
        Health Monitor version.
        Attributes: non-creatable, non-modifiable
        """
        return self._mon_version
    @mon_version.setter
    def mon_version(self, val):
        if val != None:
            self.validate('mon_version', val)
        self._mon_version = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'subsystem',
            'monitor',
            'aggregator',
            'sub-pol-versions',
            'init-state',
            'health',
            'resources',
            'context',
            'pol-version',
            'mon-version',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'subsystem': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'monitor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggregator': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sub_pol_versions': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'init_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'health': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'resources': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'context': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pol_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mon_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
