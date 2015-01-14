from netapp.netapp_object import NetAppObject

class EnabledPreset(NetAppObject):
    """
    Archive-Enabled Performance Preset Info
    """
    
    _preset = None
    @property
    def preset(self):
        """
        Enabled Performance Preset Names
        Attributes: non-creatable, non-modifiable
        """
        return self._preset
    @preset.setter
    def preset(self, val):
        if val != None:
            self.validate('preset', val)
        self._preset = val
    
    @staticmethod
    def get_api_name():
          return "enabled-preset"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'preset',
        ]
    
    def describe_properties(self):
        return {
            'preset': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
