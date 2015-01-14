from netapp.netapp_object import NetAppObject

class SecurityLoginRoleInfo(NetAppObject):
    """
    User role information.
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
        Name of the Vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _command_directory_name = None
    @property
    def command_directory_name(self):
        """
        The command or command directory to which the role has an
        access.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._command_directory_name
    @command_directory_name.setter
    def command_directory_name(self, val):
        if val != None:
            self.validate('command_directory_name', val)
        self._command_directory_name = val
    
    _access_level = None
    @property
    def access_level(self):
        """
        Access level for the role. Possible values:
        'none', 'readonly', 'all'.
        The default value is 'all'.
        Attributes: optional-for-create, modifiable
        """
        return self._access_level
    @access_level.setter
    def access_level(self, val):
        if val != None:
            self.validate('access_level', val)
        self._access_level = val
    
    _role_name = None
    @property
    def role_name(self):
        """
        Name of the role.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._role_name
    @role_name.setter
    def role_name(self, val):
        if val != None:
            self.validate('role_name', val)
        self._role_name = val
    
    _role_query = None
    @property
    def role_query(self):
        """
        A query for the role. The query must apply to the
        specified command or directory name.
        Example: The command is 'volume show' and the query is
        '-volume vol1'. The query is applied to the command
        resulting in populating only the volumes with name vol1.
        Attributes: optional-for-create, modifiable
        """
        return self._role_query
    @role_query.setter
    def role_query(self, val):
        if val != None:
            self.validate('role_query', val)
        self._role_query = val
    
    @staticmethod
    def get_api_name():
          return "security-login-role-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'command-directory-name',
            'access-level',
            'role-name',
            'role-query',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'command_directory_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'access_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'role_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'role_query': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
