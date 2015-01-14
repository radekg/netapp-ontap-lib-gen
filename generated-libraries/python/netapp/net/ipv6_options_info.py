from netapp.netapp_object import NetAppObject

class Ipv6OptionsInfo(NetAppObject):
    """
    Network options ipv6 typedef
    """
    
    _enabled = None
    @property
    def enabled(self):
        """
        IPv6 Enabled
        Attributes: non-creatable, modifiable
        """
        return self._enabled
    @enabled.setter
    def enabled(self, val):
        if val != None:
            self.validate('enabled', val)
        self._enabled = val
    
    @staticmethod
    def get_api_name():
          return "ipv6-options-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'enabled',
        ]
    
    def describe_properties(self):
        return {
            'enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
