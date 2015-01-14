from netapp.netapp_object import NetAppObject

class CifsShareInfo(NetAppObject):
    """
    Information about a single cifs share.
    """
    
    _is_symlink_strict_security = None
    @property
    def is_symlink_strict_security(self):
        """
        If true or not specified, strict symlink security is enabled.
        If false, allows clients to follow symbolic links to
        destinations on this filer but outside of the current share.
        Its value is returned only if it is non-default value.
        Its default value is true.
        """
        return self._is_symlink_strict_security
    @is_symlink_strict_security.setter
    def is_symlink_strict_security(self, val):
        if val != None:
            self.validate('is_symlink_strict_security', val)
        self._is_symlink_strict_security = val
    
    _forcegroup = None
    @property
    def forcegroup(self):
        """
        name of the group to which files to be created
        in the share belong to.
        """
        return self._forcegroup
    @forcegroup.setter
    def forcegroup(self, val):
        if val != None:
            self.validate('forcegroup', val)
        self._forcegroup = val
    
    _description = None
    @property
    def description(self):
        """
        description of the share.
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _dir_umask = None
    @property
    def dir_umask(self):
        """
        File mode creation mask for a share in qtrees with Unix
        or mixed security styles. The mask restricts the initial
        permissions setting of a newly created directory.  This
        mask overrides one set with "umask".
        """
        return self._dir_umask
    @dir_umask.setter
    def dir_umask(self, val):
        if val != None:
            self.validate('dir_umask', val)
        self._dir_umask = val
    
    _is_namespace_caching_allowed = None
    @property
    def is_namespace_caching_allowed(self):
        """
        If true, namespace caching is enabled on the share.
        If false or not specified, namespace caching is disabled.
        If namespace caching is enabled on a share, clients are
        allowed to cache the directory enumeration results for
        better performance.
        """
        return self._is_namespace_caching_allowed
    @is_namespace_caching_allowed.setter
    def is_namespace_caching_allowed(self, val):
        if val != None:
            self.validate('is_namespace_caching_allowed', val)
        self._is_namespace_caching_allowed = val
    
    _share_name = None
    @property
    def share_name(self):
        """
        name of the cifs share.
        """
        return self._share_name
    @share_name.setter
    def share_name(self, val):
        if val != None:
            self.validate('share_name', val)
        self._share_name = val
    
    _is_vscanread = None
    @property
    def is_vscanread(self):
        """
        If true or not specified, virus scan is done when clients
        open files on this share for read access. Its value is
        returned only if it is non-default value. Its defalut
        value is true.
        """
        return self._is_vscanread
    @is_vscanread.setter
    def is_vscanread(self, val):
        if val != None:
            self.validate('is_vscanread', val)
        self._is_vscanread = val
    
    _umask = None
    @property
    def umask(self):
        """
        File mode creation mask for a share in qtrees with Unix
        or mixed security styles. The mask restricts the initial
        permissions setting of newly created files and directories.
        This field is ignored when both dir-umask and file-umask
        are present.
        """
        return self._umask
    @umask.setter
    def umask(self, val):
        if val != None:
            self.validate('umask', val)
        self._umask = val
    
    _is_browse = None
    @property
    def is_browse(self):
        """
        if true, this share can be browsed. Its values is returned
        only if it is non-default value. Its default value is true.
        """
        return self._is_browse
    @is_browse.setter
    def is_browse(self, val):
        if val != None:
            self.validate('is_browse', val)
        self._is_browse = val
    
    _is_vscan = None
    @property
    def is_vscan(self):
        """
        If true or not specified, virus scan is done when clients
        open files on this share. Its value is returned only if it
        is non-default value. Its default value is true.
        """
        return self._is_vscan
    @is_vscan.setter
    def is_vscan(self, val):
        if val != None:
            self.validate('is_vscan', val)
        self._is_vscan = val
    
    _mount_point = None
    @property
    def mount_point(self):
        """
        mount point of the share.
        """
        return self._mount_point
    @mount_point.setter
    def mount_point(self, val):
        if val != None:
            self.validate('mount_point', val)
        self._mount_point = val
    
    _caching = None
    @property
    def caching(self):
        """
        String specifying the type of caching: "no_caching",
        "auto_document_caching", "auto_program_caching" and
        "manual_caching".
        """
        return self._caching
    @caching.setter
    def caching(self, val):
        if val != None:
            self.validate('caching', val)
        self._caching = val
    
    _maxusers = None
    @property
    def maxusers(self):
        """
        max no. of simultaneous connections to the share.
        """
        return self._maxusers
    @maxusers.setter
    def maxusers(self, val):
        if val != None:
            self.validate('maxusers', val)
        self._maxusers = val
    
    _is_widelink = None
    @property
    def is_widelink(self):
        """
        If true, allows clients to follow absolute symbolic
        links outside of this share, subject to NT security.
        Its value is returned only if it is non-default value.
        Its default value is false.
        """
        return self._is_widelink
    @is_widelink.setter
    def is_widelink(self, val):
        if val != None:
            self.validate('is_widelink', val)
        self._is_widelink = val
    
    _is_vol_offline = None
    @property
    def is_vol_offline(self):
        """
        If true, volume is offline and the shares are
        not available. Its value is returned only if it
        is non-default value. Its default value is false.
        """
        return self._is_vol_offline
    @is_vol_offline.setter
    def is_vol_offline(self, val):
        if val != None:
            self.validate('is_vol_offline', val)
        self._is_vol_offline = val
    
    _is_access_based_enum = None
    @property
    def is_access_based_enum(self):
        """
        If true Access Based Enumeration (ABE) is enabled,
        else it is disabled.  ABE filtered shared folders
        are visible to a user based on that individual
        user's access rights,  preventing the display
        of folders or other shared resources that the user
        does not have rights to access. Its value is returned
        only if it is non-default value. Its default value is
        false.
        """
        return self._is_access_based_enum
    @is_access_based_enum.setter
    def is_access_based_enum(self, val):
        if val != None:
            self.validate('is_access_based_enum', val)
        self._is_access_based_enum = val
    
    _file_umask = None
    @property
    def file_umask(self):
        """
        File mode creation mask for a share in qtrees with Unix
        or mixed security styles. The mask restricts the initial
        permissions setting of a newly created file.  This mask
        overrides one set with "umask".
        """
        return self._file_umask
    @file_umask.setter
    def file_umask(self, val):
        if val != None:
            self.validate('file_umask', val)
        self._file_umask = val
    
    @staticmethod
    def get_api_name():
          return "cifs-share-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-symlink-strict-security',
            'forcegroup',
            'description',
            'dir-umask',
            'is-namespace-caching-allowed',
            'share-name',
            'is-vscanread',
            'umask',
            'is-browse',
            'is-vscan',
            'mount-point',
            'caching',
            'maxusers',
            'is-widelink',
            'is-vol-offline',
            'is-access-based-enum',
            'file-umask',
        ]
    
    def describe_properties(self):
        return {
            'is_symlink_strict_security': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'forcegroup': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dir_umask': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_namespace_caching_allowed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'share_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_vscanread': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'umask': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_browse': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_vscan': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'mount_point': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'caching': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'maxusers': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_widelink': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_vol_offline': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_access_based_enum': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'file_umask': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
