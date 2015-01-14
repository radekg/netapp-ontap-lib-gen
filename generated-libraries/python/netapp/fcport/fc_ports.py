from netapp.netapp_object import NetAppObject

class FcPorts(NetAppObject):
    """
    Information about the ports belonging to the
    fiber channel adapter
    """
    
    _switch_name = None
    @property
    def switch_name(self):
        """
        Thsi is the switch name, if any, connected to the FC port.
        Field is not present when port-type is "l-port"
        """
        return self._switch_name
    @switch_name.setter
    def switch_name(self, val):
        if val != None:
            self.validate('switch_name', val)
        self._switch_name = val
    
    _switch_wwn = None
    @property
    def switch_wwn(self):
        """
        This is the world wide name of the switch, if any, connected
        to the FC port.
        Field is not present when port-type is "l-port"
        """
        return self._switch_wwn
    @switch_wwn.setter
    def switch_wwn(self, val):
        if val != None:
            self.validate('switch_wwn', val)
        self._switch_wwn = val
    
    _port_number = None
    @property
    def port_number(self):
        """
        This represents the physical port number of the FC port.
        Field is not present when port-type is "l-port"
        """
        return self._port_number
    @port_number.setter
    def port_number(self, val):
        if val != None:
            self.validate('port_number', val)
        self._port_number = val
    
    _port_type = None
    @property
    def port_type(self):
        """
        Type of port. Possible values:
        "l-port", loop port, node port used to connect a node to a Fibre Channel loop.
        "nl-port", network+loop port, node port which connects to both loops and switches.
        "n-port", network port, node port used to connect a node to a Fibre Channel switch.
        """
        return self._port_type
    @port_type.setter
    def port_type(self, val):
        if val != None:
            self.validate('port_type', val)
        self._port_type = val
    
    @staticmethod
    def get_api_name():
          return "fc-ports"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'switch-name',
            'switch-wwn',
            'port-number',
            'port-type',
        ]
    
    def describe_properties(self):
        return {
            'switch_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'switch_wwn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
