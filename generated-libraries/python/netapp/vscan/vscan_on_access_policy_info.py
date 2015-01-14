from netapp.netapp_object import NetAppObject

class VscanOnAccessPolicyInfo(NetAppObject):
    """
    Vscan On-Access policy information.
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
    
    _file_ext_to_exclude = None
    @property
    def file_ext_to_exclude(self):
        """
        File-Extensions for which On-Access scanning must not be
        performed.
        Attributes: optional-for-create, modifiable
        """
        return self._file_ext_to_exclude
    @file_ext_to_exclude.setter
    def file_ext_to_exclude(self, val):
        if val != None:
            self.validate('file_ext_to_exclude', val)
        self._file_ext_to_exclude = val
    
    _admin_owner = None
    @property
    def admin_owner(self):
        """
        Owner of the policy.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "vserver"   - Vserver Admin,
        <li> "cluster"   - Cluter Admin
        </ul>
        """
        return self._admin_owner
    @admin_owner.setter
    def admin_owner(self, val):
        if val != None:
            self.validate('admin_owner', val)
        self._admin_owner = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        File-Access protocol to monitor for On-Access scanning.
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "cifs" - CIFS Protocol
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _is_policy_enabled = None
    @property
    def is_policy_enabled(self):
        """
        Policy status.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_policy_enabled
    @is_policy_enabled.setter
    def is_policy_enabled(self, val):
        if val != None:
            self.validate('is_policy_enabled', val)
        self._is_policy_enabled = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Name of the policy.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _max_file_size = None
    @property
    def max_file_size(self):
        """
        Max file-size (in bytes) allowed for scanning. The
        default value of 2147483648 (2GB) is taken if not
        provided at the time of creating a policy.
        Attributes: optional-for-create, modifiable
        """
        return self._max_file_size
    @max_file_size.setter
    def max_file_size(self, val):
        if val != None:
            self.validate('max_file_size', val)
        self._max_file_size = val
    
    _paths_to_exclude = None
    @property
    def paths_to_exclude(self):
        """
        File-paths for which On-Access scanning must not be
        performed.
        Attributes: optional-for-create, modifiable
        """
        return self._paths_to_exclude
    @paths_to_exclude.setter
    def paths_to_exclude(self, val):
        if val != None:
            self.validate('paths_to_exclude', val)
        self._paths_to_exclude = val
    
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
    
    _filters = None
    @property
    def filters(self):
        """
        Filters.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "scan_mandatory"      - Enable mandatory scan,
        <li> "scan_ro_volume"      - Enable scans for read-only
        volume,
        <li> "scan_execute_access" - Scan only files opened
        with execute-access (CIFS only)
        </ul>
        """
        return self._filters
    @filters.setter
    def filters(self, val):
        if val != None:
            self.validate('filters', val)
        self._filters = val
    
    @staticmethod
    def get_api_name():
          return "vscan-on-access-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'file-ext-to-exclude',
            'admin-owner',
            'protocol',
            'is-policy-enabled',
            'policy-name',
            'max-file-size',
            'paths-to-exclude',
            'vserver',
            'filters',
        ]
    
    def describe_properties(self):
        return {
            'file_ext_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'admin_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_policy_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_file_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'paths_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'filters': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
