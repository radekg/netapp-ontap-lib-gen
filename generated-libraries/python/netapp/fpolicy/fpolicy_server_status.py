class FpolicyServerStatus(basestring):
    """
    Status
    Possible values:
    <ul>
    <li> "connected"     - Server Connected,
    <li> "disconnected"  - Server Disconnected,
    <li> "connecting"    - Connecting Server,
    <li> "disconnecting" - Disconnecting Server
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-server-status"
    
