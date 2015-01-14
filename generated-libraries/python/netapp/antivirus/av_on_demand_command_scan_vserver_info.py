from netapp.netapp_object import NetAppObject

class AvOnDemandCommandScanVserverInfo(NetAppObject):
    """
    ondemand command
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
    
    _directory_pattern = None
    @property
    def directory_pattern(self):
        """
        This specifies the directories to be scanned. This
        parameter specifies the case-insensitive regular
        expression that defines what directories to include or
        exclude from the antivirus scan. If this parameter is
        used, you must specify whether to include or exclude
        directories using the include-directories parameter.
        Attributes: optional-for-create, modifiable
        """
        return self._directory_pattern
    @directory_pattern.setter
    def directory_pattern(self, val):
        if val != None:
            self.validate('directory_pattern', val)
        self._directory_pattern = val
    
    _force = None
    @property
    def force(self):
        """
        Force the file to be scanned even if it has already been
        scanned. Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._force
    @force.setter
    def force(self, val):
        if val != None:
            self.validate('force', val)
        self._force = val
    
    _enable_subdirectory_recursion = None
    @property
    def enable_subdirectory_recursion(self):
        """
        This parameter specifies whether to enable or disable
        recursive scanning through sub-directories. If the
        parameter is set to true, recursive s     canning is not
        enabled. To allow recursive scanning, set this parameter
        to false. Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._enable_subdirectory_recursion
    @enable_subdirectory_recursion.setter
    def enable_subdirectory_recursion(self, val):
        if val != None:
            self.validate('enable_subdirectory_recursion', val)
        self._enable_subdirectory_recursion = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver which owns this on-demand command.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _command_name = None
    @property
    def command_name(self):
        """
        Name of the on-demand command. Can be any valid string.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._command_name
    @command_name.setter
    def command_name(self, val):
        if val != None:
            self.validate('command_name', val)
        self._command_name = val
    
    _file_pattern = None
    @property
    def file_pattern(self):
        """
        This specifies the files to be scanned. This parameter
        specifies the case-insensitive regular expression that
        defines what files to include or exclude from the
        antivirus scan. If this parameter is used, you must
        specify whether to include or exclude files using the
        include-files parameter.
        Attributes: optional-for-create, modifiable
        """
        return self._file_pattern
    @file_pattern.setter
    def file_pattern(self, val):
        if val != None:
            self.validate('file_pattern', val)
        self._file_pattern = val
    
    _enable_junction_following = None
    @property
    def enable_junction_following(self):
        """
        This parameter specifies whether the antivirus scan is
        allowed to follow volume junctions. If the parameter is
        set to true, following ju     nctions is not allowed. To
        allow the scan to follow junctions, set this parameter to
        false. Default is false.
        Attributes: optional-for-create, modifiable
        """
        return self._enable_junction_following
    @enable_junction_following.setter
    def enable_junction_following(self, val):
        if val != None:
            self.validate('enable_junction_following', val)
        self._enable_junction_following = val
    
    _policy_owner = None
    @property
    def policy_owner(self):
        """
        Policy belongs to cluster admin or data-vserver. Possible
        values are Cluster Admin or Vserver Admin.
        Attributes: non-creatable, non-modifiable
        """
        return self._policy_owner
    @policy_owner.setter
    def policy_owner(self, val):
        if val != None:
            self.validate('policy_owner', val)
        self._policy_owner = val
    
    _include_files = None
    @property
    def include_files(self):
        """
        This specifies whether the files defined in the parameter
        file-pattern will be included in or excluded from the
        antivirus      scan.  If true, then file-pattern is an
        inclusive match, else an exclusive match.  Default it
        true.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "include"   ,
        <li> "exclude"
        </ul>
        """
        return self._include_files
    @include_files.setter
    def include_files(self, val):
        if val != None:
            self.validate('include_files', val)
        self._include_files = val
    
    _include_directories = None
    @property
    def include_directories(self):
        """
        This specifies whether the files defined in the parameter
        directory-pattern will be included in or excluded from
        the antivirus  scan.  If true, then directory-pattern is
        an inclusive match, else an exclusive match.  Default it
        true.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "include"   ,
        <li> "exclude"
        </ul>
        """
        return self._include_directories
    @include_directories.setter
    def include_directories(self, val):
        if val != None:
            self.validate('include_directories', val)
        self._include_directories = val
    
    @staticmethod
    def get_api_name():
          return "av-on-demand-command-scan-vserver-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'directory-pattern',
            'force',
            'enable-subdirectory-recursion',
            'vserver',
            'command-name',
            'file-pattern',
            'enable-junction-following',
            'policy-owner',
            'include-files',
            'include-directories',
        ]
    
    def describe_properties(self):
        return {
            'directory_pattern': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'force': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'enable_subdirectory_recursion': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'command_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_pattern': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enable_junction_following': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'policy_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'include_files': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'include_directories': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
