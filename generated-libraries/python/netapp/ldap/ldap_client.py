from netapp.netapp_object import NetAppObject

class LdapClient(NetAppObject):
    """
    LDAP Client Information. Each entry specifies an LDAP client
    configuration that can be associated with a Vserver using the
    ldap-config-create API.
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _group_dn = None
    @property
    def group_dn(self):
        """
        The Group Distinguished Name (DN), if specified, is used
        as the starting point in the LDAP directory tree for
        group lookups. If not specified, group lookups will start
        at the base-dn.
        Attributes: optional-for-create, modifiable
        """
        return self._group_dn
    @group_dn.setter
    def group_dn(self, val):
        if val != None:
            self.validate('group_dn', val)
        self._group_dn = val
    
    _netgroup_dn = None
    @property
    def netgroup_dn(self):
        """
        The Netgoup Distinguished Name (DN), if specified, is
        used as the starting point in the LDAP directory tree for
        netgroup lookups. If not specified, netgroup lookups will
        start at the base-dn.
        Attributes: optional-for-create, modifiable
        """
        return self._netgroup_dn
    @netgroup_dn.setter
    def netgroup_dn(self, val):
        if val != None:
            self.validate('netgroup_dn', val)
        self._netgroup_dn = val
    
    _servers = None
    @property
    def servers(self):
        """
        List of LDAP Server IP addresses to use for this
        configuration. The option is NOT applicable for
        configurations using Active Directory LDAP servers.
        Attributes: optional-for-create, modifiable
        """
        return self._servers
    @servers.setter
    def servers(self, val):
        if val != None:
            self.validate('servers', val)
        self._servers = val
    
    _ad_domain = None
    @property
    def ad_domain(self):
        """
        The Active Directory Domain Name for this LDAP
        configuration. The option is ONLY applicable for
        configurations using Active Directory LDAP servers.
        Attributes: optional-for-create, modifiable
        """
        return self._ad_domain
    @ad_domain.setter
    def ad_domain(self, val):
        if val != None:
            self.validate('ad_domain', val)
        self._ad_domain = val
    
    _use_start_tls = None
    @property
    def use_start_tls(self):
        """
        This indicates if start_tls will be used over LDAP
        connections.
        Attributes: optional-for-create, modifiable
        """
        return self._use_start_tls
    @use_start_tls.setter
    def use_start_tls(self, val):
        if val != None:
            self.validate('use_start_tls', val)
        self._use_start_tls = val
    
    _bind_password = None
    @property
    def bind_password(self):
        """
        The password to be used with the bind-dn.
        Attributes: optional-for-create, modifiable
        """
        return self._bind_password
    @bind_password.setter
    def bind_password(self, val):
        if val != None:
            self.validate('bind_password', val)
        self._bind_password = val
    
    _user_scope = None
    @property
    def user_scope(self):
        """
        This indicates the scope for LDAP search when doing user
        lookups.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "base"      - Search only the base directory
        entry,
        <li> "onelevel"  - Search the base directory entry and
        the children of the base entry,
        <li> "subtree"   - Search the base directory entry and
        all its decendants
        </ul>
        """
        return self._user_scope
    @user_scope.setter
    def user_scope(self, val):
        if val != None:
            self.validate('user_scope', val)
        self._user_scope = val
    
    _is_owner = None
    @property
    def is_owner(self):
        """
        This indicates if the vserver owns the client
        configuration.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_owner
    @is_owner.setter
    def is_owner(self, val):
        if val != None:
            self.validate('is_owner', val)
        self._is_owner = val
    
    _bind_dn = None
    @property
    def bind_dn(self):
        """
        The Bind Distinguished Name (DN) is the LDAP identity
        used during the authentication process by the clients.
        This is required if the LDAP server does not support
        anonymous binds. This field is not used if
        'bind-as-cfs-server' is set to 'true'. Example :
        cn=username,cn=Users,dc=example,dc=com
        Attributes: optional-for-create, modifiable
        """
        return self._bind_dn
    @bind_dn.setter
    def bind_dn(self, val):
        if val != None:
            self.validate('bind_dn', val)
        self._bind_dn = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the Vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _min_bind_level = None
    @property
    def min_bind_level(self):
        """
        The minimum authentication level that can be used to
        authenticate with the LDAP server. If omitted, this
        parameter defaults to 'sasl' if the configuration uses
        Active Directory LDAP. For configurations that use LDAP
        servers from other vendors, this parameter defaults to
        'simple' if a 'bind-dn' is specified and 'anonymous'
        otherwise.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "anonymous" - Anonymous bind,
        <li> "simple"    - Simple bind,
        <li> "sasl"      - Simple Authentication and Security
        Layer (SASL) bind
        </ul>
        """
        return self._min_bind_level
    @min_bind_level.setter
    def min_bind_level(self, val):
        if val != None:
            self.validate('min_bind_level', val)
        self._min_bind_level = val
    
    _ldap_client_config = None
    @property
    def ldap_client_config(self):
        """
        The name of the LDAP client configuration.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._ldap_client_config
    @ldap_client_config.setter
    def ldap_client_config(self, val):
        if val != None:
            self.validate('ldap_client_config', val)
        self._ldap_client_config = val
    
    _preferred_ad_servers = None
    @property
    def preferred_ad_servers(self):
        """
        Preferred Active Directory (AD) Domain controllers to use
        for this configuration. This option is ONLY applicable
        for configurations using Active Directory LDAP servers
        Attributes: optional-for-create, modifiable
        """
        return self._preferred_ad_servers
    @preferred_ad_servers.setter
    def preferred_ad_servers(self, val):
        if val != None:
            self.validate('preferred_ad_servers', val)
        self._preferred_ad_servers = val
    
    _bind_as_cifs_server = None
    @property
    def bind_as_cifs_server(self):
        """
        If set, the cluster will use the CIFS server's
        credentials to bind to the LDAP server. If omitted, this
        parameter defaults to 'true' if the configuration uses
        Active Directory LDAP and defaults to 'false' otherwise.
        Attributes: optional-for-create, modifiable
        """
        return self._bind_as_cifs_server
    @bind_as_cifs_server.setter
    def bind_as_cifs_server(self, val):
        if val != None:
            self.validate('bind_as_cifs_server', val)
        self._bind_as_cifs_server = val
    
    _base_scope = None
    @property
    def base_scope(self):
        """
        This indicates the scope for LDAP search. If omitted,
        this parameter defaults to 'subtree'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "base"      - Search only the base directory
        entry,
        <li> "onelevel"  - Search the base directory entry and
        the children of the base entry,
        <li> "subtree"   - Search the base directory entry and
        all its decendants
        </ul>
        """
        return self._base_scope
    @base_scope.setter
    def base_scope(self, val):
        if val != None:
            self.validate('base_scope', val)
        self._base_scope = val
    
    _query_timeout = None
    @property
    def query_timeout(self):
        """
        Maximum time in seconds to wait for a query response from
        the LDAP server. The default for this parameter is 3
        seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._query_timeout
    @query_timeout.setter
    def query_timeout(self, val):
        if val != None:
            self.validate('query_timeout', val)
        self._query_timeout = val
    
    _user_dn = None
    @property
    def user_dn(self):
        """
        The User Distinguished Name (DN), if specified, is used
        as the starting point in the LDAP directory tree for user
        lookups. If this parameter is omitted, user lookups will
        start at the base-dn.
        Attributes: optional-for-create, modifiable
        """
        return self._user_dn
    @user_dn.setter
    def user_dn(self, val):
        if val != None:
            self.validate('user_dn', val)
        self._user_dn = val
    
    _netgroup_scope = None
    @property
    def netgroup_scope(self):
        """
        This indicates the scope for LDAP search when doing
        netgroup lookups.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "base"      - Search only the base directory
        entry,
        <li> "onelevel"  - Search the base directory entry and
        the children of the base entry,
        <li> "subtree"   - Search the base directory entry and
        all its decendants
        </ul>
        """
        return self._netgroup_scope
    @netgroup_scope.setter
    def netgroup_scope(self, val):
        if val != None:
            self.validate('netgroup_scope', val)
        self._netgroup_scope = val
    
    _tcp_port = None
    @property
    def tcp_port(self):
        """
        The TCP port on the LDAP server to use for this
        configuration. If omitted, this parameter defaults to
        389.
        Attributes: optional-for-create, modifiable
        """
        return self._tcp_port
    @tcp_port.setter
    def tcp_port(self, val):
        if val != None:
            self.validate('tcp_port', val)
        self._tcp_port = val
    
    _group_scope = None
    @property
    def group_scope(self):
        """
        This indicates the scope for LDAP search when doing group
        lookups.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "base"      - Search only the base directory
        entry,
        <li> "onelevel"  - Search the base directory entry and
        the children of the base entry,
        <li> "subtree"   - Search the base directory entry and
        all its decendants
        </ul>
        """
        return self._group_scope
    @group_scope.setter
    def group_scope(self, val):
        if val != None:
            self.validate('group_scope', val)
        self._group_scope = val
    
    _schema = None
    @property
    def schema(self):
        """
        LDAP schema to use for this configuration. The list of
        possible schemas can be obtained using the
        ldap-client-schema-get-iter API.
        Attributes: required-for-create, modifiable
        """
        return self._schema
    @schema.setter
    def schema(self, val):
        if val != None:
            self.validate('schema', val)
        self._schema = val
    
    _base_dn = None
    @property
    def base_dn(self):
        """
        Indicates the starting point for searches within the LDAP
        directory tree. If omitted, searches will start at the
        root of the directory tree.
        Attributes: optional-for-create, modifiable
        """
        return self._base_dn
    @base_dn.setter
    def base_dn(self, val):
        if val != None:
            self.validate('base_dn', val)
        self._base_dn = val
    
    @staticmethod
    def get_api_name():
          return "ldap-client"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'group-dn',
            'netgroup-dn',
            'servers',
            'ad-domain',
            'use-start-tls',
            'bind-password',
            'user-scope',
            'is-owner',
            'bind-dn',
            'vserver',
            'min-bind-level',
            'ldap-client-config',
            'preferred-ad-servers',
            'bind-as-cifs-server',
            'base-scope',
            'query-timeout',
            'user-dn',
            'netgroup-scope',
            'tcp-port',
            'group-scope',
            'schema',
            'base-dn',
        ]
    
    def describe_properties(self):
        return {
            'group_dn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netgroup_dn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'ad_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'use_start_tls': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'bind_password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_scope': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_owner': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'bind_dn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'min_bind_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ldap_client_config': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'preferred_ad_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'bind_as_cifs_server': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'base_scope': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'query_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'user_dn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netgroup_scope': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tcp_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group_scope': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schema': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'base_dn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
