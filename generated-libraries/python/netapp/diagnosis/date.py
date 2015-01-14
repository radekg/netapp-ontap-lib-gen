class Date(int):
    """
    Date (in seconds since Jan. 1, 1970 12:00:00)
    Range : [0..2^31-1].
    """
    
    @staticmethod
    def get_api_name():
          return "date"
    
