class SmRestartEnum(basestring):
    """
    always|never|default
    Possible values:
    <ul>
    <li> "always"   ,
    <li> "never"    ,
    <li> "default"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sm-restart-enum"
    
