from netapp.fcp.fcp_adapter_topology_attached_port_info import FcpAdapterTopologyAttachedPortInfo
from netapp.netapp_object import NetAppObject

class FcpAdapterTopologySwitchPortInfo(NetAppObject):
    """
    Information about the FC switch port.
    """
    
    _port_name = None
    @property
    def port_name(self):
        """
        World wide port name (WWPN) of the port.
        The format is: XX:XX:XX:XX:XX:XX:XX:XX
        where X is a hexadecimal digit.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _port_type = None
    @property
    def port_type(self):
        """
        Port type. Possible values: "n-port",
        "nl-port", "fnl-port", "nx-port",
        "f-port", "fl-port", "e-port",
        "b-port", "nv-port", "fv-port", "sd-port",
        "te-port", "tl-port", and "none".
        """
        return self._port_type
    @port_type.setter
    def port_type(self, val):
        if val != None:
            self.validate('port_type', val)
        self._port_type = val
    
    _fcp_adapter_topology_attached_ports = None
    @property
    def fcp_adapter_topology_attached_ports(self):
        """
        List of devices attached to this port.
        """
        return self._fcp_adapter_topology_attached_ports
    @fcp_adapter_topology_attached_ports.setter
    def fcp_adapter_topology_attached_ports(self, val):
        if val != None:
            self.validate('fcp_adapter_topology_attached_ports', val)
        self._fcp_adapter_topology_attached_ports = val
    
    _port_number = None
    @property
    def port_number(self):
        """
        Port index number. Range: [0..2^32-1]
        """
        return self._port_number
    @port_number.setter
    def port_number(self, val):
        if val != None:
            self.validate('port_number', val)
        self._port_number = val
    
    _port_state = None
    @property
    def port_state(self):
        """
        Port state. Possible values: "online",
        "offline", "testing", "fault", and
        "unknown".
        """
        return self._port_state
    @port_state.setter
    def port_state(self, val):
        if val != None:
            self.validate('port_state', val)
        self._port_state = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-topology-switch-port-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'port-name',
            'port-type',
            'fcp-adapter-topology-attached-ports',
            'port-number',
            'port-state',
        ]
    
    def describe_properties(self):
        return {
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fcp_adapter_topology_attached_ports': { 'class': FcpAdapterTopologyAttachedPortInfo, 'is_list': True, 'required': 'required' },
            'port_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'port_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
