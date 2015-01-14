from netapp.netapp_object import NetAppObject

class FpolicyVolumesListInfo(NetAppObject):
    """
    Structure containing volumes information.
    """
    
    _volume_spec = None
    @property
    def volume_spec(self):
        """
        Volume specification (including wild cards).
        The volumes are case insensitive.
        If no volume-spec is provided, then the list will
        be reset to an empty list.
        Supported wild card values: "?" to match any
        character and "*" to match any number of characters.
        Example specifications:
        vol0
        vol?
        users*
        """
        return self._volume_spec
    @volume_spec.setter
    def volume_spec(self, val):
        if val != None:
            self.validate('volume_spec', val)
        self._volume_spec = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-volumes-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-spec',
        ]
    
    def describe_properties(self):
        return {
            'volume_spec': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
