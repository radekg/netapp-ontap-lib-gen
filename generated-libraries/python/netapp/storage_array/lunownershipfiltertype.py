class Lunownershipfiltertype(basestring):
    """
    all|assigned|unassigned
    Possible values:
    <ul>
    <li> "unassigned"    - Only array LUNs that are not assigned
    to the controller,
    <li> "assigned"      - Only array LUNs that are assigned to
    the controller,
    <li> "all"           - all array LUNs visible to the
    controller
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "lunownershipfiltertype"
    
