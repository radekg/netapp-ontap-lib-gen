class SanSize(int):
    """
    Size in bytes
    Range : [0..2^63-1].
    """
    
    @staticmethod
    def get_api_name():
          return "san-size"
    
