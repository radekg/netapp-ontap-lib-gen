from netapp.ntdtest.level5_info import Level5Info
from netapp.netapp_object import NetAppObject

class Level4Info(NetAppObject):
    """
    4th nested typedef at level 4
    """
    
    _field_4 = None
    @property
    def field_4(self):
        """
        Dummy/Generic Field 4
        Attributes: key, non-creatable, non-modifiable
        """
        return self._field_4
    @field_4.setter
    def field_4(self, val):
        if val != None:
            self.validate('field_4', val)
        self._field_4 = val
    
    _level5 = None
    @property
    def level5(self):
        """
        5th nested typedef at level 5
        """
        return self._level5
    @level5.setter
    def level5(self, val):
        if val != None:
            self.validate('level5', val)
        self._level5 = val
    
    _field_3 = None
    @property
    def field_3(self):
        """
        Dummy/Generic Field 3
        Attributes: key, non-creatable, non-modifiable
        """
        return self._field_3
    @field_3.setter
    def field_3(self, val):
        if val != None:
            self.validate('field_3', val)
        self._field_3 = val
    
    @staticmethod
    def get_api_name():
          return "level4-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-4',
            'level5',
            'field-3',
        ]
    
    def describe_properties(self):
        return {
            'field_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'level5': { 'class': Level5Info, 'is_list': False, 'required': 'optional' },
            'field_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
