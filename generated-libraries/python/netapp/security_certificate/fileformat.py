class Fileformat(basestring):
    """
    certificate format
    Possible values:
    <ul>
    <li> "pkcs12"   ,
    <li> "pem"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fileformat"
    
