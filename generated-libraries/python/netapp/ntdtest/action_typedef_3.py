from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class ActionTypedef3(NetAppObject):
    """
    Output typedef for action
    """
    
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
    
    @staticmethod
    def get_api_name():
          return "action-typedef-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-5',
            'field-6',
            'field-17',
        ]
    
    def describe_properties(self):
        return {
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_17': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
        }
