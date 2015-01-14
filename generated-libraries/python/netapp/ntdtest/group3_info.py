from netapp.netapp_object import NetAppObject

class Group3Info(NetAppObject):
    """
    3rd nested typedef at level 1
    """
    
    _list_9 = None
    @property
    def list_9(self):
        """
        Generic/Dummy Field 9
        Attributes: non-creatable, non-modifiable
        """
        return self._list_9
    @list_9.setter
    def list_9(self, val):
        if val != None:
            self.validate('list_9', val)
        self._list_9 = val
    
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
    
    _list_10 = None
    @property
    def list_10(self):
        """
        Generic/Dummy Field 10
        Attributes: non-creatable, non-modifiable
        """
        return self._list_10
    @list_10.setter
    def list_10(self, val):
        if val != None:
            self.validate('list_10', val)
        self._list_10 = val
    
    @staticmethod
    def get_api_name():
          return "group3-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'list-9',
            'field-7',
            'field-8',
            'list-10',
        ]
    
    def describe_properties(self):
        return {
            'list_9': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_8': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'list_10': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
