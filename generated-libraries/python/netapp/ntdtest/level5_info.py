from netapp.netapp_object import NetAppObject

class Level5Info(NetAppObject):
    """
    5th nested typedef at level 5
    """
    
    _field_9 = None
    @property
    def field_9(self):
        """
        Dummy/Generic Field 9
        Attributes: non-creatable, non-modifiable
        """
        return self._field_9
    @field_9.setter
    def field_9(self, val):
        if val != None:
            self.validate('field_9', val)
        self._field_9 = val
    
    _field_10 = None
    @property
    def field_10(self):
        """
        Dummy/Generic Field 10
        Attributes: non-creatable, non-modifiable
        """
        return self._field_10
    @field_10.setter
    def field_10(self, val):
        if val != None:
            self.validate('field_10', val)
        self._field_10 = val
    
    @staticmethod
    def get_api_name():
          return "level5-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-9',
            'field-10',
        ]
    
    def describe_properties(self):
        return {
            'field_9': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_10': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
