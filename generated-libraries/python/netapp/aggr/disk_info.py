from netapp.netapp_object import NetAppObject

class DiskInfo(NetAppObject):
    """
    Information for each disk in
    the plex.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of a member disk.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "disk-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
