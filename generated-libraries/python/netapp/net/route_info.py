from netapp.netapp_object import NetAppObject

class RouteInfo(NetAppObject):
    """
    A kernel route.
    """
    
    _creator = None
    @property
    def creator(self):
        """
        Entity responsible for creation of route.
        Possible values: "filer" if created by d-blade for default vfiler.
        "vfiler: <vfiler name>" if created by d-blade for vfiler.
        "vserver: <vserver name>" if created by n-blade with
        cluster-wide scope.
        """
        return self._creator
    @creator.setter
    def creator(self, val):
        if val != None:
            self.validate('creator', val)
        self._creator = val
    
    _metric = None
    @property
    def metric(self):
        """
        The route metric.  Range: 0-10
        """
        return self._metric
    @metric.setter
    def metric(self, val):
        if val != None:
            self.validate('metric', val)
        self._metric = val
    
    _destination = None
    @property
    def destination(self):
        """
        Destination of route.  Possible values: An IP address,
        hostname, or "default".
        """
        return self._destination
    @destination.setter
    def destination(self, val):
        if val != None:
            self.validate('destination', val)
        self._destination = val
    
    _addr_family = None
    @property
    def addr_family(self):
        """
        Address family.
        Possible values: {af-inet6 | af-inet}.
        """
        return self._addr_family
    @addr_family.setter
    def addr_family(self, val):
        if val != None:
            self.validate('addr_family', val)
        self._addr_family = val
    
    _route_type = None
    @property
    def route_type(self):
        """
        Possible values: "net" or "host".
        """
        return self._route_type
    @route_type.setter
    def route_type(self, val):
        if val != None:
            self.validate('route_type', val)
        self._route_type = val
    
    _ipspace_name = None
    @property
    def ipspace_name(self):
        """
        IPSpace name. Must match the ipspace assigned to the creator.
        """
        return self._ipspace_name
    @ipspace_name.setter
    def ipspace_name(self, val):
        if val != None:
            self.validate('ipspace_name', val)
        self._ipspace_name = val
    
    _prefixlen = None
    @property
    def prefixlen(self):
        """
        Prefix length (netmask) for destination.
        Range: 1..32 for af-inet and 1..128 for af-inet6.
        """
        return self._prefixlen
    @prefixlen.setter
    def prefixlen(self, val):
        if val != None:
            self.validate('prefixlen', val)
        self._prefixlen = val
    
    _next_hop = None
    @property
    def next_hop(self):
        """
        Next hop (router) IP address.
        """
        return self._next_hop
    @next_hop.setter
    def next_hop(self, val):
        if val != None:
            self.validate('next_hop', val)
        self._next_hop = val
    
    @staticmethod
    def get_api_name():
          return "route-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'creator',
            'metric',
            'destination',
            'addr-family',
            'route-type',
            'ipspace-name',
            'prefixlen',
            'next-hop',
        ]
    
    def describe_properties(self):
        return {
            'creator': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'metric': { 'class': int, 'is_list': False, 'required': 'required' },
            'destination': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'addr_family': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'route_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ipspace_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'prefixlen': { 'class': int, 'is_list': False, 'required': 'optional' },
            'next_hop': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
