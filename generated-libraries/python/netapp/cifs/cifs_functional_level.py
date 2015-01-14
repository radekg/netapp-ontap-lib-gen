class CifsFunctionalLevel(basestring):
    """
    Possible values are:
    <ul>
    <li>"windows_2000"
    <li>"windows_2003_with_mixed_domain"
    <li>"windows_2003"
    <li>"windows_2008"
    <li>"windows_2008R2"
    <li>"windows_8"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-functional-level"
    
