class AdapterType(basestring):
    """
    fc|cna|nic
    Possible values:
    <ul>
    <li> "fc"  - Used for FC Adapters,
    <li> "cna" - Used for CNA Adapters,
    <li> "nic" - Used for NIC Adapters
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "adapter-type"
    
