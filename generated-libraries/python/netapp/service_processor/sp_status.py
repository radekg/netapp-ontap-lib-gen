class SpStatus(basestring):
    """
    Possible states a Service Processor or Remote LAN Module can be
    in
    Possible values:
    <ul>
    <li> "online"             - Device is up and running fine,
    <li> "offline"            - Device is out of communication,
    <li> "sp_daemon_offline"  - Daemon which communicates with the
    device is not running,
    <li> "node_offline"       - Node that hosts the device is out
    of communication,
    <li> "degraded"           - Node that hosts the device is
    missing heartbeat signals from the device,
    <li> "rebooting"          - Device is rebooting,
    <li> "unknown"            - Device status could not be
    determined
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-status"
    
