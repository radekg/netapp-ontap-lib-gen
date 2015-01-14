from netapp.netapp_object import NetAppObject

class AutosizeInfo(NetAppObject):
    """
    Autosize settings of the volume
    This appears only if the "verbose"
    parameter above is set to "true".
    """
    
    _increment_size = None
    @property
    def increment_size(self):
        """
        The increment size by which the volume would
        be grown, in kbytes.
        """
        return self._increment_size
    @increment_size.setter
    def increment_size(self, val):
        if val != None:
            self.validate('increment_size', val)
        self._increment_size = val
    
    _minimum_size = None
    @property
    def minimum_size(self):
        """
        The minimim size to which the volume can
        be shrunk automatically, in kbytes.
        """
        return self._minimum_size
    @minimum_size.setter
    def minimum_size(self, val):
        if val != None:
            self.validate('minimum_size', val)
        self._minimum_size = val
    
    _grow_threshold_percent = None
    @property
    def grow_threshold_percent(self):
        """
        The trigger capacity percentage at which the
        volume automatiacally grows.
        """
        return self._grow_threshold_percent
    @grow_threshold_percent.setter
    def grow_threshold_percent(self, val):
        if val != None:
            self.validate('grow_threshold_percent', val)
        self._grow_threshold_percent = val
    
    _maximum_size = None
    @property
    def maximum_size(self):
        """
        The maximum size to which the volume would be
        grown automatically, in kbytes.
        """
        return self._maximum_size
    @maximum_size.setter
    def maximum_size(self, val):
        if val != None:
            self.validate('maximum_size', val)
        self._maximum_size = val
    
    _shrink_threshold_percent = None
    @property
    def shrink_threshold_percent(self):
        """
        The trigger capacity percentage at which the
        volume automatically shrinks.
        """
        return self._shrink_threshold_percent
    @shrink_threshold_percent.setter
    def shrink_threshold_percent(self, val):
        if val != None:
            self.validate('shrink_threshold_percent', val)
        self._shrink_threshold_percent = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        This element is deprecated in Data ONTAP 8.2
        and later. Please use autosize-mode instead.
        The value of 'true' means that autosize is
        enabled, while 'false' means that the autosize
        mode is 'off'.
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _mode = None
    @property
    def mode(self):
        """
        Defines the current mode of volume autosize.
        Legal modes include "grow", "grow_shrink",
        and "off".
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    @staticmethod
    def get_api_name():
          return "autosize-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'increment-size',
            'minimum-size',
            'grow-threshold-percent',
            'maximum-size',
            'shrink-threshold-percent',
            'is-enabled',
            'mode',
        ]
    
    def describe_properties(self):
        return {
            'increment_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'minimum_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'grow_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maximum_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'shrink_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
