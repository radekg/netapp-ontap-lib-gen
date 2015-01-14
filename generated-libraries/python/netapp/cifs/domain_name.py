class DomainName(basestring):
    """
    The domain name is an identification label that defines a realm
    based on Domain Name Service (DNS).
    """
    
    @staticmethod
    def get_api_name():
          return "domain-name"
    
