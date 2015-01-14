from netapp.netapp_object import NetAppObject

class QuotaUser(NetAppObject):
    """
    Information about a quota user or group.
    """
    
    _quota_user_name = None
    @property
    def quota_user_name(self):
        """
        Name of the user, group, or sid.
        """
        return self._quota_user_name
    @quota_user_name.setter
    def quota_user_name(self, val):
        if val != None:
            self.validate('quota_user_name', val)
        self._quota_user_name = val
    
    _quota_user_type = None
    @property
    def quota_user_type(self):
        """
        The type of quota user.  There are
        two possible values: sid (for Windows
        users), uid (for UNIX users), and gid (for UNIX groups).
        """
        return self._quota_user_type
    @quota_user_type.setter
    def quota_user_type(self, val):
        if val != None:
            self.validate('quota_user_type', val)
        self._quota_user_type = val
    
    _quota_user_id = None
    @property
    def quota_user_id(self):
        """
        The id of the user.  The quota-user-type
        determines the format.  For uid and gid, the
        format is an integer.  For sid, the format
        is the usual "S-*" style.
        """
        return self._quota_user_id
    @quota_user_id.setter
    def quota_user_id(self, val):
        if val != None:
            self.validate('quota_user_id', val)
        self._quota_user_id = val
    
    @staticmethod
    def get_api_name():
          return "quota-user"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'quota-user-name',
            'quota-user-type',
            'quota-user-id',
        ]
    
    def describe_properties(self):
        return {
            'quota_user_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'quota_user_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'quota_user_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
