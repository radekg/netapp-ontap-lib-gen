class AsupStatus(basestring):
    """
    AutoSupport general status
    Possible values:
    <ul>
    <li> "initializing"            - ASUP request is being
    processed,
    <li> "collection_failed"       - The AutoSupport Collection
    failed. See 'Last Error' for more information,
    <li> "collection_in_progress"  - The AutoSupport Collection is
    in progress,
    <li> "queued"                  - ASUP is queued for delivery,
    <li> "transmitting"            - ASUP transmission is in
    progress,
    <li> "sent_successful"         - ASUP was successfully sent,
    <li> "ignore"                  - ASUP was processed
    successfully but has no destinations configured,
    <li> "re_queued"               - ASUP transmission failed and
    has been re-queued,
    <li> "transmission_failed"     - ASUP transmission has failed
    and the retry limit has been exceeded,
    <li> "ondemand_ignore"         - ASUP was processed
    successfully but ASUP OnDemand has declined delivery
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-status"
    
