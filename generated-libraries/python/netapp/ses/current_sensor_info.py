from netapp.netapp_object import NetAppObject

class CurrentSensorInfo(NetAppObject):
    """
    Presents the electrical current sensor information, if implemented
    on the system.
    """
    
    _sensor_reading = None
    @property
    def sensor_reading(self):
        """
        Current reading of the sensor. This field will be not
        be present if unable to read the sensor value properly.
        """
        return self._sensor_reading
    @sensor_reading.setter
    def sensor_reading(self, val):
        if val != None:
            self.validate('sensor_reading', val)
        self._sensor_reading = val
    
    _is_sensor_not_installed = None
    @property
    def is_sensor_not_installed(self):
        """
        Indicates the current sensor elements is not installed.
        This will only be present if the element is
        missing, in such case no further data for this
        element will be presented.
        """
        return self._is_sensor_not_installed
    @is_sensor_not_installed.setter
    def is_sensor_not_installed(self, val):
        if val != None:
            self.validate('is_sensor_not_installed', val)
        self._is_sensor_not_installed = val
    
    _current_sensor_no = None
    @property
    def current_sensor_no(self):
        """
        Current sensor number.
        """
        return self._current_sensor_no
    @current_sensor_no.setter
    def current_sensor_no(self, val):
        if val != None:
            self.validate('current_sensor_no', val)
        self._current_sensor_no = val
    
    _sensor_condition = None
    @property
    def sensor_condition(self):
        """
        A Text string describing whether the sensor-reading field
        is within normal operating range. This field is present
        only if sensor-reading field is also present.
        Possible values are:
        "overcurrent_failure",
        "overcurrent_warning",
        "normal_operating_range".
        """
        return self._sensor_condition
    @sensor_condition.setter
    def sensor_condition(self, val):
        if val != None:
            self.validate('sensor_condition', val)
        self._sensor_condition = val
    
    _is_sensor_error = None
    @property
    def is_sensor_error(self):
        """
        Will indicate whether the sensor has encountered an error.
        """
        return self._is_sensor_error
    @is_sensor_error.setter
    def is_sensor_error(self, val):
        if val != None:
            self.validate('is_sensor_error', val)
        self._is_sensor_error = val
    
    @staticmethod
    def get_api_name():
          return "current-sensor-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'sensor-reading',
            'is-sensor-not-installed',
            'current-sensor-no',
            'sensor-condition',
            'is-sensor-error',
        ]
    
    def describe_properties(self):
        return {
            'sensor_reading': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_sensor_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'current_sensor_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'sensor_condition': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_sensor_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
