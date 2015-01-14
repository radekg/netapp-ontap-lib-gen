from netapp.netapp_object import NetAppObject

class IscsiSecurityEntryInfo(NetAppObject):
    """
    Information about a single authentication entry.
    """
    
    _user_name = None
    @property
    def user_name(self):
        """
        Inbound CHAP user name, returned only if auth-type is CHAP.
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _auth_chap_policy = None
    @property
    def auth_chap_policy(self):
        """
        CHAP authentication path. Possible values: "local",
        "radius".
        """
        return self._auth_chap_policy
    @auth_chap_policy.setter
    def auth_chap_policy(self, val):
        if val != None:
            self.validate('auth_chap_policy', val)
        self._auth_chap_policy = val
    
    _initiator = None
    @property
    def initiator(self):
        """
        Name of initiator. The initiator name must conform to
        RFC 3720, for example:
        "iqn.1987-06.com.initvendor1:appsrv.sn.2346",
        or "default" if this is a default auth entry.
        """
        return self._initiator
    @initiator.setter
    def initiator(self, val):
        if val != None:
            self.validate('initiator', val)
        self._initiator = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing this authentication information.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _auth_type = None
    @property
    def auth_type(self):
        """
        Authentication type. Possible values: "CHAP", "none", "deny".
        """
        return self._auth_type
    @auth_type.setter
    def auth_type(self, val):
        if val != None:
            self.validate('auth_type', val)
        self._auth_type = val
    
    _outbound_user_name = None
    @property
    def outbound_user_name(self):
        """
        Outbound CHAP user name, returned only if auth-type is CHAP,
        and outbound authentication is set for initiator.
        """
        return self._outbound_user_name
    @outbound_user_name.setter
    def outbound_user_name(self, val):
        if val != None:
            self.validate('outbound_user_name', val)
        self._outbound_user_name = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-security-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-name',
            'auth-chap-policy',
            'initiator',
            'vserver',
            'auth-type',
            'outbound-user-name',
        ]
    
    def describe_properties(self):
        return {
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'auth_chap_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'auth_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'outbound_user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
