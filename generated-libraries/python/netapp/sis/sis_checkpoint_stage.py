class SisCheckpointStage(basestring):
    """
    sis checkpoint stage
    Possible values:
    <ul>
    <li> "Gathering"          - Scanning the volume for
    fingerprints,
    <li> "Sorting"            - Sorting the gathered
    fingerprints,
    <li> "Compress_preproc"   - Preprocessing volume data for
    compression,
    <li> "Compressing"        - Compressing the volume data,
    <li> "Saving_pass1"       - Creating duplicate list from the
    newly gathered fingerprints,
    <li> "Saving_pass2"       - Creating duplicate list from the
    fingerprint database,
    <li> "Saving_sharing"     - Creating shared data structures in
    the volume,
    <li> "Saving_end"         - Completing sis
    operations,
    <li> "Checking_pass0"     - Organizing data in the fingerprint
    database for block sharing,
    <li> "Checking_pass1"     - Organizing data in the fingerprint
    database for block sharing,
    <li> "Checking_pass2"     - Organizing data in the fingerprint
    database for block sharing,
    <li> "Unknown_stage"      - Invalid stage
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-checkpoint-stage"
    
