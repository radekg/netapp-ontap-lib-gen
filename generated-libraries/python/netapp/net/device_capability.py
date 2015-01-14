class DeviceCapability(basestring):
    """
    router|trans-bridge|source-route-bridge|switch|host|igmp|repeater|phone
    Possible values:
    <ul>
    <li> "router"                  - Router,
    <li> "trans_bridge"            - Trans Bridge,
    <li> "source_route_bridge"     - Source Route Bridge,
    <li> "switch"                  - Switch,
    <li> "host"                    - Host,
    <li> "igmp"                    - IGMP,
    <li> "repeater"                - Repeater,
    <li> "phone"                   - Phone
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "device-capability"
    
