class AccessProtocol(basestring):
    """
    any|nfs3|nfs|cifs|nfs4|flexcache
    Possible values:
    <ul>
    <li> "any"           - Any,
    <li> "nfs2"          - NFS Version 2,
    <li> "nfs3"          - NFS Version 3,
    <li> "nfs"           - Any Version of NFS,
    <li> "cifs"          - CIFS,
    <li> "nfs4"          - NFS Version 4,
    <li> "flexcache"     - Flexcache
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "access-protocol"
    
