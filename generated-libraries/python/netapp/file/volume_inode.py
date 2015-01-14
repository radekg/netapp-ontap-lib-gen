from netapp.netapp_object import NetAppObject

class VolumeInode(NetAppObject):
    """
    Volume and inode specification for a file.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        The volume where the file is located.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _is_private = None
    @property
    def is_private(self):
        """
        If true, the inode number specified in element 'inode'
        is in private inode space.
        If false, the inode number is in public inode space.
        The default value is false if this element is missing.
        """
        return self._is_private
    @is_private.setter
    def is_private(self, val):
        if val != None:
            self.validate('is_private', val)
        self._is_private = val
    
    _inode = None
    @property
    def inode(self):
        """
        The inode number of the file in the volume.
        """
        return self._inode
    @inode.setter
    def inode(self, val):
        if val != None:
            self.validate('inode', val)
        self._inode = val
    
    @staticmethod
    def get_api_name():
          return "volume-inode"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'is-private',
            'inode',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_private': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'inode': { 'class': int, 'is_list': False, 'required': 'required' },
        }
