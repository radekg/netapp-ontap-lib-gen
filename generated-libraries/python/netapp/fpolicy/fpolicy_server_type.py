class FpolicyServerType(basestring):
    """
    Server Type
    Possible values:
    <ul>
    <li> "primary"       - Primary Server,
    <li> "secondary"     - Secondary Server
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-server-type"
    
