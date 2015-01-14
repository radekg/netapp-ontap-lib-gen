class UndoSelectiveEnum(basestring):
    """
    all|wrong
    Possible values:
    <ul>
    <li> "all"      - Undo all shared data,
    <li> "wrong"    - Only undo the incorrectly shared data
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "undo-selective-enum"
    
