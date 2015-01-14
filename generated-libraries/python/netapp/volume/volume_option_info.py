from netapp.netapp_object import NetAppObject

class VolumeOptionInfo(NetAppObject):
    """
    Option key and value.
    """
    
    _name = None
    @property
    def name(self):
        """
        Option key.
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
        Option value.
        """
        return self._value
    @value.setter
    def value(self, val):
        if val != None:
            self.validate('value', val)
        self._value = val
    
    @staticmethod
    def get_api_name():
          return "volume-option-info"
    
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
