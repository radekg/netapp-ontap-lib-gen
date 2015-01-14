class MaintTestId(basestring):
    """
    Test identifiers. 'disk-maint-list' returns a list of tests and identifiers.
    """
    
    @staticmethod
    def get_api_name():
          return "maint-test-id"
    
