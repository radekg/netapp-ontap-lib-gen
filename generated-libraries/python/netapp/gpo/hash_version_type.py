class HashVersionType(basestring):
    """
    Hash Version
    Possible values:
    <ul>
    <li> "all_versions"  - Version 1 and 2 (V1 and V2).,
    <li> "version1"      - Version 1 (V1).,
    <li> "version2"      - Version 2 (V2).
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hash-version-type"
    
