from netapp.netapp_object import NetAppObject

class UnixUserInfo(NetAppObject):
    """
    UNIX user information
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
        Specifies the Vserver for the UNIX user.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _full_name = None
    @property
    def full_name(self):
        """
        Specifies the full name of the UNIX user.
        Attributes: optional-for-create, modifiable
        """
        return self._full_name
    @full_name.setter
    def full_name(self, val):
        if val != None:
            self.validate('full_name', val)
        self._full_name = val
    
    _user_name = None
    @property
    def user_name(self):
        """
        Specifies user's UNIX account name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _user_id = None
    @property
    def user_id(self):
        """
        Specifies an identification number for the UNIX user.
        Attributes: required-for-create, modifiable
        """
        return self._user_id
    @user_id.setter
    def user_id(self, val):
        if val != None:
            self.validate('user_id', val)
        self._user_id = val
    
    _group_id = None
    @property
    def group_id(self):
        """
        Specifies the primary group identification number for the
        UNIX user.
        Attributes: required-for-create, modifiable
        """
        return self._group_id
    @group_id.setter
    def group_id(self, val):
        if val != None:
            self.validate('group_id', val)
        self._group_id = val
    
    @staticmethod
    def get_api_name():
          return "unix-user-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'full-name',
            'user-name',
            'user-id',
            'group-id',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'full_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
