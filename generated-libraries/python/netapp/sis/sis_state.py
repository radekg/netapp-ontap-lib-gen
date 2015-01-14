class SisState(basestring):
    """
    Disabled|Enabled
    Possible values:
    <ul>
    <li> "disabled" ,
    <li> "enabled"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-state"
    
