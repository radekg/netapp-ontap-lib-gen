from netapp.netapp_object import NetAppObject

class FcpDownHbaInfo(NetAppObject):
    """
    Information about a down FCP HBA
    """
    
    _adapter = None
    @property
    def adapter(self):
        """
        Which FC adapter.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _state = None
    @property
    def state(self):
        """
        Description of HBAs state.
        Possible values:
        STARTUP
        UNINITIALIZED
        INITIALIZING FIRMWARE
        LINK NOT CONNECTED
        WAITING FOR LINK UP
        ONLINE
        LINK DISCONNECTED
        RESETTING
        OFFLINE
        OFFLINED BY USER/SYSTEM
        Unknown state
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    @staticmethod
    def get_api_name():
          return "fcp-down-hba-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter',
            'state',
        ]
    
    def describe_properties(self):
        return {
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
