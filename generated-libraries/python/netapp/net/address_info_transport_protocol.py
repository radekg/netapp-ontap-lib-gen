class AddressInfoTransportProtocol(basestring):
    """
    Denotes the type of transport protocol for which address will
    be used. Possible values are:
    { ipproto_ip | iproto_hopopts | iproto_icmp | ipproto_igmp | ipproto_ggp |
    ipproto_ipv4 | ipproto_ipip | iproto_tcp | ipproto_egp | ipproto_pup |
    iprpoto_udp | ipproto_idp | ipproto_tp | ipproto_ipv6 | ipproto_routing |
    ipproto_fragment | ipproto_gre | iprpoto_esp | ipproto_ah | ipproto_icmpv6 |
    ipproto_none | ipproto_dstopts | ipproto_eon | ipproto_encap | ipproto_ssl |
    ipproto_ipcomp | ipproto_raw | ipproto_done }
    "ipproto_ip" - dummy for IP protocol type.
    "ipproto_hopopts" - IPv6 hop-by-hop options.
    "ipproto_icmp" - control message protocol.
    "ipproto_igmp" - group mgmt protocol
    "ipproto_ggp" -	gateway protocol
    "ipproto_ipv4" - IPv4 encapsulation
    "ipproto_ipip" - for compatibility with IPV4
    "ipproto_tcp" - transport control protocol
    "ipproto_egp" -	Exterior gateway protocol
    "ipproto_pup" -	pup
    "iprpoto_udp" -	 user datagram protocol
    "ipproto_idp" - xns idp
    "ipproto_tp" - tp-4 class negotiation
    "ipproto_ipv6" - IPv6 header
    "ipproto_routing" - IPv6 routing header
    "ipproto_fragment" - IPv6 fragmentation header
    "ipproto_gre" - Generic Routing Encapsulation
    "iprpoto_esp" - IPv6 Encap Sec. Payload
    "ipproto_ah" -IPv6 Auth Header
    "ipproto_icmpv6" ICMP6
    "ipproto_none" - IPv6 no next header
    "ipproto_dstopts" - IPv6 destination option
    "ipproto_eon" - ISO cnlp
    "ipproto_encap" - encapsulation header
    "ipproto_ssl" ssl protocol
    "ipproto_ipcomp" - IP Payload Compression Protocol
    "ipproto_raw" - raw protocl
    "ipproto_done" - all job for this pkt is done
    """
    
    @staticmethod
    def get_api_name():
          return "address-info-transport-protocol"
    
