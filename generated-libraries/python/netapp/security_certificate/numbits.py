class Numbits(basestring):
    """
    size of requested certificate in bits
    Possible values:
    <ul>
    <li> "512"      - 512 bits private key,
    <li> "1024"     - 1024 bits private key,
    <li> "1536"     - 1536 bits private key,
    <li> "2048"     - 2048 bits private key
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "numbits"
    
