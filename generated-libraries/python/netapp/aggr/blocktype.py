class Blocktype(basestring):
    """
    32-bit|64-bit
    Possible values:
    <ul>
    <li> "32_bit"   ,
    <li> "64_bit"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "blocktype"
    
