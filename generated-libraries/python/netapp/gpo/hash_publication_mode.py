class HashPublicationMode(basestring):
    """
    Hash Support
    Possible values:
    <ul>
    <li> "per_share"     - Allow hash publication only for shared
    folders on which BranchCache is enabled.,
    <li> "disabled"      - Disallow hash publication on all shared
    folders.,
    <li> "all_shares"    - Allow hash publication for all shared
    folder.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hash-publication-mode"
    
