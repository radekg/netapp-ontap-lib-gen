class AsupDestination(basestring):
    """
    smtp|http|noteto|retransmit
    Possible values:
    <ul>
    <li> "smtp"          ,
    <li> "http"          ,
    <li> "noteto"        ,
    <li> "retransmit"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-destination"
    
