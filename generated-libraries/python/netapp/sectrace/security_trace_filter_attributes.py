from netapp.netapp_object import NetAppObject

class SecurityTraceFilterAttributes(NetAppObject):
    """
    Security trace configuration.
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
    
    _index = None
    @property
    def index(self):
        """
        internally created index for the filter.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._index
    @index.setter
    def index(self, val):
        if val != None:
            self.validate('index', val)
        self._index = val
    
    _time_enabled = None
    @property
    def time_enabled(self):
        """
        The admin can specify a timeout for this filter after
        which it would be disabled.
        Attributes: optional-for-create, modifiable
        """
        return self._time_enabled
    @time_enabled.setter
    def time_enabled(self, val):
        if val != None:
            self.validate('time_enabled', val)
        self._time_enabled = val
    
    _client_ip = None
    @property
    def client_ip(self):
        """
        The IP address of the client.
        Attributes: optional-for-create, modifiable
        """
        return self._client_ip
    @client_ip.setter
    def client_ip(self, val):
        if val != None:
            self.validate('client_ip', val)
        self._client_ip = val
    
    _enabled = None
    @property
    def enabled(self):
        """
        This is used to enable or disable the filter.
        Attributes: optional-for-create, modifiable
        """
        return self._enabled
    @enabled.setter
    def enabled(self, val):
        if val != None:
            self.validate('enabled', val)
        self._enabled = val
    
    _windows_name = None
    @property
    def windows_name(self):
        """
        Windows User Name to trace.
        Attributes: optional-for-create, modifiable
        """
        return self._windows_name
    @windows_name.setter
    def windows_name(self, val):
        if val != None:
            self.validate('windows_name', val)
        self._windows_name = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver on which the permission tracing is applied.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _unix_name = None
    @property
    def unix_name(self):
        """
        Unix user name to trace.
        Attributes: optional-for-create, modifiable
        """
        return self._unix_name
    @unix_name.setter
    def unix_name(self, val):
        if val != None:
            self.validate('unix_name', val)
        self._unix_name = val
    
    _path = None
    @property
    def path(self):
        """
        Path to match.
        Attributes: optional-for-create, modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _trace_allow = None
    @property
    def trace_allow(self):
        """
        The deny events are traced by default. This option is to
        record trace results for allow events as well.
        Attributes: optional-for-create, modifiable
        """
        return self._trace_allow
    @trace_allow.setter
    def trace_allow(self, val):
        if val != None:
            self.validate('trace_allow', val)
        self._trace_allow = val
    
    @staticmethod
    def get_api_name():
          return "security-trace-filter-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'index',
            'time-enabled',
            'client-ip',
            'enabled',
            'windows-name',
            'vserver',
            'unix-name',
            'path',
            'trace-allow',
        ]
    
    def describe_properties(self):
        return {
            'index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time_enabled': { 'class': int, 'is_list': False, 'required': 'optional' },
            'client_ip': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enabled': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'windows_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'unix_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trace_allow': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
