from netapp.netapp_object import NetAppObject

class ExportsHostnameInfo(NetAppObject):
    """
    Structure containing information pertaining to a host.
    """
    
    _negate = None
    @property
    def negate(self):
        """
        In Data ONTAP 7-Mode, default is false. If true, the rule
        applies to every host but this one. Used most commonly
        when adding a group minus a few hosts.
        In Data ONTAP Cluster-Mode, negations are not supported.
        An error will be returned if true.
        """
        return self._negate
    @negate.setter
    def negate(self, val):
        if val != None:
            self.validate('negate', val)
        self._negate = val
    
    _name = None
    @property
    def name(self):
        """
        A hostname can be ONE of the following formats. If
        'all-hosts' is true, 'name' must not have a value.
        machine-name: Alphanumeric string based on DNS.
        netgroup: Alphanumeric string describing a group of
        &nbsp; machine names
        ip: An IP address in dotted decimal format AAA.BBB.CCC.DDD
        subnet: "[network] subnet [netmask] netmask"
        ip-subnet: IP/numbits. The IP is a subnet number and the
        &nbsp; numbits specifies the size of the subnet by the
        &nbsp; number of leading bits of the netmask.
        dns: A DNS domain. An Alphanumeric starting with a '.'
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _all_hosts = None
    @property
    def all_hosts(self):
        """
        Default value is false. If true,  enables all hosts to
        have this rule's access rights. A hostname of 'all-hosts'
        must exist as the only non-negated element in a hostname
        array.
        """
        return self._all_hosts
    @all_hosts.setter
    def all_hosts(self, val):
        if val != None:
            self.validate('all_hosts', val)
        self._all_hosts = val
    
    @staticmethod
    def get_api_name():
          return "exports-hostname-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'negate',
            'name',
            'all-hosts',
        ]
    
    def describe_properties(self):
        return {
            'negate': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'all_hosts': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
