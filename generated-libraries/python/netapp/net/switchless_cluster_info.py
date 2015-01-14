from netapp.netapp_object import NetAppObject

class SwitchlessClusterInfo(NetAppObject):
    """
    Network options switchless-cluster typedef
    """
    
    _enabled = None
    @property
    def enabled(self):
        """
        Enable Switchless Cluster
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
          return "switchless-cluster-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'enabled',
        ]
    
    def describe_properties(self):
        return {
            'enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
