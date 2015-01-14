class Aggrverifyactiontype(basestring):
    """
    start|stop|resume|suspend|status
    Possible values:
    <ul>
    <li> "start"    - Start Verifying,
    <li> "stop"     - Stop Verifying,
    <li> "resume"   - Resume Verifying,
    <li> "suspend"  - Suspend Verifying,
    <li> "status"   - Check Verifying Status
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "aggrverifyactiontype"
    
