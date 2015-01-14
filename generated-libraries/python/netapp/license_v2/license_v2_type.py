class LicenseV2Type(basestring):
    """
    This field indicates the type of a license. A typical license will be of "license"
    type, which indicates that it's associated with a specific controller. A "site"
    license is a special license provided under Enterprise Level Agreements. A
    "demo" license is a temporary license with an expiration time. It is usually
    issued for trial purposes only.
    Possible values:
    <ul>
    <li> "license"  ,
    <li> "site"     ,
    <li> "demo"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "license-v2-type"
    
