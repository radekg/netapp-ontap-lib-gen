from netapp.netapp_object import NetAppObject

class ServiceProcessorNetworkInfo(NetAppObject):
    """
    Service processor network configuration
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
    
    _node = None
    @property
    def node(self):
        """
        Node on which the device is located
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _status = None
    @property
    def status(self):
        """
        Current status of the device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "online"              - Device is up and running
        fine,
        <li> "offline"             - Device is out of
        communication,
        <li> "sp_daemon_offline"   - Daemon which communicates
        with the device is not running,
        <li> "node_offline"        - Node that hosts the device
        is out of communication,
        <li> "degraded"            - Node that hosts the device
        is missing heartbeat signals from the device,
        <li> "rebooting"           - Device is rebooting,
        <li> "unknown"             - Device status could not be
        determined
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _prefix_length = None
    @property
    def prefix_length(self):
        """
        Prefix length of subnet mask
        Attributes: non-creatable, modifiable
        """
        return self._prefix_length
    @prefix_length.setter
    def prefix_length(self, val):
        if val != None:
            self.validate('prefix_length', val)
        self._prefix_length = val
    
    _device_type = None
    @property
    def device_type(self):
        """
        Type of device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "rlm"  - Remote LAN Module,
        <li> "sp"   - Service Processor,
        <li> "none" - None
        </ul>
        """
        return self._device_type
    @device_type.setter
    def device_type(self, val):
        if val != None:
            self.validate('device_type', val)
        self._device_type = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        IP address currently held by the device
        Attributes: non-creatable, modifiable
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _address_type = None
    @property
    def address_type(self):
        """
        Network configuration that is being addressed i.e. IPv4
        or IPv6
        Attributes: key, non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "ipv4" - Internet Protocol version 4,
        <li> "ipv6" - Internet Protocol version 6
        </ul>
        """
        return self._address_type
    @address_type.setter
    def address_type(self, val):
        if val != None:
            self.validate('address_type', val)
        self._address_type = val
    
    _router_ip_address = None
    @property
    def router_ip_address(self):
        """
        Router assigned IP address
        Attributes: non-creatable, non-modifiable
        """
        return self._router_ip_address
    @router_ip_address.setter
    def router_ip_address(self, val):
        if val != None:
            self.validate('router_ip_address', val)
        self._router_ip_address = val
    
    _link_status = None
    @property
    def link_status(self):
        """
        Current status of the underlying network link used by
        this address
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "up"        - Link is connected,
        <li> "down"      - Link is severed,
        <li> "disabled"  - Link has been disabled by user,
        <li> "unknown"   - Link status is no known
        </ul>
        """
        return self._link_status
    @link_status.setter
    def link_status(self, val):
        if val != None:
            self.validate('link_status', val)
        self._link_status = val
    
    _netmask = None
    @property
    def netmask(self):
        """
        Netmask for the device
        Attributes: non-creatable, modifiable
        """
        return self._netmask
    @netmask.setter
    def netmask(self, val):
        if val != None:
            self.validate('netmask', val)
        self._netmask = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Is this address configuration enabled
        Attributes: non-creatable, modifiable
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _dhcp = None
    @property
    def dhcp(self):
        """
        DHCP status for the configuration
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "v4"   - DHCP for IPv4,
        <li> "none" - DHCP not enabled
        </ul>
        """
        return self._dhcp
    @dhcp.setter
    def dhcp(self, val):
        if val != None:
            self.validate('dhcp', val)
        self._dhcp = val
    
    _link_local_ip_address = None
    @property
    def link_local_ip_address(self):
        """
        Link local IP address
        Attributes: non-creatable, non-modifiable
        """
        return self._link_local_ip_address
    @link_local_ip_address.setter
    def link_local_ip_address(self, val):
        if val != None:
            self.validate('link_local_ip_address', val)
        self._link_local_ip_address = val
    
    _mac_address = None
    @property
    def mac_address(self):
        """
        MAC address of the device
        Attributes: non-creatable, non-modifiable
        """
        return self._mac_address
    @mac_address.setter
    def mac_address(self, val):
        if val != None:
            self.validate('mac_address', val)
        self._mac_address = val
    
    _gateway_ip_address = None
    @property
    def gateway_ip_address(self):
        """
        IP address of the network gateway
        Attributes: non-creatable, modifiable
        """
        return self._gateway_ip_address
    @gateway_ip_address.setter
    def gateway_ip_address(self, val):
        if val != None:
            self.validate('gateway_ip_address', val)
        self._gateway_ip_address = val
    
    @staticmethod
    def get_api_name():
          return "service-processor-network-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'status',
            'prefix-length',
            'device-type',
            'ip-address',
            'address-type',
            'router-ip-address',
            'link-status',
            'netmask',
            'is-enabled',
            'dhcp',
            'link-local-ip-address',
            'mac-address',
            'gateway-ip-address',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'prefix_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'device_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'router_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'link_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netmask': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'dhcp': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'link_local_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gateway_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
