from netapp.netapp_object import NetAppObject

class ConflictingMapInfo(NetAppObject):
    """
    lun mapping conflict.
    """
    
    _initiator_name = None
    @property
    def initiator_name(self):
        """
        Fibre channel initiator nodename that has
        a lun mapped from both filers in the cluster
        using the same LUN-id.
        """
        return self._initiator_name
    @initiator_name.setter
    def initiator_name(self, val):
        if val != None:
            self.validate('initiator_name', val)
        self._initiator_name = val
    
    _lun_id = None
    @property
    def lun_id(self):
        """
        lun-id used in mappings to the initiator from
        both filers in the cluster.
        """
        return self._lun_id
    @lun_id.setter
    def lun_id(self, val):
        if val != None:
            self.validate('lun_id', val)
        self._lun_id = val
    
    @staticmethod
    def get_api_name():
          return "conflicting-map-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-name',
            'lun-id',
        ]
    
    def describe_properties(self):
        return {
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
