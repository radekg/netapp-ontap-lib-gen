class AsupInvokeStyle(basestring):
    """
    test|performance|all
    Possible values:
    <ul>
    <li> "test"          - Test AutoSupport send and receive
    only,
    <li> "performance"   - Generate a Performance AutoSupport as
    requested by technical support,
    <li> "all"           - Send all AutoSupport data without time
    or size limit, as requested by technical support
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "asup-invoke-style"
    
