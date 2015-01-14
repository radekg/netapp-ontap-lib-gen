class LicensedMethod(basestring):
    """
    Licensed Method
    Possible values:
    <ul>
    <li> "none"     - None,
    <li> "license"  - License,
    <li> "site"     - Site,
    <li> "demo"     - Demo
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "licensed-method"
    
