from netapp.netapp_object import NetAppObject

class AccessRightsInfo(NetAppObject):
    """
    Access rights of single user or single Unix group.
    """
    
    _user_name = None
    @property
    def user_name(self):
        """
        Name of the user.
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _access_rights = None
    @property
    def access_rights(self):
        """
        User access rights. The format of the rights
        can be Unix-style combinations of r w x - or
        NT-style "No Access", "Read", "Change", and
        "Full Control".
        """
        return self._access_rights
    @access_rights.setter
    def access_rights(self, val):
        if val != None:
            self.validate('access_rights', val)
        self._access_rights = val
    
    _unix_group_name = None
    @property
    def unix_group_name(self):
        """
        Name of the Unix group.
        """
        return self._unix_group_name
    @unix_group_name.setter
    def unix_group_name(self, val):
        if val != None:
            self.validate('unix_group_name', val)
        self._unix_group_name = val
    
    @staticmethod
    def get_api_name():
          return "access-rights-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-name',
            'access-rights',
            'unix-group-name',
        ]
    
    def describe_properties(self):
        return {
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'access_rights': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'unix_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
