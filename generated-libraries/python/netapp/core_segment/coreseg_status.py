class CoresegStatus(basestring):
    """
    The status fo the core segmentation job
    Possible values:
    <ul>
    <li> "queued"   - Queued,
    <li> "running"  - Running,
    <li> "stopping" - Stopping,
    <li> "finished" - Completed
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "coreseg-status"
    
