from netapp.netapp_object import NetAppObject

class SystemImageAttributes(NetAppObject):
    """
    These attributes describe or modify the configuration of the
    nodes's boot images.
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
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _rootfs_path = None
    @property
    def rootfs_path(self):
        """
        Root Filesystem Image Path
        Attributes: non-creatable, non-modifiable
        """
        return self._rootfs_path
    @rootfs_path.setter
    def rootfs_path(self, val):
        if val != None:
            self.validate('rootfs_path', val)
        self._rootfs_path = val
    
    _install_time = None
    @property
    def install_time(self):
        """
        Install Date
        Attributes: non-creatable, non-modifiable
        """
        return self._install_time
    @install_time.setter
    def install_time(self, val):
        if val != None:
            self.validate('install_time', val)
        self._install_time = val
    
    _image = None
    @property
    def image(self):
        """
        Image Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._image
    @image.setter
    def image(self, val):
        if val != None:
            self.validate('image', val)
        self._image = val
    
    _kernel_path = None
    @property
    def kernel_path(self):
        """
        Kernel Image Path
        Attributes: non-creatable, non-modifiable
        """
        return self._kernel_path
    @kernel_path.setter
    def kernel_path(self, val):
        if val != None:
            self.validate('kernel_path', val)
        self._kernel_path = val
    
    _is_default = None
    @property
    def is_default(self):
        """
        Is Default Image
        Attributes: non-creatable, modifiable
        """
        return self._is_default
    @is_default.setter
    def is_default(self, val):
        if val != None:
            self.validate('is_default', val)
        self._is_default = val
    
    _version = None
    @property
    def version(self):
        """
        Software Version
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _is_current = None
    @property
    def is_current(self):
        """
        Is Current Image
        Attributes: non-creatable, non-modifiable
        """
        return self._is_current
    @is_current.setter
    def is_current(self, val):
        if val != None:
            self.validate('is_current', val)
        self._is_current = val
    
    @staticmethod
    def get_api_name():
          return "system-image-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'rootfs-path',
            'install-time',
            'image',
            'kernel-path',
            'is-default',
            'version',
            'is-current',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rootfs_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'install_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'image': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kernel_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_default': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_current': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
