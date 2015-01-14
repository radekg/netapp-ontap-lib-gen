from netapp.useradmin.useradmin_capability_info import UseradminCapabilityInfo
from netapp.useradmin.useradmin_role_info import UseradminRoleInfo
from netapp.netapp_object import NetAppObject

class UseradminGroupInfo(NetAppObject):
    """
    Structure containing information pertaining to a group.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        Comment for the group.
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _rid = None
    @property
    def rid(self):
        """
        Unique relative identifier (per domain) for this group.
        (Used only for Windows.)
        """
        return self._rid
    @rid.setter
    def rid(self, val):
        if val != None:
            self.validate('rid', val)
        self._rid = val
    
    _allowed_capabilities = None
    @property
    def allowed_capabilities(self):
        """
        List of capabilities the group is allowed.
        """
        return self._allowed_capabilities
    @allowed_capabilities.setter
    def allowed_capabilities(self, val):
        if val != None:
            self.validate('allowed_capabilities', val)
        self._allowed_capabilities = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the group.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _useradmin_roles = None
    @property
    def useradmin_roles(self):
        """
        List of roles this group contains. The only
        included entry in this structure is the name field.
        For full role information user useradmin-role-list.
        """
        return self._useradmin_roles
    @useradmin_roles.setter
    def useradmin_roles(self, val):
        if val != None:
            self.validate('useradmin_roles', val)
        self._useradmin_roles = val
    
    @staticmethod
    def get_api_name():
          return "useradmin-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'rid',
            'allowed-capabilities',
            'name',
            'useradmin-roles',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'allowed_capabilities': { 'class': UseradminCapabilityInfo, 'is_list': True, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'useradmin_roles': { 'class': UseradminRoleInfo, 'is_list': True, 'required': 'optional' },
        }
