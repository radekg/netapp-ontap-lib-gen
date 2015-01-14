from netapp.netapp_object import NetAppObject

class AggrInodeAttributes(NetAppObject):
    """
    A structure returning inode-related information for
    a given aggregate's Active File System (AFS).
    """
    
    _inodefile_public_capacity = None
    @property
    def inodefile_public_capacity(self):
        """
        [not settable, online-only]
        Number of inodes that can currently be stored
        on disk for user-visible files.  This number
        will dynamically increase as more user-visible
        files are created.
        """
        return self._inodefile_public_capacity
    @inodefile_public_capacity.setter
    def inodefile_public_capacity(self, val):
        if val != None:
            self.validate('inodefile_public_capacity', val)
        self._inodefile_public_capacity = val
    
    _maxfiles_used = None
    @property
    def maxfiles_used(self):
        """
        [not settable, online-only]
        The number of user-visible files currently in use on
        the referenced file system.
        """
        return self._maxfiles_used
    @maxfiles_used.setter
    def maxfiles_used(self, val):
        if val != None:
            self.validate('maxfiles_used', val)
        self._maxfiles_used = val
    
    _inodefile_private_capacity = None
    @property
    def inodefile_private_capacity(self):
        """
        [not settable, online-only]
        Number of inodes that can currently be stored
        on disk for system (not user-visible) files.
        This number will dynamically increase as more
        system files are created.
        """
        return self._inodefile_private_capacity
    @inodefile_private_capacity.setter
    def inodefile_private_capacity(self, val):
        if val != None:
            self.validate('inodefile_private_capacity', val)
        self._inodefile_private_capacity = val
    
    _files_private_used = None
    @property
    def files_private_used(self):
        """
        [not settable, online-only]
        Number of system (not user-visible) files (inodes)
        used.  If the referenced file system is restricted
        or offline, a value of 0 is returned.
        """
        return self._files_private_used
    @files_private_used.setter
    def files_private_used(self, val):
        if val != None:
            self.validate('files_private_used', val)
        self._files_private_used = val
    
    _maxfiles_available = None
    @property
    def maxfiles_available(self):
        """
        [not settable, always]
        The count of the maximum number of user-visible files
        currently allowable on the referenced file system.
        """
        return self._maxfiles_available
    @maxfiles_available.setter
    def maxfiles_available(self, val):
        if val != None:
            self.validate('maxfiles_available', val)
        self._maxfiles_available = val
    
    _maxfiles_possible = None
    @property
    def maxfiles_possible(self):
        """
        [not settable, always]
        The largest value to which the maxfiles-available
        parameter can be increased by reconfiguration,
        on the referenced file system.
        """
        return self._maxfiles_possible
    @maxfiles_possible.setter
    def maxfiles_possible(self, val):
        if val != None:
            self.validate('maxfiles_possible', val)
        self._maxfiles_possible = val
    
    _files_total = None
    @property
    def files_total(self):
        """
        [settable, online-only]
        Total user-visible file (inode) count, i.e.,
        maximum number of user-visible files (inodes)
        that this referenced file system can currently
        hold. If the referenced file system is restricted
        or offline, a value of 0 is returned.
        """
        return self._files_total
    @files_total.setter
    def files_total(self, val):
        if val != None:
            self.validate('files_total', val)
        self._files_total = val
    
    _percent_inode_used_capacity = None
    @property
    def percent_inode_used_capacity(self):
        """
        [not settable, online-only]
        The percentage of disk space currently in use based
        on user-visible file (inode) count on the referenced
        file system.
        """
        return self._percent_inode_used_capacity
    @percent_inode_used_capacity.setter
    def percent_inode_used_capacity(self, val):
        if val != None:
            self.validate('percent_inode_used_capacity', val)
        self._percent_inode_used_capacity = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        [not settable, online-only]
        Number of user-visible files (inodes) used in the
        referenced file system. If the referenced file system
        is restricted or offline, a value of 0 is returned.
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "aggr-inode-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'inodefile-public-capacity',
            'maxfiles-used',
            'inodefile-private-capacity',
            'files-private-used',
            'maxfiles-available',
            'maxfiles-possible',
            'files-total',
            'percent-inode-used-capacity',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'inodefile_public_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maxfiles_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodefile_private_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_private_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maxfiles_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maxfiles_possible': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_inode_used_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
