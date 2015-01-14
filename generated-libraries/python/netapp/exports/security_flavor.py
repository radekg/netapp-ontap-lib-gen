class SecurityFlavor(basestring):
    """
    any|none|never|krb5|ntlm|sys
    Possible values:
    <ul>
    <li> "any"      - Any,
    <li> "none"     - Anonymous Access Allowed If Security Type
    Not Already Listed,
    <li> "never"    - Never,
    <li> "krb5"     - Kerberos 5 Authentication,
    <li> "ntlm"     - CIFS NTLM,
    <li> "sys"      - NFS AUTH_SYS,
    <li> "spinauth" - SpinAuth
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "security-flavor"
    
