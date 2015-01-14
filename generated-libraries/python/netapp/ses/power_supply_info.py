from netapp.netapp_object import NetAppObject

class PowerSupplyInfo(NetAppObject):
    """
    Power supply information
    """
    
    _is_auto_power_reset_enabled = None
    @property
    def is_auto_power_reset_enabled(self):
        """
        Indicates whether the auto power reset of the supply is
        enabled. This field will not be present if the power supply
        is missing.
        """
        return self._is_auto_power_reset_enabled
    @is_auto_power_reset_enabled.setter
    def is_auto_power_reset_enabled(self, val):
        if val != None:
            self.validate('is_auto_power_reset_enabled', val)
        self._is_auto_power_reset_enabled = val
    
    _power_supply_part_no = None
    @property
    def power_supply_part_no(self):
        """
        Power supply part number. The field will not be present
        if part number is unavailable or not implemented or
        if the power supply is missing.
        """
        return self._power_supply_part_no
    @power_supply_part_no.setter
    def power_supply_part_no(self, val):
        if val != None:
            self.validate('power_supply_part_no', val)
        self._power_supply_part_no = val
    
    _power_supply_serial_no = None
    @property
    def power_supply_serial_no(self):
        """
        Power supply serial number.
        This field will not be present if the power supply is
        missing.
        """
        return self._power_supply_serial_no
    @power_supply_serial_no.setter
    def power_supply_serial_no(self, val):
        if val != None:
            self.validate('power_supply_serial_no', val)
        self._power_supply_serial_no = val
    
    _power_supply_is_error = None
    @property
    def power_supply_is_error(self):
        """
        Indicates whether the power supply has reported any errors.
        This field will not be present if the power supply is
        missing.
        """
        return self._power_supply_is_error
    @power_supply_is_error.setter
    def power_supply_is_error(self, val):
        if val != None:
            self.validate('power_supply_is_error', val)
        self._power_supply_is_error = val
    
    _power_supply_firmware_revision = None
    @property
    def power_supply_firmware_revision(self):
        """
        Power supply firmware revision. This field will not be
        present if firmware rev is unavailable or feature not
        implemented, or if the power supply is missing.
        """
        return self._power_supply_firmware_revision
    @power_supply_firmware_revision.setter
    def power_supply_firmware_revision(self, val):
        if val != None:
            self.validate('power_supply_firmware_revision', val)
        self._power_supply_firmware_revision = val
    
    _power_supply_type = None
    @property
    def power_supply_type(self):
        """
        Power supply type. This field will not be present if power
        supply type is unavailable or feature is not implemented,
        or if the power supply is missing.
        """
        return self._power_supply_type
    @power_supply_type.setter
    def power_supply_type(self, val):
        if val != None:
            self.validate('power_supply_type', val)
        self._power_supply_type = val
    
    _power_supply_swap_count = None
    @property
    def power_supply_swap_count(self):
        """
        Number of power supply swap counts since boot.
        This field will not be present if the power supply is
        missing.
        """
        return self._power_supply_swap_count
    @power_supply_swap_count.setter
    def power_supply_swap_count(self, val):
        if val != None:
            self.validate('power_supply_swap_count', val)
        self._power_supply_swap_count = val
    
    _power_supply_is_not_installed = None
    @property
    def power_supply_is_not_installed(self):
        """
        Indicates the power supply for this element
        is not installed. This will only be presented if
        the power supply is missing, in which case no further
        information for the element will be available.
        """
        return self._power_supply_is_not_installed
    @power_supply_is_not_installed.setter
    def power_supply_is_not_installed(self, val):
        if val != None:
            self.validate('power_supply_is_not_installed', val)
        self._power_supply_is_not_installed = val
    
    _power_supply_element_number = None
    @property
    def power_supply_element_number(self):
        """
        Element number the power supply.
        """
        return self._power_supply_element_number
    @power_supply_element_number.setter
    def power_supply_element_number(self, val):
        if val != None:
            self.validate('power_supply_element_number', val)
        self._power_supply_element_number = val
    
    _is_power_reset_capable = None
    @property
    def is_power_reset_capable(self):
        """
        Indicates whether the power supply can be reset via software
        control. This field will not be present if power supply is
        missing.
        """
        return self._is_power_reset_capable
    @is_power_reset_capable.setter
    def is_power_reset_capable(self, val):
        if val != None:
            self.validate('is_power_reset_capable', val)
        self._is_power_reset_capable = val
    
    @staticmethod
    def get_api_name():
          return "power-supply-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-auto-power-reset-enabled',
            'power-supply-part-no',
            'power-supply-serial-no',
            'power-supply-is-error',
            'power-supply-firmware-revision',
            'power-supply-type',
            'power-supply-swap-count',
            'power-supply-is-not-installed',
            'power-supply-element-number',
            'is-power-reset-capable',
        ]
    
    def describe_properties(self):
        return {
            'is_auto_power_reset_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'power_supply_part_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'power_supply_serial_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'power_supply_is_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'power_supply_firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'power_supply_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'power_supply_swap_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'power_supply_is_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'power_supply_element_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_power_reset_capable': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
