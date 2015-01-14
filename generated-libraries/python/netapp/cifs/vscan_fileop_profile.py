class VscanFileopProfile(basestring):
    """
    Profile-set of file-ops to which Vscan On-Access scanning
    is applicable.
    Possible values:
    <ul>
    <li> "no_scan"     - Virus scans are never triggered for
    accesses to this share,
    <li> "standard"    - Virus scans can be triggered by open,
    close, and rename operations,
    <li> "strict"      - Virus scans can be triggered by open,
    read, close, and rename operations,
    <li> "writes_only" - Virus scans can be triggered only when
    a file that has been modified is closed.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-fileop-profile"
    
