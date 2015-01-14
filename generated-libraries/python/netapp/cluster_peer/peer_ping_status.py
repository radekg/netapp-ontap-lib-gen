class PeerPingStatus(basestring):
    """
    The status of the ping operation.
    Possible values:
    <ul>
    <li> "unknown_node"            - Unknown Node,
    <li> "internal_error"          - Internal Error,
    <li> "unreachable"             - Unreachable,
    <li> "session_reachable"       - Session Reachable,
    <li> "interface_reachable"     - Interface Reachable
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "peer-ping-status"
    
