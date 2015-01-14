from netapp.netapp_object import NetAppObject

class CifsOptions(NetAppObject):
    """
    The CIFS specific tunables that can be set on a Vserver.
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
    
    _file_system_sector_size = None
    @property
    def file_system_sector_size(self):
        """
        This optional parameter specifies the size of file system
        sector in bytes reported to SMB Clients.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "512"  - Reported file system sector size to SMB
        clients is 512 bytes,
        <li> "4096" - Reported file system sector size to SMB
        clients is 4096 bytes
        </ul>
        """
        return self._file_system_sector_size
    @file_system_sector_size.setter
    def file_system_sector_size(self, val):
        if val != None:
            self.validate('file_system_sector_size', val)
        self._file_system_sector_size = val
    
    _is_copy_offload_enabled = None
    @property
    def is_copy_offload_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        is capable of performing copy offload operation. The
        default value for this parameter is true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_copy_offload_enabled
    @is_copy_offload_enabled.setter
    def is_copy_offload_enabled(self, val):
        if val != None:
            self.validate('is_copy_offload_enabled', val)
        self._is_copy_offload_enabled = val
    
    _is_smb3_enabled = None
    @property
    def is_smb3_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        negotiates the SMB3 version of the CIFS protocol. The
        default value for this parameter is true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_smb3_enabled
    @is_smb3_enabled.setter
    def is_smb3_enabled(self, val):
        if val != None:
            self.validate('is_smb3_enabled', val)
        self._is_smb3_enabled = val
    
    _shadowcopy_dir_depth = None
    @property
    def shadowcopy_dir_depth(self):
        """
        This optional parameter specifies the maximum depth of
        directories to shadow copy.
        Attributes: optional-for-create, modifiable
        """
        return self._shadowcopy_dir_depth
    @shadowcopy_dir_depth.setter
    def shadowcopy_dir_depth(self, val):
        if val != None:
            self.validate('shadowcopy_dir_depth', val)
        self._shadowcopy_dir_depth = val
    
    _is_referral_enabled = None
    @property
    def is_referral_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        refers clients to more optimal data access paths (LIFs).
        The default value for this parameter is false.
        Attributes: optional-for-create, modifiable
        """
        return self._is_referral_enabled
    @is_referral_enabled.setter
    def is_referral_enabled(self, val):
        if val != None:
            self.validate('is_referral_enabled', val)
        self._is_referral_enabled = val
    
    _is_local_users_and_groups_enabled = None
    @property
    def is_local_users_and_groups_enabled(self):
        """
        This optional parameter specifies whether the CIFS local
        users and groups feature is enabled on the cluster.
        Attributes: optional-for-create, modifiable
        """
        return self._is_local_users_and_groups_enabled
    @is_local_users_and_groups_enabled.setter
    def is_local_users_and_groups_enabled(self, val):
        if val != None:
            self.validate('is_local_users_and_groups_enabled', val)
        self._is_local_users_and_groups_enabled = val
    
    _is_shadowcopy_enabled = None
    @property
    def is_shadowcopy_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        is capable of performing shadow copy operations.
        Attributes: optional-for-create, modifiable
        """
        return self._is_shadowcopy_enabled
    @is_shadowcopy_enabled.setter
    def is_shadowcopy_enabled(self, val):
        if val != None:
            self.validate('is_shadowcopy_enabled', val)
        self._is_shadowcopy_enabled = val
    
    _is_use_junctions_as_reparse_points_enabled = None
    @property
    def is_use_junctions_as_reparse_points_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        exposes junction points as reparse points to Windows
        clients.
        Attributes: optional-for-create, modifiable
        """
        return self._is_use_junctions_as_reparse_points_enabled
    @is_use_junctions_as_reparse_points_enabled.setter
    def is_use_junctions_as_reparse_points_enabled(self, val):
        if val != None:
            self.validate('is_use_junctions_as_reparse_points_enabled', val)
        self._is_use_junctions_as_reparse_points_enabled = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_trusted_domain_enum_search_enabled = None
    @property
    def is_trusted_domain_enum_search_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        is capable of performing enumeration of trusted domains
        and search to map a UNIX user to a Windows user.
        Attributes: optional-for-create, modifiable
        """
        return self._is_trusted_domain_enum_search_enabled
    @is_trusted_domain_enum_search_enabled.setter
    def is_trusted_domain_enum_search_enabled(self, val):
        if val != None:
            self.validate('is_trusted_domain_enum_search_enabled', val)
        self._is_trusted_domain_enum_search_enabled = val
    
    _is_exportpolicy_enabled = None
    @property
    def is_exportpolicy_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        uses export policies to control client access. The
        default value for this parameter is false.
        Attributes: optional-for-create, modifiable
        """
        return self._is_exportpolicy_enabled
    @is_exportpolicy_enabled.setter
    def is_exportpolicy_enabled(self, val):
        if val != None:
            self.validate('is_exportpolicy_enabled', val)
        self._is_exportpolicy_enabled = val
    
    _wins_servers = None
    @property
    def wins_servers(self):
        """
        List of Windows Internet Name Service (WINS) IP
        addresses. The Vserver will send NetBIOS name resolution
        requests to these addresses.
        Attributes: optional-for-create, modifiable
        """
        return self._wins_servers
    @wins_servers.setter
    def wins_servers(self, val):
        if val != None:
            self.validate('wins_servers', val)
        self._wins_servers = val
    
    _is_local_auth_enabled = None
    @property
    def is_local_auth_enabled(self):
        """
        This optional parameter specifies whether CIFS local
        users can authenticate.
        Attributes: optional-for-create, modifiable
        """
        return self._is_local_auth_enabled
    @is_local_auth_enabled.setter
    def is_local_auth_enabled(self, val):
        if val != None:
            self.validate('is_local_auth_enabled', val)
        self._is_local_auth_enabled = val
    
    _is_smb2_enabled = None
    @property
    def is_smb2_enabled(self):
        """
        This optional parameter specifies whether the CIFS server
        negotiates the SMB2 versions of the CIFS protocol. The
        default value for this parameter is true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_smb2_enabled
    @is_smb2_enabled.setter
    def is_smb2_enabled(self, val):
        if val != None:
            self.validate('is_smb2_enabled', val)
        self._is_smb2_enabled = val
    
    _max_mpx = None
    @property
    def max_mpx(self):
        """
        This option controls maximum simultaneous operations the
        CIFS server reports it can process per TCP connection.
        The default value for this option is 255.
        Attributes: optional-for-create, modifiable
        """
        return self._max_mpx
    @max_mpx.setter
    def max_mpx(self, val):
        if val != None:
            self.validate('max_mpx', val)
        self._max_mpx = val
    
    _read_grants_execute = None
    @property
    def read_grants_execute(self):
        """
        On a file with UNIX Style security effective on it, if
        the file has read permission on it, a CIFS user would be
        allowed to execute permissions if this option is
        enabled.
        Attributes: optional-for-create, modifiable
        """
        return self._read_grants_execute
    @read_grants_execute.setter
    def read_grants_execute(self, val):
        if val != None:
            self.validate('read_grants_execute', val)
        self._read_grants_execute = val
    
    _default_unix_group = None
    @property
    def default_unix_group(self):
        """
        The default UNIX group used if the identity of a CIFS
        group cannot be mapped using normal group mapping rules.
        Attributes: optional-for-create, modifiable
        """
        return self._default_unix_group
    @default_unix_group.setter
    def default_unix_group(self, val):
        if val != None:
            self.validate('default_unix_group', val)
        self._default_unix_group = val
    
    _default_unix_user = None
    @property
    def default_unix_user(self):
        """
        The default UNIX user used if the identity of a CIFS user
        cannot be mapped using normal user mapping rules.
        Attributes: optional-for-create, modifiable
        """
        return self._default_unix_user
    @default_unix_user.setter
    def default_unix_user(self, val):
        if val != None:
            self.validate('default_unix_user', val)
        self._default_unix_user = val
    
    @staticmethod
    def get_api_name():
          return "cifs-options"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'file-system-sector-size',
            'is-copy-offload-enabled',
            'is-smb3-enabled',
            'shadowcopy-dir-depth',
            'is-referral-enabled',
            'is-local-users-and-groups-enabled',
            'is-shadowcopy-enabled',
            'is-use-junctions-as-reparse-points-enabled',
            'vserver',
            'is-trusted-domain-enum-search-enabled',
            'is-exportpolicy-enabled',
            'wins-servers',
            'is-local-auth-enabled',
            'is-smb2-enabled',
            'max-mpx',
            'read-grants-execute',
            'default-unix-group',
            'default-unix-user',
        ]
    
    def describe_properties(self):
        return {
            'file_system_sector_size': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_copy_offload_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_smb3_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'shadowcopy_dir_depth': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_referral_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_local_users_and_groups_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_shadowcopy_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_use_junctions_as_reparse_points_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_trusted_domain_enum_search_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_exportpolicy_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'wins_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'is_local_auth_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_smb2_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_mpx': { 'class': int, 'is_list': False, 'required': 'optional' },
            'read_grants_execute': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'default_unix_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'default_unix_user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
