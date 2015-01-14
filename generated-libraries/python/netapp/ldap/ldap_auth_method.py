class LdapAuthMethod(basestring):
    """
    anonymous|simple|sasl
    Possible values:
    <ul>
    <li> "anonymous"     - Anonymous bind,
    <li> "simple"        - Simple bind,
    <li> "sasl"          - Simple Authentication and Security
    Layer (SASL) bind
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ldap-auth-method"
    
