from netapp.netapp_object import NetAppObject

class TreemigrateFilesEstimate(NetAppObject):
    """
    structure containing numbers of files limits
    """
    
    _avail = None
    @property
    def avail(self):
        """
        Number of files that can still be migrated
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
        Number of files currently being migrated
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
        Maximum number of files that can be migrated at a time
        """
        return self._maximum
    @maximum.setter
    def maximum(self, val):
        if val != None:
            self.validate('maximum', val)
        self._maximum = val
    
    @staticmethod
    def get_api_name():
          return "treemigrate-files-estimate"
    
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
