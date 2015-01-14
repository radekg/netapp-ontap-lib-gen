class VscanDisconnectReason(basestring):
    """
    reason
    Possible values:
    <ul>
    <li> "na"                      - Not applicable,
    <li> "vscan_disabled"          - Vscan disabled on the
    vserver,
    <li> "no_data_lif"             - Vserver does not have data
    lif on the node,
    <li> "session_uninitialized"   - Session not initialized,
    <li> "remote_closed"           - Closure from Server,
    <li> "invalid_protocol_msg"    - Invalid protocol-message
    received,
    <li> "invalid_session_id"      - Invalid session-id received,
    <li> "inactive_connection"     - No activity on connection
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-disconnect-reason"
    
