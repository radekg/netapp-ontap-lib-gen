from netapp.netapp_object import NetAppObject

class CfAggregateGivebackInfo(NetAppObject):
    """
    Giveback status of an aggregate
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
        Node performing the giveback of aggregate
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _aggr_giveback_state = None
    @property
    def aggr_giveback_state(self):
        """
        Giveback status of the aggregate
        Possible values include:
        <ul>
        <li>"sfo_am_done" - Giveback done</li>
        <li>"sfo_am_failed" - Giveback failed</li>
        <li>"sfo_am_inprog" - Giveback in progress</li>
        <li>"sfo_am_not_started" - Giveback not started</li>
        <li>"sfo_am_nothing_to_gb" - No aggregates to giveback</li>
        <li>"sfo_disk_inventory_not_exchanged" - Auto giveback failed
        because disk inventory was not exchanged between HA
        partners</li>
        <li>"sfo_disk_inventory_mismatch" - Auto giveback failed
        because there was mismatch in disk inventory</li>
        <li>"sfo_am_failed_bdfu_source" - Giveback failed as failed to
        disable background disk firmware update on source node.</li>
        <li>"sfo_am_failed_bdfu_dest" - Giveback failed as failed to
        disable background disk firmware update on destination node.</li>
        <li>"sfo_am_delayed_bdfu_source" - Giveback delayed as disk
        firmware update is in progress on source node.</li>
        <li>"sfo_am_delayed_bdfu_dest" - Giveback delayed as disk
        firmware update is in progress on destination node.</li>
        <li>"sfo_am_running_checks" - Performing veto checks.</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._aggr_giveback_state
    @aggr_giveback_state.setter
    def aggr_giveback_state(self, val):
        if val != None:
            self.validate('aggr_giveback_state', val)
        self._aggr_giveback_state = val
    
    _aggr_giveback_module = None
    @property
    def aggr_giveback_module(self):
        """
        If giveback is in progress, then this is
        set to the module which is currently running. If
        giveback was failed or vetoed by a certain
        module then this is set to the first module which
        failed the giveback.
        Example: WAFL.
        Attributes: non-creatable, non-modifiable
        """
        return self._aggr_giveback_module
    @aggr_giveback_module.setter
    def aggr_giveback_module(self, val):
        if val != None:
            self.validate('aggr_giveback_module', val)
        self._aggr_giveback_module = val
    
    _aggr_giveback_error = None
    @property
    def aggr_giveback_error(self):
        """
        Failure reason, incase giveback of this
        aggregate failed.
        Possible values include:
        <ul>
        <li>"sfo_am_shutdown" - Node is being shutdown</li>
        <li>"sfo_am_not_homed_partner" - Aggregate not owned by partner</li>
        <li>"sfo_am_not_sfo" - Aggregate does not have SFO policy</li>
        <li>"sfo_am_failed_limbo" - Aggregate in failed or limbo state</li>
        <li>"sfo_am_offline_failed" - Aggregate could not be
        offlined during giveback</li>
        <li>"sfo_am_migrating" - Aggregate is being migrated</li>
        <li>"sfo_am_veto" - Giveback was vetoed.</li>
        <li>"sfo_am_communication_err" - Giveback failed because
        node cannot communicate with the partner</li>
        <li>"sfo_am_online_timeout" - Aggregate did not come online
        after giveback</li>
        <li>"sfo_am_online_failed" - Failed to online the
        aggregate after giveback</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._aggr_giveback_error
    @aggr_giveback_error.setter
    def aggr_giveback_error(self, val):
        if val != None:
            self.validate('aggr_giveback_error', val)
        self._aggr_giveback_error = val
    
    _aggregate = None
    @property
    def aggregate(self):
        """
        Aggregate name
        Attributes: non-creatable, non-modifiable
        """
        return self._aggregate
    @aggregate.setter
    def aggregate(self, val):
        if val != None:
            self.validate('aggregate', val)
        self._aggregate = val
    
    _destination_node = None
    @property
    def destination_node(self):
        """
        Node to which the aggregate is being given back
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_node
    @destination_node.setter
    def destination_node(self, val):
        if val != None:
            self.validate('destination_node', val)
        self._destination_node = val
    
    @staticmethod
    def get_api_name():
          return "cf-aggregate-giveback-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'aggr-giveback-state',
            'aggr-giveback-module',
            'aggr-giveback-error',
            'aggregate',
            'destination-node',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_giveback_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_giveback_module': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_giveback_error': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
