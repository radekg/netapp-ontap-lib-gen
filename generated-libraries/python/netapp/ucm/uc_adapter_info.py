from netapp.netapp_object import NetAppObject

class UcAdapterInfo(NetAppObject):
    """
    Information for one adapter.
    """
    
    _status = None
    @property
    def status(self):
        """
        The status of this adapter.
        Possible values:
        <ul>
        <li> "online"
        <li> "offline"
        <li> "unsupported"
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _supported_mode = None
    @property
    def supported_mode(self):
        """
        Return a list of supported modes
        for the specified adapter.
        """
        return self._supported_mode
    @supported_mode.setter
    def supported_mode(self, val):
        if val != None:
            self.validate('supported_mode', val)
        self._supported_mode = val
    
    _supported_fc4_type_for_fc_mode = None
    @property
    def supported_fc4_type_for_fc_mode(self):
        """
        Return a list of supported FC-4 types for the adapter
        if configured in fc mode.
        """
        return self._supported_fc4_type_for_fc_mode
    @supported_fc4_type_for_fc_mode.setter
    def supported_fc4_type_for_fc_mode(self, val):
        if val != None:
            self.validate('supported_fc4_type_for_fc_mode', val)
        self._supported_fc4_type_for_fc_mode = val
    
    _fc4_type = None
    @property
    def fc4_type(self):
        """
        The current FC-4 type of this adapter.
        """
        return self._fc4_type
    @fc4_type.setter
    def fc4_type(self, val):
        if val != None:
            self.validate('fc4_type', val)
        self._fc4_type = val
    
    _supported_fc4_type_for_cna_mode = None
    @property
    def supported_fc4_type_for_cna_mode(self):
        """
        Return a list of supported FC-4 types for the adapter
        if configured in cna mode.
        """
        return self._supported_fc4_type_for_cna_mode
    @supported_fc4_type_for_cna_mode.setter
    def supported_fc4_type_for_cna_mode(self, val):
        if val != None:
            self.validate('supported_fc4_type_for_cna_mode', val)
        self._supported_fc4_type_for_cna_mode = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The name of the node where the adapter is installed.
        This is only reported in Clustered ONTAP.
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
        The slot name of the adapter (e.g. 0e)
        """
        return self._adapter_name
    @adapter_name.setter
    def adapter_name(self, val):
        if val != None:
            self.validate('adapter_name', val)
        self._adapter_name = val
    
    _mode = None
    @property
    def mode(self):
        """
        The current mode of this adapter.
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _pending_fc4_type = None
    @property
    def pending_fc4_type(self):
        """
        This is the pending change that has been made to the
        FC4-type on this adapter, but a controller reboot has
        not been performed for the change to take effect. A
        controller reboot is required for any pending changes
        to take effect. This will not be reported if there is
        no pending change on this adapter See fc4-type
        element for possible values.
        """
        return self._pending_fc4_type
    @pending_fc4_type.setter
    def pending_fc4_type(self, val):
        if val != None:
            self.validate('pending_fc4_type', val)
        self._pending_fc4_type = val
    
    _pending_mode = None
    @property
    def pending_mode(self):
        """
        This is the pending change that has been made to the
        mode on this adapter, but a controller reboot has not
        been performed for the change to take effect. A
        controller reboot is required for any pending changes
        to take effect. This will not be reported if there is
        no pending change on this adapter. See the mode element
        for possible values.
        """
        return self._pending_mode
    @pending_mode.setter
    def pending_mode(self, val):
        if val != None:
            self.validate('pending_mode', val)
        self._pending_mode = val
    
    @staticmethod
    def get_api_name():
          return "uc-adapter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'supported-mode',
            'supported-fc4-type-for-fc-mode',
            'fc4-type',
            'supported-fc4-type-for-cna-mode',
            'node-name',
            'adapter-name',
            'mode',
            'pending-fc4-type',
            'pending-mode',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'supported_mode': { 'class': basestring, 'is_list': True, 'required': 'required' },
            'supported_fc4_type_for_fc_mode': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'fc4_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'supported_fc4_type_for_cna_mode': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'pending_fc4_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pending_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
