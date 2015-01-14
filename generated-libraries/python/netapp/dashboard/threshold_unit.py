class ThresholdUnit(basestring):
    """
    Dashboard Threshold Units
    Possible values:
    <ul>
    <li> "none"     - none,
    <li> "ms"       - milliseconds,
    <li> "percent"  - percent
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "threshold-unit"
    
