from netapp.fcp.fcp_adapter_topology_switch_port_info import FcpAdapterTopologySwitchPortInfo
from netapp.netapp_object import NetAppObject

class FcpAdapterTopologySwitchInfo(NetAppObject):
    """
    Information about an FC switch connected
    to an FC adapter.
    """
    
    _fcp_adapter_topology_switch_ports = None
    @property
    def fcp_adapter_topology_switch_ports(self):
        """
        List of ports for the FC switch. This is only returned
        if verbose is set to true.
        """
        return self._fcp_adapter_topology_switch_ports
    @fcp_adapter_topology_switch_ports.setter
    def fcp_adapter_topology_switch_ports(self, val):
        if val != None:
            self.validate('fcp_adapter_topology_switch_ports', val)
        self._fcp_adapter_topology_switch_ports = val
    
    _domain = None
    @property
    def domain(self):
        """
        The domain identifier of the FC switch.
        Range: [1..255]
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _vendor = None
    @property
    def vendor(self):
        """
        The name of the FC switch vendor. The maximum length is
        64.
        """
        return self._vendor
    @vendor.setter
    def vendor(self, val):
        if val != None:
            self.validate('vendor', val)
        self._vendor = val
    
    _adapter = None
    @property
    def adapter(self):
        """
        The name of the adapter this switch is visible through.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _logical_name = None
    @property
    def logical_name(self):
        """
        The logical name of the FC switch. The maximum length
        is 64.
        """
        return self._logical_name
    @logical_name.setter
    def logical_name(self, val):
        if val != None:
            self.validate('logical_name', val)
        self._logical_name = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        Node name of the FC switch. The format is:
        XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal digit.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _release = None
    @property
    def release(self):
        """
        The release version of the FC switch. The maximum length
        is 64.
        """
        return self._release
    @release.setter
    def release(self, val):
        if val != None:
            self.validate('release', val)
        self._release = val
    
    _port_count = None
    @property
    def port_count(self):
        """
        The number of ports discovered on the FC switch.
        Range: [0..2^32-1]
        """
        return self._port_count
    @port_count.setter
    def port_count(self, val):
        if val != None:
            self.validate('port_count', val)
        self._port_count = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-topology-switch-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fcp-adapter-topology-switch-ports',
            'domain',
            'vendor',
            'adapter',
            'logical-name',
            'node-name',
            'release',
            'port-count',
        ]
    
    def describe_properties(self):
        return {
            'fcp_adapter_topology_switch_ports': { 'class': FcpAdapterTopologySwitchPortInfo, 'is_list': True, 'required': 'optional' },
            'domain': { 'class': int, 'is_list': False, 'required': 'required' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'logical_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'release': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
