from netapp.netapp_object import NetAppObject

class DashboardAlarmThresholdInfo(NetAppObject):
    """
    Alarm threshold configuration settings
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
    
    _threshold_units = None
    @property
    def threshold_units(self):
        """
        Threshold Units
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "none"      - none,
        <li> "ms"        - milliseconds,
        <li> "percent"   - percent
        </ul>
        """
        return self._threshold_units
    @threshold_units.setter
    def threshold_units(self, val):
        if val != None:
            self.validate('threshold_units', val)
        self._threshold_units = val
    
    _polling_interval = None
    @property
    def polling_interval(self):
        """
        The refresh interval for the alarm dashboard metrics (in
        seconds).
        Attributes: required-for-create, modifiable
        """
        return self._polling_interval
    @polling_interval.setter
    def polling_interval(self, val):
        if val != None:
            self.validate('polling_interval', val)
        self._polling_interval = val
    
    _warning_threshold = None
    @property
    def warning_threshold(self):
        """
        The threshold value that must be reached to generate a
        warning alarm for this type of metric. Get request is
        returned with % sign for percent values and ms for
        milliseconds value. Example : 85%, 200ms
        Attributes: required-for-create, modifiable
        """
        return self._warning_threshold
    @warning_threshold.setter
    def warning_threshold(self, val):
        if val != None:
            self.validate('warning_threshold', val)
        self._warning_threshold = val
    
    _dashboard_metric_type = None
    @property
    def dashboard_metric_type(self):
        """
        The type of metric being monitored.
        Attributes: key, required-for-create, non-modifiable
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
    
    _is_user_notification_enabled = None
    @property
    def is_user_notification_enabled(self):
        """
        Specifies whether user notifications are enabled.
        Attributes: required-for-create, modifiable
        """
        return self._is_user_notification_enabled
    @is_user_notification_enabled.setter
    def is_user_notification_enabled(self, val):
        if val != None:
            self.validate('is_user_notification_enabled', val)
        self._is_user_notification_enabled = val
    
    _critical_threshold = None
    @property
    def critical_threshold(self):
        """
        The threshold value that must be reached to generate a
        critical alarm for this type of metric. Get request is
        returned with % sign for percent values and ms for
        milliseconds value. Example : 95%, 500ms
        Attributes: optional-for-create, modifiable
        """
        return self._critical_threshold
    @critical_threshold.setter
    def critical_threshold(self, val):
        if val != None:
            self.validate('critical_threshold', val)
        self._critical_threshold = val
    
    @staticmethod
    def get_api_name():
          return "dashboard-alarm-threshold-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'threshold-units',
            'polling-interval',
            'warning-threshold',
            'dashboard-metric-type',
            'is-user-notification-enabled',
            'critical-threshold',
        ]
    
    def describe_properties(self):
        return {
            'threshold_units': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'polling_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'warning_threshold': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dashboard_metric_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_user_notification_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'critical_threshold': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
