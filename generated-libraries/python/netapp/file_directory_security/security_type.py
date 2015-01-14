class SecurityType(basestring):
    """
    ntfs|nfsv4
    Possible values:
    <ul>
    <li> "ntfs"     ,
    <li> "nfsv4"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "security-type"
    
