class FcpConnection(basestring):
    """
    loop|ptp
    Possible values:
    <ul>
    <li> "loop"     ,
    <li> "ptp"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fcp-connection"
    
