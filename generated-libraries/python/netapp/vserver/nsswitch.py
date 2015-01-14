class Nsswitch(basestring):
    """
    nis|file|ldap
    Possible values:
    <ul>
    <li> "nis"      ,
    <li> "file"     ,
    <li> "ldap"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "nsswitch"
    
