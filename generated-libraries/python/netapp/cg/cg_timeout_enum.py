class CgTimeoutEnum(basestring):
    """
    urgent|medium|relaxed
    Possible values:
    <ul>
    <li> "urgent"   ,
    <li> "medium"   ,
    <li> "relaxed"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cg-timeout-enum"
    
