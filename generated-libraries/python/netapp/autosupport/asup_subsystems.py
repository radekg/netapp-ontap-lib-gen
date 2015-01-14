class AsupSubsystems(basestring):
    """
    AutoSupport collection subsystems
    Possible values:
    <ul>
    <li> "platform"                - Hardware information about
    the node,
    <li> "mhost"                   - User Space application
    information for a node,
    <li> "log_files"               - Log files for a node,
    <li> "performance"             - This subsystem gathers the
    .cm_stats_hourly_done file and user space counters,
    <li> "performance_asup"        - Performance specific
    information for a node,
    <li> "nht"                     - This subsystem gathers the
    /mroot/etc/log/nht_info content,
    <li> "san"                     - SAN specific information for
    a node,
    <li> "snapvault"               - SNAPVAULT specific
    information for a node,
    <li> "snapmirror"              - Snapmirror specific
    information for a node,
    <li> "dedupe"                  - Dedupe specific information
    for a node,
    <li> "nfs"                     - NFS specific information for
    a node,
    <li> "wafl"                    - WAFL specific information for
    a node,
    <li> "mot"                     - MOT specific information for
    a node,
    <li> "ha"                      - HA specific information for a
    node,
    <li> "networking"              - Networking specific
    information for a node,
    <li> "cifs"                    - CIFS specific information for
    a node,
    <li> "fpolicy"                 - Fpolicy specific information
    for a node,
    <li> "multistore"              - Multistore specific
    information for a node,
    <li> "raid"                    - RAID specific information for
    a node,
    <li> "storage"                 - Storage specific information
    for a node,
    <li> "asup_ems"                - ASUP EMS specific information
    for a node,
    <li> "tape"                    - Tape specific information for
    a node,
    <li> "kernel"                  - kernel specific information
    for a node,
    <li> "secd"                    - SECD specific information for
    a node,
    <li> "metrocluster"            - Metrocluster specific
    information for a node,
    <li> "mandatory"               - Mandatory Basic information
    for a node,
    <li> "repository"              - Repository specific
    information for a node,
    <li> "splog_downcontroller"    - SPLOG saved when ontap is
    abnormal down,
    <li> "splog_latest"            - Up-to-date SPLOG from Service
    Processor FW  ,
    <li> "splog_before_spreboot"   - Up-to-date SPLOG from Service
    Processor FW before SP reboot,
    <li> "hm"                      - Health Monitor Alerts
    specific information,
    <li> "kcs"                     - Kernel Cluster Services
    information for a node,
    <li> "av"                      - Antivirus specific
    information for a node,
    <li> "san_ffdc"                - SAN specific trace dumps for
    a node,
    <li> "nwd"                     - Node Watchdog specific
    information for a node,
    <li> "vscan"                   - Vscan specific information
    for a node
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-subsystems"
    
