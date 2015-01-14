class JobPriority(basestring):
    """
    Execution priority of a job. There are thread pools for each
    priority level. Higher priority jobs may run in the pools of
    lower priorities. So High-priority jobs may run in the High,
    Medium or Low thread pools, Medium-priority jobs may run in the
    Medium or Low thread pools and Low-priority jobs may only run in
    the Low thread pool. The exception to this is Exclusive jobs:
    Exclusive-priority jobs will only run in the Exclusive thread
    pool and only Exclusive-priority jobs will be run in the
    Exclusive thread pool.
    Possible values:
    <ul>
    <li> "low"           ,
    <li> "medium"        ,
    <li> "high"          ,
    <li> "exclusive"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-priority"
    
