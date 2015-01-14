class Volmovecutoveraction(basestring):
    """
    abort_on_failure|defer_on_failure|force|wait
    Possible values:
    <ul>
    <li> "abort_on_failure"   ,
    <li> "defer_on_failure"   ,
    <li> "force"              ,
    <li> "wait"               ,
    <li> "retry_on_failure"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "volmovecutoveraction"
    
