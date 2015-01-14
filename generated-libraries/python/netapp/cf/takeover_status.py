from netapp.netapp_object import NetAppObject

class TakeoverStatus(NetAppObject):
    """
    Takeover status of a node and all of its partner aggregates.
    When returned as part of the output, all elements of this
    typedef are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be
    returned in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, assuming that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be
    omitted in which case the resulting set of objects is not constrained
    by any specific value of that attribute.
    """
    
    _node = None
    @property
    def node(self):
        """
        Name of the node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _node_takeover_status = None
    @property
    def node_takeover_status(self):
        """
        Takeover status of the node.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_takeover_status
    @node_takeover_status.setter
    def node_takeover_status(self, val):
        if val != None:
            self.validate('node_takeover_status', val)
        self._node_takeover_status = val
    
    _taken_over_aggregate = None
    @property
    def taken_over_aggregate(self):
        """
        Name of the taken over aggregate.
        Attributes: non-creatable, non-modifiable
        """
        return self._taken_over_aggregate
    @taken_over_aggregate.setter
    def taken_over_aggregate(self, val):
        if val != None:
            self.validate('taken_over_aggregate', val)
        self._taken_over_aggregate = val
    
    _aggregate_takeover_status = None
    @property
    def aggregate_takeover_status(self):
        """
        Takeover status of the partner aggregate.
        This includes the reason for the failure of takeover
        of an aggregate. If takeover is in progress in a
        particular module, or if takeover was vetoed by a
        particular module, that is also indicated.
        Possible values include:
        <ul>
        <li>Done</li>
        <li>Failed</li>
        <li>In progress, Module: wafl</li>
        <li>Not attempted yet</li>
        <li>Failed: Operation was vetoed,
        Module: example. The aggregate will be taken over during
        CFO phase of takeover.</li>
        <li>Failed: Aggregate does not have SFO HA
        policy. The aggregate will be taken over during CFO phase
        of takeover.</li>
        <li>Failed: Aggregate is in failed or limbo
        state. The aggregate will be taken over during CFO phase
        of takeover.</li>
        <li>Failed to offline the aggregate. The aggregate will
        be taken over during CFO phase of takeover.</li>
        <li>No aggregates to relocate</li>
        <li>Failed: Node cannot communicate with
        the destination node. To takeover the remaining
        aggregates, run the "storage failover takeover -ofnode
        <node_to_be_taken_over> -bypass-optimization true" command.
        To giveback the relocated aggregates, run the
        "storage failover giveback -ofnode <node_to_be_given_back>"
        command.</li>
        <li>Failed: Destination node did not
        online the aggregate on time. To takeover the remaining
        aggregates, run the "storage failover takeover -ofnode
        <node_to_be_taken_over> -bypass-optimization true"
        command. To giveback the relocated aggregates, run the
        "storage failover giveback -ofnode <node_to_be_given_back>"
        command.</li>
        <li>Failed: Destination node failed to
        online the aggregate. To takeover the remaining
        aggregates, run the "storage failover takeover -ofnode
        <node_to_be_taken_over> -bypass-optimization true"
        command. To giveback the relocated aggregates, run the
        "storage failover giveback -ofnode
        <node_to_be_given_back>" command.</li>
        <li>Failed: Destination cannot receive
        the aggregate. To takeover the remaining
        aggregates, run the "storage failover takeover -ofnode
        <node_to_be_taken_over> -bypass-optimization true"
        command. To giveback the relocated aggregates, run the
        "storage failover giveback -ofnode
        <node_to_be_given_back>" command.</li>
        <li>Failed: Aggregate is restricted. The aggregate will
        be taken over during CFO phase of takeover.</li>
        <li>Failed: Aggregate does not have disks.
        The aggregate will be taken over during CFO phase
        of takeover.</li>
        <li>Failed: Aggregate is foreign. The aggregate will be
        taken over during CFO phase of takeover.</li>
        <li>Failed: Aggregate is offline.
        The aggregate will be taken over during CFO phase
        of takeover.</li>
        <li>Failed: Mirrored aggregate does not have both plexes
        online. The aggregate will be taken over during CFO phase
        of takeover.</li>
        <li>Failed, could not disable firmware updates on
        <node_where_BDFU_could_not_be_disabled>.</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._aggregate_takeover_status
    @aggregate_takeover_status.setter
    def aggregate_takeover_status(self, val):
        if val != None:
            self.validate('aggregate_takeover_status', val)
        self._aggregate_takeover_status = val
    
    @staticmethod
    def get_api_name():
          return "takeover-status"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'node-takeover-status',
            'taken-over-aggregate',
            'aggregate-takeover-status',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node_takeover_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'taken_over_aggregate': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'aggregate_takeover_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
