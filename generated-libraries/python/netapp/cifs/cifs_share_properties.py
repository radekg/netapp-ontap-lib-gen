class CifsShareProperties(basestring):
    """
    The list of properties on a CIFS share.
    Possible values:
    <ul>
    <li> "oplocks"            - This specifies that opportunistic
    locks (client-side caching) are enabled on this share.,
    <li> "browsable"          - This specifies that the share can
    be browsed by Windows clients.,
    <li> "showsnapshot"       - This specifies that Snapshots can
    be viewed and traversed by clients.,
    <li> "changenotify"       - This specifies that CIFS clients
    can request for change notifications for directories on this
    share.,
    <li> "homedirectory"      - This specifies that the share is
    added and enabled as part of the CIFS home directory feature. The
    configuration of this share should be done using CIFS home
    directory feature interface.,
    <li> "attributecache"     - This specifies that connections
    through this share are caching attributes for a short time to
    improve performance.
    <li> "branchcache" - This specifies that clients connecting
    to this share can make requests using BranchCache technology that
    allows them to cache the content in an attempt to reduce WAN
    utilization from a remote office.
    <li> "continuously_available" - This specifies that clients
    connecting to this share can open files in a persistent manner.
    Files opened this way are protected from disruptive events, such
    as failover and giveback.
    <li> "shadowcopy" - This specifies that the share is pointing
    to a shadow copy. This attribute cannot be added nor removed from
    a share.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-share-properties"
    
