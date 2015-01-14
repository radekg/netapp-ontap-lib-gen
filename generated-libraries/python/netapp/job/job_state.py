class JobState(basestring):
    """
    Jobs execute as self-contained state machines.  They follow a
    series of careful steps from creation to destruction.  These
    steps are dictated by the states that they find themselves in as
    well as the allowable list of states they may transition into.
    The state can be an indicator of whether a job is executing and
    if not, why that is the case.
    Possible values:
    <ul>
    <li> "initial"       - Initializing,
    <li> "queued"        - Queued,
    <li> "running"       - Running,
    <li> "waiting"       - Waiting For Another Job,
    <li> "pausing"       - Entering Paused State,
    <li> "paused"        - Paused,
    <li> "quitting"      - Entering Quit State,
    <li> "success"       - Succeeded,
    <li> "failure"       - Failed,
    <li> "reschedule"    - Forcing Reschedule,
    <li> "error"         - Internal Error,
    <li> "quit"          - Quit,
    <li> "dead"          - Died,
    <li> "unknown"       - Unknown,
    <li> "restart"       - Forcing Restart,
    <li> "dormant"       - Waiting For External Event
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-state"
    
