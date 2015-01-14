from netapp.netapp_object import NetAppObject

class OpLock(NetAppObject):
    """
    Description of op-locks
    """
    
    _oplock_level = None
    @property
    def oplock_level(self):
        """
        Oplock level.
        Possible values are:
        <ul>
        <li>"null",</li>
        <li>"exclusive",</li>
        <li>"read",</li>
        <li>"batch",</li>
        <li>"read-batch".</li>
        </ul>
        """
        return self._oplock_level
    @oplock_level.setter
    def oplock_level(self, val):
        if val != None:
            self.validate('oplock_level', val)
        self._oplock_level = val
    
    _smb2_open_group_id = None
    @property
    def smb2_open_group_id(self):
        """
        Indicates the open group id for the smb2 lock.
        This is a byte string provided by the CIFS
        client and opaque to the d-blade.
        """
        return self._smb2_open_group_id
    @smb2_open_group_id.setter
    def smb2_open_group_id(self, val):
        if val != None:
            self.validate('smb2_open_group_id', val)
        self._smb2_open_group_id = val
    
    _smb2_connect_state = None
    @property
    def smb2_connect_state(self):
        """
        Indicates the connection state of smb2 lock.
        Possible values are:
        <ul>
        <li>"connected",</li>
        <li>"disconnected".</li>
        </ul>
        """
        return self._smb2_connect_state
    @smb2_connect_state.setter
    def smb2_connect_state(self, val):
        if val != None:
            self.validate('smb2_connect_state', val)
        self._smb2_connect_state = val
    
    @staticmethod
    def get_api_name():
          return "op-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'oplock-level',
            'smb2-open-group-id',
            'smb2-connect-state',
        ]
    
    def describe_properties(self):
        return {
            'oplock_level': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'smb2_open_group_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'smb2_connect_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
