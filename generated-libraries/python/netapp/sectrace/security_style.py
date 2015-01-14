class SecurityStyle(basestring):
    """
    Effective security style on file
    Possible values:
    <ul>
    <li> "security_none"           - Security not Set,
    <li> "security_unix_modebits"  - UNIX and UNIX permissions,
    <li> "security_unix_acl"       - UNIX and NFSv4 ACL,
    <li> "security_unix_sd"        - UNIX and NT ACL,
    <li> "security_mixed_modebits" - MIXED and UNIX permissions,
    <li> "security_mixed_acl"      - MIXED and NFSv4 ACL,
    <li> "security_mixed_sd"       - MIXED and NT ACL,
    <li> "security_ntfs_modebits"  - NTFS and UNIX permissions,
    <li> "security_ntfs_acl"       - NTFS and NT ACL,
    <li> "security_ntfs_sd"        - NTFS and NT ACL,
    <li> "security_unix"           - UNIX,
    <li> "security_mixed"          - MIXED,
    <li> "security_ntfs"           - NTFS,
    <li> "security_modebits"       - UNIX permissions,
    <li> "security_acl"            - ACL,
    <li> "security_sd"             - SD
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "security-style"
    
