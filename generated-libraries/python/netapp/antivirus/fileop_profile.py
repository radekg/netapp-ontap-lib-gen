class FileopProfile(basestring):
    """
    cifs-nfs4-only|nfs3_only|multi-proto-standard|multi-proto-strict
    Possible values:
    <ul>
    <li> "cifs_nfs4_only"          ,
    <li> "nfs3_only"               ,
    <li> "multi_proto_standard"    ,
    <li> "multi_proto_strict"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fileop-profile"
    
