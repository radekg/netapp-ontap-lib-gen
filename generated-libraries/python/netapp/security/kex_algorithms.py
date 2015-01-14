class KexAlgorithms(basestring):
    """
    algorithm name
    Possible values:
    <ul>
    <li> "diffie_hellman_group_exchange_sha256"   ,
    <li> "diffie_hellman_group_exchange_sha1"     ,
    <li> "diffie_hellman_group14_sha1"            ,
    <li> "diffie_hellman_group1_sha1"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "kex-algorithms"
    
