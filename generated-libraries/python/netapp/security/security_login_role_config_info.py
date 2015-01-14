from netapp.netapp_object import NetAppObject

class SecurityLoginRoleConfigInfo(NetAppObject):
    """
    User role configuration information.
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
    
    _min_username_size = None
    @property
    def min_username_size(self):
        """
        The minimum length of the user name. Possible values
        range from 3 to 16 characters. The default setting is 3
        characters.
        Attributes: non-creatable, modifiable
        """
        return self._min_username_size
    @min_username_size.setter
    def min_username_size(self, val):
        if val != None:
            self.validate('min_username_size', val)
        self._min_username_size = val
    
    _require_initial_password_update = None
    @property
    def require_initial_password_update(self):
        """
        This optionally specifies to change the password upon
        first-login to the storage controller from SSH or
        serial-console. Default is false.
        Attributes: non-creatable, modifiable
        """
        return self._require_initial_password_update
    @require_initial_password_update.setter
    def require_initial_password_update(self, val):
        if val != None:
            self.validate('require_initial_password_update', val)
        self._require_initial_password_update = val
    
    _change_password_duration_in_days = None
    @property
    def change_password_duration_in_days(self):
        """
        This optionally specifies the number of days that must
        pass between password changes. The default setting is 0
        (zero) meaning the user is allowed to change the password
        immediately.
        Attributes: non-creatable, modifiable
        """
        return self._change_password_duration_in_days
    @change_password_duration_in_days.setter
    def change_password_duration_in_days(self, val):
        if val != None:
            self.validate('change_password_duration_in_days', val)
        self._change_password_duration_in_days = val
    
    _password_expiration_duration = None
    @property
    def password_expiration_duration(self):
        """
        This optionally specifies the password expiry in days. A
        value of 0 means it expiries now. Default is 2^32-1 (ie.,
        never expire).
        Attributes: non-creatable, modifiable
        """
        return self._password_expiration_duration
    @password_expiration_duration.setter
    def password_expiration_duration(self, val):
        if val != None:
            self.validate('password_expiration_duration', val)
        self._password_expiration_duration = val
    
    _last_passwords_disallowed_count = None
    @property
    def last_passwords_disallowed_count(self):
        """
        This optionally specifies the number of previous
        passwords that are disallowed for reuse. The default
        setting is 6.
        Attributes: non-creatable, modifiable
        """
        return self._last_passwords_disallowed_count
    @last_passwords_disallowed_count.setter
    def last_passwords_disallowed_count(self, val):
        if val != None:
            self.validate('last_passwords_disallowed_count', val)
        self._last_passwords_disallowed_count = val
    
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
    
    _require_username_alpha_numeric = None
    @property
    def require_username_alpha_numeric(self):
        """
        If this field is set it specifies that the username must
        have atleast 1 alpha and 1 numeric character.
        Attributes: non-creatable, modifiable
        """
        return self._require_username_alpha_numeric
    @require_username_alpha_numeric.setter
    def require_username_alpha_numeric(self, val):
        if val != None:
            self.validate('require_username_alpha_numeric', val)
        self._require_username_alpha_numeric = val
    
    _max_failed_login_attempts = None
    @property
    def max_failed_login_attempts(self):
        """
        This optionally specifies the maximum number of invalid
        login attempts after which the account gets locked.
        Default is 0.
        Attributes: non-creatable, modifiable
        """
        return self._max_failed_login_attempts
    @max_failed_login_attempts.setter
    def max_failed_login_attempts(self, val):
        if val != None:
            self.validate('max_failed_login_attempts', val)
        self._max_failed_login_attempts = val
    
    _role_name = None
    @property
    def role_name(self):
        """
        Name of the role.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._role_name
    @role_name.setter
    def role_name(self, val):
        if val != None:
            self.validate('role_name', val)
        self._role_name = val
    
    _lockout_duration = None
    @property
    def lockout_duration(self):
        """
        This optionally specifies the number of days to lock the
        account if maximum number of failed attempts occur.
        Default is 0.
        Attributes: non-creatable, modifiable
        """
        return self._lockout_duration
    @lockout_duration.setter
    def lockout_duration(self, val):
        if val != None:
            self.validate('lockout_duration', val)
        self._lockout_duration = val
    
    _min_password_size = None
    @property
    def min_password_size(self):
        """
        This optionally specifies the minimum length of the
        password. Possible values range from 3 to 64 characters.
        The default setting is 8 characters.
        Attributes: non-creatable, modifiable
        """
        return self._min_password_size
    @min_password_size.setter
    def min_password_size(self, val):
        if val != None:
            self.validate('min_password_size', val)
        self._min_password_size = val
    
    _require_password_alpha_numeric = None
    @property
    def require_password_alpha_numeric(self):
        """
        If this field is set it specifies that the password must
        have atleast 1 alpha and 1 numeric character.
        Attributes: non-creatable, modifiable
        """
        return self._require_password_alpha_numeric
    @require_password_alpha_numeric.setter
    def require_password_alpha_numeric(self, val):
        if val != None:
            self.validate('require_password_alpha_numeric', val)
        self._require_password_alpha_numeric = val
    
    _min_passwd_specialchar = None
    @property
    def min_passwd_specialchar(self):
        """
        This optionally specifies the minimum special characters
        required in password. The default setting is no special
        chars i.e. 0.
        Attributes: non-creatable, modifiable
        """
        return self._min_passwd_specialchar
    @min_passwd_specialchar.setter
    def min_passwd_specialchar(self, val):
        if val != None:
            self.validate('min_passwd_specialchar', val)
        self._min_passwd_specialchar = val
    
    @staticmethod
    def get_api_name():
          return "security-login-role-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'min-username-size',
            'require-initial-password-update',
            'change-password-duration-in-days',
            'password-expiration-duration',
            'last-passwords-disallowed-count',
            'vserver',
            'require-username-alpha-numeric',
            'max-failed-login-attempts',
            'role-name',
            'lockout-duration',
            'min-password-size',
            'require-password-alpha-numeric',
            'min-passwd-specialchar',
        ]
    
    def describe_properties(self):
        return {
            'min_username_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'require_initial_password_update': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'change_password_duration_in_days': { 'class': int, 'is_list': False, 'required': 'optional' },
            'password_expiration_duration': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_passwords_disallowed_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'require_username_alpha_numeric': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_failed_login_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'role_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lockout_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'min_password_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'require_password_alpha_numeric': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'min_passwd_specialchar': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
