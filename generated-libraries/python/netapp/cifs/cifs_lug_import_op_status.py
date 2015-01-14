class CifsLugImportOpStatus(basestring):
    """
    Status of the import operation of CIFS local users and groups
    Possible values:
    <ul>
    <li> "unknown"                 ,
    <li> "success"                 ,
    <li> "success_with_warnings"   ,
    <li> "failed"                  ,
    <li> "in_progress"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-lug-import-op-status"
    
