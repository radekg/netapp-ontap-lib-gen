from netapp.netapp_object import NetAppObject

class VolumesListInfo(NetAppObject):
    """
    Information about a single volume.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    @staticmethod
    def get_api_name():
          return "volumes-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
