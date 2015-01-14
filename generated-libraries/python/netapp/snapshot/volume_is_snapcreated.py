from netapp.netapp_object import NetAppObject

class VolumeIsSnapcreated(NetAppObject):
    """
    The status of the snapshot creation for a given volume.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of a volume.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _is_snapcreated = None
    @property
    def is_snapcreated(self):
        """
        TRUE means a snapshot has been created for the volume.
        """
        return self._is_snapcreated
    @is_snapcreated.setter
    def is_snapcreated(self, val):
        if val != None:
            self.validate('is_snapcreated', val)
        self._is_snapcreated = val
    
    @staticmethod
    def get_api_name():
          return "volume-is-snapcreated"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'is-snapcreated',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_snapcreated': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
