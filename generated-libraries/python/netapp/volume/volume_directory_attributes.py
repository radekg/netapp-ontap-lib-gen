from netapp.netapp_object import NetAppObject

class VolumeDirectoryAttributes(NetAppObject):
    """
    Information related to directories in the volume.
    """
    
    _i2p_enabled = None
    @property
    def i2p_enabled(self):
        """
        If true, native inode-to-parent information is kept for
        inodes. By default, this field is true.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._i2p_enabled
    @i2p_enabled.setter
    def i2p_enabled(self, val):
        if val != None:
            self.validate('i2p_enabled', val)
        self._i2p_enabled = val
    
    _max_dir_size = None
    @property
    def max_dir_size(self):
        """
        The maximum size (in bytes) to which any directory in
        this volume can grow.
        <p>
        The default maximum directory size is set to 1% of the
        system memory. So if the system memory is 1GB, then the
        maximum directory size value will be 10MB which allows
        upto 300,000 files. The number of files that the
        directory actually can hold varies depending on such
        things as the length of the names and whether it needs to
        use double-byte UNICODE characters.
        <p>
        Most users should not need to change this field's default
        setting. It is useful for environments where system users
        may grow a directory to a size that starts impacting
        system performance.  When a user tries to create a file
        in a directory that is at the limit, the system returns a
        ENOSPC error and fails the create.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._max_dir_size
    @max_dir_size.setter
    def max_dir_size(self, val):
        if val != None:
            self.validate('max_dir_size', val)
        self._max_dir_size = val
    
    _root_dir_gen = None
    @property
    def root_dir_gen(self):
        """
        This field contains the generation number of the root
        directory.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._root_dir_gen
    @root_dir_gen.setter
    def root_dir_gen(self, val):
        if val != None:
            self.validate('root_dir_gen', val)
        self._root_dir_gen = val
    
    @staticmethod
    def get_api_name():
          return "volume-directory-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'i2p-enabled',
            'max-dir-size',
            'root-dir-gen',
        ]
    
    def describe_properties(self):
        return {
            'i2p_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_dir_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'root_dir_gen': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
