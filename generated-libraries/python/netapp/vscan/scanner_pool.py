class ScannerPool(basestring):
    """
    Scanner pool is a set of attributes which are used to validate
    and manage connections between clustered ONTAP and Vscan servers
    (virus scanners).
    """
    
    @staticmethod
    def get_api_name():
          return "scanner-pool"
    
