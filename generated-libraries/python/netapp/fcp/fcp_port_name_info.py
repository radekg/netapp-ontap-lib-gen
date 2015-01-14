from netapp.netapp_object import NetAppObject

class FcpPortNameInfo(NetAppObject):
    """
    Information for one valid local port name.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing this port name
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        A Fibre Channel WWPN in the form
        XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal digit.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _fcp_adapter = None
    @property
    def fcp_adapter(self):
        """
        Only if this WWPN is being used by a Fibre Channel
        interface, the name of the interface is returned.
        In Data ONTAP 7-Mode, the name of a local adapter.
        In Data ONTAP Cluster-Mode, the name of an FCP
        data LIF.
        """
        return self._fcp_adapter
    @fcp_adapter.setter
    def fcp_adapter(self, val):
        if val != None:
            self.validate('fcp_adapter', val)
        self._fcp_adapter = val
    
    _is_used = None
    @property
    def is_used(self):
        """
        This indicates whether this WWPN is being used by a
        Fibre Channel target interface.
        """
        return self._is_used
    @is_used.setter
    def is_used(self, val):
        if val != None:
            self.validate('is_used', val)
        self._is_used = val
    
    @staticmethod
    def get_api_name():
          return "fcp-port-name-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'port-name',
            'fcp-adapter',
            'is-used',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fcp_adapter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_used': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
