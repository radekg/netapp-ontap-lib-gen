from netapp.netapp_object import NetAppObject

class CloneIdInfo(NetAppObject):
    """
    Structure containing clone ID information.
    """
    
    _clone_op_id = None
    @property
    def clone_op_id(self):
        """
        ID of the clone operation.
        """
        return self._clone_op_id
    @clone_op_id.setter
    def clone_op_id(self, val):
        if val != None:
            self.validate('clone_op_id', val)
        self._clone_op_id = val
    
    _volume_uuid = None
    @property
    def volume_uuid(self):
        """
        uuid of the volume.
        """
        return self._volume_uuid
    @volume_uuid.setter
    def volume_uuid(self, val):
        if val != None:
            self.validate('volume_uuid', val)
        self._volume_uuid = val
    
    @staticmethod
    def get_api_name():
          return "clone-id-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'clone-op-id',
            'volume-uuid',
        ]
    
    def describe_properties(self):
        return {
            'clone_op_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
