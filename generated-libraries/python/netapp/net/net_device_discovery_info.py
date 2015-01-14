from netapp.netapp_object import NetAppObject

class NetDeviceDiscoveryInfo(NetAppObject):
    """
    Information about discovered devices
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
        The node on which the network port resides.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _hold_time_remaining = None
    @property
    def hold_time_remaining(self):
        """
        Remaining packet hold time in seconds for the discovered
        device.
        Attributes: non-creatable, non-modifiable
        """
        return self._hold_time_remaining
    @hold_time_remaining.setter
    def hold_time_remaining(self, val):
        if val != None:
            self.validate('hold_time_remaining', val)
        self._hold_time_remaining = val
    
    _discovered_device = None
    @property
    def discovered_device(self):
        """
        Device discovered by the physical network port.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._discovered_device
    @discovered_device.setter
    def discovered_device(self, val):
        if val != None:
            self.validate('discovered_device', val)
        self._discovered_device = val
    
    _capabilities = None
    @property
    def capabilities(self):
        """
        Capabilities of the discovered devices. For example:
        switch, igmp.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "router"              - Router,
        <li> "trans_bridge"        - Trans Bridge,
        <li> "source_route_bridge" - Source Route Bridge,
        <li> "switch"              - Switch,
        <li> "host"                - Host,
        <li> "igmp"                - IGMP,
        <li> "repeater"            - Repeater,
        <li> "phone"               - Phone
        </ul>
        """
        return self._capabilities
    @capabilities.setter
    def capabilities(self, val):
        if val != None:
            self.validate('capabilities', val)
        self._capabilities = val
    
    _device_ip = None
    @property
    def device_ip(self):
        """
        IP address(es) of the discovered device. At present, only
        IPv4 addresses are included.
        Attributes: non-creatable, non-modifiable
        """
        return self._device_ip
    @device_ip.setter
    def device_ip(self, val):
        if val != None:
            self.validate('device_ip', val)
        self._device_ip = val
    
    _platform = None
    @property
    def platform(self):
        """
        Platform of the discovered device. For example:
        N5K-C5010P-BF
        Attributes: non-creatable, non-modifiable
        """
        return self._platform
    @platform.setter
    def platform(self, val):
        if val != None:
            self.validate('platform', val)
        self._platform = val
    
    _version = None
    @property
    def version(self):
        """
        Software version of the discovered device.
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _interface = None
    @property
    def interface(self):
        """
        Interface port of the discovered device. The format is
        dependent on
        the reporting device. For example: FastEthernet0/12 or
        e0a
        Attributes: key, non-creatable, non-modifiable
        """
        return self._interface
    @interface.setter
    def interface(self, val):
        if val != None:
            self.validate('interface', val)
        self._interface = val
    
    _port = None
    @property
    def port(self):
        """
        The name of the physical network port for device
        discovery. For example: e0a
        Attributes: key, non-creatable, non-modifiable
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    @staticmethod
    def get_api_name():
          return "net-device-discovery-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'hold-time-remaining',
            'discovered-device',
            'capabilities',
            'device-ip',
            'platform',
            'version',
            'interface',
            'port',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hold_time_remaining': { 'class': int, 'is_list': False, 'required': 'optional' },
            'discovered_device': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'capabilities': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'device_ip': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'platform': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interface': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
