from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class TestExtensiveType3(NetAppObject):
    """
    Test output typedef 3
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
    
    @staticmethod
    def get_api_name():
          return "test-extensive-type-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-16',
            'field-17',
        ]
    
    def describe_properties(self):
        return {
            'field_16': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_17': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
        }
