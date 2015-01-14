from netapp.netapp_object import NetAppObject

class MaintTestListInfo(NetAppObject):
    """
    Maintenance Center test information.
    """
    
    _id = None
    @property
    def id(self):
        """
        Test identifier. This is an identifier for the test that
        is used for the input to disk-maint-start.
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the test. This is a more descriptive test name
        than the id.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "maint-test-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'id',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
