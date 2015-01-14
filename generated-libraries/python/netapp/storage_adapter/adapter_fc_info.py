from netapp.storage_adapter.adapter_bar_info import AdapterBarInfo
from netapp.storage_adapter.adapter_sff_info import AdapterSffInfo
from netapp.storage_adapter.adapter_sfp_info import AdapterSfpInfo
from netapp.netapp_object import NetAppObject

class AdapterFcInfo(NetAppObject):
    """
    Detailed information for fc adapter.
    """
    
    _is_redundant = None
    @property
    def is_redundant(self):
        """
        Is the adapter used in dual-attached config? true or false
        """
        return self._is_redundant
    @is_redundant.setter
    def is_redundant(self, val):
        if val != None:
            self.validate('is_redundant', val)
        self._is_redundant = val
    
    _is_pci_64_capable = None
    @property
    def is_pci_64_capable(self):
        """
        Is the adapter pci-64-capable? true or false.
        """
        return self._is_pci_64_capable
    @is_pci_64_capable.setter
    def is_pci_64_capable(self, val):
        if val != None:
            self.validate('is_pci_64_capable', val)
        self._is_pci_64_capable = val
    
    _fc_node_name = None
    @property
    def fc_node_name(self):
        """
        Fibre Channel node name.
        """
        return self._fc_node_name
    @fc_node_name.setter
    def fc_node_name(self, val):
        if val != None:
            self.validate('fc_node_name', val)
        self._fc_node_name = val
    
    _adapter_model = None
    @property
    def adapter_model(self):
        """
        Model of the adapter.
        """
        return self._adapter_model
    @adapter_model.setter
    def adapter_model(self, val):
        if val != None:
            self.validate('adapter_model', val)
        self._adapter_model = val
    
    _fc_port_name = None
    @property
    def fc_port_name(self):
        """
        Fibre Channel World Wide Port Name (WWPN) of adapter.
        """
        return self._fc_port_name
    @fc_port_name.setter
    def fc_port_name(self, val):
        if val != None:
            self.validate('fc_port_name', val)
        self._fc_port_name = val
    
    _adapter_bar = None
    @property
    def adapter_bar(self):
        """
        List of base address information
        """
        return self._adapter_bar
    @adapter_bar.setter
    def adapter_bar(self, val):
        if val != None:
            self.validate('adapter_bar', val)
        self._adapter_bar = val
    
    _firmware_rev = None
    @property
    def firmware_rev(self):
        """
        Firmware revision of adapter.
        """
        return self._firmware_rev
    @firmware_rev.setter
    def firmware_rev(self, val):
        if val != None:
            self.validate('firmware_rev', val)
        self._firmware_rev = val
    
    _host_port_id = None
    @property
    def host_port_id(self):
        """
        Storage port adapter's port id,
        """
        return self._host_port_id
    @host_port_id.setter
    def host_port_id(self, val):
        if val != None:
            self.validate('host_port_id', val)
        self._host_port_id = val
    
    _is_in_use = None
    @property
    def is_in_use(self):
        """
        Is the adapter inuse? true or false
        """
        return self._is_in_use
    @is_in_use.setter
    def is_in_use(self, val):
        if val != None:
            self.validate('is_in_use', val)
        self._is_in_use = val
    
    _hardware_rev = None
    @property
    def hardware_rev(self):
        """
        Hardware revision of adapter.
        """
        return self._hardware_rev
    @hardware_rev.setter
    def hardware_rev(self, val):
        if val != None:
            self.validate('hardware_rev', val)
        self._hardware_rev = val
    
    _fc_packet_size = None
    @property
    def fc_packet_size(self):
        """
        Size of Fibre Channel packets.
        """
        return self._fc_packet_size
    @fc_packet_size.setter
    def fc_packet_size(self, val):
        if val != None:
            self.validate('fc_packet_size', val)
        self._fc_packet_size = val
    
    _cache_line_sz = None
    @property
    def cache_line_sz(self):
        """
        Storage port adapter's data cache size,
        """
        return self._cache_line_sz
    @cache_line_sz.setter
    def cache_line_sz(self, val):
        if val != None:
            self.validate('cache_line_sz', val)
        self._cache_line_sz = val
    
    _host_loop_id = None
    @property
    def host_loop_id(self):
        """
        Storage port adapter's Fibre Channel loop id,
        """
        return self._host_loop_id
    @host_loop_id.setter
    def host_loop_id(self, val):
        if val != None:
            self.validate('host_loop_id', val)
        self._host_loop_id = val
    
    _adapter_sff_info = None
    @property
    def adapter_sff_info(self):
        """
        If the port has a small form factor
        transceiver/connector (also known as sff), then
        this is the vendor information on the sff.
        """
        return self._adapter_sff_info
    @adapter_sff_info.setter
    def adapter_sff_info(self, val):
        if val != None:
            self.validate('adapter_sff_info', val)
        self._adapter_sff_info = val
    
    _is_sram_parity = None
    @property
    def is_sram_parity(self):
        """
        Is the adapter sram parity configured and enabled? true or false.
        """
        return self._is_sram_parity
    @is_sram_parity.setter
    def is_sram_parity(self, val):
        if val != None:
            self.validate('is_sram_parity', val)
        self._is_sram_parity = val
    
    _preload_table_rev = None
    @property
    def preload_table_rev(self):
        """
        Preload table revision of adapter.
        """
        return self._preload_table_rev
    @preload_table_rev.setter
    def preload_table_rev(self, val):
        if val != None:
            self.validate('preload_table_rev', val)
        self._preload_table_rev = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Is the adapter enabled? true or false.
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _adapter_sfp_info = None
    @property
    def adapter_sfp_info(self):
        """
        If the port has a small form factor pluggable
        transceiver/connector (also known as sfp), then
        this is the vendor information on the sfp.
        """
        return self._adapter_sfp_info
    @adapter_sfp_info.setter
    def adapter_sfp_info(self, val):
        if val != None:
            self.validate('adapter_sfp_info', val)
        self._adapter_sfp_info = val
    
    _fc_link_rate = None
    @property
    def fc_link_rate(self):
        """
        Link rate of Fibre Channel port.
        """
        return self._fc_link_rate
    @fc_link_rate.setter
    def fc_link_rate(self, val):
        if val != None:
            self.validate('fc_link_rate', val)
        self._fc_link_rate = val
    
    _is_ext_gbic = None
    @property
    def is_ext_gbic(self):
        """
        Is the Fibre Channel gbic external? true or false.
        """
        return self._is_ext_gbic
    @is_ext_gbic.setter
    def is_ext_gbic(self, val):
        if val != None:
            self.validate('is_ext_gbic', val)
        self._is_ext_gbic = val
    
    @staticmethod
    def get_api_name():
          return "adapter-fc-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-redundant',
            'is-pci-64-capable',
            'fc-node-name',
            'adapter-model',
            'fc-port-name',
            'adapter-bar',
            'firmware-rev',
            'host-port-id',
            'is-in-use',
            'hardware-rev',
            'fc-packet-size',
            'cache-line-sz',
            'host-loop-id',
            'adapter-sff-info',
            'is-sram-parity',
            'preload-table-rev',
            'is-enabled',
            'adapter-sfp-info',
            'fc-link-rate',
            'is-ext-gbic',
        ]
    
    def describe_properties(self):
        return {
            'is_redundant': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_pci_64_capable': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'fc_node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fc_port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_bar': { 'class': AdapterBarInfo, 'is_list': True, 'required': 'optional' },
            'firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'host_port_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_in_use': { 'class': bool, 'is_list': False, 'required': 'required' },
            'hardware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fc_packet_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'cache_line_sz': { 'class': int, 'is_list': False, 'required': 'optional' },
            'host_loop_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'adapter_sff_info': { 'class': AdapterSffInfo, 'is_list': False, 'required': 'optional' },
            'is_sram_parity': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'preload_table_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'adapter_sfp_info': { 'class': AdapterSfpInfo, 'is_list': False, 'required': 'optional' },
            'fc_link_rate': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_ext_gbic': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
