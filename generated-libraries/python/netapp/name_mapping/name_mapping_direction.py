class NameMappingDirection(basestring):
    """
    Direction of the name mapping.
    Possible values:
    <ul>
    <li> "krb_unix" - Kerberos principal name to UNIX user name
    mapping,
    <li> "win_unix" - Windows user name to UNIX user name
    mapping,
    <li> "unix_win" - UNIX user name to Windows user name mapping
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "name-mapping-direction"
    
