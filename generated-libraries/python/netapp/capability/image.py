class Image(basestring):
    """
    default|current
    Possible values:
    <ul>
    <li> "default"  - Default image,
    <li> "current"  - Current image
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "image"
    
