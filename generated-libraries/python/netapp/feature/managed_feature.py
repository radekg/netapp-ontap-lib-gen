class ManagedFeature(basestring):
    """
    Managed Feature
    Possible values:
    <ul>
    <li> "cifs"                    ,
    <li> "nfs"                     ,
    <li> "iscsi"                   ,
    <li> "fcp"                     ,
    <li> "dedupe"                  ,
    <li> "flexclone"               ,
    <li> "compression"             ,
    <li> "snaprestore"             ,
    <li> "snaplock"                ,
    <li> "snaplock_enterprise"     ,
    <li> "snapvault_primary"       ,
    <li> "snapvault_secondary"     ,
    <li> "snapmirror"              ,
    <li> "syncmirror"              ,
    <li> "flexcache"               ,
    <li> "ndmp"                    ,
    <li> "multistore"              ,
    <li> "cdmi"                    ,
    <li> "snapdrive_windows"       ,
    <li> "snapmanager_exchange"    ,
    <li> "snapmanager_sql"         ,
    <li> "snapmanager_sharepoint"  ,
    <li> "snapmanager_hyperv"      ,
    <li> "snapdrive_unix"          ,
    <li> "snapmanager_oracle"      ,
    <li> "snapmanager_sap"         ,
    <li> "v_storageattach"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "managed-feature"
    
