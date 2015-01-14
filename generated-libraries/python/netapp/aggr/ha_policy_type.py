class HaPolicyType(basestring):
    """
    HA Policy of aggregate. It can be
    controller failover or storage failover
    or unspecified.
    Allowed values are:
    <ul>
    <li>"cfo": Controller FailOver
    <li>"sfo": Storage FailOver
    <li>"none": Unspecified
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ha-policy-type"
    
