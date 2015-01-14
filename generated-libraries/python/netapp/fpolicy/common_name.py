class CommonName(basestring):
    """
    Represents the domain name in FQDN form that specifies its exact
    location in the tree hierarchy of the Domain Name System (DNS).
    """
    
    @staticmethod
    def get_api_name():
          return "common-name"
    
