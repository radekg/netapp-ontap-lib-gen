from netapp.netapp_object import NetAppObject

class Group2ExtensiveInfo(NetAppObject):
    """
    2nd nested typedef at level 1
    """
    
    _field_5 = None
    @property
    def field_5(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
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
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._field_6
    @field_6.setter
    def field_6(self, val):
        if val != None:
            self.validate('field_6', val)
        self._field_6 = val
    
    _field_7 = None
    @property
    def field_7(self):
        """
        Generic/Dummy Field 7
        Attributes: non-creatable, non-modifiable
        """
        return self._field_7
    @field_7.setter
    def field_7(self, val):
        if val != None:
            self.validate('field_7', val)
        self._field_7 = val
    
    _field_8 = None
    @property
    def field_8(self):
        """
        Generic/Dummy Field 8
        Attributes: non-creatable, non-modifiable
        """
        return self._field_8
    @field_8.setter
    def field_8(self, val):
        if val != None:
            self.validate('field_8', val)
        self._field_8 = val
    
    @staticmethod
    def get_api_name():
          return "group2-extensive-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-5',
            'field-6',
            'field-7',
            'field-8',
        ]
    
    def describe_properties(self):
        return {
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_8': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
