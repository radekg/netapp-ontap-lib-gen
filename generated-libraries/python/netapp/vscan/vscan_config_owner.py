class VscanConfigOwner(basestring):
    """
    Configuration owner
    Possible values:
    <ul>
    <li> "vserver"  - Vserver Admin,
    <li> "cluster"  - Cluter Admin
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vscan-config-owner"
    
