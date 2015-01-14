class UcmType(basestring):
    """
    The FC-4 type of the adapter.
    Possible values:
    <ul>
    <li> "initiator"     - Initiator mode,
    <li> "target"        - Target mode
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ucm-type"
    
