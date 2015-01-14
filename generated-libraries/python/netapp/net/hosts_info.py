from netapp.netapp_object import NetAppObject

class HostsInfo(NetAppObject):
    """
    Name attributes for one host
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
    
    _hostname = None
    @property
    def hostname(self):
        """
        Canonical hostname in a simple string or in FQDN
        Attributes: required-for-create, modifiable
        """
        return self._hostname
    @hostname.setter
    def hostname(self, val):
        if val != None:
            self.validate('hostname', val)
        self._hostname = val
    
    _host_ip_address = None
    @property
    def host_ip_address(self):
        """
        IPv4 address in dotted form as '123.123.123.123'.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._host_ip_address
    @host_ip_address.setter
    def host_ip_address(self, val):
        if val != None:
            self.validate('host_ip_address', val)
        self._host_ip_address = val
    
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
    
    _aliases = None
    @property
    def aliases(self):
        """
        The list of aliases such as 'host1.sales.foo.com'.
        Attributes: optional-for-create, modifiable
        """
        return self._aliases
    @aliases.setter
    def aliases(self, val):
        if val != None:
            self.validate('aliases', val)
        self._aliases = val
    
    @staticmethod
    def get_api_name():
          return "hosts-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hostname',
            'host-ip-address',
            'vserver-name',
            'aliases',
        ]
    
    def describe_properties(self):
        return {
            'hostname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'host_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aliases': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
