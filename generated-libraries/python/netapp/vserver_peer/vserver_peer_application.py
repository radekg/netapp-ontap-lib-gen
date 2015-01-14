class VserverPeerApplication(basestring):
    """
    Application using the Vserver peering relationship
    Possible values:
    <ul>
    <li> "snapmirror"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "vserver-peer-application"
    
