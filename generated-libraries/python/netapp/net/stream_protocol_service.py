class StreamProtocolService(basestring):
    """
    The stream protocol connection classification
    Possible values:
    <ul>
    <li> "mount"         - Mount stream protocol,
    <li> "nfs"           - NFS stream protocol,
    <li> "nfs_v2"        - NFS version 2 stream protocol,
    <li> "nfs_v3"        - NFS version 3 stream protocol,
    <li> "nlm_v4"        - Network lock manager stream protocol,
    <li> "sm"            - Session Manager stream protocol,
    <li> "ftp_ctrl"      - FTP control stream protocol,
    <li> "ftp_data"      - FTP data stream protocol,
    <li> "http_1_0"      - HTTP version 1 stream protocol,
    <li> "http_1_1"      - HTTP version 1.1 stream protocol,
    <li> "iscsi"         - ISCSI stream protocol,
    <li> "cifs_srv"      - CIFS server stream protocol,
    <li> "cifs_nam"      - CIFS name server stream protocol,
    <li> "loopback"      - loopback stream protocol,
    <li> "rf"            - RC stream protocol,
    <li> "rawscp"        - Raw secure copy stream protocol,
    <li> "discard"       - Descard stream protocol,
    <li> "port_map"      - Port map stream protocol,
    <li> "pass_thru"     - Passthru stream protocol,
    <li> "rclopcp"       - Rc connection stream protocol,
    <li> "nfs_v4"        - NFS version 4 stream protocol,
    <li> "fcache"        - Flex cache stream protocol,
    <li> "ctlopcp"       - Ct connection stream protocol,
    <li> "rquota"        - Rquota stream protocol,
    <li> "cifs_msrpc"    - CIFS MsRpc stream protocol,
    <li> "unknown"       - unknown protocol
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "stream-protocol-service"
    
