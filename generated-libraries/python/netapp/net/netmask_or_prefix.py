class NetmaskOrPrefix(basestring):
    """
    netmask.  Possible values: dotted decimal or
    hex integer (range: 0x1 .. 0xffffffff)
    or '/' followed by hex integer (range: 0x1 .. 0x40)
    Default if not specified is classful:
    Class A address - 255.0.0.0 or 0xff000000 or /8
    Class B address - 255.255.0.0 or 0xffff0000 or /16
    Class C address - 255.255.255.0 or 0xffffff00 or /24
    IPV6 address prefix - /1 through /128
    """
    
    @staticmethod
    def get_api_name():
          return "netmask-or-prefix"
    
