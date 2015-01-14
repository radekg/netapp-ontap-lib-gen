from netapp.netapp_object import NetAppObject

class InstanceInfo(NetAppObject):
    """
    Description of an instance of an object.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the instance
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        UUID of the instance
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    @staticmethod
    def get_api_name():
          return "instance-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'uuid',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
