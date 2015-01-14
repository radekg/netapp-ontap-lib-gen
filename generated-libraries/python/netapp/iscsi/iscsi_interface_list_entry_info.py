from netapp.netapp_object import NetAppObject

class IscsiInterfaceListEntryInfo(NetAppObject):
    """
    Information about a single interface
    """
    
    _current_node = None
    @property
    def current_node(self):
        """
        Name of the node currently hosting the
        LIF.
        """
        return self._current_node
    @current_node.setter
    def current_node(self, val):
        if val != None:
            self.validate('current_node', val)
        self._current_node = val
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        Id of target portal group interface
        is associated with.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _is_interface_enabled = None
    @property
    def is_interface_enabled(self):
        """
        "true" if interface enabled for iSCSI, "false" otherwise.
        """
        return self._is_interface_enabled
    @is_interface_enabled.setter
    def is_interface_enabled(self, val):
        if val != None:
            self.validate('is_interface_enabled', val)
        self._is_interface_enabled = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        Name of target portal group interface is associated with.
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of interface.
        In Data ONTAP 7-Mode, this is the name of a
        physical ethernet interface, for example: "e0c".
        In Data ONTAP Cluster-Mode, this is the name
        of an iSCSI data LIF in the Vserver.
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
        The SCSI Relative Target Port Identifier
        of the LIF.
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
        The name of the vserver containing
        this iSCSI data LIF.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _ip_port = None
    @property
    def ip_port(self):
        """
        iSCSI target portal TCP port.
        """
        return self._ip_port
    @ip_port.setter
    def ip_port(self, val):
        if val != None:
            self.validate('ip_port', val)
        self._ip_port = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        iSCSI target portal IP address.
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _current_port = None
    @property
    def current_port(self):
        """
        Name of the physical ethernet interface
        currently hosting the LIF.
        """
        return self._current_port
    @current_port.setter
    def current_port(self, val):
        if val != None:
            self.validate('current_port', val)
        self._current_port = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-interface-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'current-node',
            'tpgroup-tag',
            'is-interface-enabled',
            'tpgroup-name',
            'interface-name',
            'relative-port-id',
            'vserver',
            'ip-port',
            'ip-address',
            'current-port',
        ]
    
    def describe_properties(self):
        return {
            'current_node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_interface_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'relative_port_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
