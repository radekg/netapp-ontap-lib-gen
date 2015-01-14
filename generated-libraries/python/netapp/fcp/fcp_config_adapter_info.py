from netapp.netapp_object import NetAppObject

class FcpConfigAdapterInfo(NetAppObject):
    """
    Configuration information for one physical FC adapter.
    """
    
    _pci_bus_width = None
    @property
    def pci_bus_width(self):
        """
        PCI bus width in bits. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.1.1.
        """
        return self._pci_bus_width
    @pci_bus_width.setter
    def pci_bus_width(self, val):
        if val != None:
            self.validate('pci_bus_width', val)
        self._pci_bus_width = val
    
    _external_gbic_enabled = None
    @property
    def external_gbic_enabled(self):
        """
        "true" if enabled, "false" otherwise. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.1.1.
        """
        return self._external_gbic_enabled
    @external_gbic_enabled.setter
    def external_gbic_enabled(self, val):
        if val != None:
            self.validate('external_gbic_enabled', val)
        self._external_gbic_enabled = val
    
    _fabric_name = None
    @property
    def fabric_name(self):
        """
        The name of the FC fabric this adapter is connected to. Only returned if the
        adapter is logged into the fabric.
        This field is available in Data ONTAP 8.2 and later.
        """
        return self._fabric_name
    @fabric_name.setter
    def fabric_name(self, val):
        if val != None:
            self.validate('fabric_name', val)
        self._fabric_name = val
    
    _cache_line_size = None
    @property
    def cache_line_size(self):
        """
        Cache line size of adapter. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.1.1.
        """
        return self._cache_line_size
    @cache_line_size.setter
    def cache_line_size(self, val):
        if val != None:
            self.validate('cache_line_size', val)
        self._cache_line_size = val
    
    _pci_clock_speed = None
    @property
    def pci_clock_speed(self):
        """
        PCI clock speed in MHz. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.1.1.
        """
        return self._pci_clock_speed
    @pci_clock_speed.setter
    def pci_clock_speed(self, val):
        if val != None:
            self.validate('pci_clock_speed', val)
        self._pci_clock_speed = val
    
    _sram_parity_enabled = None
    @property
    def sram_parity_enabled(self):
        """
        "true" if enabled, "false" otherwise. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.1.1.
        """
        return self._sram_parity_enabled
    @sram_parity_enabled.setter
    def sram_parity_enabled(self, val):
        if val != None:
            self.validate('sram_parity_enabled', val)
        self._sram_parity_enabled = val
    
    _partner_adapter = None
    @property
    def partner_adapter(self):
        """
        Name of partner adapter for takeover if configured.
        Value of "none" indicates no partner set for this adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        Starting with Data ONTAP 8.0, only single_image cfmode is supported.
        Outputs related to other cfmodes are deprecated and no longer
        returned by this api.
        """
        return self._partner_adapter
    @partner_adapter.setter
    def partner_adapter(self, val):
        if val != None:
            self.validate('partner_adapter', val)
        self._partner_adapter = val
    
    _vlan_id = None
    @property
    def vlan_id(self):
        """
        Assigned FC VLAN ID. verbose only.
        This is only available for converged network
        adapters (CNA).
        """
        return self._vlan_id
    @vlan_id.setter
    def vlan_id(self, val):
        if val != None:
            self.validate('vlan_id', val)
        self._vlan_id = val
    
    _phy_firmware_rev = None
    @property
    def phy_firmware_rev(self):
        """
        PHY Firmware revision of adapter. verbose only.
        This is only available for converged network
        adapters (CNA).
        """
        return self._phy_firmware_rev
    @phy_firmware_rev.setter
    def phy_firmware_rev(self, val):
        if val != None:
            self.validate('phy_firmware_rev', val)
        self._phy_firmware_rev = val
    
    _error_msg = None
    @property
    def error_msg(self):
        """
        Error message, if an error occured while
        retrieving info for this adapter.  This will
        only be used if listing all adapters.
        If an error occurred while retrieving
        info for a specific adapter, the API will
        fail with error message.
        """
        return self._error_msg
    @error_msg.setter
    def error_msg(self, val):
        if val != None:
            self.validate('error_msg', val)
        self._error_msg = val
    
    _speed = None
    @property
    def speed(self):
        """
        Speed configured for this adapter. Possible values:
        "auto", "1Gb", "2Gb", "4Gb", "8Gb", "10Gb", "16Gb".
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._speed
    @speed.setter
    def speed(self, val):
        if val != None:
            self.validate('speed', val)
        self._speed = val
    
    _port_address = None
    @property
    def port_address(self):
        """
        Host port address of adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._port_address
    @port_address.setter
    def port_address(self, val):
        if val != None:
            self.validate('port_address', val)
        self._port_address = val
    
    _adapter_type = None
    @property
    def adapter_type(self):
        """
        Type of the adapter.  Possible values are
        "physical", "local", "standby", "partner".
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        Starting with Data ONTAP 8.0, only single_image cfmode is supported.
        Outputs related to other cfmodes are deprecated and no longer
        returned by this api.
        """
        return self._adapter_type
    @adapter_type.setter
    def adapter_type(self, val):
        if val != None:
            self.validate('adapter_type', val)
        self._adapter_type = val
    
    _physical_data_link_rate = None
    @property
    def physical_data_link_rate(self):
        """
        Physical Data Link Rate in Gbits. verbose only.
        This is only available for converged network
        adapters (CNA).
        """
        return self._physical_data_link_rate
    @physical_data_link_rate.setter
    def physical_data_link_rate(self, val):
        if val != None:
            self.validate('physical_data_link_rate', val)
        self._physical_data_link_rate = val
    
    _hardware_rev = None
    @property
    def hardware_rev(self):
        """
        Hardware revision of adapter. verbose only.
        """
        return self._hardware_rev
    @hardware_rev.setter
    def hardware_rev(self, val):
        if val != None:
            self.validate('hardware_rev', val)
        self._hardware_rev = val
    
    _state = None
    @property
    def state(self):
        """
        Status of the adapter.  Possible values are
        "startup", "uninitialized", "initializing firmware",
        "link not connected", "waiting for link up", "online",
        "link disconnected", "resetting", "offline",
        "offlined by user/system".
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _preload_table_rev = None
    @property
    def preload_table_rev(self):
        """
        Flash preload revision for FC adapter. verbose only.
        """
        return self._preload_table_rev
    @preload_table_rev.setter
    def preload_table_rev(self, val):
        if val != None:
            self.validate('preload_table_rev', val)
        self._preload_table_rev = val
    
    _connection_established = None
    @property
    def connection_established(self):
        """
        Type of connection established, "ptp" or "loop".
        """
        return self._connection_established
    @connection_established.setter
    def connection_established(self, val):
        if val != None:
            self.validate('connection_established', val)
        self._connection_established = val
    
    _node = None
    @property
    def node(self):
        """
        The name of the node where the adapter is installed.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _loop_id = None
    @property
    def loop_id(self):
        """
        Loop address of adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        This value lies between 0 and 255.
        Starting with Data ONTAP 8.0, only single_image cfmode is supported.
        Outputs related to other cfmodes are deprecated and no longer
        returned by this api.
        """
        return self._loop_id
    @loop_id.setter
    def loop_id(self, val):
        if val != None:
            self.validate('loop_id', val)
        self._loop_id = val
    
    _media_type = None
    @property
    def media_type(self):
        """
        Media configured for this adapter, "ptp", "loop", or "auto".
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._media_type
    @media_type.setter
    def media_type(self, val):
        if val != None:
            self.validate('media_type', val)
        self._media_type = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        FCP World Wide Node Name (WWNN) of the adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _physical_link_state = None
    @property
    def physical_link_state(self):
        """
        Physical Status of the adapter. verbose only.
        Possible values are "link up", "link down".
        This is only available for converged network
        adapters (CNA).
        """
        return self._physical_link_state
    @physical_link_state.setter
    def physical_link_state(self, val):
        if val != None:
            self.validate('physical_link_state', val)
        self._physical_link_state = val
    
    _packet_size = None
    @property
    def packet_size(self):
        """
        FC packet size of adapter. verbose only.
        This field is obsolete and no longer returned beginning with Data ONTAP 8.2.
        """
        return self._packet_size
    @packet_size.setter
    def packet_size(self, val):
        if val != None:
            self.validate('packet_size', val)
        self._packet_size = val
    
    _switch_port = None
    @property
    def switch_port(self):
        """
        Switch and port this adapter is connected to.
        The string will be of the form X:Y where X is
        the name of the switch and Y is the port value.
        verbose only.
        """
        return self._switch_port
    @switch_port.setter
    def switch_port(self, val):
        if val != None:
            self.validate('switch_port', val)
        self._switch_port = val
    
    _physical_protocol = None
    @property
    def physical_protocol(self):
        """
        The physical protocol of the adapter. Possible values:
        <ul>
        <li> "fibre_channel" - The adapter is a Fibre Channel
        adapter,
        <li> "ethernet" - The adapter is a Fibre Channel over
        Ethernet adapter.
        </ul>
        """
        return self._physical_protocol
    @physical_protocol.setter
    def physical_protocol(self, val):
        if val != None:
            self.validate('physical_protocol', val)
        self._physical_protocol = val
    
    _data_link_rate = None
    @property
    def data_link_rate(self):
        """
        Data Link Rate in Gbits. verbose only.
        """
        return self._data_link_rate
    @data_link_rate.setter
    def data_link_rate(self, val):
        if val != None:
            self.validate('data_link_rate', val)
        self._data_link_rate = val
    
    _firmware_rev = None
    @property
    def firmware_rev(self):
        """
        Firmware revision of adapter. verbose only.
        """
        return self._firmware_rev
    @firmware_rev.setter
    def firmware_rev(self, val):
        if val != None:
            self.validate('firmware_rev', val)
        self._firmware_rev = val
    
    _standby = None
    @property
    def standby(self):
        """
        "true" if adapter is on standby, "false" otherwise.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        Starting with Data ONTAP 8.0, only single_image cfmode is supported.
        Outputs related to other cfmodes are deprecated and no longer
        returned by this api.
        """
        return self._standby
    @standby.setter
    def standby(self, val):
        if val != None:
            self.validate('standby', val)
        self._standby = val
    
    _adapter = None
    @property
    def adapter(self):
        """
        The slot name of the FC adapter.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _fabric_established = None
    @property
    def fabric_established(self):
        """
        "true" if fabric is established to this adapter,
        "false" otherwise. verbose only.
        """
        return self._fabric_established
    @fabric_established.setter
    def fabric_established(self, val):
        if val != None:
            self.validate('fabric_established', val)
        self._fabric_established = val
    
    _info_name = None
    @property
    def info_name(self):
        """
        Info name given to this adapter. verbose only.
        """
        return self._info_name
    @info_name.setter
    def info_name(self, val):
        if val != None:
            self.validate('info_name', val)
        self._info_name = val
    
    _port_id = None
    @property
    def port_id(self):
        """
        Port address of adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        Starting with Data ONTAP 8.0, only single_image cfmode is supported.
        Outputs related to other cfmodes are deprecated and no longer
        returned by this api.
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    _max_speed = None
    @property
    def max_speed(self):
        """
        The maximum speed of this adapter in Gbit/sec.
        """
        return self._max_speed
    @max_speed.setter
    def max_speed(self, val):
        if val != None:
            self.validate('max_speed', val)
        self._max_speed = val
    
    _mpi_firmware_rev = None
    @property
    def mpi_firmware_rev(self):
        """
        MPI Firmware revision of adapter. verbose only.
        This is only available for converged network
        adapters (CNA).
        """
        return self._mpi_firmware_rev
    @mpi_firmware_rev.setter
    def mpi_firmware_rev(self, val):
        if val != None:
            self.validate('mpi_firmware_rev', val)
        self._mpi_firmware_rev = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        FCP World Wide Port Name (WWPN) of adapter.
        If an error occured while retrieving info
        for this adapter, this will not be returned.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    @staticmethod
    def get_api_name():
          return "fcp-config-adapter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'pci-bus-width',
            'external-gbic-enabled',
            'fabric-name',
            'cache-line-size',
            'pci-clock-speed',
            'sram-parity-enabled',
            'partner-adapter',
            'vlan-id',
            'phy-firmware-rev',
            'error-msg',
            'speed',
            'port-address',
            'adapter-type',
            'physical-data-link-rate',
            'hardware-rev',
            'state',
            'preload-table-rev',
            'connection-established',
            'node',
            'loop-id',
            'media-type',
            'node-name',
            'physical-link-state',
            'packet-size',
            'switch-port',
            'physical-protocol',
            'data-link-rate',
            'firmware-rev',
            'standby',
            'adapter',
            'fabric-established',
            'info-name',
            'port-id',
            'max-speed',
            'mpi-firmware-rev',
            'port-name',
        ]
    
    def describe_properties(self):
        return {
            'pci_bus_width': { 'class': int, 'is_list': False, 'required': 'optional' },
            'external_gbic_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'fabric_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_line_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'pci_clock_speed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'sram_parity_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'partner_adapter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vlan_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'phy_firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'error_msg': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'speed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_address': { 'class': int, 'is_list': False, 'required': 'optional' },
            'adapter_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'physical_data_link_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'hardware_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'preload_table_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connection_established': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'loop_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'media_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'physical_link_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'packet_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'switch_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'physical_protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'data_link_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
            'firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'standby': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fabric_established': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'info_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'max_speed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mpi_firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
