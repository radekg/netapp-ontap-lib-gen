class NetbiosName(basestring):
    """
    Name of a client or a server participating in a NetBIOS Windows
    File sharing service network. This can be different from the host
    name.
    """
    
    @staticmethod
    def get_api_name():
          return "netbios-name"
    
