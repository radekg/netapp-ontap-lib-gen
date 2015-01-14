class QosClass(basestring):
    """
    preset|user-defined|system-defined
    Possible values:
    <ul>
    <li> "preset"             - Preset,
    <li> "user_defined"       - User Defined,
    <li> "system_defined"     - System Defined
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "qos-class"
    
