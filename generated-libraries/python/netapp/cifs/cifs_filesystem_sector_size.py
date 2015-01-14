class CifsFilesystemSectorSize(basestring):
    """
    CIFS File System Sector sizes reported to SMB Clients (in
    bytes).
    Possible values:
    <ul>
    <li> "512"      - Reported file system sector size to SMB
    clients is 512 bytes,
    <li> "4096"     - Reported file system sector size to SMB
    clients is 4096 bytes
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-filesystem-sector-size"
    
