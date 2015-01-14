class AlarmState(basestring):
    """
    Alarm Monitoring State
    Possible values:
    <ul>
    <li> "ok"       ,
    <li> "warning"  ,
    <li> "critical"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "alarm-state"
    
