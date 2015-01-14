class CifsSymlinkLocality(basestring):
    """
    Locality of the destination where this symbolic link points.
    Possible values:
    <ul>
    <li> "local"    - Share On This VServer,
    <li> "widelink" - Share On Another CIFS Server
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-symlink-locality"
    
