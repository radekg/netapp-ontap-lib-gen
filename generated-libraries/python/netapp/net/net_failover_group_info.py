from netapp.netapp_object import NetAppObject

class NetFailoverGroupInfo(NetAppObject):
    """
    Network failover group information
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
        The node on which the failover target (a network port or
        interface group) is located.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _port = None
    @property
    def port(self):
        """
        The network port or interface group in the failover
        group.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._port
    @port.setter
    def port(self, val):
        if val != None:
            self.validate('port', val)
        self._port = val
    
    _failover_group = None
    @property
    def failover_group(self):
        """
        A grouping of failover targets for logical interfaces on
        one or more nodes.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._failover_group
    @failover_group.setter
    def failover_group(self, val):
        if val != None:
            self.validate('failover_group', val)
        self._failover_group = val
    
    @staticmethod
    def get_api_name():
          return "net-failover-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'port',
            'failover-group',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'failover_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
