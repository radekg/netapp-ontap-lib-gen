from netapp.netapp_object import NetAppObject

class AvOnAccessPolicyInfo(NetAppObject):
    """
    on acces policy for antivirus
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
    
    _is_scan_enabled = None
    @property
    def is_scan_enabled(self):
        """
        This specifies whether an on-access scan is enabled on
        the virtual server or volume. Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._is_scan_enabled
    @is_scan_enabled.setter
    def is_scan_enabled(self, val):
        if val != None:
            self.validate('is_scan_enabled', val)
        self._is_scan_enabled = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Name of the on-access policy.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _is_cifs_execute_access_scan_enabled = None
    @property
    def is_cifs_execute_access_scan_enabled(self):
        """
        If true, only the files opened with execute access are
        scanned, otherwise all files will be scanned (CIFS only).
        Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._is_cifs_execute_access_scan_enabled
    @is_cifs_execute_access_scan_enabled.setter
    def is_cifs_execute_access_scan_enabled(self, val):
        if val != None:
            self.validate('is_cifs_execute_access_scan_enabled', val)
        self._is_cifs_execute_access_scan_enabled = val
    
    _is_row_volume_scan_enabled = None
    @property
    def is_row_volume_scan_enabled(self):
        """
        This specifies whether an on-access scan is enabled on a
        read-only volume. Default is false. Currently not
        supported.
        Attributes: optional-for-create, modifiable
        """
        return self._is_row_volume_scan_enabled
    @is_row_volume_scan_enabled.setter
    def is_row_volume_scan_enabled(self, val):
        if val != None:
            self.validate('is_row_volume_scan_enabled', val)
        self._is_row_volume_scan_enabled = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver which owns this on-access policy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _include_cifs_share = None
    @property
    def include_cifs_share(self):
        """
        This specifies whether the CIFS shares defined in the
        parameter cifs-share-list-pattern will be included in or
        excluded from the antivirus scan.  If true, then
        cifs-share-list-pattern is an inclusive match, else an
        exclusive match.  Default it true.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "include"   ,
        <li> "exclude"
        </ul>
        """
        return self._include_cifs_share
    @include_cifs_share.setter
    def include_cifs_share(self, val):
        if val != None:
            self.validate('include_cifs_share', val)
        self._include_cifs_share = val
    
    _cifs_share_list_pattern = None
    @property
    def cifs_share_list_pattern(self):
        """
        This specifies the regular expression that lists CIFS
        shares to be included in or excluded from an antivirus
        scan. Uses GNU-compatible regular expressions.
        Attributes: optional-for-create, modifiable
        """
        return self._cifs_share_list_pattern
    @cifs_share_list_pattern.setter
    def cifs_share_list_pattern(self, val):
        if val != None:
            self.validate('cifs_share_list_pattern', val)
        self._cifs_share_list_pattern = val
    
    _include_cifs_file = None
    @property
    def include_cifs_file(self):
        """
        This specifies whether the files defined in the parameter
        cifs-file-list-pattern will be included in or excluded
        from an antivirus scan. If true, then
        cifs-file-list-pattern is an inclusive match, else an
        exclusive match. Default is true.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "include"   ,
        <li> "exclude"
        </ul>
        """
        return self._include_cifs_file
    @include_cifs_file.setter
    def include_cifs_file(self, val):
        if val != None:
            self.validate('include_cifs_file', val)
        self._include_cifs_file = val
    
    _cifs_file_list_pattern = None
    @property
    def cifs_file_list_pattern(self):
        """
        This specifies the regular expression that lists files to
        be included in or excluded from an antivirus scan. Uses
        GNU-compatible regular expressions.
        Attributes: optional-for-create, modifiable
        """
        return self._cifs_file_list_pattern
    @cifs_file_list_pattern.setter
    def cifs_file_list_pattern(self, val):
        if val != None:
            self.validate('cifs_file_list_pattern', val)
        self._cifs_file_list_pattern = val
    
    _policy_owner = None
    @property
    def policy_owner(self):
        """
        Policy belongs to cluster admin or data-vserver. Possible
        values are Cluster Admin or Vserver Admin
        Attributes: non-creatable, non-modifiable
        """
        return self._policy_owner
    @policy_owner.setter
    def policy_owner(self, val):
        if val != None:
            self.validate('policy_owner', val)
        self._policy_owner = val
    
    _fileop_profile = None
    @property
    def fileop_profile(self):
        """
        This option enables you specify the file profile. This
        determines what scan action should be taken for each
        incoming file operations. Each of this options provide
        different level or priority of scanning for different
        file operations and some of them are very strict in
        scanning and will have performance impact for example
        multi-protocols-strict is very safe, does not allow any
        virus to be returned to the clients  but has a
        performance hit when a file is subject to multiple read
        or write sequences, each read of the sequence will launch
        a scan. multi-protocols-standard is  less safe, doesn't
        protect CIFS or NFSv4 in the case a virus is written to
        the file while it's open and has better performance for
        CIFS.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "cifs_nfs4_only"           ,
        <li> "nfs3_only"                ,
        <li> "multi_proto_standard"     ,
        <li> "multi_proto_strict"
        </ul>
        """
        return self._fileop_profile
    @fileop_profile.setter
    def fileop_profile(self, val):
        if val != None:
            self.validate('fileop_profile', val)
        self._fileop_profile = val
    
    _is_scan_mandatory = None
    @property
    def is_scan_mandatory(self):
        """
        This specifies if an access to a file is allowed in the
        event that the system has no antivirus scan servers
        available to perform the scan. Default is true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_scan_mandatory
    @is_scan_mandatory.setter
    def is_scan_mandatory(self, val):
        if val != None:
            self.validate('is_scan_mandatory', val)
        self._is_scan_mandatory = val
    
    _protocols = None
    @property
    def protocols(self):
        """
        This specifies a list of protocols supported for
        scanning. Default protocols are cifs and nfsv4.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "cifs" ,
        <li> "nfs3" ,
        <li> "nfs4"
        </ul>
        """
        return self._protocols
    @protocols.setter
    def protocols(self, val):
        if val != None:
            self.validate('protocols', val)
        self._protocols = val
    
    _is_nfs_execute_permission_scan_enabled = None
    @property
    def is_nfs_execute_permission_scan_enabled(self):
        """
        If true, only the files with execute permission are
        scanned, otherwise files with all permissions are scanned
        (NFS only).Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._is_nfs_execute_permission_scan_enabled
    @is_nfs_execute_permission_scan_enabled.setter
    def is_nfs_execute_permission_scan_enabled(self, val):
        if val != None:
            self.validate('is_nfs_execute_permission_scan_enabled', val)
        self._is_nfs_execute_permission_scan_enabled = val
    
    @staticmethod
    def get_api_name():
          return "av-on-access-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-scan-enabled',
            'policy-name',
            'is-cifs-execute-access-scan-enabled',
            'is-row-volume-scan-enabled',
            'vserver',
            'include-cifs-share',
            'cifs-share-list-pattern',
            'include-cifs-file',
            'cifs-file-list-pattern',
            'policy-owner',
            'fileop-profile',
            'is-scan-mandatory',
            'protocols',
            'is-nfs-execute-permission-scan-enabled',
        ]
    
    def describe_properties(self):
        return {
            'is_scan_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_cifs_execute_access_scan_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_row_volume_scan_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'include_cifs_share': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_share_list_pattern': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'include_cifs_file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_file_list_pattern': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fileop_profile': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_scan_mandatory': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'protocols': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'is_nfs_execute_permission_scan_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
