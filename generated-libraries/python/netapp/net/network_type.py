class NetworkType(basestring):
    """
    The network topology classification
    Possible values:
    <ul>
    <li> "wan"           ,
    <li> "lan"           ,
    <li> "undefined"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "network-type"
    
