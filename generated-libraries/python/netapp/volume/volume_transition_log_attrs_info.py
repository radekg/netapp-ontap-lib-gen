from netapp.netapp_object import NetAppObject

class VolumeTransitionLogAttrsInfo(NetAppObject):
    """
    Information about attributes included in an Action record.
    """
    
    _attr_value = None
    @property
    def attr_value(self):
        """
        Attribute value.
        """
        return self._attr_value
    @attr_value.setter
    def attr_value(self, val):
        if val != None:
            self.validate('attr_value', val)
        self._attr_value = val
    
    _attr_type = None
    @property
    def attr_type(self):
        """
        Describes the type of attribute.
        """
        return self._attr_type
    @attr_type.setter
    def attr_type(self, val):
        if val != None:
            self.validate('attr_type', val)
        self._attr_type = val
    
    @staticmethod
    def get_api_name():
          return "volume-transition-log-attrs-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'attr-value',
            'attr-type',
        ]
    
    def describe_properties(self):
        return {
            'attr_value': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'attr_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
