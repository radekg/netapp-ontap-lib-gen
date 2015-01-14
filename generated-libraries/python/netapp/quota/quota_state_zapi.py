class QuotaStateZapi(basestring):
    """
    Quota State ZAPI
    Possible values:
    <ul>
    <li> "off"           ,
    <li> "on"            ,
    <li> "initializing"  ,
    <li> "resizing"      ,
    <li> "corrupt"       ,
    <li> "upgrading"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "quota-state-zapi"
    
