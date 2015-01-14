from netapp.netapp_object import NetAppObject

class OptionsRelatedInfo(NetAppObject):
    """
    Options Info
    """
    
    _auto_giveback_enabled = None
    @property
    def auto_giveback_enabled(self):
        """
        True, if auto-giveback is enabled, false otherwise.
        Attributes: non-creatable, modifiable
        """
        return self._auto_giveback_enabled
    @auto_giveback_enabled.setter
    def auto_giveback_enabled(self, val):
        if val != None:
            self.validate('auto_giveback_enabled', val)
        self._auto_giveback_enabled = val
    
    @staticmethod
    def get_api_name():
          return "options-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'auto-giveback-enabled',
        ]
    
    def describe_properties(self):
        return {
            'auto_giveback_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
