class SisCheckpointSubstage(basestring):
    """
    sis checkpoint sub-stage
    Possible values:
    <ul>
    <li> "Sort_pass2" - Sorting the fingerprints for deduplication
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-checkpoint-substage"
    
