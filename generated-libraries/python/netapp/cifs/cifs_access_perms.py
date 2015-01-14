class CifsAccessPerms(basestring):
    """
    access rights
    Possible values:
    <ul>
    <li> "no_access"     - No access,
    <li> "read"          - Read,
    <li> "change"        - Change,
    <li> "full_control"  - Full Control
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-access-perms"
    
