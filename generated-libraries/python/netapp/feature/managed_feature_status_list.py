class ManagedFeatureStatusList(basestring):
    """
    on|available|on-not-configurable|off|not-available
    Possible values:
    <ul>
    <li> "on"                      - On,
    <li> "available"               - Available,
    <li> "on_not_configurable"     - On Not Configurable,
    <li> "off"                     - Off,
    <li> "not_available"           - Not Available
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "managed-feature-status-list"
    
