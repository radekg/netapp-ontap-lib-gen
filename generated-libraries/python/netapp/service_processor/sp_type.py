class SpType(basestring):
    """
    Types of remote management device that can be found in a node
    Possible values:
    <ul>
    <li> "rlm"      - Remote LAN Module,
    <li> "sp"       - Service Processor,
    <li> "none"     - None
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-type"
    
