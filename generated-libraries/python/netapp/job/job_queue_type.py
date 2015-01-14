class JobQueueType(basestring):
    """
    Job Manager organizes its workload of active jobs into one of a
    number of different queues in the system.  The type of queue that
    a job is in can indicate its current state.  For instance, a job
    in the pending queue is waiting on some external event to cause
    it to run again.  The queues are internal features of the job
    manager and should only be used for coarse debugging activities.
    Possible values:
    <ul>
    <li> "queued"             ,
    <li> "runnable"           ,
    <li> "cluster_queued"     ,
    <li> "cluster_runnable"   ,
    <li> "pending"            ,
    <li> "paused"             ,
    <li> "cleanup"            ,
    <li> "startup"            ,
    <li> "shutdown"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-queue-type"
    
