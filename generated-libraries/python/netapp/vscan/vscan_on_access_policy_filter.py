class VscanOnAccessPolicyFilter(basestring):
    """
    Filters to to define the scope of On-Access scanning more
    precisely.
    Possible values:
    <ul>
    <li> "scan_mandatory"          - Enable mandatory scan,
    <li> "scan_ro_volume"          - Enable scans for read-only
    volume,
    <li> "scan_execute_access"     - Scan only files opened with
    execute-access (CIFS only)
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-on-access-policy-filter"
    
