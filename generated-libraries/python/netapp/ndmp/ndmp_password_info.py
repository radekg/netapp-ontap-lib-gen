from netapp.netapp_object import NetAppObject

class NdmpPasswordInfo(NetAppObject):
    """
    Information about generate password
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
    
    _user_name = None
    @property
    def user_name(self):
        """
        The user for which the password is to be generated.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _password = None
    @property
    def password(self):
        """
        The generated NDMP password for the given user. The
        command fails if such a user does not exist in the
        Vserver context.
        Attributes: non-creatable, non-modifiable
        """
        return self._password
    @password.setter
    def password(self, val):
        if val != None:
            self.validate('password', val)
        self._password = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        The Vserver on which the user password is to be generated
        for the given user.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    @staticmethod
    def get_api_name():
          return "ndmp-password-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-name',
            'password',
            'vserver-name',
        ]
    
    def describe_properties(self):
        return {
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
