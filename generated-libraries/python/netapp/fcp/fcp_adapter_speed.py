class FcpAdapterSpeed(basestring):
    """
    1|2|4|8|10|16|auto
    Possible values:
    <ul>
    <li> "auto"     ,
    <li> "1"        ,
    <li> "2"        ,
    <li> "4"        ,
    <li> "8"        ,
    <li> "10"       ,
    <li> "16"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-speed"
    
