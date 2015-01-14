from netapp.netapp_object import NetAppObject

class FpolicyScopeConfig(NetAppObject):
    """
    Vserver FPolicy Scope configuration and management on name
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
    
    _export_policies_to_include = None
    @property
    def export_policies_to_include(self):
        """
        Export policies to include for file access monitoring. By
        default no export policy is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._export_policies_to_include
    @export_policies_to_include.setter
    def export_policies_to_include(self, val):
        if val != None:
            self.validate('export_policies_to_include', val)
        self._export_policies_to_include = val
    
    _volumes_to_include = None
    @property
    def volumes_to_include(self):
        """
        Volumes that are active for the file policy. The list can
        include items which are regular expressions, such as
        'vol*' or 'user?'. By default no volume is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._volumes_to_include
    @volumes_to_include.setter
    def volumes_to_include(self, val):
        if val != None:
            self.validate('volumes_to_include', val)
        self._volumes_to_include = val
    
    _volumes_to_exclude = None
    @property
    def volumes_to_exclude(self):
        """
        Volumes that are inactive for the file policy. The list
        can include items which are regular expressions, such as
        'vol*' or 'user?'. Note that if a policy has both an
        exclude list and an include list, the include list is
        ignored by the filer when processing user requests. By
        default no volume is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._volumes_to_exclude
    @volumes_to_exclude.setter
    def volumes_to_exclude(self, val):
        if val != None:
            self.validate('volumes_to_exclude', val)
        self._volumes_to_exclude = val
    
    _file_extensions_to_exclude = None
    @property
    def file_extensions_to_exclude(self):
        """
        File extensions excluded for screening. By default no
        file extension is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._file_extensions_to_exclude
    @file_extensions_to_exclude.setter
    def file_extensions_to_exclude(self, val):
        if val != None:
            self.validate('file_extensions_to_exclude', val)
        self._file_extensions_to_exclude = val
    
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
    
    _export_policies_to_exclude = None
    @property
    def export_policies_to_exclude(self):
        """
        Export Policies to exclude for file access monitoring. By
        default no export policy is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._export_policies_to_exclude
    @export_policies_to_exclude.setter
    def export_policies_to_exclude(self, val):
        if val != None:
            self.validate('export_policies_to_exclude', val)
        self._export_policies_to_exclude = val
    
    _check_extensions_on_directories = None
    @property
    def check_extensions_on_directories(self):
        """
        Indicates whether directory names are also subjected to
        extensions check, similar to file names. By default, the
        value is false.
        Attributes: optional-for-create, modifiable
        """
        return self._check_extensions_on_directories
    @check_extensions_on_directories.setter
    def check_extensions_on_directories(self, val):
        if val != None:
            self.validate('check_extensions_on_directories', val)
        self._check_extensions_on_directories = val
    
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
    
    _shares_to_exclude = None
    @property
    def shares_to_exclude(self):
        """
        Shares to exclude for file access monitoring. By default
        no share is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._shares_to_exclude
    @shares_to_exclude.setter
    def shares_to_exclude(self, val):
        if val != None:
            self.validate('shares_to_exclude', val)
        self._shares_to_exclude = val
    
    _file_extensions_to_include = None
    @property
    def file_extensions_to_include(self):
        """
        File extensions included for screening. By default no
        file extension is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._file_extensions_to_include
    @file_extensions_to_include.setter
    def file_extensions_to_include(self, val):
        if val != None:
            self.validate('file_extensions_to_include', val)
        self._file_extensions_to_include = val
    
    _shares_to_include = None
    @property
    def shares_to_include(self):
        """
        Shares to include for file access monitoring. By default
        no share is selected.
        Attributes: optional-for-create, modifiable
        """
        return self._shares_to_include
    @shares_to_include.setter
    def shares_to_include(self, val):
        if val != None:
            self.validate('shares_to_include', val)
        self._shares_to_include = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-scope-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'export-policies-to-include',
            'volumes-to-include',
            'volumes-to-exclude',
            'file-extensions-to-exclude',
            'policy-name',
            'export-policies-to-exclude',
            'check-extensions-on-directories',
            'vserver',
            'shares-to-exclude',
            'file-extensions-to-include',
            'shares-to-include',
        ]
    
    def describe_properties(self):
        return {
            'export_policies_to_include': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'volumes_to_include': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'volumes_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'file_extensions_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'export_policies_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'check_extensions_on_directories': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shares_to_exclude': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'file_extensions_to_include': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'shares_to_include': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
