from netapp.netapp_object import NetAppObject

class AggrVolumeCountAttributes(NetAppObject):
    """
    WAFL volume count specific information of the aggregate
    """
    
    _flexvol_count_quiesced = None
    @property
    def flexvol_count_quiesced(self):
        """
        When present, this field indicates the number of
        quiesced online volumes.
        """
        return self._flexvol_count_quiesced
    @flexvol_count_quiesced.setter
    def flexvol_count_quiesced(self, val):
        if val != None:
            self.validate('flexvol_count_quiesced', val)
        self._flexvol_count_quiesced = val
    
    _flexvol_count_striped = None
    @property
    def flexvol_count_striped(self):
        """
        Number of striped volume constituents in the
        aggregate.  These volumes are also reported
        in the full volume-count value.
        This field is for internal use only.
        """
        return self._flexvol_count_striped
    @flexvol_count_striped.setter
    def flexvol_count_striped(self, val):
        if val != None:
            self.validate('flexvol_count_striped', val)
        self._flexvol_count_striped = val
    
    _flexvol_count_not_online = None
    @property
    def flexvol_count_not_online(self):
        """
        When present, this field indicates the number of
        volumes that are not online (offline and restricted
        volumes).
        """
        return self._flexvol_count_not_online
    @flexvol_count_not_online.setter
    def flexvol_count_not_online(self, val):
        if val != None:
            self.validate('flexvol_count_not_online', val)
        self._flexvol_count_not_online = val
    
    _flexvol_count_collective = None
    @property
    def flexvol_count_collective(self):
        """
        Number of striped volume constituents in the
        aggregate which also represent a collective
        striped volume.
        This field is for internal use only.
        """
        return self._flexvol_count_collective
    @flexvol_count_collective.setter
    def flexvol_count_collective(self, val):
        if val != None:
            self.validate('flexvol_count_collective', val)
        self._flexvol_count_collective = val
    
    _flexvol_count = None
    @property
    def flexvol_count(self):
        """
        Number of volumes in the aggregate.
        """
        return self._flexvol_count
    @flexvol_count.setter
    def flexvol_count(self, val):
        if val != None:
            self.validate('flexvol_count', val)
        self._flexvol_count = val
    
    @staticmethod
    def get_api_name():
          return "aggr-volume-count-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'flexvol-count-quiesced',
            'flexvol-count-striped',
            'flexvol-count-not-online',
            'flexvol-count-collective',
            'flexvol-count',
        ]
    
    def describe_properties(self):
        return {
            'flexvol_count_quiesced': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_count_striped': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_count_not_online': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_count_collective': { 'class': int, 'is_list': False, 'required': 'optional' },
            'flexvol_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
