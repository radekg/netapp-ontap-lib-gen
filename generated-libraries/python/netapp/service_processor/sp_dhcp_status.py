class SpDhcpStatus(basestring):
    """
    Possible configurations for DHCP protocol
    Possible values:
    <ul>
    <li> "v4"       - DHCP for IPv4,
    <li> "none"     - DHCP not enabled
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-dhcp-status"
    
