from netapp.netapp_object import NetAppObject

class IpAddressInfo(NetAppObject):
    """
    A configured IP Address
    """
    
    _netmask_or_prefix = None
    @property
    def netmask_or_prefix(self):
        """
        netmask or prefix
        Default if not specified is autogenerated classful.
        """
        return self._netmask_or_prefix
    @netmask_or_prefix.setter
    def netmask_or_prefix(self, val):
        if val != None:
            self.validate('netmask_or_prefix', val)
        self._netmask_or_prefix = val
    
    _lif_type = None
    @property
    def lif_type(self):
        """
        type of LIF.  Possible values are 7G, Data, Cluster, Mgmt,
        ClusMgmt, InterCluster
        """
        return self._lif_type
    @lif_type.setter
    def lif_type(self, val):
        if val != None:
            self.validate('lif_type', val)
        self._lif_type = val
    
    _creator = None
    @property
    def creator(self):
        """
        Entity responsible for creation of address.
        "vfiler:<vfiler name>" if created by d-blade for vfiler.
        "vserver:<vserver name>" if created by n-blade with
        cluster-wide scope.
        """
        return self._creator
    @creator.setter
    def creator(self, val):
        if val != None:
            self.validate('creator', val)
        self._creator = val
    
    _no_ddns = None
    @property
    def no_ddns(self):
        """
        true: the address is not advertised to ddns.
        Default if not specified is true.
        """
        return self._no_ddns
    @no_ddns.setter
    def no_ddns(self, val):
        if val != None:
            self.validate('no_ddns', val)
        self._no_ddns = val
    
    _broadcast = None
    @property
    def broadcast(self):
        """
        broadcast address.  Default if not specified
        is computed from IP address and netmask.  Not
        used for IPV6.  Must be consistent with netmask.
        """
        return self._broadcast
    @broadcast.setter
    def broadcast(self, val):
        if val != None:
            self.validate('broadcast', val)
        self._broadcast = val
    
    _addr_family = None
    @property
    def addr_family(self):
        """
        Address family.  Possible values: {af-inet6 | af-inet}.
        """
        return self._addr_family
    @addr_family.setter
    def addr_family(self, val):
        if val != None:
            self.validate('addr_family', val)
        self._addr_family = val
    
    _address = None
    @property
    def address(self):
        """
        IP address.
        """
        return self._address
    @address.setter
    def address(self, val):
        if val != None:
            self.validate('address', val)
        self._address = val
    
    @staticmethod
    def get_api_name():
          return "ip-address-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'netmask-or-prefix',
            'lif-type',
            'creator',
            'no-ddns',
            'broadcast',
            'addr-family',
            'address',
        ]
    
    def describe_properties(self):
        return {
            'netmask_or_prefix': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lif_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creator': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'no_ddns': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'broadcast': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'addr_family': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'address': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
