class HmSubsystemDiscoveryState(basestring):
    """
    Health Monitor Subsystem Initialization
    State(initailizing,starting_discovery,discovery_done_partially,discovery_done,initialized)
    Possible values:
    <ul>
    <li> "invalid"                 ,
    <li> "initializing"            ,
    <li> "initialized"             ,
    <li> "start_discovery"         ,
    <li> "start_rediscovery"       ,
    <li> "discovered_partially"    ,
    <li> "discovery_done"          ,
    <li> "discovery_max"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "hm-subsystem-discovery-state"
    
