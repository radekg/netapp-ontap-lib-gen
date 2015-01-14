class SisChkpointSubstage(basestring):
    """
    Checkpoint sub-stage
    Possible values:
    <ul>
    <li> "sort_pass1"         - Sorting the fingerprints for
    deduplication,
    <li> "sort_p1merge"       - Merging the fingerprints for
    deduplication,
    <li> "sort_pass2"         - Merging the fingerprints for
    deduplication,
    <li> "bucket_sort_init"   - Sorting the fingerprints for
    deduplication,
    <li> "bucket_sort"        - Sorting the fingerprints for
    deduplication,
    <li> "bucket_sort_done"   - Sorting the fingerprints for
    deduplication
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-chkpoint-substage"
    
