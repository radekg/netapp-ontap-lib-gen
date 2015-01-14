from netapp.ntdtest.level4_info import Level4Info
from netapp.netapp_object import NetAppObject

class Level3Info(NetAppObject):
    """
    3rd nested typedef at level 3
    """
    
    _level4 = None
    @property
    def level4(self):
        """
        4th nested typedef at level 4
        """
        return self._level4
    @level4.setter
    def level4(self, val):
        if val != None:
            self.validate('level4', val)
        self._level4 = val
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Dummy/Generic Field 2
        Attributes: key, non-creatable, non-modifiable
        """
        return self._field_2
    @field_2.setter
    def field_2(self, val):
        if val != None:
            self.validate('field_2', val)
        self._field_2 = val
    
    @staticmethod
    def get_api_name():
          return "level3-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'level4',
            'field-2',
        ]
    
    def describe_properties(self):
        return {
            'level4': { 'class': Level4Info, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
