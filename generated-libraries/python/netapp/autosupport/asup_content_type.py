class AsupContentType(basestring):
    """
    Type of AutoSupport content
    Possible values:
    <ul>
    <li> "basic"              - ASUP will contain minimal set of
    data for this subsystem,
    <li> "troubleshooting"    - ASUP will contain detailed
    collection of data for this subsystem
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-content-type"
    
