from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class OutExtensiveCreate(NetAppObject):
    """
    Output typedef for alternate create 1
    """
    
    _field_17 = None
    @property
    def field_17(self):
        """
        Generic/Dummy Field 17
        Attributes: required-for-create, modifiable
        """
        return self._field_17
    @field_17.setter
    def field_17(self, val):
        if val != None:
            self.validate('field_17', val)
        self._field_17 = val
    
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
    
    _field_13 = None
    @property
    def field_13(self):
        """
        Generic/Dummy Field 13
        Attributes: non-creatable, non-modifiable
        """
        return self._field_13
    @field_13.setter
    def field_13(self, val):
        if val != None:
            self.validate('field_13', val)
        self._field_13 = val
    
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
    
    @staticmethod
    def get_api_name():
          return "out-extensive-create"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-17',
            'field-5',
            'field-13',
            'field-1',
            'field-9',
        ]
    
    def describe_properties(self):
        return {
            'field_17': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_13': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_9': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
