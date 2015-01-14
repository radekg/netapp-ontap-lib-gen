class KdcVendor(basestring):
    """
    Kerberos Key Distribution Center (KDC) Vendor
    Possible values:
    <ul>
    <li> "microsoft"     ,
    <li> "other"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "kdc-vendor"
    
