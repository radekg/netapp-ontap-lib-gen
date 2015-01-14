class LdapSearchScope(basestring):
    """
    base|onelevel|subtree
    Possible values:
    <ul>
    <li> "base"     - Search only the base directory entry,
    <li> "onelevel" - Search the base directory entry and the
    children of the base entry,
    <li> "subtree"  - Search the base directory entry and all its
    decendants
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "ldap-search-scope"
    
