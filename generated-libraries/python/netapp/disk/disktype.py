class Disktype(basestring):
    """
    ATA | BSAS | FCAL | FSAS | LUN | MSATA | SAS  | SATA | SSD
    Possible values:
    <ul>
    <li> "ata"      - Advanced Technology Attachment,
    <li> "bsas"     - Bridged Serial Attached SCSI (bridged from
    SATA),
    <li> "fcal"     - Fibre Channel Arbitrated Loop,
    <li> "fsas"     - High-Capacity (Fat) Serial Attached SCSI,
    <li> "lun"      - SCSI Logical Unit Number (e.g. Array),
    <li> "msata"    - Multiple bridged SATA disks in a single
    carrier,
    <li> "sas"      - Serial Attached SCSI,
    <li> "sata"     - Serial Advanced Technology Attachment,
    <li> "ssd"      - Solid-State Disk
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "disktype"
    
