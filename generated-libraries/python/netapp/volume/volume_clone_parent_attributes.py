from netapp.netapp_object import NetAppObject

class VolumeCloneParentAttributes(NetAppObject):
    """
    Information describing the parentage of a clone volume.
    """
    
    _uuid = None
    @property
    def uuid(self):
        """
        The clone parent volume's UUID.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _snapshot_id = None
    @property
    def snapshot_id(self):
        """
        The clone parent volume's base snapshot identifier.
        <p>
        The only legal value for a snapshot identifier is its
        Data Set ID.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_id
    @snapshot_id.setter
    def snapshot_id(self, val):
        if val != None:
            self.validate('snapshot_id', val)
        self._snapshot_id = val
    
    _msid = None
    @property
    def msid(self):
        """
        The clone's parent volume's Mirror Set ID.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._msid
    @msid.setter
    def msid(self, val):
        if val != None:
            self.validate('msid', val)
        self._msid = val
    
    _dsid = None
    @property
    def dsid(self):
        """
        The clone parent volume's Data Set ID.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._dsid
    @dsid.setter
    def dsid(self, val):
        if val != None:
            self.validate('dsid', val)
        self._dsid = val
    
    _snapshot_name = None
    @property
    def snapshot_name(self):
        """
        The clone parent volume's base snapshot name.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._snapshot_name
    @snapshot_name.setter
    def snapshot_name(self, val):
        if val != None:
            self.validate('snapshot_name', val)
        self._snapshot_name = val
    
    _name = None
    @property
    def name(self):
        """
        The clone parent volume's human-readable name.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "volume-clone-parent-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'uuid',
            'snapshot-id',
            'msid',
            'dsid',
            'snapshot-name',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapshot_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'msid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
