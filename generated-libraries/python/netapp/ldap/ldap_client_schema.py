from netapp.netapp_object import NetAppObject

class LdapClientSchema(NetAppObject):
    """
    An LDAP Client Schema Definition. A schema definition is a way of
    defining what attribute names are to be used in LDAP queries to
    get information that the storage system needs for its operation.
    This will depend on the schema that the LDAP server supports. For
    example, to query for user account information, the LDAP query
    should ask for the 'posixAccount' class if the LDAP server is
    compatible with RFC-2307 and it should ask for 'User' class if
    the LDAP server is an Active Directory LDAP Server. The default
    LDAP configuration has two schemas defined namely 'RFC-2307' and
    'AD-SFU'. The 'RFC-2307' schema is the default schema that should
    be used to query servers that support RFC-2307. The 'AD-SFU'
    schema is the default schema that should be used to query Active
    Directory LDAP servers. These schemas are read-only and cannot be
    modified. The default schemas will work with most common LDAP
    configurations. If it is required to support other schema
    configurations, 499       :existing schemas can be copied using
    the 'ldap-client-schema-copy' API and modified using the
    'ldap-client-schema-modify' API to work for the new
    configuration.
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
    
    _comment = None
    @property
    def comment(self):
        """
        A comment that can be associated with the schema.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _uid_attribute = None
    @property
    def uid_attribute(self):
        """
        Name that represents the RFC 1274 userid attribute used
        by RFC 2307 as uid.
        Attributes: optional-for-create, modifiable
        """
        return self._uid_attribute
    @uid_attribute.setter
    def uid_attribute(self, val):
        if val != None:
            self.validate('uid_attribute', val)
        self._uid_attribute = val
    
    _posix_group_object_class = None
    @property
    def posix_group_object_class(self):
        """
        Name that represents the RFC 2307 posixGroup object
        class.
        Attributes: optional-for-create, modifiable
        """
        return self._posix_group_object_class
    @posix_group_object_class.setter
    def posix_group_object_class(self, val):
        if val != None:
            self.validate('posix_group_object_class', val)
        self._posix_group_object_class = val
    
    _is_owner = None
    @property
    def is_owner(self):
        """
        This indicates if the vserver owns the client schema.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_owner
    @is_owner.setter
    def is_owner(self, val):
        if val != None:
            self.validate('is_owner', val)
        self._is_owner = val
    
    _home_directory_attribute = None
    @property
    def home_directory_attribute(self):
        """
        Name that represents the RFC 2307 homeDirectory
        attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._home_directory_attribute
    @home_directory_attribute.setter
    def home_directory_attribute(self, val):
        if val != None:
            self.validate('home_directory_attribute', val)
        self._home_directory_attribute = val
    
    _member_uid_attribute = None
    @property
    def member_uid_attribute(self):
        """
        Name that represents the RFC 2307 memberUid attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._member_uid_attribute
    @member_uid_attribute.setter
    def member_uid_attribute(self, val):
        if val != None:
            self.validate('member_uid_attribute', val)
        self._member_uid_attribute = val
    
    _gid_number_attribute = None
    @property
    def gid_number_attribute(self):
        """
        Name that represents the RFC 2307 gidNumber attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._gid_number_attribute
    @gid_number_attribute.setter
    def gid_number_attribute(self, val):
        if val != None:
            self.validate('gid_number_attribute', val)
        self._gid_number_attribute = val
    
    _nis_netgroup_triple_attribute = None
    @property
    def nis_netgroup_triple_attribute(self):
        """
        Name that represents the RFC 2307 nisNetgroupTriple
        attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._nis_netgroup_triple_attribute
    @nis_netgroup_triple_attribute.setter
    def nis_netgroup_triple_attribute(self, val):
        if val != None:
            self.validate('nis_netgroup_triple_attribute', val)
        self._nis_netgroup_triple_attribute = val
    
    _gecos_attribute = None
    @property
    def gecos_attribute(self):
        """
        Name that represents the RFC 2307 gecos attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._gecos_attribute
    @gecos_attribute.setter
    def gecos_attribute(self, val):
        if val != None:
            self.validate('gecos_attribute', val)
        self._gecos_attribute = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _cn_group_attribute = None
    @property
    def cn_group_attribute(self):
        """
        Name that represents the RFC 2256 cn attribute used by
        RFC 2307 when working with groups.
        Attributes: optional-for-create, modifiable
        """
        return self._cn_group_attribute
    @cn_group_attribute.setter
    def cn_group_attribute(self, val):
        if val != None:
            self.validate('cn_group_attribute', val)
        self._cn_group_attribute = val
    
    _uid_number_attribute = None
    @property
    def uid_number_attribute(self):
        """
        Name that represents the RFC 2307 uidNumber attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._uid_number_attribute
    @uid_number_attribute.setter
    def uid_number_attribute(self, val):
        if val != None:
            self.validate('uid_number_attribute', val)
        self._uid_number_attribute = val
    
    _login_shell_attribute = None
    @property
    def login_shell_attribute(self):
        """
        Name that represents the RFC 2307 loginShell attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._login_shell_attribute
    @login_shell_attribute.setter
    def login_shell_attribute(self, val):
        if val != None:
            self.validate('login_shell_attribute', val)
        self._login_shell_attribute = val
    
    _user_password_attribute = None
    @property
    def user_password_attribute(self):
        """
        Name that represents the RFC 2256 userPassword attribute
        used by RFC 2307.
        Attributes: optional-for-create, modifiable
        """
        return self._user_password_attribute
    @user_password_attribute.setter
    def user_password_attribute(self, val):
        if val != None:
            self.validate('user_password_attribute', val)
        self._user_password_attribute = val
    
    _posix_account_object_class = None
    @property
    def posix_account_object_class(self):
        """
        Name that represents the RFC 2307 posixAccount object
        class.
        Attributes: optional-for-create, modifiable
        """
        return self._posix_account_object_class
    @posix_account_object_class.setter
    def posix_account_object_class(self, val):
        if val != None:
            self.validate('posix_account_object_class', val)
        self._posix_account_object_class = val
    
    _nis_netgroup_object_class = None
    @property
    def nis_netgroup_object_class(self):
        """
        Name that represents the RFC 2307 nisNetgroup object
        class.
        Attributes: optional-for-create, modifiable
        """
        return self._nis_netgroup_object_class
    @nis_netgroup_object_class.setter
    def nis_netgroup_object_class(self, val):
        if val != None:
            self.validate('nis_netgroup_object_class', val)
        self._nis_netgroup_object_class = val
    
    _cn_netgroup_attribute = None
    @property
    def cn_netgroup_attribute(self):
        """
        Name that represents the RFC 2256 cn attribute used by
        RFC 2307 when working with netgroups.
        Attributes: optional-for-create, modifiable
        """
        return self._cn_netgroup_attribute
    @cn_netgroup_attribute.setter
    def cn_netgroup_attribute(self, val):
        if val != None:
            self.validate('cn_netgroup_attribute', val)
        self._cn_netgroup_attribute = val
    
    _member_nis_netgroup_attribute = None
    @property
    def member_nis_netgroup_attribute(self):
        """
        Name that represents the RFC 2307 memberNisNetgroup
        attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._member_nis_netgroup_attribute
    @member_nis_netgroup_attribute.setter
    def member_nis_netgroup_attribute(self, val):
        if val != None:
            self.validate('member_nis_netgroup_attribute', val)
        self._member_nis_netgroup_attribute = val
    
    _windows_account_attribute = None
    @property
    def windows_account_attribute(self):
        """
        Attribute name to be used to get the windows account
        information for a unix user account.
        Attributes: optional-for-create, modifiable
        """
        return self._windows_account_attribute
    @windows_account_attribute.setter
    def windows_account_attribute(self, val):
        if val != None:
            self.validate('windows_account_attribute', val)
        self._windows_account_attribute = val
    
    _schema = None
    @property
    def schema(self):
        """
        A name for the schema.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._schema
    @schema.setter
    def schema(self, val):
        if val != None:
            self.validate('schema', val)
        self._schema = val
    
    @staticmethod
    def get_api_name():
          return "ldap-client-schema"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'uid-attribute',
            'posix-group-object-class',
            'is-owner',
            'home-directory-attribute',
            'member-uid-attribute',
            'gid-number-attribute',
            'nis-netgroup-triple-attribute',
            'gecos-attribute',
            'vserver',
            'cn-group-attribute',
            'uid-number-attribute',
            'login-shell-attribute',
            'user-password-attribute',
            'posix-account-object-class',
            'nis-netgroup-object-class',
            'cn-netgroup-attribute',
            'member-nis-netgroup-attribute',
            'windows-account-attribute',
            'schema',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uid_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'posix_group_object_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_owner': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'home_directory_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'member_uid_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gid_number_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nis_netgroup_triple_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gecos_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cn_group_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uid_number_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'login_shell_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_password_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'posix_account_object_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nis_netgroup_object_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cn_netgroup_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'member_nis_netgroup_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'windows_account_attribute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schema': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
