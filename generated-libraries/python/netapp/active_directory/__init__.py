from netapp.connection import NaConnection
from active_directory_account_get_iter_key_td import ActiveDirectoryAccountGetIterKeyTd # 1 properties
from active_directory_account_config import ActiveDirectoryAccountConfig # 5 properties

class ActiveDirectoryConnection(NaConnection):
    
    def active_directory_account_modify(self, admin_username=None, force_account_overwrite=None, domain=None, admin_password=None):
        """
        Modify the Windows Active Directory domain. If a CIFS server
        already exists for the requested Vserver, cifs-server-modify API
        should be used to modify the Windows Active Directory domain.
        
        :param admin_username: Administrator username required for Active Directory account
                creation in the given domain.
        
        :param force_account_overwrite: If true and a machine account with the same name as specified in
                'account-name' exists in Active Directory, it will be overwritten
                and reused. The default value for this field is false.
        
        :param domain: Fully qualified domain name.
        
        :param admin_password: Administrator password required for Active Directory account
                creation in the given domain.
        """
        return self.request( "active-directory-account-modify", {
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'force_account_overwrite': [ force_account_overwrite, 'force-account-overwrite', [ bool, 'None' ], False ],
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def active_directory_account_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of active directory accounts
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                active-directory-account object.
                All active-directory-account objects matching this query up to
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
        return self.request( "active-directory-account-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ActiveDirectoryAccountConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ActiveDirectoryAccountConfig, 'None' ], False ],
        }, {
            'attributes-list': [ ActiveDirectoryAccountConfig, True ],
        } )
    
    def active_directory_account_create(self, domain, admin_username, account_name, admin_password, force_account_overwrite=None, organizational_unit=None):
        """
        Create an Active Directory account for the given Vserver. If a
        CIFS server already exists for the requested Vserver, then this
        command will fail. The existing CIFS server should be deleted
        before retrying again.
        
        :param domain: Fully qualified domain name.
        
        :param admin_username: Administrator username required for Active Directory account
                creation.
        
        :param account_name: Active Directory account NetBIOS name.
        
        :param admin_password: Administrator password required for Active Directory account
                creation.
        
        :param force_account_overwrite: If true and a machine account with the same name as specified in
                'account-name' exists in Active Directory, it will be overwritten
                and reused. The default value for this field is false.
        
        :param organizational_unit: Organizational unit under which the Active Directory account will
                be created.
        """
        return self.request( "active-directory-account-create", {
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'force_account_overwrite': [ force_account_overwrite, 'force-account-overwrite', [ bool, 'None' ], False ],
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'organizational_unit': [ organizational_unit, 'organizational-unit', [ basestring, 'None' ], False ],
            'account_name': [ account_name, 'account-name', [ basestring, 'netbios-name' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def active_directory_account_password_change(self):
        """
        Generate a new password for the machine account and change it in
        the Windows Active Directory domain.
        """
        return self.request( "active-directory-account-password-change", {
        }, {
        } )
    
    def active_directory_account_password_reset(self, admin_username, admin_password):
        """
        Reset the machine account password in the Windows Active
        Directory domain. This may be required if the password stored
        along with the machine account in the Windows Active Directory
        domain is changed or reset without the Vserver's knowledge. This
        operation requires the credentials for a user with permission to
        reset the password in the organizational unit (OU) that the
        machine account is a member of.
        
        :param admin_username: Administrator username required for Active Directory account
                password reset.
        
        :param admin_password: Administrator password required for Active Directory account
                password reset.
        """
        return self.request( "active-directory-account-password-reset", {
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def active_directory_account_delete(self, admin_username=None, admin_password=None):
        """
        Delete the Active Directory account. If a CIFS server already
        exists for the requested Vserver, cifs-server-delete API should
        be used to delete the machine account.
        
        :param admin_username: Administrator username required for Active Directory account
                deletion.
        
        :param admin_password: Administrator password required for Active Directory account
                deletion.
        """
        return self.request( "active-directory-account-delete", {
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
