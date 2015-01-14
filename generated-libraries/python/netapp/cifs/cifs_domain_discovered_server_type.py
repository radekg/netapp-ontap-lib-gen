class CifsDomainDiscoveredServerType(basestring):
    """
    The classification of servers based on service provided.
    Possible values:
    <ul>
    <li> "unknown"  - The server type is not known,
    <li> "kerberos" - Kerberos server,
    <li> "ms_ldap"  - Microsoft Lightweight Directory Access
    Protocol (LDAP) server,
    <li> "ms_dc"    - Microsoft Domain Controller,
    <li> "ldap"     - Lightweight Directory Access Protocol (LDAP)
    server,
    <li> "nis"      - Network Information Service (NIS) server
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-discovered-server-type"
    
