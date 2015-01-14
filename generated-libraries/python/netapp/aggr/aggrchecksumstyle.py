class Aggrchecksumstyle(basestring):
    """
    checksum style
    Possible values:
    <ul>
    <li> "none"               ,
    <li> "zoned"              ,
    <li> "block"              ,
    <li> "wafl"               ,
    <li> "mixed"              ,
    <li> "unknown"            ,
    <li> "azcs"               ,
    <li> "advanced_zoned"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "aggrchecksumstyle"
    
