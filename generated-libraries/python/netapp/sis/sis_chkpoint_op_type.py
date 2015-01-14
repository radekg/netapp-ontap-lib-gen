class SisChkpointOpType(basestring):
    """
    Checkpoint type
    Possible values:
    <ul>
    <li> "scan"          - Scanning volume for fingerprints,
    <li> "start"         - Starting a storage efficiency
    operation,
    <li> "check"         - Checking for stale data in the
    fingerprint database,
    <li> "undo"          - Undoing storage efficiency on the
    volume,
    <li> "downgrade"     - Storage efficiency operations necessary
    for downgrade activity,
    <li> "post_transfer" - Starting a storage efficiency operation
    post mirror transfer
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-chkpoint-op-type"
    
