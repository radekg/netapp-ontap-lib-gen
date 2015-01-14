from netapp.netapp_object import NetAppObject

class FlashThreshold(NetAppObject):
    """
    A definition for a threshold element. Each threshold
    specifies what level of errors or failures the specified domain
    can sustain before the specified action is taken.
    """
    
    _threshold_units = None
    @property
    def threshold_units(self):
        """
        The metric for threshold.
        Possible values: "count", or "percentage".
        """
        return self._threshold_units
    @threshold_units.setter
    def threshold_units(self, val):
        if val != None:
            self.validate('threshold_units', val)
        self._threshold_units = val
    
    _time_slice = None
    @property
    def time_slice(self):
        """
        The time slice. Available if the 'threshold-unit' is
        "count". If not, output will say 'none'.
        Possible values: "none", "seconds", "minutes", or
        "hours".
        """
        return self._time_slice
    @time_slice.setter
    def time_slice(self, val):
        if val != None:
            self.validate('time_slice', val)
        self._time_slice = val
    
    _domain = None
    @property
    def domain(self):
        """
        The type of domain.
        Possible values:
        "card",
        "bank",
        "chip" (in Data ONTAP 7.3.x to 8.1)
        or "lun" (from Data ONTAP 8.2 onwards).
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _action = None
    @property
    def action(self):
        """
        Action to be taken if this threshold is exceeded.
        Possible values:
        "log an EMS event",
        "log an EMS_event, and disable the 'domain'",
        "log an EMS event, and send an AutoSupport message",
        "log an EMS event, send an AutoSupport message, and
        disable the 'domain'"
        """
        return self._action
    @action.setter
    def action(self, val):
        if val != None:
            self.validate('action', val)
        self._action = val
    
    _threshold_value = None
    @property
    def threshold_value(self):
        """
        Threshold value in 'threshold-units'.
        """
        return self._threshold_value
    @threshold_value.setter
    def threshold_value(self, val):
        if val != None:
            self.validate('threshold_value', val)
        self._threshold_value = val
    
    @staticmethod
    def get_api_name():
          return "flash-threshold"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'threshold-units',
            'time-slice',
            'domain',
            'action',
            'threshold-value',
        ]
    
    def describe_properties(self):
        return {
            'threshold_units': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'time_slice': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'domain': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'action': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'threshold_value': { 'class': int, 'is_list': False, 'required': 'required' },
        }
