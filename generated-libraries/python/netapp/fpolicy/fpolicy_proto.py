class FpolicyProto(basestring):
    """
    Protocol
    Possible values:
    <ul>
    <li> "cifs"     - CIFS protocol,
    <li> "nfsv3"    - NFSv3 protocol,
    <li> "nfsv4"    - NFSv4 protocol
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-proto"
    
