from netapp.netapp_object import NetAppObject

class NetPortInfo(NetAppObject):
    """
    Network port information
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
    
    _ifgrp_distribution_function = None
    @property
    def ifgrp_distribution_function(self):
        """
        For a port of type 'ifgrp', specifies the traffic
        distribution function.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "mac"            - Network traffic is distributed
        on the basis of MAC addresses,
        <li> "ip"             - Network traffic is distributed
        on the basis of IP addresses,
        <li> "sequential"     - Network traffic is distributed
        round-robin to each interface,
        <li> "port"           - Network traffic is distributed
        by transport layer address 4-tuple
        </ul>
        """
        return self._ifgrp_distribution_function
    @ifgrp_distribution_function.setter
    def ifgrp_distribution_function(self, val):
        if val != None:
            self.validate('ifgrp_distribution_function', val)
        self._ifgrp_distribution_function = val
    
    _remote_device_id = None
    @property
    def remote_device_id(self):
        """
        Remote device ID reported by L2 discovery protocol
        Attributes: non-creatable, non-modifiable
        """
        return self._remote_device_id
    @remote_device_id.setter
    def remote_device_id(self, val):
        if val != None:
            self.validate('remote_device_id', val)
        self._remote_device_id = val
    
    _is_administrative_auto_negotiate = None
    @property
    def is_administrative_auto_negotiate(self):
        """
        Enables or disables Ethernet auto-negotiation of speed,
        duplex and flow control.
        Attributes: required-for-create, modifiable
        """
        return self._is_administrative_auto_negotiate
    @is_administrative_auto_negotiate.setter
    def is_administrative_auto_negotiate(self, val):
        if val != None:
            self.validate('is_administrative_auto_negotiate', val)
        self._is_administrative_auto_negotiate = val
    
    _operational_speed = None
    @property
    def operational_speed(self):
        """
        Speed setting reported by the port after Ethernet
        auto-negotiation.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "undef"     - No defined speed,
        <li> "auto"      - Auto-negotiate speed for link,
        <li> "10"        - 10 megabits per second,
        <li> "100"       - 100 megabits per second,
        <li> "1000"      - 1 gigabit per second,
        <li> "10000"     - 10 gigabits per second
        </ul>
        """
        return self._operational_speed
    @operational_speed.setter
    def operational_speed(self, val):
        if val != None:
            self.validate('operational_speed', val)
        self._operational_speed = val
    
    _ifgrp_node = None
    @property
    def ifgrp_node(self):
        """
        For a port of type 'physical' that is a member of an
        interface group (ifgrp), specifies the name of the node
        on which the interface group was created.
        Attributes: non-creatable, non-modifiable
        """
        return self._ifgrp_node
    @ifgrp_node.setter
    def ifgrp_node(self, val):
        if val != None:
            self.validate('ifgrp_node', val)
        self._ifgrp_node = val
    
    _is_administrative_up = None
    @property
    def is_administrative_up(self):
        """
        If true, it changes the state of the port to 'up'.
        Attributes: required-for-create, modifiable
        """
        return self._is_administrative_up
    @is_administrative_up.setter
    def is_administrative_up(self, val):
        if val != None:
            self.validate('is_administrative_up', val)
        self._is_administrative_up = val
    
    _vlan_port = None
    @property
    def vlan_port(self):
        """
        For a port of type 'vlan', specifies the name of the
        physical port on which the vlan is created.
        Attributes: non-creatable, non-modifiable
        """
        return self._vlan_port
    @vlan_port.setter
    def vlan_port(self, val):
        if val != None:
            self.validate('vlan_port', val)
        self._vlan_port = val
    
    _autorevert_delay = None
    @property
    def autorevert_delay(self):
        """
        For a port with role 'cluster', specifies the delay in
        seconds before autoreverting a LIF to this port.
        Attributes: optional-for-create, modifiable
        """
        return self._autorevert_delay
    @autorevert_delay.setter
    def autorevert_delay(self, val):
        if val != None:
            self.validate('autorevert_delay', val)
        self._autorevert_delay = val
    
    _operational_flowcontrol = None
    @property
    def operational_flowcontrol(self):
        """
        Flow control setting reported by the port after Ethernet
        auto-negotiation.
        Attributes: non-creatable, non-modifiable
        """
        return self._operational_flowcontrol
    @operational_flowcontrol.setter
    def operational_flowcontrol(self, val):
        if val != None:
            self.validate('operational_flowcontrol', val)
        self._operational_flowcontrol = val
    
    _vlan_id = None
    @property
    def vlan_id(self):
        """
        For a port of type 'vlan', specifies the vlan
        identification number.
        Attributes: non-creatable, non-modifiable
        """
        return self._vlan_id
    @vlan_id.setter
    def vlan_id(self, val):
        if val != None:
            self.validate('vlan_id', val)
        self._vlan_id = val
    
    _port = None
    @property
    def port(self):
        """
        Specifies the name of port.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    _role = None
    @property
    def role(self):
        """
        Specifies the role associated with the port.
        Possible values:
        <ul>
        <li> 'undef          - No defined role',
        <li> 'cluster        - Used for communication using the
        private cluster network',
        <li> 'data           - Used for communicating with file
        service clients',
        <li> 'node_mgmt      - Used by administrators to
        configure the node',
        <li> 'intercluster   - Used for communication with a
        different cluster'
        </ul>
        Attributes: required-for-create, modifiable
        """
        return self._role
    @role.setter
    def role(self, val):
        if val != None:
            self.validate('role', val)
        self._role = val
    
    _ifgrp_mode = None
    @property
    def ifgrp_mode(self):
        """
        For a port of type 'ifgrp', specifies the link policy.
        Possible values:
        <ul>
        <li> 'multimode      - All links are simultaneously
        active',
        <li> 'multimode_lacp - Link state is managed by the
        switch using link aggregation control protocol (LACP)
        (IEEE 802.3ad)',
        <li> 'singlemode     - Only one link is active at a
        time'
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._ifgrp_mode
    @ifgrp_mode.setter
    def ifgrp_mode(self, val):
        if val != None:
            self.validate('ifgrp_mode', val)
        self._ifgrp_mode = val
    
    _mac_address = None
    @property
    def mac_address(self):
        """
        Specifies the MAC address of the port.
        Attributes: non-creatable, non-modifiable
        """
        return self._mac_address
    @mac_address.setter
    def mac_address(self, val):
        if val != None:
            self.validate('mac_address', val)
        self._mac_address = val
    
    _is_operational_auto_negotiate = None
    @property
    def is_operational_auto_negotiate(self):
        """
        True if Ethernet auto negotiation is successful, false
        otherwise.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_operational_auto_negotiate
    @is_operational_auto_negotiate.setter
    def is_operational_auto_negotiate(self, val):
        if val != None:
            self.validate('is_operational_auto_negotiate', val)
        self._is_operational_auto_negotiate = val
    
    _node = None
    @property
    def node(self):
        """
        Specifies the name of node.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _vlan_node = None
    @property
    def vlan_node(self):
        """
        Specifies the name of the node on which vlan is created.
        Attributes: non-creatable, non-modifiable
        """
        return self._vlan_node
    @vlan_node.setter
    def vlan_node(self, val):
        if val != None:
            self.validate('vlan_node', val)
        self._vlan_node = val
    
    _operational_duplex = None
    @property
    def operational_duplex(self):
        """
        Duplex setting reported by the port after Ethernet
        auto-negotiation.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "undef"     - No defined duplex,
        <li> "auto"      - Auto-negotiate duplex setting for
        link,
        <li> "half"      - Half-duplex link usage,
        <li> "full"      - Full-duplex link usage
        </ul>
        """
        return self._operational_duplex
    @operational_duplex.setter
    def operational_duplex(self, val):
        if val != None:
            self.validate('operational_duplex', val)
        self._operational_duplex = val
    
    _administrative_speed = None
    @property
    def administrative_speed(self):
        """
        Specifies the user preferred speed setting of the port.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "undef"     - No defined speed,
        <li> "auto"      - Auto-negotiate speed for link,
        <li> "10"        - 10 megabits per second,
        <li> "100"       - 100 megabits per second,
        <li> "1000"      - 1 gigabit per second,
        <li> "10000"     - 10 gigabits per second
        </ul>
        """
        return self._administrative_speed
    @administrative_speed.setter
    def administrative_speed(self, val):
        if val != None:
            self.validate('administrative_speed', val)
        self._administrative_speed = val
    
    _ifgrp_port = None
    @property
    def ifgrp_port(self):
        """
        For a port of type 'physical' that is a member of an
        interface group (ifgrp), specifies the name of the
        interface group.
        Attributes: non-creatable, non-modifiable
        """
        return self._ifgrp_port
    @ifgrp_port.setter
    def ifgrp_port(self, val):
        if val != None:
            self.validate('ifgrp_port', val)
        self._ifgrp_port = val
    
    _administrative_duplex = None
    @property
    def administrative_duplex(self):
        """
        Specifies the user preferred duplex setting of the port.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "undef"     - No defined duplex,
        <li> "auto"      - Auto-negotiate duplex setting for
        link,
        <li> "half"      - Half-duplex link usage,
        <li> "full"      - Full-duplex link usage
        </ul>
        """
        return self._administrative_duplex
    @administrative_duplex.setter
    def administrative_duplex(self, val):
        if val != None:
            self.validate('administrative_duplex', val)
        self._administrative_duplex = val
    
    _mtu = None
    @property
    def mtu(self):
        """
        Specifies the maximum transmission unit (MTU) of the
        port.
        Attributes: required-for-create, modifiable
        """
        return self._mtu
    @mtu.setter
    def mtu(self, val):
        if val != None:
            self.validate('mtu', val)
        self._mtu = val
    
    _link_status = None
    @property
    def link_status(self):
        """
        Specifies the link status of the port.
        Possible values:
        <ul>
        <li> 'unknown        - Port status unknown',
        <li> 'up             - Port is up',
        <li> 'down           - Port is down'
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._link_status
    @link_status.setter
    def link_status(self, val):
        if val != None:
            self.validate('link_status', val)
        self._link_status = val
    
    _administrative_flowcontrol = None
    @property
    def administrative_flowcontrol(self):
        """
        Specifies the user preferred flow control setting of the
        port.
        Attributes: required-for-create, modifiable
        """
        return self._administrative_flowcontrol
    @administrative_flowcontrol.setter
    def administrative_flowcontrol(self, val):
        if val != None:
            self.validate('administrative_flowcontrol', val)
        self._administrative_flowcontrol = val
    
    _port_type = None
    @property
    def port_type(self):
        """
        Specifies the type of port.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "physical"  - Physical network interface,
        <li> "if_group"  - Logical interface group (IEEE 802.3,
        section 43),
        <li> "vlan"      - Virtual LAN (IEEE 802.1Q),
        <li> "undef"     - No defined port type
        </ul>
        """
        return self._port_type
    @port_type.setter
    def port_type(self, val):
        if val != None:
            self.validate('port_type', val)
        self._port_type = val
    
    @staticmethod
    def get_api_name():
          return "net-port-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ifgrp-distribution-function',
            'remote-device-id',
            'is-administrative-auto-negotiate',
            'operational-speed',
            'ifgrp-node',
            'is-administrative-up',
            'vlan-port',
            'autorevert-delay',
            'operational-flowcontrol',
            'vlan-id',
            'port',
            'role',
            'ifgrp-mode',
            'mac-address',
            'is-operational-auto-negotiate',
            'node',
            'vlan-node',
            'operational-duplex',
            'administrative-speed',
            'ifgrp-port',
            'administrative-duplex',
            'mtu',
            'link-status',
            'administrative-flowcontrol',
            'port-type',
        ]
    
    def describe_properties(self):
        return {
            'ifgrp_distribution_function': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'remote_device_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_administrative_auto_negotiate': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'operational_speed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ifgrp_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_administrative_up': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vlan_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'autorevert_delay': { 'class': int, 'is_list': False, 'required': 'optional' },
            'operational_flowcontrol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vlan_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'role': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ifgrp_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_operational_auto_negotiate': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vlan_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'operational_duplex': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'administrative_speed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ifgrp_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'administrative_duplex': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mtu': { 'class': int, 'is_list': False, 'required': 'optional' },
            'link_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'administrative_flowcontrol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
