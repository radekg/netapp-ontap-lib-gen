from netapp.netapp_object import NetAppObject

class FpolicyExternalEngineInfo(NetAppObject):
    """
    External engine configuration and management.
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
    
    _engine_name = None
    @property
    def engine_name(self):
        """
        Name of the external engine.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._engine_name
    @engine_name.setter
    def engine_name(self, val):
        if val != None:
            self.validate('engine_name', val)
        self._engine_name = val
    
    _certificate_serial = None
    @property
    def certificate_serial(self):
        """
        Serial number of certificate. No default value is set for
        this field.
        Attributes: optional-for-create, modifiable
        """
        return self._certificate_serial
    @certificate_serial.setter
    def certificate_serial(self, val):
        if val != None:
            self.validate('certificate_serial', val)
        self._certificate_serial = val
    
    _server_progress_timeout = None
    @property
    def server_progress_timeout(self):
        """
        Timeout in seconds in which a throttled FPolicy server
        must complete at least one screen request. If no request
        is processed within the timeout, connection to FPolicy
        server is terminated. Default value set for this field is
        60 seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._server_progress_timeout
    @server_progress_timeout.setter
    def server_progress_timeout(self, val):
        if val != None:
            self.validate('server_progress_timeout', val)
        self._server_progress_timeout = val
    
    _secondary_servers = None
    @property
    def secondary_servers(self):
        """
        Secondary FPolicy servers. No default value is set for
        this field.
        Attributes: optional-for-create, modifiable
        """
        return self._secondary_servers
    @secondary_servers.setter
    def secondary_servers(self, val):
        if val != None:
            self.validate('secondary_servers', val)
        self._secondary_servers = val
    
    _certificate_ca = None
    @property
    def certificate_ca(self):
        """
        Certificate authority name. No default value is set for
        this field.
        Attributes: optional-for-create, modifiable
        """
        return self._certificate_ca
    @certificate_ca.setter
    def certificate_ca(self, val):
        if val != None:
            self.validate('certificate_ca', val)
        self._certificate_ca = val
    
    _request_cancel_timeout = None
    @property
    def request_cancel_timeout(self):
        """
        Timeout in seconds for a screen request to be processed
        by an FPolicy server. Default value set for this field is
        20 seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._request_cancel_timeout
    @request_cancel_timeout.setter
    def request_cancel_timeout(self, val):
        if val != None:
            self.validate('request_cancel_timeout', val)
        self._request_cancel_timeout = val
    
    _port_number = None
    @property
    def port_number(self):
        """
        Port number of the FPolicy server application.
        Attributes: required-for-create, modifiable
        """
        return self._port_number
    @port_number.setter
    def port_number(self, val):
        if val != None:
            self.validate('port_number', val)
        self._port_number = val
    
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
    
    _keep_alive_interval = None
    @property
    def keep_alive_interval(self):
        """
        Interval time in seconds for storage appliance to send
        keep-alive message to FPolicy server. Default value set
        for this field is 10 seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._keep_alive_interval
    @keep_alive_interval.setter
    def keep_alive_interval(self, val):
        if val != None:
            self.validate('keep_alive_interval', val)
        self._keep_alive_interval = val
    
    _primary_servers = None
    @property
    def primary_servers(self):
        """
        Primary FPolicy servers.
        Attributes: required-for-create, modifiable
        """
        return self._primary_servers
    @primary_servers.setter
    def primary_servers(self, val):
        if val != None:
            self.validate('primary_servers', val)
        self._primary_servers = val
    
    _extern_engine_type = None
    @property
    def extern_engine_type(self):
        """
        External engine type. If the engine is asynchronous, no
        reply is sent from FPolicy servers. Default value set for
        this field is synchronous.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "synchronous"    - Synchronous External Engine,
        <li> "asynchronous"   - Asynchronous External Engine
        </ul>
        """
        return self._extern_engine_type
    @extern_engine_type.setter
    def extern_engine_type(self, val):
        if val != None:
            self.validate('extern_engine_type', val)
        self._extern_engine_type = val
    
    _max_connection_retries = None
    @property
    def max_connection_retries(self):
        """
        Number of times storage appliance will attempt to
        establish a broken connection to FPolicy server. Default
        value set for this field is 5.
        Attributes: optional-for-create, modifiable
        """
        return self._max_connection_retries
    @max_connection_retries.setter
    def max_connection_retries(self, val):
        if val != None:
            self.validate('max_connection_retries', val)
        self._max_connection_retries = val
    
    _request_abort_timeout = None
    @property
    def request_abort_timeout(self):
        """
        Timeout in seconds for a screen request to be aborted by
        storage appliance. Default value set for this field is 40
        seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._request_abort_timeout
    @request_abort_timeout.setter
    def request_abort_timeout(self, val):
        if val != None:
            self.validate('request_abort_timeout', val)
        self._request_abort_timeout = val
    
    _ssl_option = None
    @property
    def ssl_option(self):
        """
        SSL option for external communication. No default value
        is set for this field.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "no_auth"        - Communication over TCP,
        <li> "server_auth"    - Authentication of FPolicy
        server only,
        <li> "mutual_auth"    - Mutual authentication of
        storage system and FPolicy server
        </ul>
        """
        return self._ssl_option
    @ssl_option.setter
    def ssl_option(self, val):
        if val != None:
            self.validate('ssl_option', val)
        self._ssl_option = val
    
    _certificate_common_name = None
    @property
    def certificate_common_name(self):
        """
        FQDN or custom common name of certificate. No default
        value is set for this field.
        Attributes: optional-for-create, modifiable
        """
        return self._certificate_common_name
    @certificate_common_name.setter
    def certificate_common_name(self, val):
        if val != None:
            self.validate('certificate_common_name', val)
        self._certificate_common_name = val
    
    _max_server_requests = None
    @property
    def max_server_requests(self):
        """
        Maximum number of outstanding screen requests that will
        be queued for an FPolicy Server. Default value set for
        this field is 50.
        Attributes: optional-for-create, modifiable
        """
        return self._max_server_requests
    @max_server_requests.setter
    def max_server_requests(self, val):
        if val != None:
            self.validate('max_server_requests', val)
        self._max_server_requests = val
    
    _status_request_interval = None
    @property
    def status_request_interval(self):
        """
        Interval time in seconds for storage appliance to query
        status request from FPolicy server. Default value set for
        this field is 10 seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._status_request_interval
    @status_request_interval.setter
    def status_request_interval(self, val):
        if val != None:
            self.validate('status_request_interval', val)
        self._status_request_interval = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-external-engine-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'engine-name',
            'certificate-serial',
            'server-progress-timeout',
            'secondary-servers',
            'certificate-ca',
            'request-cancel-timeout',
            'port-number',
            'vserver',
            'keep-alive-interval',
            'primary-servers',
            'extern-engine-type',
            'max-connection-retries',
            'request-abort-timeout',
            'ssl-option',
            'certificate-common-name',
            'max-server-requests',
            'status-request-interval',
        ]
    
    def describe_properties(self):
        return {
            'engine_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'certificate_serial': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_progress_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'secondary_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'certificate_ca': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'request_cancel_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'keep_alive_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'primary_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'extern_engine_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_connection_retries': { 'class': int, 'is_list': False, 'required': 'optional' },
            'request_abort_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ssl_option': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'certificate_common_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_server_requests': { 'class': int, 'is_list': False, 'required': 'optional' },
            'status_request_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
