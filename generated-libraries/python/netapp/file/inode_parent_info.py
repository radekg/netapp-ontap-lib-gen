from netapp.netapp_object import NetAppObject

class InodeParentInfo(NetAppObject):
    """
    Inode's path and parent information.
    """
    
    _inode_name = None
    @property
    def inode_name(self):
        """
        Name of inode in parent directory.
        """
        return self._inode_name
    @inode_name.setter
    def inode_name(self, val):
        if val != None:
            self.validate('inode_name', val)
        self._inode_name = val
    
    _inode_parent_inode_number = None
    @property
    def inode_parent_inode_number(self):
        """
        Inode number of the parent directory.
        """
        return self._inode_parent_inode_number
    @inode_parent_inode_number.setter
    def inode_parent_inode_number(self, val):
        if val != None:
            self.validate('inode_parent_inode_number', val)
        self._inode_parent_inode_number = val
    
    _inode_parent_cookie = None
    @property
    def inode_parent_cookie(self):
        """
        The opaque readdir cookie to determine the index of the inode
        in the parent directory tree.  Note that this value is used
        as a testing hook, we do not plan to support its semantics
        and those semantics might change over time.
        """
        return self._inode_parent_cookie
    @inode_parent_cookie.setter
    def inode_parent_cookie(self, val):
        if val != None:
            self.validate('inode_parent_cookie', val)
        self._inode_parent_cookie = val
    
    _inode_path = None
    @property
    def inode_path(self):
        """
        Full path to inode
        """
        return self._inode_path
    @inode_path.setter
    def inode_path(self, val):
        if val != None:
            self.validate('inode_path', val)
        self._inode_path = val
    
    @staticmethod
    def get_api_name():
          return "inode-parent-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'inode-name',
            'inode-parent-inode-number',
            'inode-parent-cookie',
            'inode-path',
        ]
    
    def describe_properties(self):
        return {
            'inode_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'inode_parent_inode_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inode_parent_cookie': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inode_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
