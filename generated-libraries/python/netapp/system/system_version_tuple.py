from netapp.netapp_object import NetAppObject

class SystemVersionTuple(NetAppObject):
    """
    Contains the Data ONTAP version tuple corresponding to the
    lowest version across the cluster.
    """
    
    _generation = None
    @property
    def generation(self):
        """
        First integer of the Data ONTAP version tuple corresponding
        the lowest version across the cluster.
        """
        return self._generation
    @generation.setter
    def generation(self, val):
        if val != None:
            self.validate('generation', val)
        self._generation = val
    
    _major = None
    @property
    def major(self):
        """
        Second integer of the Data ONTAP version tuple corresponding
        the lowest version across the cluster.
        """
        return self._major
    @major.setter
    def major(self, val):
        if val != None:
            self.validate('major', val)
        self._major = val
    
    _minor = None
    @property
    def minor(self):
        """
        Third integer of the Data ONTAP version tuple corresponding
        the lowest version across the cluster.
        """
        return self._minor
    @minor.setter
    def minor(self, val):
        if val != None:
            self.validate('minor', val)
        self._minor = val
    
    @staticmethod
    def get_api_name():
          return "system-version-tuple"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'generation',
            'major',
            'minor',
        ]
    
    def describe_properties(self):
        return {
            'generation': { 'class': int, 'is_list': False, 'required': 'required' },
            'major': { 'class': int, 'is_list': False, 'required': 'required' },
            'minor': { 'class': int, 'is_list': False, 'required': 'required' },
        }
