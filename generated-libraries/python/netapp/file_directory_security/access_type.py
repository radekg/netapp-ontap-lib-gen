class AccessType(basestring):
    """
    deny|allow
    Possible values:
    <ul>
    <li> "deny"     ,
    <li> "allow"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "access-type"
    
