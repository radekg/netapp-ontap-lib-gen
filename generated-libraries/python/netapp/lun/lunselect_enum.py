class LunselectEnum(basestring):
    """
    active|copy|mirror
    Possible values:
    <ul>
    <li> "active"   ,
    <li> "copy"     ,
    <li> "mirror"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "lunselect-enum"
    
