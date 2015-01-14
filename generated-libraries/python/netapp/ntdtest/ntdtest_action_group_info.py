from netapp.netapp_object import NetAppObject

class NtdtestActionGroupInfo(NetAppObject):
    """
    Action Typedef containing keys
    """
    
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
          return "ntdtest-action-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-1',
            'field-2',
        ]
    
    def describe_properties(self):
        return {
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
