class AddressInfoSocketType(basestring):
    """
    Denotes the type of socket for which address will be used.
    For example: stream socket/datagram socket.
    Possible values are: { sock_stream | sock_dgram | sock_raw | sock_rdm
    | sock_seqpacket | sock_stream_nonblk }
    "sock_stream" - stream socket.
    "sock_dgram" - datagram socket.
    "sock_raw" - raw protocol interface.
    "sock_rdm" - reliably delivered message.
    "sock_seqpacket" - sequenced packet stream.
    "sock_stream_nonblk" - sequenced packet stream non block.
    """
    
    @staticmethod
    def get_api_name():
          return "address-info-socket-type"
    
