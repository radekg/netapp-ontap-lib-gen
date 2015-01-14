from netapp.netapp_object import NetAppObject

class FileDirectorySecurityPolicyTask(NetAppObject):
    """
    File security policy task management
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
    
    _ntfs_mode = None
    @property
    def ntfs_mode(self):
        """
        Specifies the NTFS propagation mode.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "propagate" ,
        <li> "ignore"    ,
        <li> "replace"
        </ul>
        """
        return self._ntfs_mode
    @ntfs_mode.setter
    def ntfs_mode(self, val):
        if val != None:
            self.validate('ntfs_mode', val)
        self._ntfs_mode = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Specifies the name of the policy who has the task.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _task_index_number = None
    @property
    def task_index_number(self):
        """
        Specifies the target index/position of this task in the
        policy. If the task is currently placed in 5th position
        in a policy and you want to reorder this task as 2nd
        task, you can set the index-num to 2. If the index number
        exceeds the number of positions, it will go at the end.
        Attributes: optional-for-create, modifiable
        """
        return self._task_index_number
    @task_index_number.setter
    def task_index_number(self, val):
        if val != None:
            self.validate('task_index_number', val)
        self._task_index_number = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _ntfs_sd = None
    @property
    def ntfs_sd(self):
        """
        Specifies the NTFS security descriptor identifier.
        Attributes: optional-for-create, modifiable
        """
        return self._ntfs_sd
    @ntfs_sd.setter
    def ntfs_sd(self, val):
        if val != None:
            self.validate('ntfs_sd', val)
        self._ntfs_sd = val
    
    _path = None
    @property
    def path(self):
        """
        Specifies the file or folder path of a task.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _security_type = None
    @property
    def security_type(self):
        """
        Specifies the type of security.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "ntfs"      ,
        <li> "nfsv4"
        </ul>
        """
        return self._security_type
    @security_type.setter
    def security_type(self, val):
        if val != None:
            self.validate('security_type', val)
        self._security_type = val
    
    @staticmethod
    def get_api_name():
          return "file-directory-security-policy-task"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntfs-mode',
            'policy-name',
            'task-index-number',
            'vserver',
            'ntfs-sd',
            'path',
            'security-type',
        ]
    
    def describe_properties(self):
        return {
            'ntfs_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'task_index_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ntfs_sd': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
