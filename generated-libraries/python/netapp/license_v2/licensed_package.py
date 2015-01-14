class LicensedPackage(basestring):
    """
    Licensable Package
    Possible values:
    <ul>
    <li> "base"                    - Cluster Base License,
    <li> "nfs"                     - NFS License,
    <li> "cifs"                    - CIFS License,
    <li> "iscsi"                   - iSCSI License,
    <li> "fcp"                     - FCP License,
    <li> "cdmi"                    - CDMI License,
    <li> "snaprestore"             - SnapRestore License,
    <li> "snapmirror"              - SnapMirror License,
    <li> "flexclone"               - FlexClone License,
    <li> "snapvault"               - SnapVault License,
    <li> "snaplock"                - SnapLock Compliance License,
    <li> "snapmanagersuite"        - SnapManagerSuite License,
    <li> "snapprotectapps"         - SnapProtectApp License,
    <li> "v_storageattach"         - Virtual Attached Storage
    License,
    <li> "snaplock_enterprise"     - SnapLock Enterprise License,
    <li> "insight_balance"         - OnCommand Balance
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "licensed-package"
    
