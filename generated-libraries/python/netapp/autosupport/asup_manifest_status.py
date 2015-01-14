class AsupManifestStatus(basestring):
    """
    AutoSupport manifest collection status
    Possible values:
    <ul>
    <li> "requested"                              - ASUP request
    has been added to the queue and is waiting processing by the
    collector,
    <li> "working"                                - ASUP Collector
    is actively gathering the needed data,
    <li> "file_not_found"                         - ASUP
    collection failed, a needed file is missing,
    <li> "no_such_table"                          - ASUP
    collection was unable to find the requested SMF table,
    <li> "collection_truncated_size_limit"        - ASUP
    collection truncated due to size limits and partial data is
    available,
    <li> "collection_skipped_size_limit"          - ASUP
    collection skipped due to size limits and no data is available,
    <li> "collection_truncated_time_limit"        - ASUP
    collection truncated due to time limits and partial data is
    available,
    <li> "collection_skipped_time_limit"          - ASUP
    collection skipped due to time limits and no data is available,
    <li> "delivery_skipped_size_limit"            - ASUP data was
    skipped at delivery time due to size limits,
    <li> "general_error"                          - ASUP
    collection failed, additional information if any will be in the
    Error String field,
    <li> "completed"                              - ASUP
    collection is complete, ready for delivery,
    <li> "content_not_collected_mode"             - ASUP content
    was not collected, incompatible operational mode,
    <li> "content_not_collected_precheck"         - ASUP content
    was not collected, pre-check function violation,
    <li> "content_not_collected_privacy"          - ASUP content
    was not collected, the operation is disabled in privacy mode,
    <li> "content_empty"                          - ASUP content
    was collected successfully, but output was empty,
    <li> "collection_aborted"                     - ASUP
    collection aborted,
    <li> "collection_truncated_file_size_limit"   - ASUP file
    truncated due to size limits and partial data is available
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-manifest-status"
    
