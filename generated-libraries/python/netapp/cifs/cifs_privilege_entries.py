class CifsPrivilegeEntries(basestring):
    """
    Privilege
    Possible values:
    <ul>
    <li> "setcbprivilege"               - Act as part of the
    operating system,
    <li> "sebackupprivilege"            - Back up files and
    directories, overriding any ACLs,
    <li> "serestoreprivilege"           - Restore files and
    directories, overriding any ACLs,
    <li> "setakeownershipprivilege"     - Take ownership of files
    or other objects,
    <li> "sesecurityprivilege"          - Manage auditing and
    viewing/dumping/clearing the security log
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-privilege-entries"
    
