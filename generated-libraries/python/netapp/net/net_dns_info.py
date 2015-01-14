from netapp.netapp_object import NetAppObject

class NetDnsInfo(NetAppObject):
    """
    Contains DNS configuration information of a Vserver
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
    
    _dns_state = None
    @property
    def dns_state(self):
        """
        Enable/Disable DNS. Possible values are 'enabled' or
        'disabled'.
        Attributes: required-for-create, modifiable
        """
        return self._dns_state
    @dns_state.setter
    def dns_state(self, val):
        if val != None:
            self.validate('dns_state', val)
        self._dns_state = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _attempts = None
    @property
    def attempts(self):
        """
        Max number of trials before giving up and returning
        error. Default is one.
        Attributes: optional-for-create, modifiable
        """
        return self._attempts
    @attempts.setter
    def attempts(self, val):
        if val != None:
            self.validate('attempts', val)
        self._attempts = val
    
    _name_servers = None
    @property
    def name_servers(self):
        """
        IPv4 addresses of name servers such as
        '123.123.123.123'.
        Attributes: optional-for-create, modifiable
        """
        return self._name_servers
    @name_servers.setter
    def name_servers(self, val):
        if val != None:
            self.validate('name_servers', val)
        self._name_servers = val
    
    _timeout = None
    @property
    def timeout(self):
        """
        Number of seconds to wait for a response from a name
        server before trying a different name server. Default is
        two seconds.
        Attributes: optional-for-create, modifiable
        """
        return self._timeout
    @timeout.setter
    def timeout(self, val):
        if val != None:
            self.validate('timeout', val)
        self._timeout = val
    
    _domains = None
    @property
    def domains(self):
        """
        List of DNS domains such as 'sales.bar.com'. The first
        domain is the one that the Vserver belongs to.
        Attributes: required-for-create, modifiable
        """
        return self._domains
    @domains.setter
    def domains(self, val):
        if val != None:
            self.validate('domains', val)
        self._domains = val
    
    @staticmethod
    def get_api_name():
          return "net-dns-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'dns-state',
            'vserver-name',
            'attempts',
            'name-servers',
            'timeout',
            'domains',
        ]
    
    def describe_properties(self):
        return {
            'dns_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'name_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'domains': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
