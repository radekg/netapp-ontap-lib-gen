class IpAddressOrHostname(basestring):
    """
    IP address string.  For example, 198.18.100.12,
    or "`hostname`-e0c"  (backquoted hostname is allowed)
    or "toaster"  (assuming toaster resolves to an IP address)
    or fd20:8b1e:b255:104:230:48ff:fe8c:6326
    """
    
    @staticmethod
    def get_api_name():
          return "ip-address-or-hostname"
    
