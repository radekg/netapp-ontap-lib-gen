class InterimLicensedFeature(basestring):
    """
    Licensable Features
    Possible values:
    <ul>
    <li> "base"               - Base License w/cluster size limit
    (nodes),
    <li> "mirror"             - Mirror License,
    <li> "flexvol_hpo"        - FlexVol HPO License,
    <li> "cifs"               - CIFS License,
    <li> "snaprestore"        - SnapRestore License,
    <li> "flexclone"          - FlexClone License,
    <li> "nfs"                - NFS License,
    <li> "snapmirror_dp"      - SnapMirror Data Protection
    License,
    <li> "iscsi"              - iSCSI License,
    <li> "striped_volume"     - Striped Volume License,
    <li> "fcp"                - FCP License,
    <li> "snapmanager_suite"  - SnapManager Suite License,
    <li> "spa"                - SPA License,
    <li> "insight_balance"    - OnCommand Balance
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "interim-licensed-feature"
    
