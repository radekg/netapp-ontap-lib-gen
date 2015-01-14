from netapp.netapp_object import NetAppObject

class TreemigrateMigrations(NetAppObject):
    """
    structure containing limits for data migrations
    """
    
    _avail = None
    @property
    def avail(self):
        """
        Number of migrations that can still be started
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
        Number of migrations currently running
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
        Maximum number of concurrent migrations
        """
        return self._maximum
    @maximum.setter
    def maximum(self, val):
        if val != None:
            self.validate('maximum', val)
        self._maximum = val
    
    @staticmethod
    def get_api_name():
          return "treemigrate-migrations"
    
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
