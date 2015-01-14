from netapp.netapp_object import NetAppObject

class AggrRelocationInfo(NetAppObject):
    """
    Aggregate Information
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
    
    _aggregate = None
    @property
    def aggregate(self):
        """
        Aggregate Name
        Attributes: non-creatable, non-modifiable
        """
        return self._aggregate
    @aggregate.setter
    def aggregate(self, val):
        if val != None:
            self.validate('aggregate', val)
        self._aggregate = val
    
    _destination = None
    @property
    def destination(self):
        """
        Destination for Relocation
        Attributes: non-creatable, non-modifiable
        """
        return self._destination
    @destination.setter
    def destination(self, val):
        if val != None:
            self.validate('destination', val)
        self._destination = val
    
    _relocation_status = None
    @property
    def relocation_status(self):
        """
        Aggregates Relocation Status
        Attributes: non-creatable, non-modifiable
        Possible values include:
        <ul>
        <li>Done</li>
        <li>Failed</li>
        <li>In progress</li>
        <li>Not attempted yet</li>
        <li>Failed: Migration of the aggregate failed</li>
        <li>Failed: Node is being shut down</li>
        <li>Failed: Aggregate does not have SFO HA policy</li>
        <li>Failed: Aggregate is in failed or limbo state.</li>
        <li>Failed to offline the aggregate</li>
        <li>Failed: Aggregate is being given back or relocated</li>
        <li>Failed: Operation was vetoed</li>
        <li>No aggregates to relocate</li>
        <li>Performing relocation veto checks</li>
        <li>check EMS logs</li>
        <li>Failed: Node cannot communicate with the destination node</li>
        <li>Failed: Destination node did not online the aggregate on time</li>
        <li>Failed: Destination node failed to online the aggregate. Check EMS logs on destination node</li>
        <li>Failed: Destination cannot receive the aggregate</li>
        <li>Failed: Aggregate is restricted</li>
        <li>Failed: Aggregate does not have disks</li>
        <li>Operation was aborted</li>
        <li>Failed: Aggregate is foreign</li>
        <li>Failed: Aggregate is offline</li>
        <li>Failed: Mirrored aggregate does not have both plexes online</li>
        <li>Aborted. Failed to disable background disk firmware updates on the source node.</li>
        <li>Aborted. Failed to disable background disk firmware updates on the destination node.</li>
        <li>Deferred. Background disk firmware update is in progress on source node.</li>
        <li>Deferred. Background disk firmware update is in progress on destination node.</li>
        <ul>
        """
        return self._relocation_status
    @relocation_status.setter
    def relocation_status(self, val):
        if val != None:
            self.validate('relocation_status', val)
        self._relocation_status = val
    
    _source_node = None
    @property
    def source_node(self):
        """
        Name of the source node in which aggregate resides
        Attributes: key, non-creatable, non-modifiable
        """
        return self._source_node
    @source_node.setter
    def source_node(self, val):
        if val != None:
            self.validate('source_node', val)
        self._source_node = val
    
    @staticmethod
    def get_api_name():
          return "aggr-relocation-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'aggregate',
            'destination',
            'relocation-status',
            'source-node',
        ]
    
    def describe_properties(self):
        return {
            'aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'relocation_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
