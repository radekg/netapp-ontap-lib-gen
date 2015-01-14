from netapp.netapp_object import NetAppObject

class SecurityLoginAccountInfo(NetAppObject):
    """
    User account information
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
    
    _comment = None
    @property
    def comment(self):
        """
        Comments for the user account. The length of comment
        should be less than or equal to 128 charaters.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _user_name = None
    @property
    def user_name(self):
        """
        Name of the user.
        When creating a SNMPv1 or SNMPv2 user with 'snmp'
        application and 'community' authentication-method, the
        user name is the community string.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _authentication_method = None
    @property
    def authentication_method(self):
        """
        Authentication method for the application.
        Possible values: 'community', 'password', 'publickey',
        'domain', 'nsswitch' and 'usm'.
        Not all authentication methods are valid for an
        application. Valid authentication methods for each
        application are:
        'password' for 'console' application.
        'password', 'domain', 'nsswitch', 'cert' for 'http'
        application.
        'password', 'domain', 'nsswitch', 'cert'  for 'ontapi'
        application.
        'community' for 'snmp' application (when creating SNMPv1
        and SNMPv2 users).
        'usm' and 'community' for 'snmp' application (when
        creating SNMPv3 users).
        'password' for 'sp' application.
        'password' for 'rsh' application.
        'password' for 'telnet' application.
        'password', 'publickey', 'domain', 'nsswitch' for 'ssh'
        application.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._authentication_method
    @authentication_method.setter
    def authentication_method(self, val):
        if val != None:
            self.validate('authentication_method', val)
        self._authentication_method = val
    
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
    
    _application = None
    @property
    def application(self):
        """
        Name of the application. Possible
        values: 'console', 'http', 'ontapi', 'rsh',
        'snmp', 'sp', 'ssh', 'telnet'.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._application
    @application.setter
    def application(self, val):
        if val != None:
            self.validate('application', val)
        self._application = val
    
    _role_name = None
    @property
    def role_name(self):
        """
        Name of the role.
        Attributes: required-for-create, modifiable
        """
        return self._role_name
    @role_name.setter
    def role_name(self, val):
        if val != None:
            self.validate('role_name', val)
        self._role_name = val
    
    _is_locked = None
    @property
    def is_locked(self):
        """
        Account Locked
        Attributes: non-creatable, non-modifiable
        """
        return self._is_locked
    @is_locked.setter
    def is_locked(self, val):
        if val != None:
            self.validate('is_locked', val)
        self._is_locked = val
    
    @staticmethod
    def get_api_name():
          return "security-login-account-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'user-name',
            'authentication-method',
            'vserver',
            'application',
            'role-name',
            'is-locked',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'authentication_method': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'application': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'role_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_locked': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
