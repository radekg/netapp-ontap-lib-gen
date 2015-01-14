class NtfsPropagationMode(basestring):
    """
    propagate|ignore|replace
    Possible values:
    <ul>
    <li> "propagate"     ,
    <li> "ignore"        ,
    <li> "replace"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ntfs-propagation-mode"
    
