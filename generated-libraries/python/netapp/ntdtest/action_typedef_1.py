from netapp.ntdtest.action_typedef_2 import ActionTypedef2
from netapp.netapp_object import NetAppObject

class ActionTypedef1(NetAppObject):
    """
    Top level input typedef for action
    """
    
    _field_4 = None
    @property
    def field_4(self):
        """
        Dummy/Generic Action Field 4
        Attributes: required-for-create, non-modifiable
        """
        return self._field_4
    @field_4.setter
    def field_4(self, val):
        if val != None:
            self.validate('field_4', val)
        self._field_4 = val
    
    _field_5 = None
    @property
    def field_5(self):
        """
        Dummy/Generic Action Field 5
        Attributes: required-for-create, non-modifiable
        """
        return self._field_5
    @field_5.setter
    def field_5(self, val):
        if val != None:
            self.validate('field_5', val)
        self._field_5 = val
    
    _input_typedef_2 = None
    @property
    def input_typedef_2(self):
        """
        Nested input typedef for action
        """
        return self._input_typedef_2
    @input_typedef_2.setter
    def input_typedef_2(self, val):
        if val != None:
            self.validate('input_typedef_2', val)
        self._input_typedef_2 = val
    
    _field_1 = None
    @property
    def field_1(self):
        """
        Dummy/Generic Action Field 1
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    _field_3 = None
    @property
    def field_3(self):
        """
        Dummy/Generic Action Field 3
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
          return "action-typedef-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-4',
            'field-5',
            'input-typedef-2',
            'field-1',
            'field-3',
        ]
    
    def describe_properties(self):
        return {
            'field_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'input_typedef_2': { 'class': ActionTypedef2, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
