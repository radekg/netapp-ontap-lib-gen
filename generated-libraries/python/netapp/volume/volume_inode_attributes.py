from netapp.netapp_object import NetAppObject

class VolumeInodeAttributes(NetAppObject):
    """
    Information about inodes in the volume.
    """
    
    _inodefile_public_capacity = None
    @property
    def inodefile_public_capacity(self):
        """
        Number of inodes that can currently be stored on disk for
        user-visible files. This number will dynamically increase
        as more user-visible files are created. This field is
        valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._inodefile_public_capacity
    @inodefile_public_capacity.setter
    def inodefile_public_capacity(self, val):
        if val != None:
            self.validate('inodefile_public_capacity', val)
        self._inodefile_public_capacity = val
    
    _inodefile_private_capacity = None
    @property
    def inodefile_private_capacity(self):
        """
        Number of inodes that can currently be stored on disk for
        system (not user-visible) files. This number will
        dynamically increase as more system files are created.
        This field is valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
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
        Number of system (not user-visible) files (inodes) used.
        This field is valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._files_private_used
    @files_private_used.setter
    def files_private_used(self, val):
        if val != None:
            self.validate('files_private_used', val)
        self._files_private_used = val
    
    _files_total = None
    @property
    def files_total(self):
        """
        Total user-visible file (inode) count, i.e., current
        maximum number of user-visible files (inodes) that this
        volume can currently hold.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._files_total
    @files_total.setter
    def files_total(self, val):
        if val != None:
            self.validate('files_total', val)
        self._files_total = val
    
    _block_type = None
    @property
    def block_type(self):
        """
        The indirect block format of the volume.
        <p>
        Possible values:
        <ul>
        <li> '32_bit',
        <li> '64_bit'
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._block_type
    @block_type.setter
    def block_type(self, val):
        if val != None:
            self.validate('block_type', val)
        self._block_type = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        Number of user-visible files (inodes) used. This field is
        valid only when the volume is online.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "volume-inode-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'inodefile-public-capacity',
            'inodefile-private-capacity',
            'files-private-used',
            'files-total',
            'block-type',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'inodefile_public_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'inodefile_private_capacity': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_private_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_total': { 'class': int, 'is_list': False, 'required': 'optional' },
            'block_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
