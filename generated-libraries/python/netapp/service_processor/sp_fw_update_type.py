class SpFwUpdateType(basestring):
    """
    Possible choices for a firmware update type
    Possible values:
    <ul>
    <li> "full"          - Replace the fimrware completely with
    new package,
    <li> "differential"  - Replace only parts of firmware which
    have changed in new package
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-fw-update-type"
    
