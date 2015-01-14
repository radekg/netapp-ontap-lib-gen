from netapp.netapp_object import NetAppObject

class Group1ViewInfo(NetAppObject):
    """
    1st nested typedef at level 1
    """
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _field_4 = None
    @property
    def field_4(self):
        """
        Generic/Dummy Field 4
        Attributes: required-for-create, non-modifiable
        """
        return self._field_4
    @field_4.setter
    def field_4(self, val):
        if val != None:
            self.validate('field_4', val)
        self._field_4 = val
    
    _field_1 = None
    @property
    def field_1(self):
        """
        This is zapi description for field1.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Generic/Dummy Field 2
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_2
    @field_2.setter
    def field_2(self, val):
        if val != None:
            self.validate('field_2', val)
        self._field_2 = val
    
    _field_3 = None
    @property
    def field_3(self):
        """
        Generic/Dummy Field 3
        Attributes: required-for-create, non-modifiable
        """
        return self._field_3
    @field_3.setter
    def field_3(self, val):
        if val != None:
            self.validate('field_3', val)
        self._field_3 = val
    
    @staticmethod
    def get_api_name():
          return "group1-view-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'field-4',
            'field-1',
            'field-2',
            'field-3',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
