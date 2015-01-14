class AuthMechanism(basestring):
    """
    The list of possible known authentication mechanisms supported by the CIFS server.
    Possible values:
    <ul>
    <li> "None"              - None
    <li> "NTLMv1"            - NTLMv1
    <li> "NTLMv2"            - NTLMv2
    <li> "Kerberos"          - Kerberos
    <li> "Anonymous"         - Anonymous
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "auth-mechanism"
    
