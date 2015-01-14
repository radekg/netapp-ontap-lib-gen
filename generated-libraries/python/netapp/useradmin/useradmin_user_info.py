from netapp.useradmin.useradmin_capability_info import UseradminCapabilityInfo
from netapp.useradmin.useradmin_group_info import UseradminGroupInfo
from netapp.netapp_object import NetAppObject

class UseradminUserInfo(NetAppObject):
    """
    Structure containing information pertaining to a user.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        Comment for the user. This is only set if the
        user has a comment.
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _status = None
    @property
    def status(self):
        """
        Current status of the user account. This element cannot
        be used as an input. It is used as an output for
        useradmin-user-list. Possible values: "enabled",
        "disabled", or "expired".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the user.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _password_minimum_age = None
    @property
    def password_minimum_age(self):
        """
        Number of days that this user's password must be
        active before the user can change it. Default
        value is 0.
        """
        return self._password_minimum_age
    @password_minimum_age.setter
    def password_minimum_age(self, val):
        if val != None:
            self.validate('password_minimum_age', val)
        self._password_minimum_age = val
    
    _password_maximum_age = None
    @property
    def password_maximum_age(self):
        """
        Number of days that this user's password can be
        active before the user must change it. Default
        value is 2^31-1 days.
        """
        return self._password_maximum_age
    @password_maximum_age.setter
    def password_maximum_age(self, val):
        if val != None:
            self.validate('password_maximum_age', val)
        self._password_maximum_age = val
    
    _allowed_capabilities = None
    @property
    def allowed_capabilities(self):
        """
        List of capabilities the user is allowed.
        """
        return self._allowed_capabilities
    @allowed_capabilities.setter
    def allowed_capabilities(self, val):
        if val != None:
            self.validate('allowed_capabilities', val)
        self._allowed_capabilities = val
    
    _full_name = None
    @property
    def full_name(self):
        """
        Full name of the user. (Used only for Windows.)
        This is only set if the user has a full-name.
        """
        return self._full_name
    @full_name.setter
    def full_name(self, val):
        if val != None:
            self.validate('full_name', val)
        self._full_name = val
    
    _useradmin_groups = None
    @property
    def useradmin_groups(self):
        """
        List of groups this user is part of. The only
        included entry in this structure is the name field.
        For full group information user useradmin-group-list.
        """
        return self._useradmin_groups
    @useradmin_groups.setter
    def useradmin_groups(self, val):
        if val != None:
            self.validate('useradmin_groups', val)
        self._useradmin_groups = val
    
    _rid = None
    @property
    def rid(self):
        """
        Unique relative identifier (per domain) for this user.
        (Used only for Windows.)
        """
        return self._rid
    @rid.setter
    def rid(self, val):
        if val != None:
            self.validate('rid', val)
        self._rid = val
    
    @staticmethod
    def get_api_name():
          return "useradmin-user-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'status',
            'name',
            'password-minimum-age',
            'password-maximum-age',
            'allowed-capabilities',
            'full-name',
            'useradmin-groups',
            'rid',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'password_minimum_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'password_maximum_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'allowed_capabilities': { 'class': UseradminCapabilityInfo, 'is_list': True, 'required': 'optional' },
            'full_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'useradmin_groups': { 'class': UseradminGroupInfo, 'is_list': True, 'required': 'required' },
            'rid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
