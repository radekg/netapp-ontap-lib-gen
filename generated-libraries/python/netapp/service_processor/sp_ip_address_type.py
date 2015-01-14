class SpIpAddressType(basestring):
    """
    Choices for which IP version to use
    Possible values:
    <ul>
    <li> "ipv4"     - Internet Protocol version 4,
    <li> "ipv6"     - Internet Protocol version 6
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-ip-address-type"
    
