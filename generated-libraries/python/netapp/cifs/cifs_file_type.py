class CifsFileType(basestring):
    """
    The list of possible types of files opened through CIFS servers.
    Possible values:
    <ul>
    <li> "Regular"            - Regular file
    <li> "Symlink"            - Symlink file
    <li> "Stream"             - Stream file
    <li> "Directory"          - Directory
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-file-type"
    
