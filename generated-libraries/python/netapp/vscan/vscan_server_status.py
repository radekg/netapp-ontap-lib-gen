class VscanServerStatus(basestring):
    """
    Status
    Possible values:
    <ul>
    <li> "disconnected"  - Disconnected,
    <li> "disconnecting" - Disconnecting,
    <li> "connecting"    - Connecting,
    <li> "connected"     - Connected
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-server-status"
    
