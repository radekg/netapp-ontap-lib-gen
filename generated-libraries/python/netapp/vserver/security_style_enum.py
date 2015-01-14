class SecurityStyleEnum(basestring):
    """
    unix|ntfs|mixed|unified
    Possible values:
    <ul>
    <li> "unix"     - NFS,
    <li> "ntfs"     - CIFS,
    <li> "mixed"    - Mixed,
    <li> "unified"  - Unified
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "security-style-enum"
    
