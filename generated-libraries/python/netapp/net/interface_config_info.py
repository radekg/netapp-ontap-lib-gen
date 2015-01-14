from netapp.net.ip_address_info import IpAddressInfo
from netapp.netapp_object import NetAppObject

class InterfaceConfigInfo(NetAppObject):
    """
    Configuration for one interface.
    """
    
    _partner = None
    @property
    def partner(self):
        """
        Name of CFO partner interface that will failover to this interface.
        Default is no partner.
        """
        return self._partner
    @partner.setter
    def partner(self, val):
        if val != None:
            self.validate('partner', val)
        self._partner = val
    
    _v6_primary_address = None
    @property
    def v6_primary_address(self):
        """
        The primary ipv6 address for this interface
        If missing, it means the interface has no statically configured ipv6 addresses.
        """
        return self._v6_primary_address
    @v6_primary_address.setter
    def v6_primary_address(self, val):
        if val != None:
            self.validate('v6_primary_address', val)
        self._v6_primary_address = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of the interface.
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _dad_attempts = None
    @property
    def dad_attempts(self):
        """
        Number of IPv6 Duplicate Address Detection attempts for this interface.
        """
        return self._dad_attempts
    @dad_attempts.setter
    def dad_attempts(self, val):
        if val != None:
            self.validate('dad_attempts', val)
        self._dad_attempts = val
    
    _is_trusted = None
    @property
    def is_trusted(self):
        """
        true: interface is trusted.
        Default is true.
        """
        return self._is_trusted
    @is_trusted.setter
    def is_trusted(self, val):
        if val != None:
            self.validate('is_trusted', val)
        self._is_trusted = val
    
    _mediatype = None
    @property
    def mediatype(self):
        """
        Specifies the Ethernet media type used.
        Possible values: {tp | tp-fd | 100tx | 100tx-fd |
        1000fx | 10g-sr | auto}
        10/100, 100/1000, and 10/100/1000 Mbps Copper Interfaces:
        The acceptable types (which vary from card to card) are "tp"
        (Half-duplex 10BaseT RJ-45 twisted-pair), "tp-fd" (Full
        duplex 10Base-T RJ-45 twisted-pair), "100tx" (Half-duplex
        100Base-T RJ-45 twisted-pair), "100tx-fd" (Full duplex
        100Base-T RJ-45 twisted-pair), and "auto" (Auto RJ-45
        twisted-pair). The default media type is set to "tp" or to
        "auto" where applicable.
        1000 Mbps Fiber Interfaces: The Gigabit Ethernet Controllers
        only support the mediatype "auto".   The Gigabit
        Ethernet Controllers only support full-duplex.
        10G bps Fiber Interfaces: The 10G TOE/Ethernet Controllers
        support the mediatype "10g-sr" and "auto". The interface does
        not do auto-negotiatition, it only supports 10Gb speed,
        full duplex.
        Not all interfaces have a mediatype (e.g. loopback does not)
        """
        return self._mediatype
    @mediatype.setter
    def mediatype(self, val):
        if val != None:
            self.validate('mediatype', val)
        self._mediatype = val
    
    _v4_primary_address = None
    @property
    def v4_primary_address(self):
        """
        The primary ipv4 address for this interface
        If missing, it means the interface has no ipv4 addresses.
        """
        return self._v4_primary_address
    @v4_primary_address.setter
    def v4_primary_address(self, val):
        if val != None:
            self.validate('v4_primary_address', val)
        self._v4_primary_address = val
    
    _port_role = None
    @property
    def port_role(self):
        """
        Possible values: [mgmt|storage-acp|cluster|data].  Default is data.
        Mgmt role cannot be modified in 7Mode.
        """
        return self._port_role
    @port_role.setter
    def port_role(self, val):
        if val != None:
            self.validate('port_role', val)
        self._port_role = val
    
    _flowcontrol = None
    @property
    def flowcontrol(self):
        """
        Specifies the flow control type.
        Possible values: {none | receive | send | full}
        The meaning of these values is:
        "none" (no flow control), "receive" (only receive flow
        control frames), "send" (only send flow control frames),
        and "full" (send and receive flow control frames).
        If the flowcontrol option is not specified, the default value
        is interface-dependent.
        Fiber Interfaces: If the interface detects that the link
        partner auto-negotiates, then the operational flow control
        setting is negotiated (and the configured or default setting
        for flow control is ignored).
        Not all interfaces have a flowcontrol (e.g. loopback does not)
        Default is NIC-specific.
        """
        return self._flowcontrol
    @flowcontrol.setter
    def flowcontrol(self, val):
        if val != None:
            self.validate('flowcontrol', val)
        self._flowcontrol = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Administrative status.  (true: interface is administratively up).
        Default is true.
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _is_wins_enabled = None
    @property
    def is_wins_enabled(self):
        """
        true: interface is advertised to the WINS server.
        Default is true.
        """
        return self._is_wins_enabled
    @is_wins_enabled.setter
    def is_wins_enabled(self, val):
        if val != None:
            self.validate('is_wins_enabled', val)
        self._is_wins_enabled = val
    
    _mtusize = None
    @property
    def mtusize(self):
        """
        Maximum  Transfer  Unit  (MTU)  of  an interface.
        Range: 296-9196
        Default is 1500.
        """
        return self._mtusize
    @mtusize.setter
    def mtusize(self, val):
        if val != None:
            self.validate('mtusize', val)
        self._mtusize = val
    
    _ipspace_name = None
    @property
    def ipspace_name(self):
        """
        Name of ipspace that the interface belongs to.
        """
        return self._ipspace_name
    @ipspace_name.setter
    def ipspace_name(self, val):
        if val != None:
            self.validate('ipspace_name', val)
        self._ipspace_name = val
    
    _is_nfo_enabled = None
    @property
    def is_nfo_enabled(self):
        """
        true: network failover is configured for this interface.
        Default is false;
        """
        return self._is_nfo_enabled
    @is_nfo_enabled.setter
    def is_nfo_enabled(self, val):
        if val != None:
            self.validate('is_nfo_enabled', val)
        self._is_nfo_enabled = val
    
    _mac_address = None
    @property
    def mac_address(self):
        """
        Interface mac address. Not provided for "lo" or "vh" interfaces
        """
        return self._mac_address
    @mac_address.setter
    def mac_address(self, val):
        if val != None:
            self.validate('mac_address', val)
        self._mac_address = val
    
    _aliases = None
    @property
    def aliases(self):
        """
        List of interface IP aliases.  Cannot include ipv4 addresses if
        v4-primary-address is empty, and cannot include ipv6 addresses if
        v6_primary-address is empty (except for autoconfigured ipv6 addresses).
        """
        return self._aliases
    @aliases.setter
    def aliases(self, val):
        if val != None:
            self.validate('aliases', val)
        self._aliases = val
    
    @staticmethod
    def get_api_name():
          return "interface-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'partner',
            'v6-primary-address',
            'interface-name',
            'dad-attempts',
            'is-trusted',
            'mediatype',
            'v4-primary-address',
            'port-role',
            'flowcontrol',
            'is-enabled',
            'is-wins-enabled',
            'mtusize',
            'ipspace-name',
            'is-nfo-enabled',
            'mac-address',
            'aliases',
        ]
    
    def describe_properties(self):
        return {
            'partner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'v6_primary_address': { 'class': IpAddressInfo, 'is_list': False, 'required': 'optional' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'dad_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_trusted': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'mediatype': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'v4_primary_address': { 'class': IpAddressInfo, 'is_list': False, 'required': 'optional' },
            'port_role': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'flowcontrol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_wins_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'mtusize': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ipspace_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_nfo_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aliases': { 'class': IpAddressInfo, 'is_list': True, 'required': 'optional' },
        }
