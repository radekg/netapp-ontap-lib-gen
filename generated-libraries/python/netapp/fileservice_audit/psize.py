class Psize(int):
    """
    size in bytes
    Range : [1..2^63-1].
    """
    
    @staticmethod
    def get_api_name():
          return "psize"
    
