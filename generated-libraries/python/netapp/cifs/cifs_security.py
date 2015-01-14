from netapp.netapp_object import NetAppObject

class CifsSecurity(NetAppObject):
    """
    CIFS security tunable parameters.
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
    
    _kerberos_renew_age = None
    @property
    def kerberos_renew_age(self):
        """
        This option determines the maximum amount of time in days
        for which a ticket can be renewed.
        Attributes: non-creatable, modifiable
        """
        return self._kerberos_renew_age
    @kerberos_renew_age.setter
    def kerberos_renew_age(self, val):
        if val != None:
            self.validate('kerberos_renew_age', val)
        self._kerberos_renew_age = val
    
    _use_start_tls_for_ad_ldap = None
    @property
    def use_start_tls_for_ad_ldap(self):
        """
        This option determines whether to use start-tls for AD
        LDAP connections. By default this option is false.
        Attributes: non-creatable, modifiable
        """
        return self._use_start_tls_for_ad_ldap
    @use_start_tls_for_ad_ldap.setter
    def use_start_tls_for_ad_ldap(self, val):
        if val != None:
            self.validate('use_start_tls_for_ad_ldap', val)
        self._use_start_tls_for_ad_ldap = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _kerberos_ticket_age = None
    @property
    def kerberos_ticket_age(self):
        """
        This option determines the maximum amount of time in
        hours that a user's ticket may be used for the purpose of
        Kerberos authentication.
        Attributes: non-creatable, modifiable
        """
        return self._kerberos_ticket_age
    @kerberos_ticket_age.setter
    def kerberos_ticket_age(self, val):
        if val != None:
            self.validate('kerberos_ticket_age', val)
        self._kerberos_ticket_age = val
    
    _is_signing_required = None
    @property
    def is_signing_required(self):
        """
        This option determines whether signing is required for
        incoming CIFS traffic. By default this option is false.
        Attributes: non-creatable, modifiable
        """
        return self._is_signing_required
    @is_signing_required.setter
    def is_signing_required(self, val):
        if val != None:
            self.validate('is_signing_required', val)
        self._is_signing_required = val
    
    _is_password_complexity_required = None
    @property
    def is_password_complexity_required(self):
        """
        This option determines whether password complexity is
        required for local users. By default this option is
        true.
        Attributes: non-creatable, modifiable
        """
        return self._is_password_complexity_required
    @is_password_complexity_required.setter
    def is_password_complexity_required(self, val):
        if val != None:
            self.validate('is_password_complexity_required', val)
        self._is_password_complexity_required = val
    
    _kerberos_clock_skew = None
    @property
    def kerberos_clock_skew(self):
        """
        The clock skew in minutes is the tolerance for accepting
        tickets with time stamps that do not exactly match the
        host's system clock.
        Attributes: non-creatable, modifiable
        """
        return self._kerberos_clock_skew
    @kerberos_clock_skew.setter
    def kerberos_clock_skew(self, val):
        if val != None:
            self.validate('kerberos_clock_skew', val)
        self._kerberos_clock_skew = val
    
    @staticmethod
    def get_api_name():
          return "cifs-security"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'kerberos-renew-age',
            'use-start-tls-for-ad-ldap',
            'vserver',
            'kerberos-ticket-age',
            'is-signing-required',
            'is-password-complexity-required',
            'kerberos-clock-skew',
        ]
    
    def describe_properties(self):
        return {
            'kerberos_renew_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'use_start_tls_for_ad_ldap': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kerberos_ticket_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_signing_required': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_password_complexity_required': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'kerberos_clock_skew': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
