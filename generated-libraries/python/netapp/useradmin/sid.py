class Sid(basestring):
    """
    Windows security identifier describing a user. A SID
    has the format S-1-5-21-int-int-int-rid.
    """
    
    @staticmethod
    def get_api_name():
          return "sid"
    
