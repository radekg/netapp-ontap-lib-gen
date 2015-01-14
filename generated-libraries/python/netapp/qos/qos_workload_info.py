from netapp.netapp_object import NetAppObject

class QosWorkloadInfo(NetAppObject):
    """
    Information about a QoS workload
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
    
    _category = None
    @property
    def category(self):
        """
        Category used to identify the workload.
        Attributes: non-creatable, non-modifiable
        """
        return self._category
    @category.setter
    def category(self, val):
        if val != None:
            self.validate('category', val)
        self._category = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name for a volume workload.
        Attributes: optional-for-create, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _read_ahead = None
    @property
    def read_ahead(self):
        """
        Name for a read-ahead tunable policy.
        Attributes: optional-for-create, modifiable
        """
        return self._read_ahead
    @read_ahead.setter
    def read_ahead(self, val):
        if val != None:
            self.validate('read_ahead', val)
        self._read_ahead = val
    
    _wid = None
    @property
    def wid(self):
        """
        Internal identifier for workload.
        Attributes: non-creatable, non-modifiable
        """
        return self._wid
    @wid.setter
    def wid(self, val):
        if val != None:
            self.validate('wid', val)
        self._wid = val
    
    _qtree = None
    @property
    def qtree(self):
        """
        Name for a qtree workload.
        Attributes: optional-for-create, non-modifiable
        """
        return self._qtree
    @qtree.setter
    def qtree(self, val):
        if val != None:
            self.validate('qtree', val)
        self._qtree = val
    
    _policy_group = None
    @property
    def policy_group(self):
        """
        Name for a QoS policy group.
        Attributes: non-creatable, non-modifiable
        """
        return self._policy_group
    @policy_group.setter
    def policy_group(self, val):
        if val != None:
            self.validate('policy_group', val)
        self._policy_group = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name for a vserver workload.
        Attributes: optional-for-create, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _workload_name = None
    @property
    def workload_name(self):
        """
        User visible name of QoS workload.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._workload_name
    @workload_name.setter
    def workload_name(self, val):
        if val != None:
            self.validate('workload_name', val)
        self._workload_name = val
    
    _file = None
    @property
    def file(self):
        """
        Name for a file workload.
        Attributes: optional-for-create, non-modifiable
        """
        return self._file
    @file.setter
    def file(self, val):
        if val != None:
            self.validate('file', val)
        self._file = val
    
    _workload_uuid = None
    @property
    def workload_uuid(self):
        """
        Universally unique identifier for the QoS workload.
        Attributes: non-creatable, non-modifiable
        """
        return self._workload_uuid
    @workload_uuid.setter
    def workload_uuid(self, val):
        if val != None:
            self.validate('workload_uuid', val)
        self._workload_uuid = val
    
    _workload_class = None
    @property
    def workload_class(self):
        """
        Class for the workload.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "preset"         - Preset,
        <li> "user_defined"   - User Defined,
        <li> "system_defined" - System Defined
        </ul>
        """
        return self._workload_class
    @workload_class.setter
    def workload_class(self, val):
        if val != None:
            self.validate('workload_class', val)
        self._workload_class = val
    
    _lun = None
    @property
    def lun(self):
        """
        Name for a lun workload.
        Attributes: optional-for-create, non-modifiable
        """
        return self._lun
    @lun.setter
    def lun(self, val):
        if val != None:
            self.validate('lun', val)
        self._lun = val
    
    @staticmethod
    def get_api_name():
          return "qos-workload-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'category',
            'volume',
            'read-ahead',
            'wid',
            'qtree',
            'policy-group',
            'vserver',
            'workload-name',
            'file',
            'workload-uuid',
            'workload-class',
            'lun',
        ]
    
    def describe_properties(self):
        return {
            'category': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'read_ahead': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'wid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'qtree': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'workload_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'workload_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'workload_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lun': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
