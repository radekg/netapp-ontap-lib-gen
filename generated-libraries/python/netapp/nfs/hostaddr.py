class Hostaddr(basestring):
    """
    the individual client hosts. could be a hostname or an IP
    address.
    """
    
    @staticmethod
    def get_api_name():
          return "hostaddr"
    
