from netapp.netapp_object import NetAppObject

class KerberosRealm(NetAppObject):
    """
    Kerberos realm configuration specifies the locations of Key
    Distribution Center (KDC) servers and administration daemons for
    the Kerberos realms of interest.
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
    
    _kdc_ip = None
    @property
    def kdc_ip(self):
        """
        IP address of the Key Distribution Centre (KDC) server
        for this Kerberos realm.
        Attributes: required-for-create, modifiable
        """
        return self._kdc_ip
    @kdc_ip.setter
    def kdc_ip(self, val):
        if val != None:
            self.validate('kdc_ip', val)
        self._kdc_ip = val
    
    _comment = None
    @property
    def comment(self):
        """
        Comment
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _realm = None
    @property
    def realm(self):
        """
        Kerberos realm name.
        Attributes: required-for-create, modifiable
        """
        return self._realm
    @realm.setter
    def realm(self, val):
        if val != None:
            self.validate('realm', val)
        self._realm = val
    
    _kdc_vendor = None
    @property
    def kdc_vendor(self):
        """
        The vendor of the Key Distribution Centre (KDC) server.
        If the configuration uses a Microsoft Active Directory
        (AD) domain for authentication, this field should be
        'microsoft'.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "microsoft" ,
        <li> "other"
        </ul>
        """
        return self._kdc_vendor
    @kdc_vendor.setter
    def kdc_vendor(self, val):
        if val != None:
            self.validate('kdc_vendor', val)
        self._kdc_vendor = val
    
    _clock_skew = None
    @property
    def clock_skew(self):
        """
        The clock skew in minutes is the tolerance for accepting
        tickets with time stamps that do not exactly match the
        host's system clock. The default for this parameter is 5
        minutes.
        Attributes: optional-for-create, modifiable
        """
        return self._clock_skew
    @clock_skew.setter
    def clock_skew(self, val):
        if val != None:
            self.validate('clock_skew', val)
        self._clock_skew = val
    
    _admin_server_port = None
    @property
    def admin_server_port(self):
        """
        The TCP port on the Kerberos administration server where
        the Kerberos administration service is running. The
        default for this parmater is 749.
        Attributes: optional-for-create, modifiable
        """
        return self._admin_server_port
    @admin_server_port.setter
    def admin_server_port(self, val):
        if val != None:
            self.validate('admin_server_port', val)
        self._admin_server_port = val
    
    _password_server_ip = None
    @property
    def password_server_ip(self):
        """
        IP address of the host where the Kerberos
        password-changing server is running. Typically, this is
        the same as the host indicated in the adminserver-ip. If
        this parameter is omitted, the IP address in kdc-ip is
        used.
        Attributes: optional-for-create, modifiable
        """
        return self._password_server_ip
    @password_server_ip.setter
    def password_server_ip(self, val):
        if val != None:
            self.validate('password_server_ip', val)
        self._password_server_ip = val
    
    _admin_server_ip = None
    @property
    def admin_server_ip(self):
        """
        IP address of the host where the Kerberos administration
        daemon is running. This is usually the master KDC. If
        this parameter is omitted, the IP address specified in
        kdc-ip is used. If specified, this should be the same as
        the kdc-ip if the kdc-vendor is 'microsoft'.
        Attributes: optional-for-create, modifiable
        """
        return self._admin_server_ip
    @admin_server_ip.setter
    def admin_server_ip(self, val):
        if val != None:
            self.validate('admin_server_ip', val)
        self._admin_server_ip = val
    
    _kdc_port = None
    @property
    def kdc_port(self):
        """
        TCP port on the KDC to be used for Kerberos
        communication. The default for this parameter is 88.
        Attributes: optional-for-create, modifiable
        """
        return self._kdc_port
    @kdc_port.setter
    def kdc_port(self, val):
        if val != None:
            self.validate('kdc_port', val)
        self._kdc_port = val
    
    _ad_server_name = None
    @property
    def ad_server_name(self):
        """
        Host name of the Active Directory Domain Controller (DC).
        This is a mandatory parameter if the kdc-vendor is
        'microsoft'
        Attributes: optional-for-create, modifiable
        """
        return self._ad_server_name
    @ad_server_name.setter
    def ad_server_name(self, val):
        if val != None:
            self.validate('ad_server_name', val)
        self._ad_server_name = val
    
    _password_server_port = None
    @property
    def password_server_port(self):
        """
        The TCP port on the Kerberos password-changing server
        where the Kerberos password-changing service is running.
        The default for this parameter is 464.
        Attributes: optional-for-create, modifiable
        """
        return self._password_server_port
    @password_server_port.setter
    def password_server_port(self, val):
        if val != None:
            self.validate('password_server_port', val)
        self._password_server_port = val
    
    _config_name = None
    @property
    def config_name(self):
        """
        Kerberos configuration name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._config_name
    @config_name.setter
    def config_name(self, val):
        if val != None:
            self.validate('config_name', val)
        self._config_name = val
    
    _ad_server_ip = None
    @property
    def ad_server_ip(self):
        """
        IP Address of the Active Directory Domain Controller
        (DC). This is a mandatory parameter if the kdc-vendor is
        'microsoft'.
        Attributes: optional-for-create, modifiable
        """
        return self._ad_server_ip
    @ad_server_ip.setter
    def ad_server_ip(self, val):
        if val != None:
            self.validate('ad_server_ip', val)
        self._ad_server_ip = val
    
    @staticmethod
    def get_api_name():
          return "kerberos-realm"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'kdc-ip',
            'comment',
            'realm',
            'kdc-vendor',
            'clock-skew',
            'admin-server-port',
            'password-server-ip',
            'admin-server-ip',
            'kdc-port',
            'ad-server-name',
            'password-server-port',
            'config-name',
            'ad-server-ip',
        ]
    
    def describe_properties(self):
        return {
            'kdc_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'realm': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kdc_vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'clock_skew': { 'class': int, 'is_list': False, 'required': 'optional' },
            'admin_server_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'password_server_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'admin_server_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kdc_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ad_server_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'password_server_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'config_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ad_server_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
