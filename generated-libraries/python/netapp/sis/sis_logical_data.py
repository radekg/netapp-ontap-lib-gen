from netapp.netapp_object import NetAppObject

class SisLogicalData(NetAppObject):
    """
    This contains logical size attributes of a volume.
    """
    
    _logical_data_size = None
    @property
    def logical_data_size(self):
        """
        The size of logical data in the volume in bytes.
        This is calculated  as [size-saved + size-used
        + compressed-data bytes].
        This parameter is not supported on Infinite Volumes.
        """
        return self._logical_data_size
    @logical_data_size.setter
    def logical_data_size(self, val):
        if val != None:
            self.validate('logical_data_size', val)
        self._logical_data_size = val
    
    _logical_data_limit = None
    @property
    def logical_data_limit(self):
        """
        Dedupe logical data limit in bytes.
        This parameter is not supported on Infinite Volumes.
        """
        return self._logical_data_limit
    @logical_data_limit.setter
    def logical_data_limit(self, val):
        if val != None:
            self.validate('logical_data_limit', val)
        self._logical_data_limit = val
    
    @staticmethod
    def get_api_name():
          return "sis-logical-data"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'logical-data-size',
            'logical-data-limit',
        ]
    
    def describe_properties(self):
        return {
            'logical_data_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'logical_data_limit': { 'class': int, 'is_list': False, 'required': 'required' },
        }
