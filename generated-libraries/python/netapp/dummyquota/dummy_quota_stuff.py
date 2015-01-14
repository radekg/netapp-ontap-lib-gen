from netapp.netapp_object import NetAppObject

class DummyQuotaStuff(NetAppObject):
    """
    Initiators connected to lif
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
    
    _soft_file_limit = None
    @property
    def soft_file_limit(self):
        """
        Soft File Limit
        Attributes: required-for-create, modifiable
        """
        return self._soft_file_limit
    @soft_file_limit.setter
    def soft_file_limit(self, val):
        if val != None:
            self.validate('soft_file_limit', val)
        self._soft_file_limit = val
    
    _quota_user_ids = None
    @property
    def quota_user_ids(self):
        """
        Quota User IDs
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_ids
    @quota_user_ids.setter
    def quota_user_ids(self, val):
        if val != None:
            self.validate('quota_user_ids', val)
        self._quota_user_ids = val
    
    _quota_type = None
    @property
    def quota_type(self):
        """
        Type (ZAPI)
        Attributes: required-for-create, modifiable
        """
        return self._quota_type
    @quota_type.setter
    def quota_type(self, val):
        if val != None:
            self.validate('quota_type', val)
        self._quota_type = val
    
    _quota_user_types = None
    @property
    def quota_user_types(self):
        """
        Quota User Types
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_types
    @quota_user_types.setter
    def quota_user_types(self, val):
        if val != None:
            self.validate('quota_user_types', val)
        self._quota_user_types = val
    
    _tree = None
    @property
    def tree(self):
        """
        Tree
        Attributes: required-for-create, modifiable
        """
        return self._tree
    @tree.setter
    def tree(self, val):
        if val != None:
            self.validate('tree', val)
        self._tree = val
    
    _volume = None
    @property
    def volume(self):
        """
        Volume Name
        Attributes: required-for-create, modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _path = None
    @property
    def path(self):
        """
        Path Based Report
        Attributes: required-for-create, modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _file_limit = None
    @property
    def file_limit(self):
        """
        Files Limit
        Attributes: required-for-create, modifiable
        """
        return self._file_limit
    @file_limit.setter
    def file_limit(self, val):
        if val != None:
            self.validate('file_limit', val)
        self._file_limit = val
    
    _quota_user_names = None
    @property
    def quota_user_names(self):
        """
        Quota User Names
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_names
    @quota_user_names.setter
    def quota_user_names(self, val):
        if val != None:
            self.validate('quota_user_names', val)
        self._quota_user_names = val
    
    _volume_index = None
    @property
    def volume_index(self):
        """
        Volume Index
        Attributes: key, required-for-create, non-modifiable
        """
        return self._volume_index
    @volume_index.setter
    def volume_index(self, val):
        if val != None:
            self.validate('volume_index', val)
        self._volume_index = val
    
    _disk_used = None
    @property
    def disk_used(self):
        """
        Disk Blocks Used
        Attributes: required-for-create, modifiable
        """
        return self._disk_used
    @disk_used.setter
    def disk_used(self, val):
        if val != None:
            self.validate('disk_used', val)
        self._disk_used = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        Files Used
        Attributes: required-for-create, modifiable
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "dummy-quota-stuff"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'soft-file-limit',
            'quota-user-ids',
            'quota-type',
            'quota-user-types',
            'tree',
            'volume',
            'path',
            'file-limit',
            'quota-user-names',
            'volume-index',
            'disk-used',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'soft_file_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'quota_user_ids': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'quota_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_user_types': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'tree': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'quota_user_names': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'volume_index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
