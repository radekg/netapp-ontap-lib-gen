class CifsShareName(basestring):
    """
    The name of the CIFS share. The CIFS share name is a Unicode
    string with the following characters being illegal: control
    characters from 0x00 to 0x1F, both inclusive, 0x22 (double
    quotes) and the characters \/[]:|<>+=;,?
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-share-name"
    
