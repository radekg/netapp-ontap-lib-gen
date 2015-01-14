class IscsiSessionType(basestring):
    """
    iSCSI Session Type
    Possible values:
    <ul>
    <li> "normal"        ,
    <li> "discovery"     ,
    <li> "error"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "iscsi-session-type"
    
