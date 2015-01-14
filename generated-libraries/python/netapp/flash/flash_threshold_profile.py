from netapp.flash.flash_threshold import FlashThreshold
from netapp.netapp_object import NetAppObject

class FlashThresholdProfile(NetAppObject):
    """
    A definition for a threshold element
    """
    
    _node = None
    @property
    def node(self):
        """
        The name of the system to which the flash thresholds apply.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _profile = None
    @property
    def profile(self):
        """
        The name of the profile in plain text.
        """
        return self._profile
    @profile.setter
    def profile(self, val):
        if val != None:
            self.validate('profile', val)
        self._profile = val
    
    _flash_threshold = None
    @property
    def flash_threshold(self):
        """
        The list of threshold entries for this profile.
        """
        return self._flash_threshold
    @flash_threshold.setter
    def flash_threshold(self, val):
        if val != None:
            self.validate('flash_threshold', val)
        self._flash_threshold = val
    
    @staticmethod
    def get_api_name():
          return "flash-threshold-profile"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'profile',
            'flash-threshold',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'profile': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'flash_threshold': { 'class': FlashThreshold, 'is_list': True, 'required': 'required' },
        }
