class ProtocolLayer4(basestring):
    """
    The network layer 4 protocol type
    Possible values:
    <ul>
    <li> "udp" - UDP,
    <li> "tcp" - TCP,
    <li> "na"  - not_available
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "protocol-layer4"
    
