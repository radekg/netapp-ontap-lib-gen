from netapp.netapp_object import NetAppObject

class VlanInfo(NetAppObject):
    """
    vlan
    """
    
    _node = None
    @property
    def node(self):
        """
        Node name of vlan interface.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _gvrp_enabled = None
    @property
    def gvrp_enabled(self):
        """
        true: GVRP is enabled.
        Default is false.
        GVRP is deprecated and this attribute is ignored in cluster
        mode. GVRP is a standard vlan trunking protocol that
        enables a port to advertise which vlans it trunks, thereby
        decreasing traffic over the trunk. This protocol eliminates
        the need to manually configure vlan information on each
        switch in the network.
        """
        return self._gvrp_enabled
    @gvrp_enabled.setter
    def gvrp_enabled(self, val):
        if val != None:
            self.validate('gvrp_enabled', val)
        self._gvrp_enabled = val
    
    _parent_interface = None
    @property
    def parent_interface(self):
        """
        The interface that hosts the vlan interface.
        """
        return self._parent_interface
    @parent_interface.setter
    def parent_interface(self, val):
        if val != None:
            self.validate('parent_interface', val)
        self._parent_interface = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of vlan interface. The name must be of the format
        &lt;parent-inteface&gt;-&lt;vlanid&gt;
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _vlanid = None
    @property
    def vlanid(self):
        """
        The vlan id.  Range: 1..4094.
        """
        return self._vlanid
    @vlanid.setter
    def vlanid(self, val):
        if val != None:
            self.validate('vlanid', val)
        self._vlanid = val
    
    @staticmethod
    def get_api_name():
          return "vlan-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'gvrp-enabled',
            'parent-interface',
            'interface-name',
            'vlanid',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gvrp_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'parent_interface': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vlanid': { 'class': int, 'is_list': False, 'required': 'required' },
        }
