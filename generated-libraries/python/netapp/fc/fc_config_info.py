from netapp.netapp_object import NetAppObject

class FcConfigInfo(NetAppObject):
    """
    """
    
    _adapter_name = None
    @property
    def adapter_name(self):
        """
        FC adapter name (e.g. 0c)
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
        Indicates what the adapter configuration state is.  Possible values:<br>
        &nbsp; "UNDEFINED" - The default state. The adapter has never been configured.<br>
        &nbsp; "CONFIGURED" - The adapter port is configured and the adapter is operational.<br>
        &nbsp; "UNCONFIGURED" - The adapter is unconfigured. The initiator driver is attached, but the adapter is not operational.<br>
        &nbsp; "PENDING" - The adapter is waiting for a filer reboot to effect an fc-type change.<br>
        While in the PENDING state the adapter can not be used
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
        Possible values:<br>
        &nbsp; "online" - adapter driver is enabled<br>
        &nbsp; "offline" - adapter driver is disabled<br>
        """
        return self._adapter_status
    @adapter_status.setter
    def adapter_status(self, val):
        if val != None:
            self.validate('adapter_status', val)
        self._adapter_status = val
    
    _adapter_type = None
    @property
    def adapter_type(self):
        """
        Indicates which driver is attached to the adapter. Possible values:<br>
        &nbsp; "initiator" - the storage Initiator driver (default)<br>
        &nbsp; "vi"        - the FC-VI cluster interconnect driver<br>
        &nbsp; "target"    - the FCP Target driver<br>
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
        If adapter-state is PENDING, this value tells what the last fc-config-set-adapter-fc-type command
        was.<br>
        """
        return self._pending_fc_type
    @pending_fc_type.setter
    def pending_fc_type(self, val):
        if val != None:
            self.validate('pending_fc_type', val)
        self._pending_fc_type = val
    
    @staticmethod
    def get_api_name():
          return "fc-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter-name',
            'adapter-state',
            'adapter-status',
            'adapter-type',
            'pending-fc-type',
        ]
    
    def describe_properties(self):
        return {
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'pending_fc_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
