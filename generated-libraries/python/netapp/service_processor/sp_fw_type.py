class SpFwType(basestring):
    """
    Choices for the two firmware images installed on a SP/RLM device
    Possible values:
    <ul>
    <li> "primary"  - Firmware which the device boots into by
    default,
    <li> "backup"   - Firmware which the device boots into if
    primary fails
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-fw-type"
    
