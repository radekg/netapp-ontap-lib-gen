from netapp.netapp_object import NetAppObject

class Group3ExtensiveInfo(NetAppObject):
    """
    3rd nested typedef at level 1
    """
    
    _field_12 = None
    @property
    def field_12(self):
        """
        Generic/Dummy Field 12
        Attributes: non-creatable, non-modifiable
        """
        return self._field_12
    @field_12.setter
    def field_12(self, val):
        if val != None:
            self.validate('field_12', val)
        self._field_12 = val
    
    _field_9 = None
    @property
    def field_9(self):
        """
        Generic/Dummy Field 9
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
        Generic/Dummy Field 10
        Attributes: non-creatable, non-modifiable
        """
        return self._field_10
    @field_10.setter
    def field_10(self, val):
        if val != None:
            self.validate('field_10', val)
        self._field_10 = val
    
    _field_11 = None
    @property
    def field_11(self):
        """
        Generic/Dummy Field 11
        Attributes: non-creatable, non-modifiable
        """
        return self._field_11
    @field_11.setter
    def field_11(self, val):
        if val != None:
            self.validate('field_11', val)
        self._field_11 = val
    
    @staticmethod
    def get_api_name():
          return "group3-extensive-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-12',
            'field-9',
            'field-10',
            'field-11',
        ]
    
    def describe_properties(self):
        return {
            'field_12': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_9': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_10': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_11': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
