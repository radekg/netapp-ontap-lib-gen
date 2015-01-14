from netapp.netapp_object import NetAppObject

class CoredumpInfo(NetAppObject):
    """
    Information about a core dump
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
    
    _is_partial = None
    @property
    def is_partial(self):
        """
        Indicates whether it is a partial core. Partial cores are
        due to missing disks. This field is only valid if
        is-saved is 'False'.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_partial
    @is_partial.setter
    def is_partial(self, val):
        if val != None:
            self.validate('is_partial', val)
        self._is_partial = val
    
    _is_saved = None
    @property
    def is_saved(self):
        """
        Indicates if the core was saved to the filesystem or not.
        This is always 'True' for application cores.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_saved
    @is_saved.setter
    def is_saved(self, val):
        if val != None:
            self.validate('is_saved', val)
        self._is_saved = val
    
    _save_attempts = None
    @property
    def save_attempts(self):
        """
        Number of attempts to save core. This field is only valid
        if is-saved is 'False'
        Attributes: non-creatable, non-modifiable
        """
        return self._save_attempts
    @save_attempts.setter
    def save_attempts(self, val):
        if val != None:
            self.validate('save_attempts', val)
        self._save_attempts = val
    
    _panic_system_id = None
    @property
    def panic_system_id(self):
        """
        System Id of node that generated the coredump.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_system_id
    @panic_system_id.setter
    def panic_system_id(self, val):
        if val != None:
            self.validate('panic_system_id', val)
        self._panic_system_id = val
    
    _core_id = None
    @property
    def core_id(self):
        """
        A unique Id of the core used for operations like show,
        delete, upload and save.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._core_id
    @core_id.setter
    def core_id(self, val):
        if val != None:
            self.validate('core_id', val)
        self._core_id = val
    
    _panic_node = None
    @property
    def panic_node(self):
        """
        Node that generated the coredump.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_node
    @panic_node.setter
    def panic_node(self, val):
        if val != None:
            self.validate('panic_node', val)
        self._panic_node = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The node that owns the coredump.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _version = None
    @property
    def version(self):
        """
        The version of Data ONTAP that was running when the core
        was dumped.
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _panic_string = None
    @property
    def panic_string(self):
        """
        Panic string for the panic that generated the core.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_string
    @panic_string.setter
    def panic_string(self, val):
        if val != None:
            self.validate('panic_string', val)
        self._panic_string = val
    
    _panic_time = None
    @property
    def panic_time(self):
        """
        Time when the panic occurred. This is expressed in
        seconds since the Epoch.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_time
    @panic_time.setter
    def panic_time(self, val):
        if val != None:
            self.validate('panic_time', val)
        self._panic_time = val
    
    _space_needed = None
    @property
    def space_needed(self):
        """
        Space needed to save core. This field is only valid if
        is-saved is 'False'.
        Attributes: non-creatable, non-modifiable
        """
        return self._space_needed
    @space_needed.setter
    def space_needed(self, val):
        if val != None:
            self.validate('space_needed', val)
        self._space_needed = val
    
    _core_name = None
    @property
    def core_name(self):
        """
        The name of the coredump file. The corename has the
        following formats: Kernel: <app
        name>.<pid>.<sysid>.<date>.<time>.nz, Application: <app
        name>.<pid>.<sysid>.<date>.<time>.ucore.bz2. Application
        cores that are not compressed won't have the .bz2
        extension.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._core_name
    @core_name.setter
    def core_name(self, val):
        if val != None:
            self.validate('core_name', val)
        self._core_name = val
    
    @staticmethod
    def get_api_name():
          return "coredump-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-partial',
            'is-saved',
            'save-attempts',
            'panic-system-id',
            'core-id',
            'panic-node',
            'node-name',
            'version',
            'panic-string',
            'panic-time',
            'space-needed',
            'core-name',
        ]
    
    def describe_properties(self):
        return {
            'is_partial': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_saved': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'save_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'panic_system_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'core_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'panic_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'panic_string': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'panic_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'space_needed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'core_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
