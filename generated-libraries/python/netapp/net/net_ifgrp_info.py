from netapp.netapp_object import NetAppObject

class NetIfgrpInfo(NetAppObject):
    """
    Network interface group information
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
        Specifies the name of node.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _up_ports = None
    @property
    def up_ports(self):
        """
        Specifies all active ports of an ifgrp.
        Attributes: non-creatable, non-modifiable
        """
        return self._up_ports
    @up_ports.setter
    def up_ports(self, val):
        if val != None:
            self.validate('up_ports', val)
        self._up_ports = val
    
    _down_ports = None
    @property
    def down_ports(self):
        """
        Specifies all inactive ports of an ifgrp.
        Attributes: non-creatable, non-modifiable
        """
        return self._down_ports
    @down_ports.setter
    def down_ports(self, val):
        if val != None:
            self.validate('down_ports', val)
        self._down_ports = val
    
    _mac_address = None
    @property
    def mac_address(self):
        """
        Specifies the MAC address of the ifgrp.
        For example: '02:0c:29:78:e1:b7'
        Attributes: non-creatable, non-modifiable
        """
        return self._mac_address
    @mac_address.setter
    def mac_address(self, val):
        if val != None:
            self.validate('mac_address', val)
        self._mac_address = val
    
    _ifgrp_name = None
    @property
    def ifgrp_name(self):
        """
        Specifies the interface group name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._ifgrp_name
    @ifgrp_name.setter
    def ifgrp_name(self, val):
        if val != None:
            self.validate('ifgrp_name', val)
        self._ifgrp_name = val
    
    _mode = None
    @property
    def mode(self):
        """
        Specifies the link policy for the ifgrp.
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
        Attributes: required-for-create, non-modifiable
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _port_participation = None
    @property
    def port_participation(self):
        """
        Port participation state of the ifgrp.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "full"      - Indicates all the ifgrp ports are
        active,
        <li> "partial"   - Indicates not all the ifgrp ports
        are active,
        <li> "none"      - Indicates none of the ifgrp ports is
        active
        </ul>
        """
        return self._port_participation
    @port_participation.setter
    def port_participation(self, val):
        if val != None:
            self.validate('port_participation', val)
        self._port_participation = val
    
    _ports = None
    @property
    def ports(self):
        """
        List of ports associated with this ifgrp.
        Attributes: non-creatable, non-modifiable
        """
        return self._ports
    @ports.setter
    def ports(self, val):
        if val != None:
            self.validate('ports', val)
        self._ports = val
    
    _distribution_function = None
    @property
    def distribution_function(self):
        """
        Specifies the traffic distribution function for the
        ifgrp.
        Attributes: required-for-create, non-modifiable
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
        return self._distribution_function
    @distribution_function.setter
    def distribution_function(self, val):
        if val != None:
            self.validate('distribution_function', val)
        self._distribution_function = val
    
    @staticmethod
    def get_api_name():
          return "net-ifgrp-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'up-ports',
            'down-ports',
            'mac-address',
            'ifgrp-name',
            'mode',
            'port-participation',
            'ports',
            'distribution-function',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'up_ports': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'down_ports': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ifgrp_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_participation': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ports': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'distribution_function': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
