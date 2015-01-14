class Datetime(int):
    """
    The number of seconds since January 1, 1970.
    Range : [0..2^31-1].
    """
    
    @staticmethod
    def get_api_name():
          return "datetime"
    
