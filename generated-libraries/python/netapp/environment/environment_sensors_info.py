from netapp.netapp_object import NetAppObject

class EnvironmentSensorsInfo(NetAppObject):
    """
    Environment Sensor Info.  The environmental subsystem monitors a
    set of hardware sensors in the system. Each sensor represents a
    pair of state and value that can be measured to reflect the
    physical state of device(s). Based on the values the sensors
    represent, the sensors can be grouped to discrete-valued sensors
    and threshold-based sensors. The discrete-valued sensors have a
    set of discrete values that represent states of sensors. The
    threshold-based sensors have a numeral value that represnts a
    value on an axis, and may have a set of thresholds (points on
    that axis) are used to define the state of the sensor (ranging
    from critically low to critically high). This typedef defines the
    information for both groups of sensors.
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _sensor_type = None
    @property
    def sensor_type(self):
        """
        Type of the sensor
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "fan"       - FAN RPM sensors,
        <li> "thermal"   - Temerature sensors,
        <li> "voltage"   - Voltage measurement sensors,
        <li> "current"   - Current measurement sensors,
        <li> "battlife"  - Sensors report battery life,
        <li> "discrete"  - Discrete sensors,
        <li> "fru"       - FRU sensors,
        <li> "nvmem"     - Sensors on the NVMEM module,
        <li> "counter"   - Sensors report in counters,
        <li> "minutes"   - Sensors report by minutes,
        <li> "percent"   - Sensors report in percentage,
        <li> "agent"     - Sensors on or throught the Agent
        device,
        <li> "unknown"   - Unknown sensors
        </ul>
        """
        return self._sensor_type
    @sensor_type.setter
    def sensor_type(self, val):
        if val != None:
            self.validate('sensor_type', val)
        self._sensor_type = val
    
    _warning_low_threshold = None
    @property
    def warning_low_threshold(self):
        """
        Warning low threshold
        Attributes: non-creatable, non-modifiable
        """
        return self._warning_low_threshold
    @warning_low_threshold.setter
    def warning_low_threshold(self, val):
        if val != None:
            self.validate('warning_low_threshold', val)
        self._warning_low_threshold = val
    
    _threshold_sensor_value = None
    @property
    def threshold_sensor_value(self):
        """
        Threshold-based sensor value
        Attributes: non-creatable, non-modifiable
        """
        return self._threshold_sensor_value
    @threshold_sensor_value.setter
    def threshold_sensor_value(self, val):
        if val != None:
            self.validate('threshold_sensor_value', val)
        self._threshold_sensor_value = val
    
    _discrete_sensor_state = None
    @property
    def discrete_sensor_state(self):
        """
        Discrete-valued sensor state
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "normal"         - The device is normal,
        <li> "warn_low"       - The device state is lower than
        the warning low threshold and higher than the critical
        low threshold,
        <li> "warn_high"      - The device state is higher than
        the warning high threshold and lower than the critical
        high threshold,
        <li> "crit_low"       - The device state is lower than
        the critical low threshold,
        <li> "crit_high"      - The device state is higher than
        the critical higher threshold,
        <li> "disabled"       - The sensor is disabled, only
        available for SP-based filers,
        <li> "uninitialized"  - The sensor is not yet
        initialized, only available for SP-based filers,
        <li> "init_failed"    - The sensor failed to
        initialize, only available for SP-based filers,
        <li> "not_available"  - The sensor is temporarily not
        able to report status, only available for SP-based
        filers,
        <li> "invalid"        - The status returned from the
        sensor is not valid, only available for SP-based filers,
        <li> "retry"          - The sensor is in the rety
        state, only available for non SP-based filers,
        <li> "bad"            - The device is bad, only
        available for non SP-based filers,
        <li> "not_present"    - The device is not present, only
        available for non SP-based filers,
        <li> "failed"         - The sensor failed to report
        status,
        <li> "ignored"        - The sensor state is ignored,
        only available for SP-based filers,
        <li> "unknown"        - The sensor state is uknown
        </ul>
        """
        return self._discrete_sensor_state
    @discrete_sensor_state.setter
    def discrete_sensor_state(self, val):
        if val != None:
            self.validate('discrete_sensor_state', val)
        self._discrete_sensor_state = val
    
    _critical_high_threshold = None
    @property
    def critical_high_threshold(self):
        """
        Critical high threshold
        Attributes: non-creatable, non-modifiable
        """
        return self._critical_high_threshold
    @critical_high_threshold.setter
    def critical_high_threshold(self, val):
        if val != None:
            self.validate('critical_high_threshold', val)
        self._critical_high_threshold = val
    
    _critical_low_threshold = None
    @property
    def critical_low_threshold(self):
        """
        Critical low threshold
        Attributes: non-creatable, non-modifiable
        """
        return self._critical_low_threshold
    @critical_low_threshold.setter
    def critical_low_threshold(self, val):
        if val != None:
            self.validate('critical_low_threshold', val)
        self._critical_low_threshold = val
    
    _discrete_sensor_value = None
    @property
    def discrete_sensor_value(self):
        """
        Discrete-valued sensor value
        Attributes: non-creatable, non-modifiable
        """
        return self._discrete_sensor_value
    @discrete_sensor_value.setter
    def discrete_sensor_value(self, val):
        if val != None:
            self.validate('discrete_sensor_value', val)
        self._discrete_sensor_value = val
    
    _warning_high_threshold = None
    @property
    def warning_high_threshold(self):
        """
        Warning high threshold
        Attributes: non-creatable, non-modifiable
        """
        return self._warning_high_threshold
    @warning_high_threshold.setter
    def warning_high_threshold(self, val):
        if val != None:
            self.validate('warning_high_threshold', val)
        self._warning_high_threshold = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        Node name the sensor is associated with
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _value_units = None
    @property
    def value_units(self):
        """
        The units of the threshold-based sensor value. More than
        90 possible unit types. Refer to the "Sensor Unit Type
        Codes" in the IPMI spec for possible types.
        Attributes: non-creatable, non-modifiable
        """
        return self._value_units
    @value_units.setter
    def value_units(self, val):
        if val != None:
            self.validate('value_units', val)
        self._value_units = val
    
    _threshold_sensor_state = None
    @property
    def threshold_sensor_state(self):
        """
        Threshold-based sensor state
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "normal"         - The device is normal,
        <li> "warn_low"       - The device state is lower than
        the warning low threshold and higher than the critical
        low threshold,
        <li> "warn_high"      - The device state is higher than
        the warning high threshold and lower than the critical
        high threshold,
        <li> "crit_low"       - The device state is lower than
        the critical low threshold,
        <li> "crit_high"      - The device state is higher than
        the critical higher threshold,
        <li> "disabled"       - The sensor is disabled, only
        available for SP-based filers,
        <li> "uninitialized"  - The sensor is not yet
        initialized, only available for SP-based filers,
        <li> "init_failed"    - The sensor failed to
        initialize, only available for SP-based filers,
        <li> "not_available"  - The sensor is temporarily not
        able to report status, only available for SP-based
        filers,
        <li> "invalid"        - The status returned from the
        sensor is not valid, only available for SP-based filers,
        <li> "retry"          - The sensor is in the rety
        state, only available for non SP-based filers,
        <li> "bad"            - The device is bad, only
        available for non SP-based filers,
        <li> "not_present"    - The device is not present, only
        available for non SP-based filers,
        <li> "failed"         - The sensor failed to report
        status,
        <li> "ignored"        - The sensor state is ignored,
        only available for SP-based filers,
        <li> "unknown"        - The sensor state is uknown
        </ul>
        """
        return self._threshold_sensor_state
    @threshold_sensor_state.setter
    def threshold_sensor_state(self, val):
        if val != None:
            self.validate('threshold_sensor_state', val)
        self._threshold_sensor_state = val
    
    _sensor_name = None
    @property
    def sensor_name(self):
        """
        Name of the sensor in the environmental subsystem. The
        maximum length of the sensor name is 32
        Attributes: non-creatable, non-modifiable
        """
        return self._sensor_name
    @sensor_name.setter
    def sensor_name(self, val):
        if val != None:
            self.validate('sensor_name', val)
        self._sensor_name = val
    
    @staticmethod
    def get_api_name():
          return "environment-sensors-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'sensor-type',
            'warning-low-threshold',
            'threshold-sensor-value',
            'discrete-sensor-state',
            'critical-high-threshold',
            'critical-low-threshold',
            'discrete-sensor-value',
            'warning-high-threshold',
            'node-name',
            'value-units',
            'threshold-sensor-state',
            'sensor-name',
        ]
    
    def describe_properties(self):
        return {
            'sensor_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'warning_low_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'threshold_sensor_value': { 'class': int, 'is_list': False, 'required': 'optional' },
            'discrete_sensor_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'critical_high_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'critical_low_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'discrete_sensor_value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'warning_high_threshold': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'value_units': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'threshold_sensor_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sensor_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
