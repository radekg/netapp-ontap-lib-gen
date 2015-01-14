class DnsZone(basestring):
    """
    Specifies the unique, fully qualified domain name of the DNS zone
    of this LIF.
    """
    
    @staticmethod
    def get_api_name():
          return "dns-zone"
    
