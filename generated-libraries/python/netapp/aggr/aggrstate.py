class Aggrstate(basestring):
    """
    aggregate state
    Possible values:
    <ul>
    <li> "online"             ,
    <li> "creating"           ,
    <li> "mounting"           ,
    <li> "relocating"         ,
    <li> "quiesced"           ,
    <li> "quiescing"          ,
    <li> "unmounted"          ,
    <li> "unmounting"         ,
    <li> "destroying"         ,
    <li> "partial"            ,
    <li> "frozen"             ,
    <li> "reverted"           ,
    <li> "restricted"         ,
    <li> "inconsistent"       ,
    <li> "iron_restricted"    ,
    <li> "unknown"            ,
    <li> "offline"            ,
    <li> "failed"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "aggrstate"
    
