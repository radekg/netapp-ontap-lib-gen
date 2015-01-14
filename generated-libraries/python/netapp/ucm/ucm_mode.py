class UcmMode(basestring):
    """
    The operational mode of the adapter.
    Possible values:
    <ul>
    <li> "fc"  - Fibre Channel,
    <li> "cna" - Converged Network Adapter
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ucm-mode"
    
