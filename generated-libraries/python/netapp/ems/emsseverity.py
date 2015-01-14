class Emsseverity(basestring):
    """
    NODE_FAULT|SVC_FAULT|NODE_ERROR|SVC_ERROR|WARNING|NOTICE|INFO|DEBUG|VAR
    Possible values:
    <ul>
    <li> "node_fault"    - A data corruption has been detected or
    the node is unable to provide client service,
    <li> "svc_fault"     - A temporary loss of service has been
    detected, typically a transient software fault,
    <li> "node_error"    - A hardware error has been detected
    which is not immediately fatal,
    <li> "svc_error"     - A software error has been detected
    which is not immediately fatal,
    <li> "warning"       - A high-priority message, does not
    indicate a fault,
    <li> "notice"        - A normal-priority message, does not
    indicate a fault,
    <li> "info"          - A low-priority message, does not
    indicate a fault,
    <li> "debug"         - A debugging message, typically
    suppressed from customer,
    <li> "var"           - Message has variable severity, selected
    at runtime
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "emsseverity"
    
