class WindowsSid(basestring):
    """
    Unique Windows Security Identifier that identifies a User or
    Group or Machine account.
    """
    
    @staticmethod
    def get_api_name():
          return "windows-sid"
    
