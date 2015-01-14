class CifsOpenMode(basestring):
    """
    The list of possible modes used when opening files over CIFS servers.
    Possible values:
    <ul>
    <li> "R"            - The file opened for read operation.
    <li> "W"            - The file opened for write operation.
    <li> "D"            - The file opened for delete operation.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-open-mode"
    
