class Lunclass(basestring):
    """
    regular|protocol-endpoint|vvol
    Possible values:
    <ul>
    <li> "regular"            ,
    <li> "protocol_endpoint"  ,
    <li> "vvol"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "lunclass"
    
