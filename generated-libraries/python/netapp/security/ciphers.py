class Ciphers(basestring):
    """
    cipher name
    Possible values:
    <ul>
    <li> "aes256_ctr"    ,
    <li> "aes192_ctr"    ,
    <li> "aes128_ctr"    ,
    <li> "aes256_cbc"    ,
    <li> "aes192_cbc"    ,
    <li> "aes128_cbc"    ,
    <li> "3des_cbc"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ciphers"
    
