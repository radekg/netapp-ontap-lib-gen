from netapp.netapp_object import NetAppObject

class FcConfig(NetAppObject):
    """
    fc config
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
    
    _adapter_type = None
    @property
    def adapter_type(self):
        """
        Adaptaer type
        Attributes: non-creatable, non-modifiable
        """
        return self._adapter_type
    @adapter_type.setter
    def adapter_type(self, val):
        if val != None:
            self.validate('adapter_type', val)
        self._adapter_type = val
    
    _pending_fc_type = None
    @property
    def pending_fc_type(self):
        """
        Pending reason
        Attributes: non-creatable, non-modifiable
        """
        return self._pending_fc_type
    @pending_fc_type.setter
    def pending_fc_type(self, val):
        if val != None:
            self.validate('pending_fc_type', val)
        self._pending_fc_type = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        Node name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _adapter_name = None
    @property
    def adapter_name(self):
        """
        Adapter name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._adapter_name
    @adapter_name.setter
    def adapter_name(self, val):
        if val != None:
            self.validate('adapter_name', val)
        self._adapter_name = val
    
    _adapter_state = None
    @property
    def adapter_state(self):
        """
        Adapter current state
        Attributes: non-creatable, non-modifiable
        """
        return self._adapter_state
    @adapter_state.setter
    def adapter_state(self, val):
        if val != None:
            self.validate('adapter_state', val)
        self._adapter_state = val
    
    _adapter_status = None
    @property
    def adapter_status(self):
        """
        Adapter online status
        Attributes: non-creatable, non-modifiable
        """
        return self._adapter_status
    @adapter_status.setter
    def adapter_status(self, val):
        if val != None:
            self.validate('adapter_status', val)
        self._adapter_status = val
    
    @staticmethod
    def get_api_name():
          return "fc-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter-type',
            'pending-fc-type',
            'node-name',
            'adapter-name',
            'adapter-state',
            'adapter-status',
        ]
    
    def describe_properties(self):
        return {
            'adapter_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pending_fc_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
