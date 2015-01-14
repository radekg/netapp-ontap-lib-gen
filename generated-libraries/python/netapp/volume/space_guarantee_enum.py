class SpaceGuaranteeEnum(basestring):
    """
    none|volume|file
    Possible values:
    <ul>
    <li> "none"     ,
    <li> "volume"   ,
    <li> "file"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "space-guarantee-enum"
    
