from netapp.netapp_object import NetAppObject

class VscanScannerPoolInfo(NetAppObject):
    """
    Vscan scanner pool information.
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
    
    _admin_owner = None
    @property
    def admin_owner(self):
        """
        Owner of the scanner pool.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "vserver"   - Vserver Admin,
        <li> "cluster"   - Cluter Admin
        </ul>
        """
        return self._admin_owner
    @admin_owner.setter
    def admin_owner(self, val):
        if val != None:
            self.validate('admin_owner', val)
        self._admin_owner = val
    
    _session_teardown_timeout = None
    @property
    def session_teardown_timeout(self):
        """
        Total session-teardown time-limit in seconds. The default
        value of 10 is taken if not provided while creating a
        scanner pool.
        Attributes: optional-for-create, modifiable
        """
        return self._session_teardown_timeout
    @session_teardown_timeout.setter
    def session_teardown_timeout(self, val):
        if val != None:
            self.validate('session_teardown_timeout', val)
        self._session_teardown_timeout = val
    
    _max_session_setup_retries = None
    @property
    def max_session_setup_retries(self):
        """
        Maximum number of consecutive session-setup attempts. The
        default value of 5 is taken if not provided while
        creating a scanner pool.
        Attributes: optional-for-create, modifiable
        """
        return self._max_session_setup_retries
    @max_session_setup_retries.setter
    def max_session_setup_retries(self, val):
        if val != None:
            self.validate('max_session_setup_retries', val)
        self._max_session_setup_retries = val
    
    _privileged_users = None
    @property
    def privileged_users(self):
        """
        List of privileged users.
        Attributes: required-for-create, modifiable
        """
        return self._privileged_users
    @privileged_users.setter
    def privileged_users(self, val):
        if val != None:
            self.validate('privileged_users', val)
        self._privileged_users = val
    
    _session_setup_timeout = None
    @property
    def session_setup_timeout(self):
        """
        Total session-setup time-limit in seconds. The default
        value of 10 is taken if not provided while creating a
        scanner pool.
        Attributes: optional-for-create, modifiable
        """
        return self._session_setup_timeout
    @session_setup_timeout.setter
    def session_setup_timeout(self, val):
        if val != None:
            self.validate('session_setup_timeout', val)
        self._session_setup_timeout = val
    
    _servers = None
    @property
    def servers(self):
        """
        List of IP addresses of Vscan servers which are allowed
        to connect to clustered Data ONTAP.
        Attributes: required-for-create, modifiable
        """
        return self._servers
    @servers.setter
    def servers(self, val):
        if val != None:
            self.validate('servers', val)
        self._servers = val
    
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
    
    _scanner_pool = None
    @property
    def scanner_pool(self):
        """
        Scanner pool is a set of attributes which are used to
        validate and manage connections between clustered Data
        ONTAP and Vscan servers (virus scanners).
        Attributes: key, required-for-create, non-modifiable
        """
        return self._scanner_pool
    @scanner_pool.setter
    def scanner_pool(self, val):
        if val != None:
            self.validate('scanner_pool', val)
        self._scanner_pool = val
    
    _scanner_policy = None
    @property
    def scanner_policy(self):
        """
        Scanner policy. Currently only system policies are
        supported.
        <p>
        Possible values:
        <ul>
        <li> 'primary'   - Makes it active always,
        <li> 'secondary' - Makes it active only when no
        primary Vscan server is connected,
        <li> 'idle'      - Makes it inactive always
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_policy
    @scanner_policy.setter
    def scanner_policy(self, val):
        if val != None:
            self.validate('scanner_policy', val)
        self._scanner_policy = val
    
    _request_timeout = None
    @property
    def request_timeout(self):
        """
        Total request-service time-limit in seconds. The default
        value of 30 is taken if not provided while creating a
        scanner pool.
        Attributes: optional-for-create, modifiable
        """
        return self._request_timeout
    @request_timeout.setter
    def request_timeout(self, val):
        if val != None:
            self.validate('request_timeout', val)
        self._request_timeout = val
    
    _is_currently_active = None
    @property
    def is_currently_active(self):
        """
        Current status of a scanner pool.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_currently_active
    @is_currently_active.setter
    def is_currently_active(self, val):
        if val != None:
            self.validate('is_currently_active', val)
        self._is_currently_active = val
    
    _scan_queue_timeout = None
    @property
    def scan_queue_timeout(self):
        """
        Scan-queue wait-time-limit in seconds. The default value
        of 20 is taken if not provided while creating a scanner
        pool.
        Attributes: optional-for-create, modifiable
        """
        return self._scan_queue_timeout
    @scan_queue_timeout.setter
    def scan_queue_timeout(self, val):
        if val != None:
            self.validate('scan_queue_timeout', val)
        self._scan_queue_timeout = val
    
    @staticmethod
    def get_api_name():
          return "vscan-scanner-pool-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'admin-owner',
            'session-teardown-timeout',
            'max-session-setup-retries',
            'privileged-users',
            'session-setup-timeout',
            'servers',
            'vserver',
            'scanner-pool',
            'scanner-policy',
            'request-timeout',
            'is-currently-active',
            'scan-queue-timeout',
        ]
    
    def describe_properties(self):
        return {
            'admin_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'session_teardown_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_session_setup_retries': { 'class': int, 'is_list': False, 'required': 'optional' },
            'privileged_users': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'session_setup_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scanner_pool': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scanner_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'request_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_currently_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'scan_queue_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
