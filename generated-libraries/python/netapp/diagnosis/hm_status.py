class HmStatus(basestring):
    """
    Health Monitor Status(ok, ok-with-suppressed, degraded, unknown)
    Possible values:
    <ul>
    <li> "ok"                 ,
    <li> "ok_with_suppressed" ,
    <li> "degraded"           ,
    <li> "unreachable"        ,
    <li> "unknown"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hm-status"
    
