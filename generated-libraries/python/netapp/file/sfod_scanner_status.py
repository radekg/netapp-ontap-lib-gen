class SfodScannerStatus(basestring):
    """
    sfod_scanner_status
    Possible values:
    <ul>
    <li> "preparing"          - Preparing,
    <li> "allocation_map"     - Allocating,
    <li> "data"               - Moving Data,
    <li> "destroy"            - Destroying,
    <li> "paused_admin"       - Paused by Admin,
    <li> "paused_error"       - Paused by Error,
    <li> "complete"           - Complete,
    <li> "failed"             - Failed
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sfod-scanner-status"
    
