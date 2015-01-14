class SisCheckpointOpType(basestring):
    """
    sis checkpoint type
    Possible values:
    <ul>
    <li> "Scan"          - Scanning volume for fingerprints,
    <li> "Start"         - Starting a sis operation,
    <li> "Check"         - Checking for stale data in the
    fingerprint database,
    <li> "Undo"          - Undoing sis on the volume,
    <li> "Downgrade"     - Downgrading sis metafiles to a previous
    Data
    ONTAP release.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-checkpoint-op-type"
    
