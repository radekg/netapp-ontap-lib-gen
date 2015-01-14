class DashboardMetricType(basestring):
    """
    Metric Type
    Possible values:
    <ul>
    <li> "cpu_busy"           - CPU Utilization,
    <li> "port_util"          - Port Utilization,
    <li> "op_latency"         - Average Client Latency of NFS and
    CIFS operations,
    <li> "aggregate_used"     - Storage Aggregate Utilization,
    <li> "port_problems"      - Packet Error Ratio
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "dashboard-metric-type"
    
