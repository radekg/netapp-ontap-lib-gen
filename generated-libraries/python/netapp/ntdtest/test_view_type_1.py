from netapp.netapp_object import NetAppObject

class TestViewType1(NetAppObject):
    """
    Test input typedef 1
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
    
    @staticmethod
    def get_api_name():
          return "test-view-type-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'field-1',
            'field-2',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
