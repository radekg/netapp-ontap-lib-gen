from netapp.netapp_object import NetAppObject

class RoutingGroupRouteInfo(NetAppObject):
    """
    Routing group route information
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
    
    _routing_group = None
    @property
    def routing_group(self):
        """
        Specifies the name of routing group.
        For example:
        <ul>
        <li> d192.168.1.0/24 ('d' stands for data LIF and
        192.168.1.0/24 is subnet),
        <li> c192.168.1.0/24 ('c' stands for cluster LIF and
        192.168.1.0/24 is subnet),
        <li> n192.168.1.0/24 ('n' stands for node management LIF
        and 192.168.1.0/24 is subnet)
        <li> dfd20:13::0/64  ('d' stands for data LIF and
        fd20:13::0/64 is IPv6 subnet)
        </ul>
        Attributes: key, required-for-create, non-modifiable
        """
        return self._routing_group
    @routing_group.setter
    def routing_group(self, val):
        if val != None:
            self.validate('routing_group', val)
        self._routing_group = val
    
    _metric = None
    @property
    def metric(self):
        """
        Specifies the metric (hop count) of the LIF.
        The default value is determined by the LIF role as
        follows:
        <ul>
        <li> If the LIF role is 'node_mgmt' or 'cluster_mgmt':
        10,
        <li> If the LIF role is 'data' or 'undef': 20,
        <li> If the LIF role is 'cluster': 30,
        <li> If the LIF role is 'intercluster': 40
        </ul>
        Attributes: optional-for-create, non-modifiable
        """
        return self._metric
    @metric.setter
    def metric(self, val):
        if val != None:
            self.validate('metric', val)
        self._metric = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Specifies the name of Vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _gateway_address = None
    @property
    def gateway_address(self):
        """
        Specifies the IP address of gateway.
        For example: '198.18.0.0', 'fd20:13::1'
        Attributes: required-for-create, non-modifiable
        """
        return self._gateway_address
    @gateway_address.setter
    def gateway_address(self, val):
        if val != None:
            self.validate('gateway_address', val)
        self._gateway_address = val
    
    _destination_address = None
    @property
    def destination_address(self):
        """
        Specifies the IP address and subnet mask of destination.
        For example: '198.18.10.0/24', 'fd20:13::0/64'
        Attributes: key, required-for-create, non-modifiable
        """
        return self._destination_address
    @destination_address.setter
    def destination_address(self, val):
        if val != None:
            self.validate('destination_address', val)
        self._destination_address = val
    
    _address_family = None
    @property
    def address_family(self):
        """
        Address Family. Possible values: ipv4, ipv6
        Attributes: non-creatable, non-modifiable
        """
        return self._address_family
    @address_family.setter
    def address_family(self, val):
        if val != None:
            self.validate('address_family', val)
        self._address_family = val
    
    @staticmethod
    def get_api_name():
          return "routing-group-route-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'routing-group',
            'metric',
            'vserver',
            'gateway-address',
            'destination-address',
            'address-family',
        ]
    
    def describe_properties(self):
        return {
            'routing_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'metric': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gateway_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address_family': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
