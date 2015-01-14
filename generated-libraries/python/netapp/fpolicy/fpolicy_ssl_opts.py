class FpolicySslOpts(basestring):
    """
    no-auth|server-auth|mutual-auth
    Possible values:
    <ul>
    <li> "no_auth"       - Communication over TCP,
    <li> "server_auth"   - Authentication of FPolicy server only,
    <li> "mutual_auth"   - Mutual authentication of storage system
    and FPolicy server
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "fpolicy-ssl-opts"
    
