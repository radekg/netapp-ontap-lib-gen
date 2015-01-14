class AlignmentState(basestring):
    """
    aligned|misaligned|partial-writes|indeterminate
    Possible values:
    <ul>
    <li> "aligned"            - All or most of the IO to the LUN
    is aligned to the underlying file,
    <li> "misaligned"         - A significant amount of IO to the
    LUN is not aligned to the underlying file,
    <li> "partial_writes"     - A significant amount of IO to the
    LUN is partial,
    <li> "indeterminate"      - There is not enough IO to
    determine the LUN's alignment state
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "alignment-state"
    
