class AddressInfoFamily(basestring):
    """
    Denotes protocol family of the address.
    Possible values: { af_unspec | af_local | af_unix |af_inet | af_implink
    | af_pup | af_chaos | af_ns |  af_iso | af_osi | af_ecma | af_datakit
    | af_ccitt | af_sna | af_decnet | af_dli |af_lat | af_hylink
    | af_appletalk | af_route | af_link | pseudo_af_xtp | af_coip
    | af_cnt | pseudo_af_rtip | af_ipx | af_sip | pseudo_af_pip | af_inet6 }
    "af_unspec" - ipv4 or ipv6 address family.
    "af_local" - local to host (pipes, portals).
    "af_unix" - same as af_local  backward compatibility
    "af_inet" - internetwork: udp, tcp, etc.
    "af_implink" - arpanet imp addresses
    "af_pup" - pup protocols: e.g. bsp
    "af_chaos" - mit chaos protocols
    "af_ns" - xerox ns protocols
    "af_iso" - iso protocols
    "af_osi" - same as af_iso backward compatibility
    "af_ecma" - european computer manufacturers
    "af_datakit" - datakit protocols
    "af_ccitt" - ccitt protocols, x.25 etc/
    "af_sna"  - ibm sna
    "af_decnet" - decnet
    "af_dli" - dec direct data link interface
    "af_lat" -  lat
    "af_hylink" - nsc hyperchannel
    "af_appletalk" - apple talk
    "af_route" - internal routing protocol
    "af_link" - link layer interface
    "pseudo_af_xtp" - express transfer protocol (no af)
    "af_coip" - connection-oriented ip
    "af_cnt" - computer network technology
    "pseudo_af_rtip" - help identify rtip packets
    "af_ipx" - novell internet protocol
    "af_sip" - simple internet protocol
    "pseudo_af_pip" - help identify pip packets
    "af_inet6" - ipv6 address family
    """
    
    @staticmethod
    def get_api_name():
          return "address-info-family"
    
