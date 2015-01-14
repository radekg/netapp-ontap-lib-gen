from netapp.netapp_object import NetAppObject

class Test2Info(NetAppObject):
    """
    This type contains information about a single error.
    """
    
    _value2 = None
    @property
    def value2(self):
        """
        Dummy value 2.
        """
        return self._value2
    @value2.setter
    def value2(self, val):
        if val != None:
            self.validate('value2', val)
        self._value2 = val
    
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
          return "test-2-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'value2',
            'value1',
        ]
    
    def describe_properties(self):
        return {
            'value2': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'value1': { 'class': int, 'is_list': False, 'required': 'required' },
        }
