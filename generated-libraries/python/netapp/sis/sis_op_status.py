class SisOpStatus(basestring):
    """
    Efficiency status
    Possible values:
    <ul>
    <li> "idle"          - No storage efficiency operations are
    happening on this volume,
    <li> "initializing"  - The storage efficiency operation is
    being initialized,
    <li> "active"        - The storage efficiency operation is
    active on the volume,
    <li> "undoing"       - The storage efficiency is being undone
    on the volume,
    <li> "pending"       - The storage efficiency operation is
    scheduled for the volume,
    <li> "downgrading"   - Storage efficiency actions necessary to
    downgrade the volume are being carried out,
    <li> "disabled"      - Storage efficiency disabled on the
    volume
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sis-op-status"
    
