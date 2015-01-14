class CifsDialects(basestring):
    """
    The list of possible known dialects Dialects negotiated by CIFS servers.
    Possible values:
    <ul>
    <li> "SMB1"            - SMB 1.0
    <li> "SMB2"            - SMB 2.0
    <li> "SMB2_1"          - SMB 2.1
    <li> "SMB3"            - SMB 3.0
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-dialects"
    
