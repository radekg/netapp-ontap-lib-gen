class SisChkpointStage(basestring):
    """
    Checkpoint stage
    Possible values:
    <ul>
    <li> "gathering"                         - Scanning the volume
    for fingerprints,
    <li> "gathering_phase2"                  - Scanning the volume
    for fingerprints,
    <li> "pre_processing_vault_changelogs"   - Pre-processing
    vault changelogs,
    <li> "generating_vault_changelogs"       - Generating vault
    changelogs,
    <li> "sorting"                           - Sorting the
    gathered fingerprints,
    <li> "compress_preproc"                  - Preprocessing
    volume data for compression,
    <li> "compressing"                       - Compressing the
    volume data,
    <li> "saving_pass1"                      - Creating duplicate
    list from the newly gathered fingerprints,
    <li> "saving_pass2"                      - Creating duplicate
    list from the fingerprint database,
    <li> "saving_sharing"                    - Creating shared
    data structures in the volume,
    <li> "saving_end"                        - Completing storage
    efficiency operations,
    <li> "checking_pass0"                    - Organizing data in
    the fingerprint database for block sharing,
    <li> "checking_pass1"                    - Organizing data in
    the fingerprint database for block sharing,
    <li> "checking_pass2"                    - Organizing data in
    the fingerprint database for block sharing,
    <li> "unknown_stage"                     - Invalid stage
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-chkpoint-stage"
    
