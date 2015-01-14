from netapp.netapp_object import NetAppObject

class ExportRuleInfo(NetAppObject):
    """
    Information about the Export rule configuration.
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
    
    _export_ntfs_unix_security_ops = None
    @property
    def export_ntfs_unix_security_ops(self):
        """
        Ignore/Fail unix security operations on NTFS volumes.
        Possible values are 'ignore', 'fail'. Default value is
        'fail'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "ignore"    ,
        <li> "fail"
        </ul>
        """
        return self._export_ntfs_unix_security_ops
    @export_ntfs_unix_security_ops.setter
    def export_ntfs_unix_security_ops(self, val):
        if val != None:
            self.validate('export_ntfs_unix_security_ops', val)
        self._export_ntfs_unix_security_ops = val
    
    _is_allow_set_uid_enabled = None
    @property
    def is_allow_set_uid_enabled(self):
        """
        If 'true', NFS server will honor SetUID bits in SETATTR
        operation. Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_allow_set_uid_enabled
    @is_allow_set_uid_enabled.setter
    def is_allow_set_uid_enabled(self, val):
        if val != None:
            self.validate('is_allow_set_uid_enabled', val)
        self._is_allow_set_uid_enabled = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        Client access protocol. Default value is 'any'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "any"       - Any,
        <li> "nfs2"      - NFS Version 2,
        <li> "nfs3"      - NFS Version 3,
        <li> "nfs"       - Any Version of NFS,
        <li> "cifs"      - CIFS,
        <li> "nfs4"      - NFS Version 4,
        <li> "flexcache" - Flexcache
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Vserver name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Export policy name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _export_chown_mode = None
    @property
    def export_chown_mode(self):
        """
        Change ownership mode. Possible values are 'restricted',
        'unrestricted'. Default value is 'restricted'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "restricted"     ,
        <li> "unrestricted"
        </ul>
        """
        return self._export_chown_mode
    @export_chown_mode.setter
    def export_chown_mode(self, val):
        if val != None:
            self.validate('export_chown_mode', val)
        self._export_chown_mode = val
    
    _rule_index = None
    @property
    def rule_index(self):
        """
        Export rule index.
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._rule_index
    @rule_index.setter
    def rule_index(self, val):
        if val != None:
            self.validate('rule_index', val)
        self._rule_index = val
    
    _rw_rule = None
    @property
    def rw_rule(self):
        """
        Rule for read-write access.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "any"       - Any,
        <li> "none"      - Anonymous Access Allowed If Security
        Type Not Already Listed,
        <li> "never"     - Never,
        <li> "krb5"      - Kerberos 5 Authentication,
        <li> "ntlm"      - CIFS NTLM,
        <li> "sys"       - NFS AUTH_SYS,
        <li> "spinauth"  - SpinAuth
        </ul>
        """
        return self._rw_rule
    @rw_rule.setter
    def rw_rule(self, val):
        if val != None:
            self.validate('rw_rule', val)
        self._rw_rule = val
    
    _super_user_security = None
    @property
    def super_user_security(self):
        """
        Security flavors for the superuser. Default value is
        'none'.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "any"       - Any,
        <li> "none"      - Anonymous Access Allowed If Security
        Type Not Already Listed,
        <li> "never"     - Never,
        <li> "krb5"      - Kerberos 5 Authentication,
        <li> "ntlm"      - CIFS NTLM,
        <li> "sys"       - NFS AUTH_SYS,
        <li> "spinauth"  - SpinAuth
        </ul>
        """
        return self._super_user_security
    @super_user_security.setter
    def super_user_security(self, val):
        if val != None:
            self.validate('super_user_security', val)
        self._super_user_security = val
    
    _client_match = None
    @property
    def client_match(self):
        """
        Client match specification for Export rule. The clients
        specified are enforced with this Export rule. The rule
        with the higher rule index value takes precedence.
        Attributes: required-for-create, modifiable
        """
        return self._client_match
    @client_match.setter
    def client_match(self, val):
        if val != None:
            self.validate('client_match', val)
        self._client_match = val
    
    _is_allow_dev_is_enabled = None
    @property
    def is_allow_dev_is_enabled(self):
        """
        If 'true', the NFS server will allow creation of devices.
        Default value is 'true'.
        Attributes: optional-for-create, modifiable
        """
        return self._is_allow_dev_is_enabled
    @is_allow_dev_is_enabled.setter
    def is_allow_dev_is_enabled(self, val):
        if val != None:
            self.validate('is_allow_dev_is_enabled', val)
        self._is_allow_dev_is_enabled = val
    
    _ro_rule = None
    @property
    def ro_rule(self):
        """
        Rule for read-only access.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "any"       - Any,
        <li> "none"      - Anonymous Access Allowed If Security
        Type Not Already Listed,
        <li> "never"     - Never,
        <li> "krb5"      - Kerberos 5 Authentication,
        <li> "ntlm"      - CIFS NTLM,
        <li> "sys"       - NFS AUTH_SYS,
        <li> "spinauth"  - SpinAuth
        </ul>
        """
        return self._ro_rule
    @ro_rule.setter
    def ro_rule(self, val):
        if val != None:
            self.validate('ro_rule', val)
        self._ro_rule = val
    
    _anonymous_user_id = None
    @property
    def anonymous_user_id(self):
        """
        User name or ID to which anonymous users are mapped.
        Default value is '65534'.
        Attributes: optional-for-create, modifiable
        """
        return self._anonymous_user_id
    @anonymous_user_id.setter
    def anonymous_user_id(self, val):
        if val != None:
            self.validate('anonymous_user_id', val)
        self._anonymous_user_id = val
    
    @staticmethod
    def get_api_name():
          return "export-rule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'export-ntfs-unix-security-ops',
            'is-allow-set-uid-enabled',
            'protocol',
            'vserver-name',
            'policy-name',
            'export-chown-mode',
            'rule-index',
            'rw-rule',
            'super-user-security',
            'client-match',
            'is-allow-dev-is-enabled',
            'ro-rule',
            'anonymous-user-id',
        ]
    
    def describe_properties(self):
        return {
            'export_ntfs_unix_security_ops': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_allow_set_uid_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'protocol': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'export_chown_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rule_index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'rw_rule': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'super_user_security': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'client_match': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_allow_dev_is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ro_rule': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'anonymous_user_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
