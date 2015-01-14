from netapp.ntdtest.level2_info import Level2Info
from netapp.netapp_object import NetAppObject

class Level1Info(NetAppObject):
    """
    1st nested typedef at level 1
    """
    
    _level2 = None
    @property
    def level2(self):
        """
        2nd nested typedef at level 2
        """
        return self._level2
    @level2.setter
    def level2(self, val):
        if val != None:
            self.validate('level2', val)
        self._level2 = val
    
    _field_7 = None
    @property
    def field_7(self):
        """
        Dummy/Generic Field 7
        Attributes: non-creatable, non-modifiable
        """
        return self._field_7
    @field_7.setter
    def field_7(self, val):
        if val != None:
            self.validate('field_7', val)
        self._field_7 = val
    
    _field_1 = None
    @property
    def field_1(self):
        """
        Dummy/Generic Field 1
        Attributes: key, non-creatable, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    @staticmethod
    def get_api_name():
          return "level1-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'level2',
            'field-7',
            'field-1',
        ]
    
    def describe_properties(self):
        return {
            'level2': { 'class': Level2Info, 'is_list': False, 'required': 'optional' },
            'field_7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
