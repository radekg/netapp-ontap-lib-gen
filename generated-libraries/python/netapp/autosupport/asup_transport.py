class AsupTransport(basestring):
    """
    smtp|http|https
    Possible values:
    <ul>
    <li> "smtp"     ,
    <li> "http"     ,
    <li> "https"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-transport"
    
