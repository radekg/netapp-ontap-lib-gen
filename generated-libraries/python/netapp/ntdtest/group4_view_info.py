from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class Group4ViewInfo(NetAppObject):
    """
    4th nested typedef at level 1
    """
    
    _field_16 = None
    @property
    def field_16(self):
        """
        Generic/Dummy Field 16
        Attributes: non-creatable, non-modifiable
        """
        return self._field_16
    @field_16.setter
    def field_16(self, val):
        if val != None:
            self.validate('field_16', val)
        self._field_16 = val
    
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
    
    _field_14 = None
    @property
    def field_14(self):
        """
        Generic/Dummy Field 14
        Attributes: non-creatable, non-modifiable
        """
        return self._field_14
    @field_14.setter
    def field_14(self, val):
        if val != None:
            self.validate('field_14', val)
        self._field_14 = val
    
    _field_15 = None
    @property
    def field_15(self):
        """
        Generic/Dummy Field 15
        Attributes: non-creatable, non-modifiable
        """
        return self._field_15
    @field_15.setter
    def field_15(self, val):
        if val != None:
            self.validate('field_15', val)
        self._field_15 = val
    
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
    
    @staticmethod
    def get_api_name():
          return "group4-view-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-16',
            'field-17',
            'field-14',
            'field-15',
            'field-13',
        ]
    
    def describe_properties(self):
        return {
            'field_16': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_17': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'field_14': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_15': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_13': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
