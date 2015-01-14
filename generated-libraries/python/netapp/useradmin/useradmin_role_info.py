from netapp.useradmin.useradmin_capability_info import UseradminCapabilityInfo
from netapp.netapp_object import NetAppObject

class UseradminRoleInfo(NetAppObject):
    """
    Structure containing information pertaining to a role.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        Comment for the role.
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _allowed_capabilities = None
    @property
    def allowed_capabilities(self):
        """
        List of capabilities the role is allowed.
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
        Name of the role.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "useradmin-role-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'allowed-capabilities',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'allowed_capabilities': { 'class': UseradminCapabilityInfo, 'is_list': True, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
