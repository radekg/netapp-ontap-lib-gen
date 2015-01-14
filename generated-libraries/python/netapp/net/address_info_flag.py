class AddressInfoFlag(basestring):
    """
    Each flag represents a filter criteria.  For example if
    the "passive" flag is used then the returned address
    information shall be suitable for use in binding a
    socket for accepting incoming connections for the
    specified service.  If the "canonical_name" flag is
    specified and the host-name argument is not null, the
    function shall attempt to determine the canonical name
    corresponding to host-name argument.
    Possible values are: { ai_passive | ai_canonname
    ai_numerichost | ai_all | ai_addrconfig |
    ai_vp4mapped | ai_addrconfig | ai_default }.
    "ai_passive" - get address to use bind().
    "ai_canonname" - fill ai_canonname.
    "ai_numerichost" - prevent name resolution.
    "ai_all" - IPv6 and IPv4-mapped (with AI_V4MAPPED).
    "ai_vp4mapped_cfg" - accept IPv4-mapped if kernel supports.
    "ai_addrconfig" - only if any address is assigned.
    "ai_vp4mapped" - accept IPv4-mapped IPv6 address.
    "ai_default" - ( ai_vp4mapped_cfg | ai_addrconfig ).
    "numeric_host" can appear in any combination along
    with "all", "ip4_mapped_configuration",
    "address_configuration", and "ip4_mapped".
    """
    
    @staticmethod
    def get_api_name():
          return "address-info-flag"
    
