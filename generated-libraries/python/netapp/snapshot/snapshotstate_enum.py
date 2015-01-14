class SnapshotstateEnum(basestring):
    """
    valid|invalid|partial
    Possible values:
    <ul>
    <li> "valid"    ,
    <li> "invalid"  ,
    <li> "partial"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "snapshotstate-enum"
    
