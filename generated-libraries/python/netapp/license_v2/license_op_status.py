class LicenseOpStatus(basestring):
    """
    License Operation Status
    Possible values:
    <ul>
    <li> "license_success"         - Operation Completed
    Successfully,
    <li> "license_invalid"         - Failed: Invalid License Key,
    <li> "license_expired"         - Failed: License Expired,
    <li> "license_notallowed"      - Failed: Operation Not
    Allowed,
    <li> "license_unavailable"     - Failed: License Not
    Available,
    <li> "license_internal"        - Failed: Internal Error,
    <li> "license_err_unknown"     - Failed: Unknown Error
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "license-op-status"
    
