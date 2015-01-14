from netapp.netapp_object import NetAppObject

class LunAttributeInfo(NetAppObject):
    """
    LUN attribute name / value pair
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the attribute.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _value = None
    @property
    def value(self):
        """
        Value of the attribute.
        """
        return self._value
    @value.setter
    def value(self, val):
        if val != None:
            self.validate('value', val)
        self._value = val
    
    @staticmethod
    def get_api_name():
          return "lun-attribute-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'value',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'value': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
