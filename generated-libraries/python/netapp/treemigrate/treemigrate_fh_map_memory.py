from netapp.netapp_object import NetAppObject

class TreemigrateFhMapMemory(NetAppObject):
    """
    structure containing File Handle map memory limits
    """
    
    _avail = None
    @property
    def avail(self):
        """
        Available FH map memory
        """
        return self._avail
    @avail.setter
    def avail(self, val):
        if val != None:
            self.validate('avail', val)
        self._avail = val
    
    _used = None
    @property
    def used(self):
        """
        FH map memory currently in use
        """
        return self._used
    @used.setter
    def used(self, val):
        if val != None:
            self.validate('used', val)
        self._used = val
    
    _maximum = None
    @property
    def maximum(self):
        """
        Maximum FH map memory
        """
        return self._maximum
    @maximum.setter
    def maximum(self, val):
        if val != None:
            self.validate('maximum', val)
        self._maximum = val
    
    @staticmethod
    def get_api_name():
          return "treemigrate-fh-map-memory"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'avail',
            'used',
            'maximum',
        ]
    
    def describe_properties(self):
        return {
            'avail': { 'class': int, 'is_list': False, 'required': 'required' },
            'used': { 'class': int, 'is_list': False, 'required': 'required' },
            'maximum': { 'class': int, 'is_list': False, 'required': 'required' },
        }
