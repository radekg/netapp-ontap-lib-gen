from netapp.netapp_object import NetAppObject

class AvOnDemandCommandScanFileInfo(NetAppObject):
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver which owns this on-demand command
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
        The name of the scan command. Can be any valid string.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._command_name
    @command_name.setter
    def command_name(self, val):
        if val != None:
            self.validate('command_name', val)
        self._command_name = val
    
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
    
    _scan_path = None
    @property
    def scan_path(self):
        """
        Full path name of the file to be scanned.
        Attributes: required-for-create, modifiable
        """
        return self._scan_path
    @scan_path.setter
    def scan_path(self, val):
        if val != None:
            self.validate('scan_path', val)
        self._scan_path = val
    
    @staticmethod
    def get_api_name():
          return "av-on-demand-command-scan-file-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'command-name',
            'policy-owner',
            'force',
            'scan-path',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'command_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'force': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'scan_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
