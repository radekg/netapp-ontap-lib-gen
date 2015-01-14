class Protocol(basestring):
    """
    Vserver protocols.
    Possible values:
    <ul>
    <li> "nfs"      - NFS protocol,
    <li> "cifs"     - CIFS protocol,
    <li> "fcp"      - FCP protocol,
    <li> "iscsi"    - iSCSI protocol,
    <li> "ndmp"     - NDMP protocol
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "protocol"
    
