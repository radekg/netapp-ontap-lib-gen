class LicenseType(basestring):
    """
    license|site|demo
    Possible values:
    <ul>
    <li> "license"  ,
    <li> "site"     ,
    <li> "demo"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "license-type"
    
