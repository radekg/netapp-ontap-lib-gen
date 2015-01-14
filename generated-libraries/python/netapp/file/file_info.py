from netapp.netapp_object import NetAppObject

class FileInfo(NetAppObject):
    """
    Information about a single file.
    """
    
    _hard_links_count = None
    @property
    def hard_links_count(self):
        """
        The number of hard links to the file.
        """
        return self._hard_links_count
    @hard_links_count.setter
    def hard_links_count(self, val):
        if val != None:
            self.validate('hard_links_count', val)
        self._hard_links_count = val
    
    _changed_timestamp = None
    @property
    def changed_timestamp(self):
        """
        Last changed time of the file.  The value is in seconds
        since January 1, 1970.
        """
        return self._changed_timestamp
    @changed_timestamp.setter
    def changed_timestamp(self, val):
        if val != None:
            self.validate('changed_timestamp', val)
        self._changed_timestamp = val
    
    _accessed_timestamp = None
    @property
    def accessed_timestamp(self):
        """
        Last asscess time of the file.  The value is in seconds
        since January 1, 1970.
        """
        return self._accessed_timestamp
    @accessed_timestamp.setter
    def accessed_timestamp(self, val):
        if val != None:
            self.validate('accessed_timestamp', val)
        self._accessed_timestamp = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the file.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _creation_timestamp = None
    @property
    def creation_timestamp(self):
        """
        Creation time of the file.  The value is in seconds
        since January 1, 1970.
        """
        return self._creation_timestamp
    @creation_timestamp.setter
    def creation_timestamp(self, val):
        if val != None:
            self.validate('creation_timestamp', val)
        self._creation_timestamp = val
    
    _acl_type = None
    @property
    def acl_type(self):
        """
        The type of access control list (acl) on the file.
        Possible values are: "no_acl", "nt_acl", "nfs_acl",
        and goddess forbid, "unknown".
        """
        return self._acl_type
    @acl_type.setter
    def acl_type(self, val):
        if val != None:
            self.validate('acl_type', val)
        self._acl_type = val
    
    _file_size = None
    @property
    def file_size(self):
        """
        The size of the file in bytes.
        """
        return self._file_size
    @file_size.setter
    def file_size(self, val):
        if val != None:
            self.validate('file_size', val)
        self._file_size = val
    
    _is_junction = None
    @property
    def is_junction(self):
        """
        Returns true if the directory is a junction.
        """
        return self._is_junction
    @is_junction.setter
    def is_junction(self, val):
        if val != None:
            self.validate('is_junction', val)
        self._is_junction = val
    
    _is_empty = None
    @property
    def is_empty(self):
        """
        This element tells whether directory is empty or not.
        Directory is considered	empty if it only contains
        entries for "." and "..".
        This element is present if file is directory.
        In some special error cases like volume goes
        offline in between or directory is moved in the
        middle of getting this info, this field might not get set.
        """
        return self._is_empty
    @is_empty.setter
    def is_empty(self, val):
        if val != None:
            self.validate('is_empty', val)
        self._is_empty = val
    
    _inode_gen_number = None
    @property
    def inode_gen_number(self):
        """
        Inode generation number
        """
        return self._inode_gen_number
    @inode_gen_number.setter
    def inode_gen_number(self, val):
        if val != None:
            self.validate('inode_gen_number', val)
        self._inode_gen_number = val
    
    _perm = None
    @property
    def perm(self):
        """
        File permission bits.
        It's similar to Unix style permission bits: 0755 gives
        read/write/execute permissions to owner and
        read/execute to group and other users. It consists of
        4 octal digits derived by adding up bits 4, 2 and 1.
        Omitted digits are assumed to be zeros. First digit
        selects the set user ID(4), set group ID (2) and
        sticky (1) attributes. The second digit selects
        permission for the owner of the file: read (4),
        write (2) and execute (1); the third selects
        permissions for other users in the same group;
        the fourth for other users not in the group.
        """
        return self._perm
    @perm.setter
    def perm(self, val):
        if val != None:
            self.validate('perm', val)
        self._perm = val
    
    _is_vm_aligned = None
    @property
    def is_vm_aligned(self):
        """
        Returns true if the file is vm-aligned.
        A vm-aligned file is a file which is padded with zero-filled
        data at the beginning so that it's actual data starts at a
        different offset instead of zero. This is done in VM environments
        so that reads/writes to this file are aligned to WAFL's 4k block
        boundary. The amount by which the start offset is adjusted depends
        on the vm-align setting of the hosting volume. Use the
        volume-list-info or the volume-get-iter API to get this information.
        """
        return self._is_vm_aligned
    @is_vm_aligned.setter
    def is_vm_aligned(self, val):
        if val != None:
            self.validate('is_vm_aligned', val)
        self._is_vm_aligned = val
    
    _inode_number = None
    @property
    def inode_number(self):
        """
        The file node number.
        """
        return self._inode_number
    @inode_number.setter
    def inode_number(self, val):
        if val != None:
            self.validate('inode_number', val)
        self._inode_number = val
    
    _modified_timestamp = None
    @property
    def modified_timestamp(self):
        """
        Last modification time of the file.  The value is in
        seconds since January 1, 1970.
        """
        return self._modified_timestamp
    @modified_timestamp.setter
    def modified_timestamp(self, val):
        if val != None:
            self.validate('modified_timestamp', val)
        self._modified_timestamp = val
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        The integer id of the owner of the file.
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _file_type = None
    @property
    def file_type(self):
        """
        Type of the file.  Possible values: file, directory,
        blockdev, chardev, symlink, socket, fifo, stream, lun.
        """
        return self._file_type
    @file_type.setter
    def file_type(self, val):
        if val != None:
            self.validate('file_type', val)
        self._file_type = val
    
    _bytes_used = None
    @property
    def bytes_used(self):
        """
        returns the number of bytes actually used on disk by this file
        """
        return self._bytes_used
    @bytes_used.setter
    def bytes_used(self, val):
        if val != None:
            self.validate('bytes_used', val)
        self._bytes_used = val
    
    _dsid = None
    @property
    def dsid(self):
        """
        Data Set ID
        """
        return self._dsid
    @dsid.setter
    def dsid(self, val):
        if val != None:
            self.validate('dsid', val)
        self._dsid = val
    
    _msid = None
    @property
    def msid(self):
        """
        Mirror Set ID
        """
        return self._msid
    @msid.setter
    def msid(self, val):
        if val != None:
            self.validate('msid', val)
        self._msid = val
    
    _group_id = None
    @property
    def group_id(self):
        """
        The integer id of the group owner of the file.
        """
        return self._group_id
    @group_id.setter
    def group_id(self, val):
        if val != None:
            self.validate('group_id', val)
        self._group_id = val
    
    @staticmethod
    def get_api_name():
          return "file-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hard-links-count',
            'changed-timestamp',
            'accessed-timestamp',
            'name',
            'creation-timestamp',
            'acl-type',
            'file-size',
            'is-junction',
            'is-empty',
            'inode-gen-number',
            'perm',
            'is-vm-aligned',
            'inode-number',
            'modified-timestamp',
            'owner-id',
            'file-type',
            'bytes-used',
            'dsid',
            'msid',
            'group-id',
        ]
    
    def describe_properties(self):
        return {
            'hard_links_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'changed_timestamp': { 'class': int, 'is_list': False, 'required': 'required' },
            'accessed_timestamp': { 'class': int, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creation_timestamp': { 'class': int, 'is_list': False, 'required': 'required' },
            'acl_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'file_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_junction': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_empty': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'inode_gen_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'perm': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_vm_aligned': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'inode_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'modified_timestamp': { 'class': int, 'is_list': False, 'required': 'required' },
            'owner_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'file_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'bytes_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'msid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
