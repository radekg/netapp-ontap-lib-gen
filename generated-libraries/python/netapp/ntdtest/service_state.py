class ServiceState(basestring):
    """
    down|up
    Possible values:
    <ul>
    <li> "down"     ,
    <li> "up"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "service-state"
    
