class RevertVersion(basestring):
    """
    revert version
    Possible values:
    <ul>
    <li> "8_1" - Data ONTAP 8.1
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "revert-version"
    
