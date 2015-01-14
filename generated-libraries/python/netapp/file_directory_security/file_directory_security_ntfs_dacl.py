from netapp.netapp_object import NetAppObject

class FileDirectorySecurityNtfsDacl(NetAppObject):
    """
    fsecurity SACL configuration
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
    
    _advanced_rights = None
    @property
    def advanced_rights(self):
        """
        Specifies DACL ACE's Advanced access rights. Mutually
        exclusive with rights and rights-raw fields.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "read_data"      ,
        <li> "write_data"     ,
        <li> "append_data"    ,
        <li> "read_ea"        ,
        <li> "write_ea"       ,
        <li> "execute_file"   ,
        <li> "delete_child"   ,
        <li> "read_attr"      ,
        <li> "write_attr"     ,
        <li> "delete"         ,
        <li> "read_perm"      ,
        <li> "write_perm"     ,
        <li> "write_owner"    ,
        <li> "full_control"
        </ul>
        """
        return self._advanced_rights
    @advanced_rights.setter
    def advanced_rights(self, val):
        if val != None:
            self.validate('advanced_rights', val)
        self._advanced_rights = val
    
    _account = None
    @property
    def account(self):
        """
        Specifies DACL ACE's SID or domain account name of NTFS
        security descriptor.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._account
    @account.setter
    def account(self, val):
        if val != None:
            self.validate('account', val)
        self._account = val
    
    _readable_access_rights = None
    @property
    def readable_access_rights(self):
        """
        Specifies the current access rights. The access rights
        must be set to one among
        rights,advanced-rights,rights-raw.
        Attributes: non-creatable, non-modifiable
        """
        return self._readable_access_rights
    @readable_access_rights.setter
    def readable_access_rights(self, val):
        if val != None:
            self.validate('readable_access_rights', val)
        self._readable_access_rights = val
    
    _rights_raw = None
    @property
    def rights_raw(self):
        """
        Specifies DACL ACE's access rights in raw. This field is
        similar to advanced-rights fields. 'advanced-rights'
        specifies the value in enum but rights-raw specifies the
        access rights in integer format. Mutually exclusive with
        rights and advanced-rights fields.
        Attributes: optional-for-create, modifiable
        """
        return self._rights_raw
    @rights_raw.setter
    def rights_raw(self, val):
        if val != None:
            self.validate('rights_raw', val)
        self._rights_raw = val
    
    _rights = None
    @property
    def rights(self):
        """
        Specifies DACL ACE's access rights. Mutually exclusive
        with advanced-rights and rights-raw fields.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "no_access"           ,
        <li> "full_control"        ,
        <li> "modify"              ,
        <li> "read_and_execute"    ,
        <li> "read"                ,
        <li> "write"
        </ul>
        """
        return self._rights
    @rights.setter
    def rights(self, val):
        if val != None:
            self.validate('rights', val)
        self._rights = val
    
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
    
    _ntfs_sd = None
    @property
    def ntfs_sd(self):
        """
        Specifies NTFS security descriptor identifier.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._ntfs_sd
    @ntfs_sd.setter
    def ntfs_sd(self, val):
        if val != None:
            self.validate('ntfs_sd', val)
        self._ntfs_sd = val
    
    _apply_to = None
    @property
    def apply_to(self):
        """
        Specifies this ACE has to be applied on.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "this_folder"    ,
        <li> "sub_folders"    ,
        <li> "files"
        </ul>
        """
        return self._apply_to
    @apply_to.setter
    def apply_to(self, val):
        if val != None:
            self.validate('apply_to', val)
        self._apply_to = val
    
    _access_type = None
    @property
    def access_type(self):
        """
        Specifies DACL ACE's access type.
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "deny"      ,
        <li> "allow"
        </ul>
        """
        return self._access_type
    @access_type.setter
    def access_type(self, val):
        if val != None:
            self.validate('access_type', val)
        self._access_type = val
    
    @staticmethod
    def get_api_name():
          return "file-directory-security-ntfs-dacl"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'advanced-rights',
            'account',
            'readable-access-rights',
            'rights-raw',
            'rights',
            'vserver',
            'ntfs-sd',
            'apply-to',
            'access-type',
        ]
    
    def describe_properties(self):
        return {
            'advanced_rights': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'account': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'readable_access_rights': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rights_raw': { 'class': int, 'is_list': False, 'required': 'optional' },
            'rights': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ntfs_sd': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'apply_to': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'access_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
