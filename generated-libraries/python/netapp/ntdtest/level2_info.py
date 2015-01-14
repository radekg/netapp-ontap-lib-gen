from netapp.ntdtest.level3_info import Level3Info
from netapp.netapp_object import NetAppObject

class Level2Info(NetAppObject):
    """
    2nd nested typedef at level 2
    """
    
    _field_6 = None
    @property
    def field_6(self):
        """
        Dummy/Generic Field 6
        Attributes: non-creatable, non-modifiable
        """
        return self._field_6
    @field_6.setter
    def field_6(self, val):
        if val != None:
            self.validate('field_6', val)
        self._field_6 = val
    
    _level3 = None
    @property
    def level3(self):
        """
        3rd nested typedef at level 3
        """
        return self._level3
    @level3.setter
    def level3(self, val):
        if val != None:
            self.validate('level3', val)
        self._level3 = val
    
    @staticmethod
    def get_api_name():
          return "level2-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-6',
            'level3',
        ]
    
    def describe_properties(self):
        return {
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'level3': { 'class': Level3Info, 'is_list': False, 'required': 'optional' },
        }
