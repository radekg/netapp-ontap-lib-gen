class AuditAccessType(basestring):
    """
    failure|success
    Possible values:
    <ul>
    <li> "failure"  ,
    <li> "success"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "audit-access-type"
    
