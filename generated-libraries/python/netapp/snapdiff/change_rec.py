from netapp.netapp_object import NetAppObject

class ChangeRec(NetAppObject):
    """
    Information about a single inode change.
    """
    
    _size = None
    @property
    def size(self):
        """
        File byte count.
        Range : [0..2^64-1]
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    _group = None
    @property
    def group(self):
        """
        The inode owner's group id.
        range: [0..2^31-1]
        """
        return self._group
    @group.setter
    def group(self, val):
        if val != None:
            self.validate('group', val)
        self._group = val
    
    _ctime = None
    @property
    def ctime(self):
        """
        Last changed time of the file.  The value is in seconds
        since January 1, 1970.
        Range : [0..2^31-1]
        """
        return self._ctime
    @ctime.setter
    def ctime(self, val):
        if val != None:
            self.validate('ctime', val)
        self._ctime = val
    
    _links = None
    @property
    def links(self):
        """
        Inode link reference count.
        range: [0..2^31-1]
        """
        return self._links
    @links.setter
    def links(self, val):
        if val != None:
            self.validate('links', val)
        self._links = val
    
    _fattr = None
    @property
    def fattr(self):
        """
        The inode's unix permissions.
        It's similar to Unix style permission
        bits, the only difference being that it
        is in decimal instead of octal. It is expected
        from the caller to convert this to octal. In octal,
        0755 gives read/write/execute permissions
        to owner and read/execute to group and other
        users. It consists of 4  digits derived by
        adding up bits 4, 2 and 1.  Omitted digits are
        assumed to be zeros. First digit selects the set
        user ID(4), set group ID (2) and sticky (1)
        attributes. The second digit selects permission
        for the owner of the file: read (4),
        write (2) and execute (1); the third selects
        permissions for other users in the same group;
        the fourth for other users not in the group.
        range: [0..0xFFF]
        """
        return self._fattr
    @fattr.setter
    def fattr(self, val):
        if val != None:
            self.validate('fattr', val)
        self._fattr = val
    
    _filename = None
    @property
    def filename(self):
        """
        The pathname of the file the inode points to, relative
        to the root of the volume in the snapshot. The
        encoding of the pathname depends on the value of the
        "file-access-protocol" element in the "snapdiff-iter-start"
        API that was used to start the snapdiff session. If "nfs",
        the pathname is an octet stream encoded to make it appear
        as valid ASCII by using the following escaping mechanism.
        If the value of the octet is 9, 10 or 13 or between
        32 and 127, then it is encoded as such without any
        transformation, except for 92 (ASCII code for the '\'
        character) and 127 (ASCII code for 'DEL' character);
        otherwise it is transformed into 3 octets that contain
        the 3 ASCII characters "\XX" where XX, in uppercase, is
        the value of the octet in hexadecimal. If "cifs", the
        pathname is a Unicode string encoded in UTF-8. The UTF-8
        encoded bytes use the same escaping mechanism with the
        same set of escaped characters as "nfs", except that only
        the following code points above 127 are escaped - 0xD800 to
        0xDFFF, 0xFFFE and 0xFFFF.
        """
        return self._filename
    @filename.setter
    def filename(self, val):
        if val != None:
            self.validate('filename', val)
        self._filename = val
    
    _ftype = None
    @property
    def ftype(self):
        """
        Type of the file. It can be one of the following type:
        <table>
        <tr> <td>File Type    </td><td> Value</td></tr>
        <tr> <td>-------------</td><td>-------</td></tr>
        <tr> <td>Regular      </td><td>  01</td></tr>
        <tr> <td>Directory    </td><td>  02</td></tr>
        <tr> <td>Block device </td><td>  03</td></tr>
        <tr> <td>Char. device </td><td>  04</td></tr>
        <tr> <td>Symlink      </td><td>  05</td></tr>
        <tr> <td>Socket       </td><td>  06</td></tr>
        <tr> <td>FIFO         </td><td>  07</td></tr>
        </table>
        """
        return self._ftype
    @ftype.setter
    def ftype(self, val):
        if val != None:
            self.validate('ftype', val)
        self._ftype = val
    
    _change_type = None
    @property
    def change_type(self):
        """
        Indicates what type of change occurred to the inode.
        It can have one of the following values:
        <ul>
        <li> "file_creation"</li>
        <li> "file_deletion"</li>
        <li> "inode_creation"</li>
        <li> "inode_modification"</li>
        <li> "inode_deletion"</li>
        </ul>
        """
        return self._change_type
    @change_type.setter
    def change_type(self, val):
        if val != None:
            self.validate('change_type', val)
        self._change_type = val
    
    _mtime = None
    @property
    def mtime(self):
        """
        Last modification time of the file.  The value is in
        seconds since January 1, 1970.
        Range : [0..2^31-1]
        """
        return self._mtime
    @mtime.setter
    def mtime(self, val):
        if val != None:
            self.validate('mtime', val)
        self._mtime = val
    
    _owner = None
    @property
    def owner(self):
        """
        The inode owner's user id.
        range: [0..2^31-1]
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _atime = None
    @property
    def atime(self):
        """
        Last access time of the file.  The value is in seconds
        since January 1, 1970.
        Range : [0..2^31-1]
        """
        return self._atime
    @atime.setter
    def atime(self, val):
        if val != None:
            self.validate('atime', val)
        self._atime = val
    
    _inode = None
    @property
    def inode(self):
        """
        wafl inode number.
        range: [64..0xFFFFFFFF]
        """
        return self._inode
    @inode.setter
    def inode(self, val):
        if val != None:
            self.validate('inode', val)
        self._inode = val
    
    _crtime = None
    @property
    def crtime(self):
        """
        Creation time of the file.  The value is in seconds.
        since January 1, 1970.
        Range : [0..2^31-1]
        """
        return self._crtime
    @crtime.setter
    def crtime(self, val):
        if val != None:
            self.validate('crtime', val)
        self._crtime = val
    
    _dos_bits = None
    @property
    def dos_bits(self):
        """
        DOS bit settings for the inode.  The DOS bits are a logical
        OR of the following values:
        <ul>
        <li>0x00000001   DOS_ARCHIVE</li>
        <li>0x00000002   DOS_HIDDEN</li>
        <li>0x00000004   DOS_SYSATTR</li>
        <li>0x00000008   DOS_COMPRESSED</li>
        <li>0x00000010   DOS_NOT_CONTENT_INDEXED</li>
        <li>0x00000020   DOS_ENCRYPTED</li>
        <li>0x00000040   DOS_OFFLINE</li>
        <li>0x00000080   DOS_SPARSE</li>
        </ul>
        """
        return self._dos_bits
    @dos_bits.setter
    def dos_bits(self, val):
        if val != None:
            self.validate('dos_bits', val)
        self._dos_bits = val
    
    @staticmethod
    def get_api_name():
          return "change-rec"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'size',
            'group',
            'ctime',
            'links',
            'fattr',
            'filename',
            'ftype',
            'change-type',
            'mtime',
            'owner',
            'atime',
            'inode',
            'crtime',
            'dos-bits',
        ]
    
    def describe_properties(self):
        return {
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ctime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'links': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fattr': { 'class': int, 'is_list': False, 'required': 'optional' },
            'filename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ftype': { 'class': int, 'is_list': False, 'required': 'required' },
            'change_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mtime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': int, 'is_list': False, 'required': 'optional' },
            'atime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inode': { 'class': int, 'is_list': False, 'required': 'required' },
            'crtime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dos_bits': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
