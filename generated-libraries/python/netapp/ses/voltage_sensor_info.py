from netapp.netapp_object import NetAppObject

class VoltageSensorInfo(NetAppObject):
    """
    Presents the voltage sensor information, if implemented on
    the system.
    """
    
    _is_sensor_not_installed = None
    @property
    def is_sensor_not_installed(self):
        """
        Indicates the voltage sensor elements is not installed.
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
    
    _sensor_reading = None
    @property
    def sensor_reading(self):
        """
        Voltage reading of the sensor. This field will be not
        be present if unable to read the sensor value properly.
        """
        return self._sensor_reading
    @sensor_reading.setter
    def sensor_reading(self, val):
        if val != None:
            self.validate('sensor_reading', val)
        self._sensor_reading = val
    
    _sensor_condition = None
    @property
    def sensor_condition(self):
        """
        A Text string describing whether the sensor-reading field
        is within normal operating range. This field is present
        only if sensor-reading field is also present.
        Possible values are:
        "overvoltage_failure",
        "overvoltage_warning",
        "undervoltage_warning",
        "undervoltage_failure",
        "normal_operating_range".
        """
        return self._sensor_condition
    @sensor_condition.setter
    def sensor_condition(self, val):
        if val != None:
            self.validate('sensor_condition', val)
        self._sensor_condition = val
    
    _voltage_sensor_no = None
    @property
    def voltage_sensor_no(self):
        """
        Voltage sensor number.
        """
        return self._voltage_sensor_no
    @voltage_sensor_no.setter
    def voltage_sensor_no(self, val):
        if val != None:
            self.validate('voltage_sensor_no', val)
        self._voltage_sensor_no = val
    
    _is_sensor_error = None
    @property
    def is_sensor_error(self):
        """
        Indicates whether the sensor has encountered an error.
        """
        return self._is_sensor_error
    @is_sensor_error.setter
    def is_sensor_error(self, val):
        if val != None:
            self.validate('is_sensor_error', val)
        self._is_sensor_error = val
    
    @staticmethod
    def get_api_name():
          return "voltage-sensor-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-sensor-not-installed',
            'sensor-reading',
            'sensor-condition',
            'voltage-sensor-no',
            'is-sensor-error',
        ]
    
    def describe_properties(self):
        return {
            'is_sensor_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'sensor_reading': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sensor_condition': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'voltage_sensor_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_sensor_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
