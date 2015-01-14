from netapp.netapp_object import NetAppObject

class SchemaValidatorInfo(NetAppObject):
    """
    This type containg test values.
    """
    
    _value1 = None
    @property
    def value1(self):
        """
        Dummy value 1.
        """
        return self._value1
    @value1.setter
    def value1(self, val):
        if val != None:
            self.validate('value1', val)
        self._value1 = val
    
    @staticmethod
    def get_api_name():
          return "schema-validator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'value1',
        ]
    
    def describe_properties(self):
        return {
            'value1': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
