from netapp.netapp_object import NetAppObject

class TestExtensiveType2(NetAppObject):
    """
    Test input typedef 2
    """
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Generic/Dummy Field 2
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_2
    @field_2.setter
    def field_2(self, val):
        if val != None:
            self.validate('field_2', val)
        self._field_2 = val
    
    @staticmethod
    def get_api_name():
          return "test-extensive-type-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-2',
        ]
    
    def describe_properties(self):
        return {
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
