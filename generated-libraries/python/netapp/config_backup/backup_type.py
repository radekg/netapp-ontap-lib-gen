class BackupType(basestring):
    """
    The type of a configuration backup.
    Possible values:
    <ul>
    <li> "node"     - Node Backup,
    <li> "cluster"  - Cluster Backup
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "backup-type"
    
