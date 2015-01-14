class PerformanceArchiveState(basestring):
    """
    The state of a Performance Archive
    Possible values:
    <ul>
    <li> "create_calculating" - Archive properties being
    calculated,
    <li> "create_queueing"    - Archive waiting to be created,
    <li> "create_packaging"   - Archive files being packaged on
    source nodes,
    <li> "create_incomplete"  - Not all requested nodes included
    in saved Archive,
    <li> "created"            - Successfully saved Archive to
    disk,
    <li> "create_failed"      - Errors occurred while saving
    Archive to disk,
    <li> "destroy_queueing"   - Archive waiting to be destroyed,
    <li> "destroy_cleaning"   - Archive actively being destroyed
    and removed from disk,
    <li> "destroy_incomplete" - Archive not completely removed
    from all nodes,
    <li> "destroyed"          - Archive successfully removed from
    the cluster,
    <li> "destroy_failed"     - Errors occurred while destroying
    Archive,
    <li> "invalid_state"      - Invalid state that should not be
    reached
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "performance-archive-state"
    
