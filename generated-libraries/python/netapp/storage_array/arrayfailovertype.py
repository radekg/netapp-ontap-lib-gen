class Arrayfailovertype(basestring):
    """
    active|passive|none
    Possible values:
    <ul>
    <li> "active"   - Active/Active Port Failover,
    <li> "passive"  - Active/Passive Port Failover,
    <li> "none"     - None
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "arrayfailovertype"
    
