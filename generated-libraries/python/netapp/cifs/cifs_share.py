from netapp.netapp_object import NetAppObject

class CifsShare(NetAppObject):
    """
    CIFS share configuration.
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
        This string gives a description of the CIFS share. CIFS
        clients see this description when browsing the Vserver's
        CIFS shares.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _volume = None
    @property
    def volume(self):
        """
        The name of the volume where the root of the CIFS share
        resides.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _cifs_server = None
    @property
    def cifs_server(self):
        """
        The NetBIOS name of the CIFS server that owns this
        share.
        Attributes: non-creatable, non-modifiable
        """
        return self._cifs_server
    @cifs_server.setter
    def cifs_server(self, val):
        if val != None:
            self.validate('cifs_server', val)
        self._cifs_server = val
    
    _dir_umask = None
    @property
    def dir_umask(self):
        """
        The value of this field controls the file mode creation
        mask for the CIFS share in qtrees with UNIX or Mixed
        security styles. The mask restricts the initial
        permissions setting of a newly created directory. The
        input value is a numeric mode comprising of one to three
        octal digits (0-7), derived by adding up the bits with
        values 4, 2, and 1. The first digit selects permissions
        for the user who owns the file: read (4), write (2), and
        execute (1); the second selects permissions for other
        users in the file's group, with the same values; and the
        third for other users not in the file's group, with the
        same values.
        Attributes: optional-for-create, modifiable
        """
        return self._dir_umask
    @dir_umask.setter
    def dir_umask(self, val):
        if val != None:
            self.validate('dir_umask', val)
        self._dir_umask = val
    
    _share_name = None
    @property
    def share_name(self):
        """
        The name of the CIFS share. The CIFS share name is a
        UTF-8 string with the following characters being illegal:
        control characters from 0x00 to 0x1F, both inclusive,
        0x22 (double quotes) and the characters \/[]:|<>+=;,?"*
        Attributes: key, required-for-create, non-modifiable
        """
        return self._share_name
    @share_name.setter
    def share_name(self, val):
        if val != None:
            self.validate('share_name', val)
        self._share_name = val
    
    _acl = None
    @property
    def acl(self):
        """
        This string list gives the applicable Access Control list
        for the CIFS share. Each list entry is a '/' separated
        pair of the User or Group name and the effective
        permissions. The permission could be 'Full Control',
        Change', 'Read' or 'No access'. e.g.: If the group is
        'Everyone' and the effective permission for this group is
        'Change', the entry would be 'Everyone / Change'.
        Attributes: non-creatable, non-modifiable
        """
        return self._acl
    @acl.setter
    def acl(self, val):
        if val != None:
            self.validate('acl', val)
        self._acl = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _share_properties = None
    @property
    def share_properties(self):
        """
        The list of properties for this CIFS share.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "oplocks"        - This specifies that
        opportunistic locks (client-side caching) are enabled on
        this share.,
        <li> "browsable"      - This specifies that the share
        can be browsed by Windows clients.,
        <li> "showsnapshot"   - This specifies that Snapshots
        can be viewed and traversed by clients.,
        <li> "changenotify"   - This specifies that CIFS
        clients can request for change notifications for
        directories on this share.,
        <li> "homedirectory"  - This specifies that the share
        is added and enabled as part of the CIFS home directory
        feature. The configuration of this share should be done
        using CIFS home directory feature interface.,
        <li> "attributecache" - This specifies that connections
        through this share are caching attributes for a short
        time to improve performance.
        <li> "branchcache" - This specifies that clients
        connecting to this share can make requests using
        BranchCache technology that allows them to cache the
        content in an attempt to reduce WAN utilization from a
        remote office.
        <li> "continuously_available" - This specifies that
        clients connecting to this share can open files in a
        persistent manner. Files opened this way are protected
        from disruptive events, such as failover and giveback.
        <li> "shadowcopy" - This specifies that the share is
        pointing to a shadow copy. This attribute cannot be added
        nor removed from a share.
        <li> "access_based_enumeration" - This specifies that Access
        Based Enumeration is enabled on this share. ABE-filtered shared
        folders are visible to a user based on that individual user's
        access rights, preventing the display of folders or other shared
        resources that the user does not have rights to access.
        </ul>
        """
        return self._share_properties
    @share_properties.setter
    def share_properties(self, val):
        if val != None:
            self.validate('share_properties', val)
        self._share_properties = val
    
    _symlink_properties = None
    @property
    def symlink_properties(self):
        """
        This flag controls whether the symlinks under this shared
        directory are hidden (option 'hide'), accessible (option
        'enable') or are accessible as read-only (option
        'read-only' along with option 'enable').
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "enable"    ,
        <li> "hide"      ,
        <li> "read_only"
        </ul>
        """
        return self._symlink_properties
    @symlink_properties.setter
    def symlink_properties(self, val):
        if val != None:
            self.validate('symlink_properties', val)
        self._symlink_properties = val
    
    _path = None
    @property
    def path(self):
        """
        The file system path that is shared through this CIFS
        share. The path is the full, user visible path relative
        to the vserver root, and it might be crossing junction
        mount points. The path is in UTF8 and uses forward slash
        as directory separator.
        Attributes: required-for-create, modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _offline_files_mode = None
    @property
    def offline_files_mode(self):
        """
        Mode of the offline file for the CIFS share.
        The default value is manual.
        Possible values:
        <ul>
        <li> "none"      - Clients are not permitted to cache
        files for offline access.,
        <li> "manual"    - Clients may cache files that are
        explicitly selected by the user for offline use.,
        <li> "documents" - Clients may automatically cache
        files that are used by the user for offline access.,
        <li> "programs"  - Clients may automatically cache
        files that are used by the user for offline access and
        may use those files in an offline mode even if the share
        is available.
        </ul>
        """
        return self._offline_files_mode
    @offline_files_mode.setter
    def offline_files_mode(self, val):
        if val != None:
            self.validate('offline_files_mode', val)
        self._offline_files_mode = val
    
    _attribute_cache_ttl = None
    @property
    def attribute_cache_ttl(self):
        """
        The lifetime of an entry in the file attribute cache, in
        seconds. This value is used if the share has the
        'attributecache' property set, which improves the
        performance of certain metadata operations in common
        workloads. The default is 10 seconds. Raising this value
        may improve performance, but the likelihood that stale
        metadata will be served increases as well. The value of
        this field must be in the range of 1 to 86400.
        Attributes: optional-for-create, modifiable
        """
        return self._attribute_cache_ttl
    @attribute_cache_ttl.setter
    def attribute_cache_ttl(self, val):
        if val != None:
            self.validate('attribute_cache_ttl', val)
        self._attribute_cache_ttl = val
    
    _file_umask = None
    @property
    def file_umask(self):
        """
        The value of this field controls the file mode creation
        mask for the CIFS share in qtrees with UNIX or Mixed
        security styles. The mask restricts the initial
        permissions setting of a newly created file. The input
        value is a numeric mode comprising of one to three octal
        digits (0-7), derived by adding up the bits with values
        4, 2, and 1. The first digit selects permissions for the
        user who owns the file: read (4), write (2), and execute
        (1); the second selects permissions for other users in
        the file's group, with the same values; and the third for
        other users not in the file's group, with the same
        values.
        Attributes: optional-for-create, modifiable
        """
        return self._file_umask
    @file_umask.setter
    def file_umask(self, val):
        if val != None:
            self.validate('file_umask', val)
        self._file_umask = val
    
    _vscan_fileop_profile = None
    @property
    def vscan_fileop_profile(self):
        """
        Profile-set of file-ops to which Vscan On-Access scanning
        is applicable. The default value is standard.
        Possible values:
        <ul>
        <li> "no_scan"     - Virus scans are never triggered for
        accesses to this share,
        <li> "standard"    - Virus scans can be triggered by open,
        close, and rename operations,
        <li> "strict"      - Virus scans can be triggered by open,
        read, close, and rename operations,
        <li> "writes_only" - Virus scans can be triggered only when
        a file that has been modified is closed.
        </ul>
        """
        return self._vscan_fileop_profile
    @vscan_fileop_profile.setter
    def vscan_fileop_profile(self, val):
        if val != None:
            self.validate('vscan_fileop_profile', val)
        self._vscan_fileop_profile = val
    
    @staticmethod
    def get_api_name():
          return "cifs-share"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'volume',
            'cifs-server',
            'dir-umask',
            'share-name',
            'acl',
            'vserver',
            'share-properties',
            'symlink-properties',
            'path',
            'offline-files-mode',
            'attribute-cache-ttl',
            'file-umask',
            'vscan-fileop-profile',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dir_umask': { 'class': int, 'is_list': False, 'required': 'optional' },
            'share_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'acl': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'share_properties': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'symlink_properties': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'offline_files_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'attribute_cache_ttl': { 'class': int, 'is_list': False, 'required': 'optional' },
            'file_umask': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vscan_fileop_profile': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
