class SleepLocation(basestring):
    """
    Used to determine where the zapi sleeps
    Possible values:
    <ul>
    <li> "mgwd"     ,
    <li> "dblade"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sleep-location"
    
