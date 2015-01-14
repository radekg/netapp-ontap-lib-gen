from netapp.netapp_object import NetAppObject

class FcpAdapterTopologyAttachedPortInfo(NetAppObject):
    """
    Information about the attached device.
    """
    
    _port_name = None
    @property
    def port_name(self):
        """
        World wide port name (WWPN)
        of the attached device.
        The format is: XX:XX:XX:XX:XX:XX:XX:XX
        where X is a hexadecimal digit.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _is_visible = None
    @property
    def is_visible(self):
        """
        Visibility of this device through this
        adapter from a zoning perspective.
        """
        return self._is_visible
    @is_visible.setter
    def is_visible(self, val):
        if val != None:
            self.validate('is_visible', val)
        self._is_visible = val
    
    _port_id = None
    @property
    def port_id(self):
        """
        Assigned port identifier of the attached
        device. A value of 0 indicates no value has
        been assigned. Range: [0..2^24-1]
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-topology-attached-port-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'port-name',
            'is-visible',
            'port-id',
        ]
    
    def describe_properties(self):
        return {
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_visible': { 'class': bool, 'is_list': False, 'required': 'required' },
            'port_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
