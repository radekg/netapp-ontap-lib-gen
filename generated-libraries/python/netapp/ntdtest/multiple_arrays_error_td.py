from netapp.netapp_object import NetAppObject

class MultipleArraysErrorTd(NetAppObject):
    """
    Error Typedef
    """
    
    _field_5 = None
    @property
    def field_5(self):
        """
        Field 5
        Attributes: non-creatable, non-modifiable
        """
        return self._field_5
    @field_5.setter
    def field_5(self, val):
        if val != None:
            self.validate('field_5', val)
        self._field_5 = val
    
    _field_6 = None
    @property
    def field_6(self):
        """
        Field 6
        Attributes: non-creatable, non-modifiable
        """
        return self._field_6
    @field_6.setter
    def field_6(self, val):
        if val != None:
            self.validate('field_6', val)
        self._field_6 = val
    
    @staticmethod
    def get_api_name():
          return "multiple-arrays-error-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-5',
            'field-6',
        ]
    
    def describe_properties(self):
        return {
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
