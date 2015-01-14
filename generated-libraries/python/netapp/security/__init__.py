from netapp.connection import NaConnection
from security_login_role_delete_iter_key_td import SecurityLoginRoleDeleteIterKeyTd # 3 properties
from hex_string import HexString # 0 properties
from security_login_role_modify_iter_info import SecurityLoginRoleModifyIterInfo # 3 properties
from security_login_role_delete_iter_info import SecurityLoginRoleDeleteIterInfo # 3 properties
from kex_algorithms import KexAlgorithms # 0 properties
from security_login_role_config_info import SecurityLoginRoleConfigInfo # 13 properties
from snmpv3_login_info import Snmpv3LoginInfo # 5 properties
from security_login_modify_iter_key_td import SecurityLoginModifyIterKeyTd # 4 properties
from security_login_role_modify_iter_key_td import SecurityLoginRoleModifyIterKeyTd # 3 properties
from security_login_role_config_get_iter_key_td import SecurityLoginRoleConfigGetIterKeyTd # 2 properties
from ciphers import Ciphers # 0 properties
from security_ssh_info import SecuritySshInfo # 3 properties
from security_login_role_get_iter_key_td import SecurityLoginRoleGetIterKeyTd # 3 properties
from security_login_account_info import SecurityLoginAccountInfo # 7 properties
from security_login_modify_iter_info import SecurityLoginModifyIterInfo # 3 properties
from security_login_delete_iter_key_td import SecurityLoginDeleteIterKeyTd # 4 properties
from security_login_role_config_modify_iter_info import SecurityLoginRoleConfigModifyIterInfo # 3 properties
from security_login_get_iter_key_td import SecurityLoginGetIterKeyTd # 4 properties
from security_login_delete_iter_info import SecurityLoginDeleteIterInfo # 3 properties
from security_login_role_info import SecurityLoginRoleInfo # 5 properties
from security_ssh_get_iter_key_td import SecuritySshGetIterKeyTd # 1 properties
from security_login_role_config_modify_iter_key_td import SecurityLoginRoleConfigModifyIterKeyTd # 2 properties

class SecurityConnection(NaConnection):
    
    def security_ssh_remove(self, vserver=None, ciphers=None, key_exchange_algorithms=None):
        """
        Removes the input algorithms and ciphers from the SSH
        configuration. API will succeed if requested algorithm or cipher
        is already currently enabled in the configuration.
        
        :param vserver: Name of Vserver.
        
        :param ciphers: List of SSH Ciphers to Remove
        
        :param key_exchange_algorithms: List of SSH Key Exchange Algorithms to Remove
        """
        return self.request( "security-ssh-remove", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'ciphers': [ ciphers, 'ciphers', [ basestring, 'ciphers' ], True ],
            'key_exchange_algorithms': [ key_exchange_algorithms, 'key-exchange-algorithms', [ basestring, 'kex-algorithms' ], True ],
        }, {
        } )
    
    def security_login_modify(self, user_name, authentication_method, vserver, application, role_name, comment=None):
        """
        Modify the attributes of a user account object. Omitted
        (optional) fields will not be changed.
        
        :param user_name: Name of the user.
                When creating a SNMPv1 or SNMPv2 user with 'snmp' application and
                'community' authentication-method, the user name is the community
                string.
        
        :param authentication_method: Authentication method for the application.
                Possible values: 'community', 'password', 'publickey', 'domain',
                'nsswitch' and 'usm'.
                Not all authentication methods are valid for an application.
                Valid authentication methods for each application are:
                'password' for 'console' application.
                'password', 'domain', 'nsswitch', 'cert' for 'http' application.
                'password', 'domain', 'nsswitch', 'cert'  for 'ontapi'
                application.
                'community' for 'snmp' application (when creating SNMPv1 and
                SNMPv2 users).
                'usm' and 'community' for 'snmp' application (when creating
                SNMPv3 users).
                'password' for 'sp' application.
                'password' for 'rsh' application.
                'password' for 'telnet' application.
                'password', 'publickey', 'domain', 'nsswitch' for 'ssh'
                application.
        
        :param vserver: Name of the Vserver.
        
        :param application: Name of the application. Possible
                values: 'console', 'http', 'ontapi', 'rsh',
                'snmp', 'sp', 'ssh', 'telnet'.
        
        :param role_name: Name of the role.
        
        :param comment: Comments for the user account. The length of comment should be
                less than or equal to 128 charaters.
        """
        return self.request( "security-login-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'authentication_method': [ authentication_method, 'authentication-method', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'application': [ application, 'application', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_lock(self, vserver, user_name):
        """
        Lock a user account that uses password as the authentication
        method. Returns an error if the user account does not use
        password authentication.
        
        :param vserver: Name of the Vserver.
        
        :param user_name: Name of the user account to be locked.
        """
        return self.request( "security-login-lock", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_unlock(self, vserver, user_name):
        """
        Unlock a user account that uses password as the authentication
        method. Returns an error if the user account does not use
        password authentication.
        
        :param vserver: Name of the Vserver.
        
        :param user_name: Name of the user account to be unlocked.
        """
        return self.request( "security-login-unlock", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_role_get(self, vserver, command_directory_name, role_name, desired_attributes=None):
        """
        Get the attributes of a user role.
        
        :param vserver: Name of the Vserver.
        
        :param command_directory_name: The command or command directory to which the role has an
                access.
        
        :param role_name: Name of the role.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-login-role-get", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'command_directory_name': [ command_directory_name, 'command-directory-name', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginRoleInfo, 'None' ], False ],
        }, {
            'attributes': [ SecurityLoginRoleInfo, False ],
        } )
    
    def security_ssh_add(self, vserver=None, ciphers=None, key_exchange_algorithms=None):
        """
        Adds the input algorithms and ciphers to the SSH configuration.
        Existing algorithms and ciphers remain in the configuration. API
        will succeed if requested algorithm or cipher is not currently
        enabled in the configuration.
        
        :param vserver: Name of Vserver.
        
        :param ciphers: List of SSH Ciphers to Add
        
        :param key_exchange_algorithms: List of SSH Key Exchange Algorithms to Add
        """
        return self.request( "security-ssh-add", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'ciphers': [ ciphers, 'ciphers', [ basestring, 'ciphers' ], True ],
            'key_exchange_algorithms': [ key_exchange_algorithms, 'key-exchange-algorithms', [ basestring, 'kex-algorithms' ], True ],
        }, {
        } )
    
    def security_login_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of user account objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security login account object.
                All security login account objects matching this query up to
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
        return self.request( "security-login-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecurityLoginAccountInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginAccountInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SecurityLoginAccountInfo, True ],
        } )
    
    def security_login_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of a user account or a group of user
        account objects.
        
        :param query: If modifying a specific security login account, this input
                element must specify all keys.
                If modifying security login account objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                security login account even when the modification of a previous
                matching security login account fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of security login
                account objects (just keys) that were successfully updated.
                If set to false, the list of security login account objects
                modified will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security login account
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                security login account even when modification of a previous
                security login account fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of security login
                account objects (just keys) that were not modified due to some
                error.
                If set to false, the list of security login account objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "security-login-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SecurityLoginAccountInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ SecurityLoginAccountInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityLoginModifyIterInfo, True ],
            'failure-list': [ SecurityLoginModifyIterInfo, True ],
        } )
    
    def security_ssh_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display SSH configuration options
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the ssh
                object.
                All ssh objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "security-ssh-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecuritySshInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecuritySshInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SecuritySshInfo, True ],
        } )
    
    def security_login_modify_password(self, new_password, user_name=None):
        """
        Changes the password of a specified user.
        
        :param new_password: New password of the user.
        
        :param user_name: The user whose password should be changed. This is
                mandatory when a user with admin role is modifying the password
                of
                another user.
        """
        return self.request( "security-login-modify-password", {
            'new_password': [ new_password, 'new-password', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_create(self, user_name, authentication_method, vserver, application, role_name, comment=None, snmpv3_login_info=None, password=None):
        """
        Create a new user account associated the specified application
        and authentication method.
        
        :param user_name: Name of the user.
                When creating a SNMPv1 or SNMPv2 user with 'snmp' application and
                'community' authentication-method, the user name is the community
                string.
        
        :param authentication_method: Authentication method for the application.
                Possible values: 'community', 'password', 'publickey', 'domain',
                'nsswitch' and 'usm'.
                Not all authentication methods are valid for an application.
                Valid authentication methods for each application are:
                'password' for 'console' application.
                'password', 'domain', 'nsswitch', 'cert' for 'http' application.
                'password', 'domain', 'nsswitch', 'cert'  for 'ontapi'
                application.
                'community' for 'snmp' application (when creating SNMPv1 and
                SNMPv2 users).
                'usm' and 'community' for 'snmp' application (when creating
                SNMPv3 users).
                'password' for 'sp' application.
                'password' for 'rsh' application.
                'password' for 'telnet' application.
                'password', 'publickey', 'domain', 'nsswitch' for 'ssh'
                application.
        
        :param vserver: Name of the Vserver.
        
        :param application: Name of the application. Possible
                values: 'console', 'http', 'ontapi', 'rsh',
                'snmp', 'sp', 'ssh', 'telnet'.
        
        :param role_name: Name of the role.
        
        :param comment: Comments for the user account. The length of comment should be
                less than or equal to 128 charaters.
        
        :param snmpv3_login_info: SNMPv3 user login information for 'usm' authentication method
        
        :param password: Password for the user account.
                This is ignored for creating snmp users. This is required for
                creating non-snmp users.
        """
        return self.request( "security-login-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'snmpv3_login_info': [ snmpv3_login_info, 'snmpv3-login-info', [ Snmpv3LoginInfo, 'None' ], False ],
            'authentication_method': [ authentication_method, 'authentication-method', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'application': [ application, 'application', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_role_config_modify(self, vserver, role_name, min_username_size=None, require_initial_password_update=None, change_password_duration_in_days=None, password_expiration_duration=None, last_passwords_disallowed_count=None, require_username_alpha_numeric=None, max_failed_login_attempts=None, lockout_duration=None, min_password_size=None, require_password_alpha_numeric=None, min_passwd_specialchar=None):
        """
        Modify the specified attributes of role configuration object.
        Omitted (optional) fields will not be changed.
        
        :param vserver: Name of the Vserver.
        
        :param role_name: Name of the role.
        
        :param min_username_size: The minimum length of the user name. Possible values range from 3
                to 16 characters. The default setting is 3 characters.
        
        :param require_initial_password_update: This optionally specifies to change the password upon first-login
                to the storage controller from SSH or serial-console. Default is
                false.
        
        :param change_password_duration_in_days: This optionally specifies the number of days that must pass
                between password changes. The default setting is 0 (zero) meaning
                the user is allowed to change the password immediately.
        
        :param password_expiration_duration: This optionally specifies the password expiry in days. A value of
                0 means it expiries now. Default is 2^32-1 (ie., never expire).
        
        :param last_passwords_disallowed_count: This optionally specifies the number of previous passwords that
                are disallowed for reuse. The default setting is 6.
        
        :param require_username_alpha_numeric: If this field is set it specifies that the username must have
                atleast 1 alpha and 1 numeric character.
        
        :param max_failed_login_attempts: This optionally specifies the maximum number of invalid login
                attempts after which the account gets locked. Default is 0.
        
        :param lockout_duration: This optionally specifies the number of days to lock the account
                if maximum number of failed attempts occur. Default is 0.
        
        :param min_password_size: This optionally specifies the minimum length of the password.
                Possible values range from 3 to 64 characters. The default
                setting is 8 characters.
        
        :param require_password_alpha_numeric: If this field is set it specifies that the password must have
                atleast 1 alpha and 1 numeric character.
        
        :param min_passwd_specialchar: This optionally specifies the minimum special characters required
                in password. The default setting is no special chars i.e. 0.
        """
        return self.request( "security-login-role-config-modify", {
            'min_username_size': [ min_username_size, 'min-username-size', [ int, 'None' ], False ],
            'require_initial_password_update': [ require_initial_password_update, 'require-initial-password-update', [ bool, 'None' ], False ],
            'change_password_duration_in_days': [ change_password_duration_in_days, 'change-password-duration-in-days', [ int, 'None' ], False ],
            'password_expiration_duration': [ password_expiration_duration, 'password-expiration-duration', [ basestring, 'None' ], False ],
            'last_passwords_disallowed_count': [ last_passwords_disallowed_count, 'last-passwords-disallowed-count', [ int, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'require_username_alpha_numeric': [ require_username_alpha_numeric, 'require-username-alpha-numeric', [ bool, 'None' ], False ],
            'max_failed_login_attempts': [ max_failed_login_attempts, 'max-failed-login-attempts', [ int, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'lockout_duration': [ lockout_duration, 'lockout-duration', [ int, 'None' ], False ],
            'min_password_size': [ min_password_size, 'min-password-size', [ int, 'None' ], False ],
            'require_password_alpha_numeric': [ require_password_alpha_numeric, 'require-password-alpha-numeric', [ bool, 'None' ], False ],
            'min_passwd_specialchar': [ min_passwd_specialchar, 'min-passwd-specialchar', [ int, 'None' ], False ],
        }, {
        } )
    
    def security_login_delete(self, vserver, application, user_name, authentication_method):
        """
        Delete an existing user account object.
        
        :param vserver: Name of the Vserver.
        
        :param application: Name of the application. Possible
                values: 'console', 'http', 'ontapi', 'rsh',
                'snmp', 'sp', 'ssh', 'telnet'.
        
        :param user_name: Name of the user.
                When creating a SNMPv1 or SNMPv2 user with 'snmp' application and
                'community' authentication-method, the user name is the community
                string.
        
        :param authentication_method: Authentication method for the application.
                Possible values: 'community', 'password', 'publickey', 'domain',
                'nsswitch' and 'usm'.
                Not all authentication methods are valid for an application.
                Valid authentication methods for each application are:
                'password' for 'console' application.
                'password', 'domain', 'nsswitch', 'cert' for 'http' application.
                'password', 'domain', 'nsswitch', 'cert'  for 'ontapi'
                application.
                'community' for 'snmp' application (when creating SNMPv1 and
                SNMPv2 users).
                'usm' and 'community' for 'snmp' application (when creating
                SNMPv3 users).
                'password' for 'sp' application.
                'password' for 'rsh' application.
                'password' for 'telnet' application.
                'password', 'publickey', 'domain', 'nsswitch' for 'ssh'
                application.
        """
        return self.request( "security-login-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'application': [ application, 'application', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'authentication_method': [ authentication_method, 'authentication-method', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_role_create(self, vserver, role_name, command_directory_name, return_record=None, access_level=None, role_query=None):
        """
        Create a new user role.
        
        :param vserver: Name of the Vserver.
        
        :param role_name: Name of the role.
        
        :param command_directory_name: The command or command directory to which the role has an
                access.
        
        :param return_record: If set to true, returns the security login role on successful
                creation.
                Default: false
        
        :param access_level: Access level for the role. Possible values:
                'none', 'readonly', 'all'.
                The default value is 'all'.
        
        :param role_query: A query for the role. The query must apply to the specified
                command or directory name.
                Example: The command is 'volume show' and the query is '-volume
                vol1'. The query is applied to the command resulting in
                populating only the volumes with name vol1.
        """
        return self.request( "security-login-role-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'command_directory_name': [ command_directory_name, 'command-directory-name', [ basestring, 'None' ], False ],
            'access_level': [ access_level, 'access-level', [ basestring, 'None' ], False ],
            'role_query': [ role_query, 'role-query', [ basestring, 'None' ], False ],
        }, {
            'result': [ SecurityLoginRoleInfo, False ],
        } )
    
    def security_login_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete an existing user account or a group of user account
        objects.
        
        :param query: If deleting a specific security login account, this input element
                must specify all keys.
                If deleting multiple security login account objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching security
                login account even when the deletion of a previous matching
                security login account fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of security login account objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of security login
                account objects (just keys) that were successfully deleted.
                If set to false, the list of security login account objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security login account
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                security login account even when the deletion of a previous
                security login account fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of security login
                account objects (just keys) that were not deleted due to some
                error.
                If set to false, the list of security login account objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "security-login-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SecurityLoginAccountInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityLoginDeleteIterInfo, True ],
            'failure-list': [ SecurityLoginDeleteIterInfo, True ],
        } )
    
    def security_login_role_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of role objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security login roleconfig object.
                All security login roleconfig objects matching this query up to
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
        return self.request( "security-login-role-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecurityLoginRoleConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginRoleConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SecurityLoginRoleConfigInfo, True ],
        } )
    
    def ssh_prepare_to_downgrade(self):
        """
        auto generated : Restore SSH configuration to releases earlier
        than Data ONTAP 8.2.1.
        """
        return self.request( "ssh-prepare-to-downgrade", {
        }, {
        } )
    
    def security_login_role_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete an existing user role or a group of user role objects.
        
        :param query: If deleting a specific security login role, this input element
                must specify all keys.
                If deleting multiple security login role objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching security
                login role even when the deletion of a previous matching security
                login role fails, and do so until the total number of objects
                failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of security login role objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of security login
                role objects (just keys) that were successfully deleted.
                If set to false, the list of security login role objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security login role
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                security login role even when the deletion of a previous security
                login role fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of security login
                role objects (just keys) that were not deleted due to some
                error.
                If set to false, the list of security login role objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "security-login-role-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SecurityLoginRoleInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityLoginRoleDeleteIterInfo, True ],
            'failure-list': [ SecurityLoginRoleDeleteIterInfo, True ],
        } )
    
    def security_login_role_modify(self, vserver, command_directory_name, role_name, access_level=None, role_query=None):
        """
        Modify the attributes of user role object. Omitted (optional)
        fields will not be changed.
        
        :param vserver: Name of the Vserver.
        
        :param command_directory_name: The command or command directory to which the role has an
                access.
        
        :param role_name: Name of the role.
        
        :param access_level: Access level for the role. Possible values:
                'none', 'readonly', 'all'.
                The default value is 'all'.
        
        :param role_query: A query for the role. The query must apply to the specified
                command or directory name.
                Example: The command is 'volume show' and the query is '-volume
                vol1'. The query is applied to the command resulting in
                populating only the volumes with name vol1.
        """
        return self.request( "security-login-role-modify", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'command_directory_name': [ command_directory_name, 'command-directory-name', [ basestring, 'None' ], False ],
            'access_level': [ access_level, 'access-level', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'role_query': [ role_query, 'role-query', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_role_config_get(self, vserver, role_name, desired_attributes=None):
        """
        Get the attributes of a role configuration.
        
        :param vserver: Name of the Vserver.
        
        :param role_name: Name of the role.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-login-role-config-get", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginRoleConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ SecurityLoginRoleConfigInfo, False ],
        } )
    
    def security_reset(self):
        """
        auto generated : Reset RBAC characteristics supported on releases
        later than Data ONTAP 8.1.2
        """
        return self.request( "security-reset", {
        }, {
        } )
    
    def security_login_role_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of user role or a group of user role
        objects.
        
        :param query: If modifying a specific security login role, this input element
                must specify all keys.
                If modifying security login role objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                security login role even when the modification of a previous
                matching security login role fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of security login
                role objects (just keys) that were successfully updated.
                If set to false, the list of security login role objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security login role
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                security login role even when modification of a previous security
                login role fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of security login
                role objects (just keys) that were not modified due to some
                error.
                If set to false, the list of security login role objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "security-login-role-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SecurityLoginRoleInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ SecurityLoginRoleInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityLoginRoleModifyIterInfo, True ],
            'failure-list': [ SecurityLoginRoleModifyIterInfo, True ],
        } )
    
    def security_login_role_delete(self, vserver, command_directory_name, role_name):
        """
        Delete an existing user role object.
        
        :param vserver: Name of the Vserver.
        
        :param command_directory_name: The command or command directory to which the role has an
                access.
        
        :param role_name: Name of the role.
        """
        return self.request( "security-login-role-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'command_directory_name': [ command_directory_name, 'command-directory-name', [ basestring, 'None' ], False ],
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_login_role_config_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of role configuration or a group of role
        configuration  objects.
        
        :param query: If modifying a specific security login roleconfig, this input
                element must specify all keys.
                If modifying security login roleconfig objects based on query,
                this input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                security login roleconfig even when the modification of a
                previous matching security login roleconfig fails, and do so
                until the total number of objects failed to be modified reaches
                the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of security login
                roleconfig objects (just keys) that were successfully updated.
                If set to false, the list of security login roleconfig objects
                modified will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security login
                roleconfig objects match a given query.
                If set to true, the API will continue modifying the next matching
                security login roleconfig even when modification of a previous
                security login roleconfig fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of security login
                roleconfig objects (just keys) that were not modified due to some
                error.
                If set to false, the list of security login roleconfig objects
                not modified will not be returned.
                Default: true
        """
        return self.request( "security-login-role-config-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ SecurityLoginRoleConfigInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ SecurityLoginRoleConfigInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityLoginRoleConfigModifyIterInfo, True ],
            'failure-list': [ SecurityLoginRoleConfigModifyIterInfo, True ],
        } )
    
    def security_ssh_reset(self, ciphers=None, key_exchange_algorithms=None):
        """
        Enable and replace SSH configuration options to this new setting
        
        :param ciphers: List of SSH Ciphers enabled.
                Possible values:
                <ul>
                <li> "aes256_ctr"     ,
                <li> "aes192_ctr"     ,
                <li> "aes128_ctr"     ,
                <li> "aes256_cbc"     ,
                <li> "aes192_cbc"     ,
                <li> "aes128_cbc"     ,
                <li> "3des_cbc"
                </ul>
        
        :param key_exchange_algorithms: List of SSH key exchange algorithms enabled.
                Possible values:
                <ul>
                <li> "diffie_hellman_group_exchange_sha256"    ,
                <li> "diffie_hellman_group_exchange_sha1"      ,
                <li> "diffie_hellman_group14_sha1"             ,
                <li> "diffie_hellman_group1_sha1"
                </ul>
        """
        return self.request( "security-ssh-reset", {
            'ciphers': [ ciphers, 'ciphers', [ basestring, 'ciphers' ], True ],
            'key_exchange_algorithms': [ key_exchange_algorithms, 'key-exchange-algorithms', [ basestring, 'kex-algorithms' ], True ],
        }, {
        } )
    
    def security_login_get(self, vserver, application, user_name, authentication_method, desired_attributes=None):
        """
        Get the attributes of a user account.
        
        :param vserver: Name of the Vserver.
        
        :param application: Name of the application. Possible
                values: 'console', 'http', 'ontapi', 'rsh',
                'snmp', 'sp', 'ssh', 'telnet'.
        
        :param user_name: Name of the user.
                When creating a SNMPv1 or SNMPv2 user with 'snmp' application and
                'community' authentication-method, the user name is the community
                string.
        
        :param authentication_method: Authentication method for the application.
                Possible values: 'community', 'password', 'publickey', 'domain',
                'nsswitch' and 'usm'.
                Not all authentication methods are valid for an application.
                Valid authentication methods for each application are:
                'password' for 'console' application.
                'password', 'domain', 'nsswitch', 'cert' for 'http' application.
                'password', 'domain', 'nsswitch', 'cert'  for 'ontapi'
                application.
                'community' for 'snmp' application (when creating SNMPv1 and
                SNMPv2 users).
                'usm' and 'community' for 'snmp' application (when creating
                SNMPv3 users).
                'password' for 'sp' application.
                'password' for 'rsh' application.
                'password' for 'telnet' application.
                'password', 'publickey', 'domain', 'nsswitch' for 'ssh'
                application.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-login-get", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'application': [ application, 'application', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'authentication_method': [ authentication_method, 'authentication-method', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginAccountInfo, 'None' ], False ],
        }, {
            'attributes': [ SecurityLoginAccountInfo, False ],
        } )
    
    def security_login_role_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of user role objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security login role object.
                All security login role objects matching this query up to
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
        return self.request( "security-login-role-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecurityLoginRoleInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityLoginRoleInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SecurityLoginRoleInfo, True ],
        } )
