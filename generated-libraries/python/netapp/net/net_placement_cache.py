from netapp.netapp_object import NetAppObject

class NetPlacementCache(NetAppObject):
    """
    Network interface (LIF) placement cached information
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
    
    _node = None
    @property
    def node(self):
        """
        Specifies the name of the node.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, required-for-create, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _address = None
    @property
    def address(self):
        """
        The IP address that was searched.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._address
    @address.setter
    def address(self, val):
        if val != None:
            self.validate('address', val)
        self._address = val
    
    _netmask_length = None
    @property
    def netmask_length(self):
        """
        The number of bits in the subnet mask (i.e. 24 or 64).
        Attributes: key, required-for-create, non-modifiable
        """
        return self._netmask_length
    @netmask_length.setter
    def netmask_length(self, val):
        if val != None:
            self.validate('netmask_length', val)
        self._netmask_length = val
    
    _found = None
    @property
    def found(self):
        """
        Whether the subnet described was found on this port.
        Attributes: non-creatable, non-modifiable
        """
        return self._found
    @found.setter
    def found(self, val):
        if val != None:
            self.validate('found', val)
        self._found = val
    
    _port = None
    @property
    def port(self):
        """
        The port name on the node.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    @staticmethod
    def get_api_name():
          return "net-placement-cache"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'vserver',
            'address',
            'netmask-length',
            'found',
            'port',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netmask_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'found': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
