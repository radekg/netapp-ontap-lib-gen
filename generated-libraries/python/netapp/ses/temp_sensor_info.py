from netapp.netapp_object import NetAppObject

class TempSensorInfo(NetAppObject):
    """
    information on the temperature sensors installed in the shelf.
    """
    
    _temp_sensor_is_not_installed = None
    @property
    def temp_sensor_is_not_installed(self):
        """
        Indicates the sensor for this element is not
        installed. This will only be presented if the
        sensor is missing, and no further data for
        this sensor will be presented.
        """
        return self._temp_sensor_is_not_installed
    @temp_sensor_is_not_installed.setter
    def temp_sensor_is_not_installed(self, val):
        if val != None:
            self.validate('temp_sensor_is_not_installed', val)
        self._temp_sensor_is_not_installed = val
    
    _temp_sensor_current_condition = None
    @property
    def temp_sensor_current_condition(self):
        """
        Current temperature condition for this sensor. One of:
        "under_temperature_warning",
        "under_temperature_failure",
        "over_temperature_warning",
        "over_temperature_failure",
        "normal_temperature_range".
        """
        return self._temp_sensor_current_condition
    @temp_sensor_current_condition.setter
    def temp_sensor_current_condition(self, val):
        if val != None:
            self.validate('temp_sensor_current_condition', val)
        self._temp_sensor_current_condition = val
    
    _temp_sensor_is_ambient = None
    @property
    def temp_sensor_is_ambient(self):
        """
        Indicates whether the temp-sensor-current-temp is
        the ambient temperature.
        """
        return self._temp_sensor_is_ambient
    @temp_sensor_is_ambient.setter
    def temp_sensor_is_ambient(self, val):
        if val != None:
            self.validate('temp_sensor_is_ambient', val)
        self._temp_sensor_is_ambient = val
    
    _temp_sensor_low_warning = None
    @property
    def temp_sensor_low_warning(self):
        """
        Low warning temperature in degree Celsius.
        """
        return self._temp_sensor_low_warning
    @temp_sensor_low_warning.setter
    def temp_sensor_low_warning(self, val):
        if val != None:
            self.validate('temp_sensor_low_warning', val)
        self._temp_sensor_low_warning = val
    
    _temp_sensor_hi_warning = None
    @property
    def temp_sensor_hi_warning(self):
        """
        High warning temperature in degree Celsius.
        """
        return self._temp_sensor_hi_warning
    @temp_sensor_hi_warning.setter
    def temp_sensor_hi_warning(self, val):
        if val != None:
            self.validate('temp_sensor_hi_warning', val)
        self._temp_sensor_hi_warning = val
    
    _temp_sensor_hi_critical = None
    @property
    def temp_sensor_hi_critical(self):
        """
        High critical temperature in degree Celsius.
        """
        return self._temp_sensor_hi_critical
    @temp_sensor_hi_critical.setter
    def temp_sensor_hi_critical(self, val):
        if val != None:
            self.validate('temp_sensor_hi_critical', val)
        self._temp_sensor_hi_critical = val
    
    _temp_sensor_current_temperature = None
    @property
    def temp_sensor_current_temperature(self):
        """
        Current temperature reading in degrees Celsius.
        """
        return self._temp_sensor_current_temperature
    @temp_sensor_current_temperature.setter
    def temp_sensor_current_temperature(self, val):
        if val != None:
            self.validate('temp_sensor_current_temperature', val)
        self._temp_sensor_current_temperature = val
    
    _temp_sensor_element_no = None
    @property
    def temp_sensor_element_no(self):
        """
        Element number for the temperature sensor.
        """
        return self._temp_sensor_element_no
    @temp_sensor_element_no.setter
    def temp_sensor_element_no(self, val):
        if val != None:
            self.validate('temp_sensor_element_no', val)
        self._temp_sensor_element_no = val
    
    _temp_sensor_low_critical = None
    @property
    def temp_sensor_low_critical(self):
        """
        Low critical temperature in degree Celsius.
        """
        return self._temp_sensor_low_critical
    @temp_sensor_low_critical.setter
    def temp_sensor_low_critical(self, val):
        if val != None:
            self.validate('temp_sensor_low_critical', val)
        self._temp_sensor_low_critical = val
    
    _temp_sensor_is_error = None
    @property
    def temp_sensor_is_error(self):
        """
        Indicates whether the sensor has indicated
        an error in temperature.
        """
        return self._temp_sensor_is_error
    @temp_sensor_is_error.setter
    def temp_sensor_is_error(self, val):
        if val != None:
            self.validate('temp_sensor_is_error', val)
        self._temp_sensor_is_error = val
    
    @staticmethod
    def get_api_name():
          return "temp-sensor-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'temp-sensor-is-not-installed',
            'temp-sensor-current-condition',
            'temp-sensor-is-ambient',
            'temp-sensor-low-warning',
            'temp-sensor-hi-warning',
            'temp-sensor-hi-critical',
            'temp-sensor-current-temperature',
            'temp-sensor-element-no',
            'temp-sensor-low-critical',
            'temp-sensor-is-error',
        ]
    
    def describe_properties(self):
        return {
            'temp_sensor_is_not_installed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'temp_sensor_current_condition': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'temp_sensor_is_ambient': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'temp_sensor_low_warning': { 'class': int, 'is_list': False, 'required': 'required' },
            'temp_sensor_hi_warning': { 'class': int, 'is_list': False, 'required': 'required' },
            'temp_sensor_hi_critical': { 'class': int, 'is_list': False, 'required': 'required' },
            'temp_sensor_current_temperature': { 'class': int, 'is_list': False, 'required': 'optional' },
            'temp_sensor_element_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'temp_sensor_low_critical': { 'class': int, 'is_list': False, 'required': 'required' },
            'temp_sensor_is_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
