from netapp.netapp_object import NetAppObject

class CoredumpConfigInfo(NetAppObject):
    """
    Coredump configuration
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
    
    _save_onstartup = None
    @property
    def save_onstartup(self):
        """
        Enable auto-save of coredumps on startup.
        Attributes: non-creatable, modifiable
        """
        return self._save_onstartup
    @save_onstartup.setter
    def save_onstartup(self, val):
        if val != None:
            self.validate('save_onstartup', val)
        self._save_onstartup = val
    
    _save_attempts = None
    @property
    def save_attempts(self):
        """
        Maximum number of attempts to save core.
        Attributes: non-creatable, modifiable
        """
        return self._save_attempts
    @save_attempts.setter
    def save_attempts(self, val):
        if val != None:
            self.validate('save_attempts', val)
        self._save_attempts = val
    
    _is_sparsecore_enabled = None
    @property
    def is_sparsecore_enabled(self):
        """
        Enable sparse cores.
        Attributes: non-creatable, modifiable
        """
        return self._is_sparsecore_enabled
    @is_sparsecore_enabled.setter
    def is_sparsecore_enabled(self, val):
        if val != None:
            self.validate('is_sparsecore_enabled', val)
        self._is_sparsecore_enabled = val
    
    _upload_location = None
    @property
    def upload_location(self):
        """
        URL for the coredump upload directory
        Attributes: non-creatable, modifiable
        """
        return self._upload_location
    @upload_location.setter
    def upload_location(self, val):
        if val != None:
            self.validate('upload_location', val)
        self._upload_location = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The node to which this coredump configuration belongs.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _coredump_attempts = None
    @property
    def coredump_attempts(self):
        """
        Maximum number of attempts to dump core.
        Attributes: non-creatable, modifiable
        """
        return self._coredump_attempts
    @coredump_attempts.setter
    def coredump_attempts(self, val):
        if val != None:
            self.validate('coredump_attempts', val)
        self._coredump_attempts = val
    
    _min_free = None
    @property
    def min_free(self):
        """
        Minimum free bytes on root filesystem needed for a core
        dump.
        Attributes: non-creatable, modifiable
        """
        return self._min_free
    @min_free.setter
    def min_free(self, val):
        if val != None:
            self.validate('min_free', val)
        self._min_free = val
    
    @staticmethod
    def get_api_name():
          return "coredump-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'save-onstartup',
            'save-attempts',
            'is-sparsecore-enabled',
            'upload-location',
            'node-name',
            'coredump-attempts',
            'min-free',
        ]
    
    def describe_properties(self):
        return {
            'save_onstartup': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'save_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_sparsecore_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'upload_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'coredump_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'min_free': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
