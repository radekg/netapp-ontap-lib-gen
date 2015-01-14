from netapp.netapp_object import NetAppObject

class FcpAdapterNameserverObjectInfo(NetAppObject):
    """
    Information about a nameserver object entry.
    """
    
    _fc4_type = None
    @property
    def fc4_type(self):
        """
        Registered FC4 Types. This element is omitted if the
        device has not registered an FC4 Type.
        Comma separated possible values:
        "llc/snap", "ipfc", "fcp", "gpp", "ipi-3m", "ipi-3s",
        "ipi-3p", "sbccs-ch", "sbccs-cu", "fc-sb-3_ch2cu",
        "fc-sb-3_cu2ch", "fc-gs", "fc-sw", "fc-al", "snmp",
        "hippi-fp", "mil-std-1553", "asm", "fc-vi", and "fc-av".
        """
        return self._fc4_type
    @fc4_type.setter
    def fc4_type(self, val):
        if val != None:
            self.validate('fc4_type', val)
        self._fc4_type = val
    
    _symbolic_port_name = None
    @property
    def symbolic_port_name(self):
        """
        Registered symbolic port name. If the device
        has not registered one, this element will be omitted.
        """
        return self._symbolic_port_name
    @symbolic_port_name.setter
    def symbolic_port_name(self, val):
        if val != None:
            self.validate('symbolic_port_name', val)
        self._symbolic_port_name = val
    
    _class_service = None
    @property
    def class_service(self):
        """
        Registered class of services as defined in the FC-FS
        standard. This element is omitted if the device has not
        registered a class of service. Comma separated possible
        values: "F", "1", "2", "3", "4", and "6".
        """
        return self._class_service
    @class_service.setter
    def class_service(self, val):
        if val != None:
            self.validate('class_service', val)
        self._class_service = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        World wide node name (WWNN) of this entry. This element
        is omitted if the device has not registered a WWNN.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _port_id = None
    @property
    def port_id(self):
        """
        Assigned port identifier of this entry.
        Range: [0..2^24-1]
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    _symbolic_node_name = None
    @property
    def symbolic_node_name(self):
        """
        Registered symbolic node name. If the device
        has not registered one, this element will be omitted.
        """
        return self._symbolic_node_name
    @symbolic_node_name.setter
    def symbolic_node_name(self, val):
        if val != None:
            self.validate('symbolic_node_name', val)
        self._symbolic_node_name = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        World wide port name (WWPN) of this entry. This element
        is omitted if the device has not registered a WWPN.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _fabric_port_name = None
    @property
    def fabric_port_name(self):
        """
        Fabric world wide port name (WWPN) of this entry. This
        element is omitted if the fabric WWPN is not registered.
        """
        return self._fabric_port_name
    @fabric_port_name.setter
    def fabric_port_name(self, val):
        if val != None:
            self.validate('fabric_port_name', val)
        self._fabric_port_name = val
    
    _adapter = None
    @property
    def adapter(self):
        """
        The adapter this nameserver object is visible through.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _port_type = None
    @property
    def port_type(self):
        """
        Port type of this entry. Possible values:
        "n-port", "nl-port", "fnl-port", "nx-port",
        "f-port", "fl-port", "e-port", "b-port", "nv-port",
        "fv-port", "sd-port", "te-port", "tl-port", and "none".
        """
        return self._port_type
    @port_type.setter
    def port_type(self, val):
        if val != None:
            self.validate('port_type', val)
        self._port_type = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-nameserver-object-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fc4-type',
            'symbolic-port-name',
            'class-service',
            'node-name',
            'port-id',
            'symbolic-node-name',
            'port-name',
            'fabric-port-name',
            'adapter',
            'port-type',
        ]
    
    def describe_properties(self):
        return {
            'fc4_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'symbolic_port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'class_service': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'symbolic_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fabric_port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
