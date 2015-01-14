from netapp.netapp_object import NetAppObject

class LunMapInfo(NetAppObject):
    """
    Information about a lun mapping
    """
    
    _lun_uuid = None
    @property
    def lun_uuid(self):
        """
        The Universally-unique identifier (UUID) of the LUN.
        """
        return self._lun_uuid
    @lun_uuid.setter
    def lun_uuid(self, val):
        if val != None:
            self.validate('lun_uuid', val)
        self._lun_uuid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing the initiator group
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _initiator_group = None
    @property
    def initiator_group(self):
        """
        Initiator group used to map the lun to the
        requested initiator.
        """
        return self._initiator_group
    @initiator_group.setter
    def initiator_group(self, val):
        if val != None:
            self.validate('initiator_group', val)
        self._initiator_group = val
    
    _lun_id = None
    @property
    def lun_id(self):
        """
        Logical Unit Number which the lun is mapped to
        for the requested initiator.
        """
        return self._lun_id
    @lun_id.setter
    def lun_id(self, val):
        if val != None:
            self.validate('lun_id', val)
        self._lun_id = val
    
    _path = None
    @property
    def path(self):
        """
        Path of the LUN which is mapped to the requested
        initiator.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _initiator_group_uuid = None
    @property
    def initiator_group_uuid(self):
        """
        The Universally-unique identifier (UUID) of the initiator
        group.
        """
        return self._initiator_group_uuid
    @initiator_group_uuid.setter
    def initiator_group_uuid(self, val):
        if val != None:
            self.validate('initiator_group_uuid', val)
        self._initiator_group_uuid = val
    
    @staticmethod
    def get_api_name():
          return "lun-map-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'lun-uuid',
            'vserver',
            'initiator-group',
            'lun-id',
            'path',
            'initiator-group-uuid',
        ]
    
    def describe_properties(self):
        return {
            'lun_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator_group': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
