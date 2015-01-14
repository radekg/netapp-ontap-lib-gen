from netapp.netapp_object import NetAppObject

class PresetInfo(NetAppObject):
    """
    Performance Preset information
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
    
    _comment = None
    @property
    def comment(self):
        """
        Preset Description
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Preset UUID
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _is_read_only = None
    @property
    def is_read_only(self):
        """
        Is Preset Read-Only?
        Attributes: non-creatable, non-modifiable
        """
        return self._is_read_only
    @is_read_only.setter
    def is_read_only(self, val):
        if val != None:
            self.validate('is_read_only', val)
        self._is_read_only = val
    
    _generation_id = None
    @property
    def generation_id(self):
        """
        Preset Generation ID
        Attributes: non-creatable, non-modifiable
        """
        return self._generation_id
    @generation_id.setter
    def generation_id(self, val):
        if val != None:
            self.validate('generation_id', val)
        self._generation_id = val
    
    _preset = None
    @property
    def preset(self):
        """
        Preset Name
        Attributes: key, required-for-create, non-modifiable
        """
        return self._preset
    @preset.setter
    def preset(self, val):
        if val != None:
            self.validate('preset', val)
        self._preset = val
    
    _privilege = None
    @property
    def privilege(self):
        """
        Preset Privilege Level
        Attributes: optional-for-create, modifiable
        """
        return self._privilege
    @privilege.setter
    def privilege(self, val):
        if val != None:
            self.validate('privilege', val)
        self._privilege = val
    
    _is_archive_enabled = None
    @property
    def is_archive_enabled(self):
        """
        Is Preset Archive-Enabled?
        Attributes: non-creatable, modifiable
        """
        return self._is_archive_enabled
    @is_archive_enabled.setter
    def is_archive_enabled(self, val):
        if val != None:
            self.validate('is_archive_enabled', val)
        self._is_archive_enabled = val
    
    _new_name = None
    @property
    def new_name(self):
        """
        New Preset Name
        Attributes: non-creatable, modifiable
        """
        return self._new_name
    @new_name.setter
    def new_name(self, val):
        if val != None:
            self.validate('new_name', val)
        self._new_name = val
    
    @staticmethod
    def get_api_name():
          return "preset-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'uuid',
            'is-read-only',
            'generation-id',
            'preset',
            'privilege',
            'is-archive-enabled',
            'new-name',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_read_only': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'generation_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'preset': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privilege': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_archive_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'new_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
