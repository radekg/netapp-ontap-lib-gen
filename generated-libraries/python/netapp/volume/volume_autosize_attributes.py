from netapp.netapp_object import NetAppObject

class VolumeAutosizeAttributes(NetAppObject):
    """
    Information about autosize settings of the volume.
    """
    
    _reset = None
    @property
    def reset(self):
        """
        Resets the values of autosize, autosize-increment,
        max-autosize, min-autosize,
        autosize-shrink-threshold-percent,
        autosize-grow-threshold-percent and autosize-mode to
        their defaults.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._reset
    @reset.setter
    def reset(self, val):
        if val != None:
            self.validate('reset', val)
        self._reset = val
    
    _increment_size = None
    @property
    def increment_size(self):
        """
        The increment size (in bytes) by which the volume would
        be grown. The default value is 5%. Increment-size and
        increment-percent are mutually exclusive, and an error
        will be generated if both are specified.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._increment_size
    @increment_size.setter
    def increment_size(self, val):
        if val != None:
            self.validate('increment_size', val)
        self._increment_size = val
    
    _increment_percent = None
    @property
    def increment_percent(self):
        """
        Using this value, the increment size will be computed as
        a percentage of the volume size at the time autosize was
        enabled. The default value is 5%. The increment-percent
        element is mutually exclusive with increment-size, and an
        error will be generated if both are specified.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._increment_percent
    @increment_percent.setter
    def increment_percent(self, val):
        if val != None:
            self.validate('increment_percent', val)
        self._increment_percent = val
    
    _grow_threshold_percent = None
    @property
    def grow_threshold_percent(self):
        """
        Used space threshold which triggers autogrow. When the
        volume-info.size-used is greater than this percent of
        volume-info.size-total, the volume will be grown. The
        computed value is rounded down. The default value of this
        element varies from 85% to 98%, depending on the volume
        size. It is an error for the grow threshold to be less
        than or equal to the shrink threshold.
        <p>
        Attributes: optional-for-create, modifiable
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
        The maximum size (in bytes) to which the volume would be
        grown automatically. The default value is 20% greater
        than the volume size at the time autosize was enabled. It
        is an error for the maximum volume size to be less than
        the current volume size. It is also an error for the
        maximum size to be less than or equal to the minimum
        size.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._maximum_size
    @maximum_size.setter
    def maximum_size(self, val):
        if val != None:
            self.validate('maximum_size', val)
        self._maximum_size = val
    
    _mode = None
    @property
    def mode(self):
        """
        The current mode of operation of volume autosize.  Valid
        modes are 'off', 'grow', and 'grow_shrink'. The default
        mode is 'off'.
        <p>
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "off"            ,
        <li> "grow"           ,
        <li> "grow_shrink"
        </ul>
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        This element is deprecated in Data ONTAP 8.2 and later.
        Please use autosize-mode instead. Setting this parameter
        to 'true' enables the 'grow' mode, while setting it to
        'false' disables autosize and sets the autosize mode to
        'off'. The default value is 'false'.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _minimum_size = None
    @property
    def minimum_size(self):
        """
        The minimum size (in bytes) below which the volume would
        not be shrunk automatically. The default value is the
        size of the volume at the time the 'grow_shrink' mode was
        enabled. It is an error for the minimum size to be
        greater than or equal to the maximum size.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._minimum_size
    @minimum_size.setter
    def minimum_size(self, val):
        if val != None:
            self.validate('minimum_size', val)
        self._minimum_size = val
    
    _shrink_threshold_percent = None
    @property
    def shrink_threshold_percent(self):
        """
        The used space threshold below which autoshrink is
        triggered. When the volume-info.size-used is less than
        this percent of volume-info.size-total, the volume will
        be shrunk. The computed value is rounded down. The
        default shrink theshold is 50%. It is an error for the
        shrink threshold to be greater than or equal to the grow
        threshold.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._shrink_threshold_percent
    @shrink_threshold_percent.setter
    def shrink_threshold_percent(self, val):
        if val != None:
            self.validate('shrink_threshold_percent', val)
        self._shrink_threshold_percent = val
    
    @staticmethod
    def get_api_name():
          return "volume-autosize-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'reset',
            'increment-size',
            'increment-percent',
            'grow-threshold-percent',
            'maximum-size',
            'mode',
            'is-enabled',
            'minimum-size',
            'shrink-threshold-percent',
        ]
    
    def describe_properties(self):
        return {
            'reset': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'increment_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'increment_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'grow_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maximum_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'minimum_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'shrink_threshold_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
