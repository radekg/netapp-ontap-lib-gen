from netapp.netapp_object import NetAppObject

class FileDirectorySecurityNtfs(NetAppObject):
    """
    NTFS security descriptor management
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
    
    _owner = None
    @property
    def owner(self):
        """
        Specifies owner's SID or domain account name of NTFS
        security descriptor.
        Attributes: optional-for-create, modifiable
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
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
    
    _group = None
    @property
    def group(self):
        """
        Specifies group's SID or domain account name of NTFS
        security descriptor.
        Attributes: optional-for-create, modifiable
        """
        return self._group
    @group.setter
    def group(self, val):
        if val != None:
            self.validate('group', val)
        self._group = val
    
    _control_flags_raw = None
    @property
    def control_flags_raw(self):
        """
        Specifies the security descriptor control flags in hexa
        decimal. The following are the bit fields of control
        flags.
        <br>1... .... .... .... = Self Relative
        <br>.0.. .... .... .... = RM Control Valid
        <br>..0. .... .... .... = SACL Protected
        <br>...0 .... .... .... = DACL Protected
        <br>.... 0... .... .... = SACL Inherited
        <br>.... .0.. .... .... = DACL Inherited
        <br>.... ..0. .... .... = SACL Inherit Required
        <br>.... ...0 .... .... = DACL Inherit Required
        <br>.... .... ..0. .... = SACL Defaulted
        <br>.... .... ...0 .... = SACL Present
        <br>.... .... .... 0... = DACL Defaulted
        <br>.... .... .... .1.. = DACL Present
        <br>.... .... .... ..0. = Group Defaulted
        <br>.... .... .... ...0 = Owner Defaulted
        <br>
        <br>At present only the following flags are honored.
        Others are ignored.
        <br>..0. .... .... .... = SACL Protected
        <br>...0 .... .... .... = DACL Protected
        <br>.... .... ..0. .... = SACL Defaulted
        <br>.... .... .... 0... = DACL Defaulted
        <br>.... .... .... ..0. = Group Defaulted
        <br>.... .... .... ...0 = Owner Defaulted
        Attributes: optional-for-create, modifiable
        """
        return self._control_flags_raw
    @control_flags_raw.setter
    def control_flags_raw(self, val):
        if val != None:
            self.validate('control_flags_raw', val)
        self._control_flags_raw = val
    
    @staticmethod
    def get_api_name():
          return "file-directory-security-ntfs"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'owner',
            'ntfs-sd',
            'group',
            'control-flags-raw',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ntfs_sd': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'control_flags_raw': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
