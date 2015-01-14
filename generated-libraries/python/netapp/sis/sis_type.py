class SisType(basestring):
    """
    Regular|SnapVault
    Possible values:
    <ul>
    <li> "regular"       ,
    <li> "snapvault"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-type"
    
