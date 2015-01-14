class AccessRights(basestring):
    """
    no-access|full-control|modify|read-and-execute|read|write
    Possible values:
    <ul>
    <li> "no_access"          ,
    <li> "full_control"       ,
    <li> "modify"             ,
    <li> "read_and_execute"   ,
    <li> "read"               ,
    <li> "write"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "access-rights"
    
