class CifsAuthStyle(basestring):
    """
    domain|workgroup
    Possible values:
    <ul>
    <li> "domain"        - DOMAIN,
    <li> "workgroup"     - WORKGROUP
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-auth-style"
    
