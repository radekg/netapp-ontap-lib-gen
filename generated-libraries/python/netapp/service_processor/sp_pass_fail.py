class SpPassFail(basestring):
    """
    Possible completion states of a task
    Possible values:
    <ul>
    <li> "failed"   - Operation failed,
    <li> "passed"   - Operation was successful
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-pass-fail"
    
