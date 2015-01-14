from netapp.connection import NaConnection
from ldap_search_scope import LdapSearchScope # 0 properties
from ldap_config import LdapConfig # 3 properties
from ldap_client import LdapClient # 22 properties
from ldap_dn import LdapDn # 0 properties
from ldap_auth_method import LdapAuthMethod # 0 properties
from ldap_client_schema import LdapClientSchema # 20 properties
from ldap_config_get_iter_key_td import LdapConfigGetIterKeyTd # 1 properties
from ldap_client_get_iter_key_td import LdapClientGetIterKeyTd # 2 properties
from ldap_client_schema_get_iter_key_td import LdapClientSchemaGetIterKeyTd # 2 properties

class LdapConnection(NaConnection):
    
    def ldap_client_schema_copy(self, new_schema_name, schema):
        """
        Copy an existing LDAP schema. If the LDAP server that the storage
        system needs to query does not support any of the default
        read-only schemas, this API can be used to create an editable
        copy of an existing read-only schema. After copying the schema,
        the copy can be modified using the ldap-client-schema-modify
        API.
        
        :param new_schema_name: New Schema Template Name
        
        :param schema: A name for the schema.
        """
        return self.request( "ldap-client-schema-copy", {
            'new_schema_name': [ new_schema_name, 'new-schema-name', [ basestring, 'None' ], False ],
            'schema': [ schema, 'schema', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ldap_config_delete(self):
        """
        Delete a Vserver's association with a Lightweight Directory
        Access Protocol (LDAP) configuration.
        """
        return self.request( "ldap-config-delete", {
        }, {
        } )
    
    def ldap_config_modify(self, client_config=None, client_enabled=None):
        """
        Modify the Lightweight Directory Access Protocol (LDAP)
        configuration for a Vserver.
        
        :param client_config: The name of an existing Lightweight Directory Access Protocol
                (LDAP) client configuration. The LDAP client configuration can be
                created using the ldap-client-create API. The
                ldap-client-get-iter API can be used to retrieve the list of
                available LDAP client configurations for the cluster.
        
        :param client_enabled: If true, the corresponding Lightweight Directory Access Protocol
                (LDAP) configuration is enabled for this Vserver.
        """
        return self.request( "ldap-config-modify", {
            'client_config': [ client_config, 'client-config', [ basestring, 'None' ], False ],
            'client_enabled': [ client_enabled, 'client-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def ldap_config_create(self, client_config, client_enabled, return_record=None):
        """
        Create a new association between a Lightweight Directory Access
        Protocol (LDAP) client configuration and a Vserver. A Vserver can
        have only one client configuration associated with it.
        
        :param client_config: The name of an existing Lightweight Directory Access Protocol
                (LDAP) client configuration. The LDAP client configuration can be
                created using the ldap-client-create API. The
                ldap-client-get-iter API can be used to retrieve the list of
                available LDAP client configurations for the cluster.
        
        :param client_enabled: If true, the corresponding Lightweight Directory Access Protocol
                (LDAP) configuration is enabled for this Vserver.
        
        :param return_record: If set to true, returns the ldap-config on successful creation.
                Default: false
        """
        return self.request( "ldap-config-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'client_config': [ client_config, 'client-config', [ basestring, 'None' ], False ],
            'client_enabled': [ client_enabled, 'client-enabled', [ bool, 'None' ], False ],
        }, {
            'result': [ LdapConfig, False ],
        } )
    
    def ldap_client_delete(self, ldap_client_config):
        """
        Delete an existing Lightweight Directory Access Protocol (LDAP)
        client configuration from the cluster.
        
        :param ldap_client_config: The name of the LDAP client configuration.
        """
        return self.request( "ldap-client-delete", {
            'ldap_client_config': [ ldap_client_config, 'ldap-client-config', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ldap_client_schema_modify(self, schema, comment=None, cn_netgroup_attribute=None, posix_group_object_class=None, home_directory_attribute=None, member_uid_attribute=None, gid_number_attribute=None, nis_netgroup_triple_attribute=None, gecos_attribute=None, uid_attribute=None, cn_group_attribute=None, uid_number_attribute=None, login_shell_attribute=None, user_password_attribute=None, posix_account_object_class=None, nis_netgroup_object_class=None, windows_account_attribute=None, member_nis_netgroup_attribute=None):
        """
        Modify an existing Lightweight Directory Access Protocol (LDAP)
        schema configuration. If the LDAP server that the storage system
        needs to query does not support any of the default read-only
        schemas, the ldap-client-schema-copy API can be used to create a
        editable copy of an existing read-only schema. After copying the
        schema, the copy can be modified using this API to support the
        target schema.
        
        :param schema: A name for the schema.
        
        :param comment: A comment that can be associated with the schema.
        
        :param cn_netgroup_attribute: Name that represents the RFC 2256 cn attribute used by RFC 2307
                when working with netgroups.
        
        :param posix_group_object_class: Name that represents the RFC 2307 posixGroup object class.
        
        :param home_directory_attribute: Name that represents the RFC 2307 homeDirectory attribute.
        
        :param member_uid_attribute: Name that represents the RFC 2307 memberUid attribute.
        
        :param gid_number_attribute: Name that represents the RFC 2307 gidNumber attribute.
        
        :param nis_netgroup_triple_attribute: Name that represents the RFC 2307 nisNetgroupTriple attribute.
        
        :param gecos_attribute: Name that represents the RFC 2307 gecos attribute.
        
        :param uid_attribute: Name that represents the RFC 1274 userid attribute used by RFC
                2307 as uid.
        
        :param cn_group_attribute: Name that represents the RFC 2256 cn attribute used by RFC 2307
                when working with groups.
        
        :param uid_number_attribute: Name that represents the RFC 2307 uidNumber attribute.
        
        :param login_shell_attribute: Name that represents the RFC 2307 loginShell attribute.
        
        :param user_password_attribute: Name that represents the RFC 2256 userPassword attribute used by
                RFC 2307.
        
        :param posix_account_object_class: Name that represents the RFC 2307 posixAccount object class.
        
        :param nis_netgroup_object_class: Name that represents the RFC 2307 nisNetgroup object class.
        
        :param windows_account_attribute: Attribute name to be used to get the windows account information
                for a unix user account.
        
        :param member_nis_netgroup_attribute: Name that represents the RFC 2307 memberNisNetgroup attribute.
        """
        return self.request( "ldap-client-schema-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'cn_netgroup_attribute': [ cn_netgroup_attribute, 'cn-netgroup-attribute', [ basestring, 'None' ], False ],
            'posix_group_object_class': [ posix_group_object_class, 'posix-group-object-class', [ basestring, 'None' ], False ],
            'home_directory_attribute': [ home_directory_attribute, 'home-directory-attribute', [ basestring, 'None' ], False ],
            'member_uid_attribute': [ member_uid_attribute, 'member-uid-attribute', [ basestring, 'None' ], False ],
            'gid_number_attribute': [ gid_number_attribute, 'gid-number-attribute', [ basestring, 'None' ], False ],
            'nis_netgroup_triple_attribute': [ nis_netgroup_triple_attribute, 'nis-netgroup-triple-attribute', [ basestring, 'None' ], False ],
            'gecos_attribute': [ gecos_attribute, 'gecos-attribute', [ basestring, 'None' ], False ],
            'uid_attribute': [ uid_attribute, 'uid-attribute', [ basestring, 'None' ], False ],
            'cn_group_attribute': [ cn_group_attribute, 'cn-group-attribute', [ basestring, 'None' ], False ],
            'uid_number_attribute': [ uid_number_attribute, 'uid-number-attribute', [ basestring, 'None' ], False ],
            'login_shell_attribute': [ login_shell_attribute, 'login-shell-attribute', [ basestring, 'None' ], False ],
            'user_password_attribute': [ user_password_attribute, 'user-password-attribute', [ basestring, 'None' ], False ],
            'posix_account_object_class': [ posix_account_object_class, 'posix-account-object-class', [ basestring, 'None' ], False ],
            'nis_netgroup_object_class': [ nis_netgroup_object_class, 'nis-netgroup-object-class', [ basestring, 'None' ], False ],
            'windows_account_attribute': [ windows_account_attribute, 'windows-account-attribute', [ basestring, 'None' ], False ],
            'member_nis_netgroup_attribute': [ member_nis_netgroup_attribute, 'member-nis-netgroup-attribute', [ basestring, 'None' ], False ],
            'schema': [ schema, 'schema', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ldap_client_create(self, ldap_client_config, schema, user_scope=None, use_start_tls=None, return_record=None, bind_dn=None, group_dn=None, tcp_port=None, preferred_ad_servers=None, bind_as_cifs_server=None, base_scope=None, servers=None, netgroup_scope=None, group_scope=None, netgroup_dn=None, user_dn=None, min_bind_level=None, ad_domain=None, query_timeout=None, bind_password=None, base_dn=None):
        """
        Create a new Lightweight Directory Access Protocol (LDAP) client
        configuration for the cluster.
        
        :param ldap_client_config: The name of the LDAP client configuration.
        
        :param schema: LDAP schema to use for this configuration. The list of possible
                schemas can be obtained using the ldap-client-schema-get-iter
                API.
        
        :param user_scope: This indicates the scope for LDAP search when doing user
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param use_start_tls: This indicates if start_tls will be used over LDAP connections.
        
        :param return_record: If set to true, returns the ldap-client on successful creation.
                Default: false
        
        :param bind_dn: The Bind Distinguished Name (DN) is the LDAP identity used during
                the authentication process by the clients. This is required if
                the LDAP server does not support anonymous binds. This field is
                not used if 'bind-as-cfs-server' is set to 'true'. Example :
                cn=username,cn=Users,dc=example,dc=com
        
        :param group_dn: The Group Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for group lookups. If
                not specified, group lookups will start at the base-dn.
        
        :param tcp_port: The TCP port on the LDAP server to use for this configuration. If
                omitted, this parameter defaults to 389.
        
        :param preferred_ad_servers: Preferred Active Directory (AD) Domain controllers to use for
                this configuration. This option is ONLY applicable for
                configurations using Active Directory LDAP servers
        
        :param bind_as_cifs_server: If set, the cluster will use the CIFS server's credentials to
                bind to the LDAP server. If omitted, this parameter defaults to
                'true' if the configuration uses Active Directory LDAP and
                defaults to 'false' otherwise.
        
        :param base_scope: This indicates the scope for LDAP search. If omitted, this
                parameter defaults to 'subtree'.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param servers: List of LDAP Server IP addresses to use for this configuration.
                The option is NOT applicable for configurations using Active
                Directory LDAP servers.
        
        :param netgroup_scope: This indicates the scope for LDAP search when doing netgroup
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param group_scope: This indicates the scope for LDAP search when doing group
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param netgroup_dn: The Netgoup Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for netgroup lookups.
                If not specified, netgroup lookups will start at the base-dn.
        
        :param user_dn: The User Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for user lookups. If
                this parameter is omitted, user lookups will start at the
                base-dn.
        
        :param min_bind_level: The minimum authentication level that can be used to authenticate
                with the LDAP server. If omitted, this parameter defaults to
                'sasl' if the configuration uses Active Directory LDAP. For
                configurations that use LDAP servers from other vendors, this
                parameter defaults to 'simple' if a 'bind-dn' is specified and
                'anonymous' otherwise.
                Possible values:
                <ul>
                <li> "anonymous" - Anonymous bind,
                <li> "simple"    - Simple bind,
                <li> "sasl"      - Simple Authentication and Security Layer
                (SASL) bind
                </ul>
        
        :param ad_domain: The Active Directory Domain Name for this LDAP configuration. The
                option is ONLY applicable for configurations using Active
                Directory LDAP servers.
        
        :param query_timeout: Maximum time in seconds to wait for a query response from the
                LDAP server. The default for this parameter is 3 seconds.
        
        :param bind_password: The password to be used with the bind-dn.
        
        :param base_dn: Indicates the starting point for searches within the LDAP
                directory tree. If omitted, searches will start at the root of
                the directory tree.
        """
        return self.request( "ldap-client-create", {
            'user_scope': [ user_scope, 'user-scope', [ basestring, 'ldap-search-scope' ], False ],
            'use_start_tls': [ use_start_tls, 'use-start-tls', [ bool, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'ldap_client_config': [ ldap_client_config, 'ldap-client-config', [ basestring, 'None' ], False ],
            'bind_dn': [ bind_dn, 'bind-dn', [ basestring, 'ldap-dn' ], False ],
            'group_dn': [ group_dn, 'group-dn', [ basestring, 'ldap-dn' ], False ],
            'tcp_port': [ tcp_port, 'tcp-port', [ int, 'None' ], False ],
            'preferred_ad_servers': [ preferred_ad_servers, 'preferred-ad-servers', [ basestring, 'ip-address' ], True ],
            'bind_as_cifs_server': [ bind_as_cifs_server, 'bind-as-cifs-server', [ bool, 'None' ], False ],
            'base_scope': [ base_scope, 'base-scope', [ basestring, 'ldap-search-scope' ], False ],
            'servers': [ servers, 'servers', [ basestring, 'ip-address' ], True ],
            'netgroup_scope': [ netgroup_scope, 'netgroup-scope', [ basestring, 'ldap-search-scope' ], False ],
            'group_scope': [ group_scope, 'group-scope', [ basestring, 'ldap-search-scope' ], False ],
            'netgroup_dn': [ netgroup_dn, 'netgroup-dn', [ basestring, 'ldap-dn' ], False ],
            'user_dn': [ user_dn, 'user-dn', [ basestring, 'ldap-dn' ], False ],
            'min_bind_level': [ min_bind_level, 'min-bind-level', [ basestring, 'ldap-auth-method' ], False ],
            'ad_domain': [ ad_domain, 'ad-domain', [ basestring, 'None' ], False ],
            'query_timeout': [ query_timeout, 'query-timeout', [ int, 'None' ], False ],
            'bind_password': [ bind_password, 'bind-password', [ basestring, 'None' ], False ],
            'base_dn': [ base_dn, 'base-dn', [ basestring, 'ldap-dn' ], False ],
            'schema': [ schema, 'schema', [ basestring, 'None' ], False ],
        }, {
            'result': [ LdapClient, False ],
        } )
    
    def ldap_client_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of Lightweight Directory Access Protocol (LDAP)
        client configurations for the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ldap-client object.
                All ldap-client objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ldap-client-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LdapClient, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LdapClient, 'None' ], False ],
        }, {
            'attributes-list': [ LdapClient, True ],
        } )
    
    def ldap_client_schema_delete(self, schema):
        """
        Delete an existing Lightweight Directory Access Protocol (LDAP)
        schema configuration. Only the schemas that are defined using the
        ldap-client-schema-copy API can be deleted using this API.
        
        :param schema: A name for the schema.
        """
        return self.request( "ldap-client-schema-delete", {
            'schema': [ schema, 'schema', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ldap_client_modify(self, ldap_client_config, user_scope=None, use_start_tls=None, bind_dn=None, group_dn=None, tcp_port=None, preferred_ad_servers=None, bind_as_cifs_server=None, base_scope=None, servers=None, netgroup_scope=None, group_scope=None, netgroup_dn=None, user_dn=None, min_bind_level=None, ad_domain=None, query_timeout=None, bind_password=None, base_dn=None, schema=None):
        """
        Modify an existing Lightweight Directory Access Protocol (LDAP)
        client configuration.
        
        :param ldap_client_config: The name of the LDAP client configuration.
        
        :param user_scope: This indicates the scope for LDAP search when doing user
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param use_start_tls: This indicates if start_tls will be used over LDAP connections.
        
        :param bind_dn: The Bind Distinguished Name (DN) is the LDAP identity used during
                the authentication process by the clients. This is required if
                the LDAP server does not support anonymous binds. This field is
                not used if 'bind-as-cfs-server' is set to 'true'. Example :
                cn=username,cn=Users,dc=example,dc=com
        
        :param group_dn: The Group Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for group lookups. If
                not specified, group lookups will start at the base-dn.
        
        :param tcp_port: The TCP port on the LDAP server to use for this configuration. If
                omitted, this parameter defaults to 389.
        
        :param preferred_ad_servers: Preferred Active Directory (AD) Domain controllers to use for
                this configuration. This option is ONLY applicable for
                configurations using Active Directory LDAP servers
        
        :param bind_as_cifs_server: If set, the cluster will use the CIFS server's credentials to
                bind to the LDAP server. If omitted, this parameter defaults to
                'true' if the configuration uses Active Directory LDAP and
                defaults to 'false' otherwise.
        
        :param base_scope: This indicates the scope for LDAP search. If omitted, this
                parameter defaults to 'subtree'.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param servers: List of LDAP Server IP addresses to use for this configuration.
                The option is NOT applicable for configurations using Active
                Directory LDAP servers.
        
        :param netgroup_scope: This indicates the scope for LDAP search when doing netgroup
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param group_scope: This indicates the scope for LDAP search when doing group
                lookups.
                Possible values:
                <ul>
                <li> "base"      - Search only the base directory entry,
                <li> "onelevel"  - Search the base directory entry and the
                children of the base entry,
                <li> "subtree"   - Search the base directory entry and all its
                decendants
                </ul>
        
        :param netgroup_dn: The Netgoup Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for netgroup lookups.
                If not specified, netgroup lookups will start at the base-dn.
        
        :param user_dn: The User Distinguished Name (DN), if specified, is used as the
                starting point in the LDAP directory tree for user lookups. If
                this parameter is omitted, user lookups will start at the
                base-dn.
        
        :param min_bind_level: The minimum authentication level that can be used to authenticate
                with the LDAP server. If omitted, this parameter defaults to
                'sasl' if the configuration uses Active Directory LDAP. For
                configurations that use LDAP servers from other vendors, this
                parameter defaults to 'simple' if a 'bind-dn' is specified and
                'anonymous' otherwise.
                Possible values:
                <ul>
                <li> "anonymous" - Anonymous bind,
                <li> "simple"    - Simple bind,
                <li> "sasl"      - Simple Authentication and Security Layer
                (SASL) bind
                </ul>
        
        :param ad_domain: The Active Directory Domain Name for this LDAP configuration. The
                option is ONLY applicable for configurations using Active
                Directory LDAP servers.
        
        :param query_timeout: Maximum time in seconds to wait for a query response from the
                LDAP server. The default for this parameter is 3 seconds.
        
        :param bind_password: The password to be used with the bind-dn.
        
        :param base_dn: Indicates the starting point for searches within the LDAP
                directory tree. If omitted, searches will start at the root of
                the directory tree.
        
        :param schema: LDAP schema to use for this configuration. The list of possible
                schemas can be obtained using the ldap-client-schema-get-iter
                API.
        """
        return self.request( "ldap-client-modify", {
            'user_scope': [ user_scope, 'user-scope', [ basestring, 'ldap-search-scope' ], False ],
            'use_start_tls': [ use_start_tls, 'use-start-tls', [ bool, 'None' ], False ],
            'ldap_client_config': [ ldap_client_config, 'ldap-client-config', [ basestring, 'None' ], False ],
            'bind_dn': [ bind_dn, 'bind-dn', [ basestring, 'ldap-dn' ], False ],
            'group_dn': [ group_dn, 'group-dn', [ basestring, 'ldap-dn' ], False ],
            'tcp_port': [ tcp_port, 'tcp-port', [ int, 'None' ], False ],
            'preferred_ad_servers': [ preferred_ad_servers, 'preferred-ad-servers', [ basestring, 'ip-address' ], True ],
            'bind_as_cifs_server': [ bind_as_cifs_server, 'bind-as-cifs-server', [ bool, 'None' ], False ],
            'base_scope': [ base_scope, 'base-scope', [ basestring, 'ldap-search-scope' ], False ],
            'servers': [ servers, 'servers', [ basestring, 'ip-address' ], True ],
            'netgroup_scope': [ netgroup_scope, 'netgroup-scope', [ basestring, 'ldap-search-scope' ], False ],
            'group_scope': [ group_scope, 'group-scope', [ basestring, 'ldap-search-scope' ], False ],
            'netgroup_dn': [ netgroup_dn, 'netgroup-dn', [ basestring, 'ldap-dn' ], False ],
            'user_dn': [ user_dn, 'user-dn', [ basestring, 'ldap-dn' ], False ],
            'min_bind_level': [ min_bind_level, 'min-bind-level', [ basestring, 'ldap-auth-method' ], False ],
            'ad_domain': [ ad_domain, 'ad-domain', [ basestring, 'None' ], False ],
            'query_timeout': [ query_timeout, 'query-timeout', [ int, 'None' ], False ],
            'bind_password': [ bind_password, 'bind-password', [ basestring, 'None' ], False ],
            'base_dn': [ base_dn, 'base-dn', [ basestring, 'ldap-dn' ], False ],
            'schema': [ schema, 'schema', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ldap_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of Lightweight Directory Access Protocol (LDAP)
        configurations in the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ldap-config object.
                All ldap-config objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ldap-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LdapConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LdapConfig, 'None' ], False ],
        }, {
            'attributes-list': [ LdapConfig, True ],
        } )
    
    def ldap_client_schema_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of Lightweight Directory Access Protocol (LDAP)
        client schema configurations that are defined for the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ldap-client-schema object.
                All ldap-client-schema objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ldap-client-schema-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ LdapClientSchema, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ LdapClientSchema, 'None' ], False ],
        }, {
            'attributes-list': [ LdapClientSchema, True ],
        } )
