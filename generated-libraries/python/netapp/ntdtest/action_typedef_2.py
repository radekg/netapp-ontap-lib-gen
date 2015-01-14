from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class ActionTypedef2(NetAppObject):
    """
    Nested input typedef for action
    """
    
    _field_17 = None
    @property
    def field_17(self):
        """
        Dummy/Generic Action Field 17
        Attributes: required-for-create, non-modifiable
        """
        return self._field_17
    @field_17.setter
    def field_17(self, val):
        if val != None:
            self.validate('field_17', val)
        self._field_17 = val
    
    _field_6 = None
    @property
    def field_6(self):
        """
        Dummy/Generic Action Field 6
        Attributes: required-for-create, non-modifiable
        """
        return self._field_6
    @field_6.setter
    def field_6(self, val):
        if val != None:
            self.validate('field_6', val)
        self._field_6 = val
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Dummy/Generic Action Field 2
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
          return "action-typedef-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-17',
            'field-6',
            'field-2',
        ]
    
    def describe_properties(self):
        return {
            'field_17': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
