class Connectiontype(basestring):
    """
    direct|fabric
    Possible values:
    <ul>
    <li> "direct"   - The port is direct attached.,
    <li> "fabric"   - The port is fabric attached.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "connectiontype"
    
