from netapp.netapp_object import NetAppObject

class FcpAdapterZoneMemberInfo(NetAppObject):
    """
    Information about a zone member.
    """
    
    _zone_member_type = None
    @property
    def zone_member_type(self):
        """
        The type of zone member. Possible values
        are: "port-name", "domain-id-port", "port-id",
        "node-name", "fabric-port-name", and "unknown".
        """
        return self._zone_member_type
    @zone_member_type.setter
    def zone_member_type(self, val):
        if val != None:
            self.validate('zone_member_type', val)
        self._zone_member_type = val
    
    _zone_member_value = None
    @property
    def zone_member_value(self):
        """
        Uninterpreted value. This element is returned if
        the zone-member-type is "unknown".
        Range: [0..2^32-1]
        """
        return self._zone_member_value
    @zone_member_value.setter
    def zone_member_value(self, val):
        if val != None:
            self.validate('zone_member_value', val)
        self._zone_member_value = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        World wide node name (WWNN) of the N-port. This
        element is returned if the zone-member-type is
        "node-name". The format is:
        XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal
        digit.
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
        Assigned port identifier. This element is
        returned if the zone-member-type is "port-id".
        Range: [0..2^24-1]
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    _domain_id = None
    @property
    def domain_id(self):
        """
        Domain identifier of the switch. This element is
        returned if the zone-member-type is
        "domain-id-port". Range: [0..2^32-1]
        """
        return self._domain_id
    @domain_id.setter
    def domain_id(self, val):
        if val != None:
            self.validate('domain_id', val)
        self._domain_id = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        World wide port name (WWPN) of the N-port. This
        element is returned if the zone-member-type is
        "port-name". The format is:
        XX:XX:XX:XX:XX:XX:XX:XX where X is a hexadecimal
        digit.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _port = None
    @property
    def port(self):
        """
        Port number on the switch. This element is
        returned if the zone-member-type is
        "domain-id-port". Range: [0..2^32-1]
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    _fabric_port_name = None
    @property
    def fabric_port_name(self):
        """
        World wide port name (WWPN) of the fabric port.
        This element is returned if the zone-member-type
        is "fabric-port-name".
        The format is: XX:XX:XX:XX:XX:XX:XX:XX
        where X is a hexadecimal digit.
        """
        return self._fabric_port_name
    @fabric_port_name.setter
    def fabric_port_name(self, val):
        if val != None:
            self.validate('fabric_port_name', val)
        self._fabric_port_name = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-zone-member-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zone-member-type',
            'zone-member-value',
            'node-name',
            'port-id',
            'domain-id',
            'port-name',
            'port',
            'fabric-port-name',
        ]
    
    def describe_properties(self):
        return {
            'zone_member_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'zone_member_value': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'domain_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fabric_port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
