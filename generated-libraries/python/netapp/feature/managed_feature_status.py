class ManagedFeatureStatus(basestring):
    """
    Represents the status of a managed feature.
    Possible values:
    <ul>
    <li> "on"       - feature is entitled and turned on,
    <li> "available" - feature is entitled and available to be
    turned on. Its current on/off status is unknown,
    <li> "on_not_configurable" - feature is no longer entitled but
    it was turned on before and remains to be on. Feature
    is not configurable at the moment,
    <li> "off"      - feature is entitled but turned off,
    <li> "not_available"  - feature is not entitled, licensing
    infrastructure is unavailable, or other
    configuration check prevents feature use. The field
    notes can provide additional information.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "managed-feature-status"
    
