class PeerPingProtocol(basestring):
    """
    The network protocol to use when performing the ping operation.
    Possible values:
    <ul>
    <li> "data"     - Data Ping,
    <li> "icmp"     - ICMP Ping
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "peer-ping-protocol"
    
