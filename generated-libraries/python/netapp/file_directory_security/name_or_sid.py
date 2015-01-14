class NameOrSid(basestring):
    """
    An user or group name that is specified in the form of valid
    username/groupname with domain or valid SID string
    """
    
    @staticmethod
    def get_api_name():
          return "name-or-sid"
    
