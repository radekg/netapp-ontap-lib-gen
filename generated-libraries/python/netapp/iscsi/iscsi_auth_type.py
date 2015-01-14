class IscsiAuthType(basestring):
    """
    CHAP|deny|none
    Possible values:
    <ul>
    <li> "chap"     ,
    <li> "deny"     ,
    <li> "none"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "iscsi-auth-type"
    
