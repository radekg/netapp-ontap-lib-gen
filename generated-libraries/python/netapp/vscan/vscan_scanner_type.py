class VscanScannerType(basestring):
    """
    Server type
    Possible values:
    <ul>
    <li> "primary"  - Primary,
    <li> "backup"   - Backup
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-scanner-type"
    
