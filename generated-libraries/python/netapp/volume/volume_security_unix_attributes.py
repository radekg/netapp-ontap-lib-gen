from netapp.netapp_object import NetAppObject

class VolumeSecurityUnixAttributes(NetAppObject):
    """
    The Unix-oriented security settings associated with this
    volume.
    """
    
    _user_id = None
    @property
    def user_id(self):
        """
        The UNIX user ID for the volume. The default value is 0
        ('root').
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._user_id
    @user_id.setter
    def user_id(self, val):
        if val != None:
            self.validate('user_id', val)
        self._user_id = val
    
    _group_id = None
    @property
    def group_id(self):
        """
        The UNIX group ID for the volume.  The default value is 0
        ('root').
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._group_id
    @group_id.setter
    def group_id(self, val):
        if val != None:
            self.validate('group_id', val)
        self._group_id = val
    
    _permissions = None
    @property
    def permissions(self):
        """
        Unix permission bits in octal string format.
        <p>
        It's similar to Unix style permission bits:
        <p>
        In Data ONTAP 7-mode, the default setting of '0755' gives
        read/write/execute permissions to owner and read/execute
        to group and other users.
        <p>
        In Data ONTAP Cluster-Mode, for security style 'mixed' or
        'unix', the default setting of '0755' gives
        read/write/execute permissions to owner and read/execute
        permissions to group and other users. For security style
        'ntfs', the default setting of '0000' gives no
        permissions to owner, group and other users.
        <p>
        It consists of 4 octal digits derived by adding up bits
        4, 2 and 1. Omitted digits are assumed to be zeros. First
        digit selects the set user ID(4), set group ID (2) and
        sticky (1) attributes. The second digit selects
        permission for the owner of the file: read (4), write (2)
        and execute (1); the third selects permissions for other
        users in the same group; the fourth for other users not
        in the group.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._permissions
    @permissions.setter
    def permissions(self, val):
        if val != None:
            self.validate('permissions', val)
        self._permissions = val
    
    @staticmethod
    def get_api_name():
          return "volume-security-unix-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-id',
            'group-id',
            'permissions',
        ]
    
    def describe_properties(self):
        return {
            'user_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'permissions': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
