class Filter(basestring):
    """
    Instance filter specified as a comma-seperated list of
    "counter=value" pairs.
    """
    
    @staticmethod
    def get_api_name():
          return "filter"
    
