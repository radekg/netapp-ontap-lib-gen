from netapp.netapp_object import NetAppObject

class VscanActiveScannerPoolInfo(NetAppObject):
    """
    Vscan active scanner pool information.
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
    
    _max_session_setup_retries = None
    @property
    def max_session_setup_retries(self):
        """
        Maximum number of consecutive session-setup attempts.
        This is set to the max of max-session-setup-retries of
        all active scanner pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._max_session_setup_retries
    @max_session_setup_retries.setter
    def max_session_setup_retries(self, val):
        if val != None:
            self.validate('max_session_setup_retries', val)
        self._max_session_setup_retries = val
    
    _session_teardown_timeout = None
    @property
    def session_teardown_timeout(self):
        """
        Total session-teardown time-limit in seconds. This is set
        to the max of the session-teardown-timeouts of all active
        scanner pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._session_teardown_timeout
    @session_teardown_timeout.setter
    def session_teardown_timeout(self, val):
        if val != None:
            self.validate('session_teardown_timeout', val)
        self._session_teardown_timeout = val
    
    _privileged_users = None
    @property
    def privileged_users(self):
        """
        List of privileged users for a vserver. Vscan server is
        given privileged access to the clustered Data ONTAP only
        if it uses one of these users.
        Attributes: non-creatable, non-modifiable
        """
        return self._privileged_users
    @privileged_users.setter
    def privileged_users(self, val):
        if val != None:
            self.validate('privileged_users', val)
        self._privileged_users = val
    
    _scanner_pools = None
    @property
    def scanner_pools(self):
        """
        List of active scanner pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._scanner_pools
    @scanner_pools.setter
    def scanner_pools(self, val):
        if val != None:
            self.validate('scanner_pools', val)
        self._scanner_pools = val
    
    _servers = None
    @property
    def servers(self):
        """
        List of allowed Vscan servers IP for a vserver. A Vscan
        server is allowed to connect to the clustered Data ONTAP
        only if its IP is part of this list.
        Attributes: non-creatable, non-modifiable
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
    
    _session_setup_timeout = None
    @property
    def session_setup_timeout(self):
        """
        Total session-setup time-limit in seconds. This is set to
        the max of the session-setup-timeouts of all active
        scanner pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._session_setup_timeout
    @session_setup_timeout.setter
    def session_setup_timeout(self, val):
        if val != None:
            self.validate('session_setup_timeout', val)
        self._session_setup_timeout = val
    
    _request_timeout = None
    @property
    def request_timeout(self):
        """
        Total request-service time-limit in seconds. This is set
        to the max of the request-timeouts of all active scanner
        pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._request_timeout
    @request_timeout.setter
    def request_timeout(self, val):
        if val != None:
            self.validate('request_timeout', val)
        self._request_timeout = val
    
    _scan_queue_timeout = None
    @property
    def scan_queue_timeout(self):
        """
        Scan-queue wait-time-limit in seconds. This is set to the
        max of the scan-queue-timeouts of all active scanner
        pools on a vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._scan_queue_timeout
    @scan_queue_timeout.setter
    def scan_queue_timeout(self, val):
        if val != None:
            self.validate('scan_queue_timeout', val)
        self._scan_queue_timeout = val
    
    @staticmethod
    def get_api_name():
          return "vscan-active-scanner-pool-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'max-session-setup-retries',
            'session-teardown-timeout',
            'privileged-users',
            'scanner-pools',
            'servers',
            'vserver',
            'session-setup-timeout',
            'request-timeout',
            'scan-queue-timeout',
        ]
    
    def describe_properties(self):
        return {
            'max_session_setup_retries': { 'class': int, 'is_list': False, 'required': 'optional' },
            'session_teardown_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'privileged_users': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'scanner_pools': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'session_setup_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'request_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_queue_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
