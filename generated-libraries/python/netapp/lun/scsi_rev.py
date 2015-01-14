class ScsiRev(basestring):
    """
    scsi2|scsi3
    Possible values:
    <ul>
    <li> "scsi2"    ,
    <li> "scsi3"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "scsi-rev"
    
