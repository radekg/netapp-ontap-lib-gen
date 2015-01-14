from netapp.netapp_object import NetAppObject

class StorageSsdInfo(NetAppObject):
    """
    Storage info block for solid-state storage devices.
    """
    
    _percent_spares_consumed = None
    @property
    def percent_spares_consumed(self):
        """
        Percentage of device spare blocks that have been used.
        Each device has a number of spare blocks that will be
        used when a data block can no longer be used to store
        data. This value reports what percentage of the spares
        have already been consumed. Omitted if value is unknown.
        """
        return self._percent_spares_consumed
    @percent_spares_consumed.setter
    def percent_spares_consumed(self, val):
        if val != None:
            self.validate('percent_spares_consumed', val)
        self._percent_spares_consumed = val
    
    _percent_spares_consumed_limit = None
    @property
    def percent_spares_consumed_limit(self):
        """
        Spares consumed percentage limit reported by the
        device. Omitted if value is unknown.
        """
        return self._percent_spares_consumed_limit
    @percent_spares_consumed_limit.setter
    def percent_spares_consumed_limit(self, val):
        if val != None:
            self.validate('percent_spares_consumed_limit', val)
        self._percent_spares_consumed_limit = val
    
    _percent_rated_life_used = None
    @property
    def percent_rated_life_used(self):
        """
        An estimate of the percentage of device life that has
        been used, based on the actual device usage and the
        manufacturer's prediction of device life. A value
        greater than 99 indicates that the estimated endurance
        has been consumed, but may not indicate a device failure.
        Omitted if value is unknown.
        """
        return self._percent_rated_life_used
    @percent_rated_life_used.setter
    def percent_rated_life_used(self, val):
        if val != None:
            self.validate('percent_rated_life_used', val)
        self._percent_rated_life_used = val
    
    @staticmethod
    def get_api_name():
          return "storage-ssd-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'percent-spares-consumed',
            'percent-spares-consumed-limit',
            'percent-rated-life-used',
        ]
    
    def describe_properties(self):
        return {
            'percent_spares_consumed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_spares_consumed_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_rated_life_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
