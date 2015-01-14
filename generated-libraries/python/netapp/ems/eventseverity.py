class Eventseverity(basestring):
    """
    EMERGENCY|ALERT|CRITICAL|ERROR|WARNING|NOTICE|INFORMATIONAL|DEBUG
    Possible values:
    <ul>
    <li> "emergency"     - System is unusable,
    <li> "alert"         - Action must be taken immediately,
    <li> "critical"      - Critical condition,
    <li> "error"         - Error condition,
    <li> "warning"       - Warning condition,
    <li> "notice"        - Normal but significant condition,
    <li> "informational" - Information message,
    <li> "debug"         - A debugging message
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "eventseverity"
    
