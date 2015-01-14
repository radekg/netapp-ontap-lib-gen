from netapp.connection import NaConnection
from threshold_unit import ThresholdUnit # 0 properties
from dashboard_alarm_info import DashboardAlarmInfo # 6 properties
from alarm_state import AlarmState # 0 properties
from dashboard_alarm_threshold_info import DashboardAlarmThresholdInfo # 6 properties
from dashboard_alarm_get_iter_key_td import DashboardAlarmGetIterKeyTd # 3 properties
from dashboard_metric_type import DashboardMetricType # 0 properties
from dashboard_alarm_threshold_get_iter_key_td import DashboardAlarmThresholdGetIterKeyTd # 1 properties

class DashboardConnection(NaConnection):
    
    def dashboard_alarm_threshold_modify(self, dashboard_metric_type, threshold_units=None, polling_interval=None, warning_threshold=None, is_user_notification_enabled=None, critical_threshold=None):
        """
        Modify alarm threshold settings for the given metric group.
        
        :param dashboard_metric_type: The type of metric being monitored.
                Possible values:
                <ul>
                <li> "cpu_busy"       - CPU Utilization,
                <li> "port_util"      - Port Utilization,
                <li> "op_latency"     - Average Client Latency of NFS and CIFS
                operations,
                <li> "aggregate_used" - Storage Aggregate Utilization,
                <li> "port_problems"  - Packet Error Ratio
                </ul>
        
        :param threshold_units: Threshold Units
                Possible values:
                <ul>
                <li> "none"      - none,
                <li> "ms"        - milliseconds,
                <li> "percent"   - percent
                </ul>
        
        :param polling_interval: The refresh interval for the alarm dashboard metrics (in
                seconds).
        
        :param warning_threshold: The threshold value that must be reached to generate a warning
                alarm for this type of metric. Get request is returned with %
                sign for percent values and ms for milliseconds value. Example :
                85%, 200ms
        
        :param is_user_notification_enabled: Specifies whether user notifications are enabled.
        
        :param critical_threshold: The threshold value that must be reached to generate a critical
                alarm for this type of metric. Get request is returned with %
                sign for percent values and ms for milliseconds value. Example :
                95%, 500ms
        """
        return self.request( "dashboard-alarm-threshold-modify", {
            'threshold_units': [ threshold_units, 'threshold-units', [ basestring, 'threshold-unit' ], False ],
            'polling_interval': [ polling_interval, 'polling-interval', [ int, 'None' ], False ],
            'warning_threshold': [ warning_threshold, 'warning-threshold', [ basestring, 'None' ], False ],
            'dashboard_metric_type': [ dashboard_metric_type, 'dashboard-metric-type', [ basestring, 'dashboard-metric-type' ], False ],
            'is_user_notification_enabled': [ is_user_notification_enabled, 'is-user-notification-enabled', [ bool, 'None' ], False ],
            'critical_threshold': [ critical_threshold, 'critical-threshold', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def dashboard_alarm_get(self, node, object_name, dashboard_metric_type, desired_attributes=None):
        """
        Get alarm monitoring data for the given node object.
        
        :param node: Name of the node associated with the alarm metrics.
        
        :param object_name: Name associated with the object being monitored.  For example,
                the object-name is the name of the node if the
                dashboard-metric-type is cpu-busy.
        
        :param dashboard_metric_type: The type of metric being monitored.
                Possible values:
                <ul>
                <li> "cpu_busy"       - CPU Utilization,
                <li> "port_util"      - Port Utilization,
                <li> "op_latency"     - Average Client Latency of NFS and CIFS
                operations,
                <li> "aggregate_used" - Storage Aggregate Utilization,
                <li> "port_problems"  - Packet Error Ratio
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "dashboard-alarm-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'object_name': [ object_name, 'object-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DashboardAlarmInfo, 'None' ], False ],
            'dashboard_metric_type': [ dashboard_metric_type, 'dashboard-metric-type', [ basestring, 'dashboard-metric-type' ], False ],
        }, {
            'attributes': [ DashboardAlarmInfo, False ],
        } )
    
    def dashboard_alarm_threshold_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "dashboard-alarm-threshold-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def dashboard_alarm_get_total_records(self):
        """
        Return the total number of records.
        """
        return self.request( "dashboard-alarm-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def dashboard_alarm_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get alarm monitoring data for all objects in the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                dashboard-alarm object.
                All dashboard-alarm objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "dashboard-alarm-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DashboardAlarmInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DashboardAlarmInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DashboardAlarmInfo, True ],
        } )
    
    def dashboard_alarm_threshold_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get alarm threshold settings for all metric groups.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                dashboard-alarm-threshold object.
                All dashboard-alarm-threshold objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "dashboard-alarm-threshold-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DashboardAlarmThresholdInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DashboardAlarmThresholdInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DashboardAlarmThresholdInfo, True ],
        } )
    
    def dashboard_alarm_threshold_get(self, dashboard_metric_type, desired_attributes=None):
        """
        Get alarm threshold settings for the given metric group.
        
        :param dashboard_metric_type: The type of metric being monitored.
                Possible values:
                <ul>
                <li> "cpu_busy"       - CPU Utilization,
                <li> "port_util"      - Port Utilization,
                <li> "op_latency"     - Average Client Latency of NFS and CIFS
                operations,
                <li> "aggregate_used" - Storage Aggregate Utilization,
                <li> "port_problems"  - Packet Error Ratio
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "dashboard-alarm-threshold-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DashboardAlarmThresholdInfo, 'None' ], False ],
            'dashboard_metric_type': [ dashboard_metric_type, 'dashboard-metric-type', [ basestring, 'dashboard-metric-type' ], False ],
        }, {
            'attributes': [ DashboardAlarmThresholdInfo, False ],
        } )
