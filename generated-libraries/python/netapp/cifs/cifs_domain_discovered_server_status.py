class CifsDomainDiscoveredServerStatus(basestring):
    """
    Classification of server based on the status of the connection.
    Possible values:
    <ul>
    <li> "ok"            - The connection to this server is
    usable.,
    <li> "unavailable"   - This server is currently unavailable
    for use.,
    <li> "slow"          - The connection to this server is usable
    but slow.,
    <li> "expired"       - The connection to this server has
    expired.,
    <li> "undetermined"  - A connection to this server has not
    been attempted.,
    <li> "unreachable"   - This server is currently unreachable.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-discovered-server-status"
    
