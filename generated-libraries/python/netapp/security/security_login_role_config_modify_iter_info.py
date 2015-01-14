from netapp.security.security_login_role_config_info import SecurityLoginRoleConfigInfo
from netapp.netapp_object import NetAppObject

class SecurityLoginRoleConfigModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against security login roleconfig object.
    query, but were not modified due to some error.
    modified due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the modify operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _security_key = None
    @property
    def security_key(self):
        """
        The keys for the security login roleconfig object to
        which the modify operation applies.
        """
        return self._security_key
    @security_key.setter
    def security_key(self, val):
        if val != None:
            self.validate('security_key', val)
        self._security_key = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the modify operation caused an
        error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "security-login-role-config-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'security-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'security_key': { 'class': SecurityLoginRoleConfigInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
