class Hashfunction(basestring):
    """
    hashing function
    Possible values:
    <ul>
    <li> "sha1"     ,
    <li> "sha256"   ,
    <li> "md5"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hashfunction"
    
