class SpLinkStatus(basestring):
    """
    Possible states for the underlying physical link for a network
    insterface
    Possible values:
    <ul>
    <li> "up"       - Link is connected,
    <li> "down"     - Link is severed,
    <li> "disabled" - Link has been disabled by user,
    <li> "unknown"  - Link status is no known
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-link-status"
    
