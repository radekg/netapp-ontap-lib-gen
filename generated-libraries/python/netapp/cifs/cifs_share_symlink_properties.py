class CifsShareSymlinkProperties(basestring):
    """
    enable|hide|read_only
    Possible values:
    <ul>
    <li> "enable"        ,
    <li> "hide"          ,
    <li> "read_only"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-share-symlink-properties"
    
