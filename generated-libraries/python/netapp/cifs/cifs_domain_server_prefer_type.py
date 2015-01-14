class CifsDomainServerPreferType(basestring):
    """
    The preference level of the server either set due to
    configuration or due to the site membership determined by server
    discovery.
    Possible values:
    <ul>
    <li> "unknown"       - The preference level of this server is
    unknown.,
    <li> "preferred"     - This server was administratively marked
    as a preferred server due to its presence in the list of
    preferred servers.,
    <li> "favored"       - This server was marked as favored by
    the server discovery process by virtue of site membership.,
    <li> "adequate"      - This server was discovered by the
    server discovery process and can be used, but has no preference
    associated with it.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-server-prefer-type"
    
