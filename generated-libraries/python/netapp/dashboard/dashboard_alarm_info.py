from netapp.netapp_object import NetAppObject

class DashboardAlarmInfo(NetAppObject):
    """
    Alarm monitoring data
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
        Name of the node associated with the alarm metrics.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _dashboard_metric_type = None
    @property
    def dashboard_metric_type(self):
        """
        The type of metric being monitored.
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "cpu_busy"       - CPU Utilization,
        <li> "port_util"      - Port Utilization,
        <li> "op_latency"     - Average Client Latency of NFS
        and CIFS operations,
        <li> "aggregate_used" - Storage Aggregate Utilization,
        <li> "port_problems"  - Packet Error Ratio
        </ul>
        """
        return self._dashboard_metric_type
    @dashboard_metric_type.setter
    def dashboard_metric_type(self, val):
        if val != None:
            self.validate('dashboard_metric_type', val)
        self._dashboard_metric_type = val
    
    _state = None
    @property
    def state(self):
        """
        The current alarm state of the object being monitored.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ok"        ,
        <li> "warning"   ,
        <li> "critical"
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _object_name = None
    @property
    def object_name(self):
        """
        Name associated with the object being monitored.  For
        example, the object-name is the name of the node if the
        dashboard-metric-type is cpu-busy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._object_name
    @object_name.setter
    def object_name(self, val):
        if val != None:
            self.validate('object_name', val)
        self._object_name = val
    
    _high_value = None
    @property
    def high_value(self):
        """
        The highest value recorded so far for this metric.
        Attributes: non-creatable, non-modifiable
        """
        return self._high_value
    @high_value.setter
    def high_value(self, val):
        if val != None:
            self.validate('high_value', val)
        self._high_value = val
    
    _last_value = None
    @property
    def last_value(self):
        """
        The last value recorded for this metric.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_value
    @last_value.setter
    def last_value(self, val):
        if val != None:
            self.validate('last_value', val)
        self._last_value = val
    
    @staticmethod
    def get_api_name():
          return "dashboard-alarm-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'dashboard-metric-type',
            'state',
            'object-name',
            'high-value',
            'last-value',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dashboard_metric_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'object_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'high_value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
