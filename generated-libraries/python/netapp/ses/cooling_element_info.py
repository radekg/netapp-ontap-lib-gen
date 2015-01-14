from netapp.netapp_object import NetAppObject

class CoolingElementInfo(NetAppObject):
    """
    Information on individual cooling elements (fans).
    """
    
    _cooling_element_number = None
    @property
    def cooling_element_number(self):
        """
        Cooling element number.
        """
        return self._cooling_element_number
    @cooling_element_number.setter
    def cooling_element_number(self, val):
        if val != None:
            self.validate('cooling_element_number', val)
        self._cooling_element_number = val
    
    _rpm = None
    @property
    def rpm(self):
        """
        Current RPM (revolutions per minutes) of the fan.
        Will not be present if RPM is not available at
        the time API is executed or if RPM detection hardware
        is not supported by the shelf or if cooling element is
        not installed.
        """
        return self._rpm
    @rpm.setter
    def rpm(self, val):
        if val != None:
            self.validate('rpm', val)
        self._rpm = val
    
    _cooling_element_is_error = None
    @property
    def cooling_element_is_error(self):
        """
        Indicated whether cooling elements has failed or
        reported any errors.
        Will not be present if cooling element is not installed.
        """
        return self._cooling_element_is_error
    @cooling_element_is_error.setter
    def cooling_element_is_error(self, val):
        if val != None:
            self.validate('cooling_element_is_error', val)
        self._cooling_element_is_error = val
    
    _cooling_element_is_not_installed = None
    @property
    def cooling_element_is_not_installed(self):
        """
        Indicates the cooling elements is not installed.
        This will only be present if the element is
        missing, in such case no further data for this
        element will be presented.
        """
        return self._cooling_element_is_not_installed
    @cooling_element_is_not_installed.setter
    def cooling_element_is_not_installed(self, val):
        if val != None:
            self.validate('cooling_element_is_not_installed', val)
        self._cooling_element_is_not_installed = val
    
    @staticmethod
    def get_api_name():
          return "cooling-element-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cooling-element-number',
            'rpm',
            'cooling-element-is-error',
            'cooling-element-is-not-installed',
        ]
    
    def describe_properties(self):
        return {
            'cooling_element_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'rpm': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cooling_element_is_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cooling_element_is_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
