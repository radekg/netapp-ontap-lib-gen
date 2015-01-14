class JobEventType(basestring):
    """
    Jobs will trigger history events at certain stages of their life
    cycle. These events are of the types described herein.
    Possible values:
    <ul>
    <li> "idle"          - The job has become idle,
    <li> "running"       - The job has started running,
    <li> "succeeded"     - The job has completed successfully,
    <li> "failed"        - The job has completed with a failure,
    <li> "paused"        - The job has been paused,
    <li> "stopped"       - The job has been stopped,
    <li> "deleted"       - The job has been deleted,
    <li> "error"         - Job Manager experienced an error while
    processing the job
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-event-type"
    
