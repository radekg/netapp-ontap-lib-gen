class ReposConstituentRole(basestring):
    """
    Constituent Roles
    Possible values:
    <ul>
    <li> "namespace"     ,
    <li> "data"          ,
    <li> "ols"           ,
    <li> "ns_mirror"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "repos-constituent-role"
    
