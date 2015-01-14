from netapp.netapp_object import NetAppObject

class ClusterNodeInfo(NetAppObject):
    """
    Information that identifies state of nodes in a cluster.
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
    
    _is_node_eligible = None
    @property
    def is_node_eligible(self):
        """
        This parameter states nodes that are eligible to
        participate in the cluster. A boolean value of true means
        the node is eligible.
        Attributes: non-creatable, modifiable
        """
        return self._is_node_eligible
    @is_node_eligible.setter
    def is_node_eligible(self, val):
        if val != None:
            self.validate('is_node_eligible', val)
        self._is_node_eligible = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The textual name of a node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _is_node_healthy = None
    @property
    def is_node_healthy(self):
        """
        This parameter is used to determine health of a node in a
        cluster. A boolean value of true means the node is
        healthy.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_node_healthy
    @is_node_healthy.setter
    def is_node_healthy(self, val):
        if val != None:
            self.validate('is_node_healthy', val)
        self._is_node_healthy = val
    
    _is_node_epsilon = None
    @property
    def is_node_epsilon(self):
        """
        You can designate a node as epsilon to add weight to its
        voting in a cluster with an even number of nodes. In a
        cluster, only one node can be designated as epsilon at
        any given time. A boolean value of true means the node is
        epsilon.
        Attributes: non-creatable, modifiable
        """
        return self._is_node_epsilon
    @is_node_epsilon.setter
    def is_node_epsilon(self, val):
        if val != None:
            self.validate('is_node_epsilon', val)
        self._is_node_epsilon = val
    
    _node_uuid = None
    @property
    def node_uuid(self):
        """
        The 128-bit universally-unique identifier, that
        designates a node forever, assigned during node
        creation.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_uuid
    @node_uuid.setter
    def node_uuid(self, val):
        if val != None:
            self.validate('node_uuid', val)
        self._node_uuid = val
    
    @staticmethod
    def get_api_name():
          return "cluster-node-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-node-eligible',
            'node-name',
            'is-node-healthy',
            'is-node-epsilon',
            'node-uuid',
        ]
    
    def describe_properties(self):
        return {
            'is_node_eligible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_node_healthy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_node_epsilon': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
