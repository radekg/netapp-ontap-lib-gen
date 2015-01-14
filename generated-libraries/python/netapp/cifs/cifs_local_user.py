from netapp.netapp_object import NetAppObject

class CifsLocalUser(NetAppObject):
    """
    List of local users, organized by Vserver
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
        Vserver
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
        Full name of the local user
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
        The name of the local user
        Attributes: key, required-for-create, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _is_account_disabled = None
    @property
    def is_account_disabled(self):
        """
        The user account is disabled
        Attributes: optional-for-create, modifiable
        """
        return self._is_account_disabled
    @is_account_disabled.setter
    def is_account_disabled(self, val):
        if val != None:
            self.validate('is_account_disabled', val)
        self._is_account_disabled = val
    
    _description = None
    @property
    def description(self):
        """
        The description of the local user
        Attributes: optional-for-create, modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    @staticmethod
    def get_api_name():
          return "cifs-local-user"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'full-name',
            'user-name',
            'is-account-disabled',
            'description',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'full_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_account_disabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
