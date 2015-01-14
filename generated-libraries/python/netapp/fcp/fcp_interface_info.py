from netapp.netapp_object import NetAppObject

class FcpInterfaceInfo(NetAppObject):
    """
    Information about a single FCP Logical Interface (LIF).
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
    
    _current_node = None
    @property
    def current_node(self):
        """
        Node currently hosting the LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_node
    @current_node.setter
    def current_node(self, val):
        if val != None:
            self.validate('current_node', val)
        self._current_node = val
    
    _port_address = None
    @property
    def port_address(self):
        """
        Host port address of LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._port_address
    @port_address.setter
    def port_address(self, val):
        if val != None:
            self.validate('port_address', val)
        self._port_address = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of the LIF.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _relative_port_id = None
    @property
    def relative_port_id(self):
        """
        The SCSI Relative Target Port Identifier of the LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._relative_port_id
    @relative_port_id.setter
    def relative_port_id(self, val):
        if val != None:
            self.validate('relative_port_id', val)
        self._relative_port_id = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver hosting the LIF.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        World Wide Node Name (WWNN) of the LIF. All LIFs in a
        Vserver have the same WWNN as the Vserver's FCP service.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        World Wide Port Name (WWPN) of the LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _current_port = None
    @property
    def current_port(self):
        """
        FC Adapter currently hosting the LIF.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_port
    @current_port.setter
    def current_port(self, val):
        if val != None:
            self.validate('current_port', val)
        self._current_port = val
    
    @staticmethod
    def get_api_name():
          return "fcp-interface-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'current-node',
            'port-address',
            'interface-name',
            'relative-port-id',
            'vserver',
            'node-name',
            'port-name',
            'current-port',
        ]
    
    def describe_properties(self):
        return {
            'current_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'relative_port_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'current_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
