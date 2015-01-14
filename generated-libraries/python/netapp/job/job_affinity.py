class JobAffinity(basestring):
    """
    All jobs are scheduled with direction as to where they should
    execute.  This affinity may either be node-specific or apply to
    all nodes (cluster).  The affinity of the job is specific to the
    type of operations the job performs and is not user
    configurable.
    Possible values:
    <ul>
    <li> "cluster"  - Cluster Affinity,
    <li> "node"     - Node Affinity
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "job-affinity"
    
