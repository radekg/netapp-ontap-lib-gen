from netapp.netapp_object import NetAppObject

class AdapterSfpInfo(NetAppObject):
    """
    Information on  small form factor pluggable
    transceiver/connector (also known as sfp).
    """
    
    _part_number = None
    @property
    def part_number(self):
        """
        Vendor's part number for the sfp.
        If data not available, value will be "not_available".
        """
        return self._part_number
    @part_number.setter
    def part_number(self, val):
        if val != None:
            self.validate('part_number', val)
        self._part_number = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number for sfp.
        If data not available, value will be "not_available".
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _vendor = None
    @property
    def vendor(self):
        """
        sfp vendor name
        If data not available, value will be "not_available".
        """
        return self._vendor
    @vendor.setter
    def vendor(self, val):
        if val != None:
            self.validate('vendor', val)
        self._vendor = val
    
    _speed_capabilities = None
    @property
    def speed_capabilities(self):
        """
        Comma separated list of speed capabilities of
        the sfp. Example: "1, 2 Gbit/Sec".
        If data not available, value will be "not_available".
        """
        return self._speed_capabilities
    @speed_capabilities.setter
    def speed_capabilities(self, val):
        if val != None:
            self.validate('speed_capabilities', val)
        self._speed_capabilities = val
    
    @staticmethod
    def get_api_name():
          return "adapter-sfp-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'part-number',
            'serial-number',
            'vendor',
            'speed-capabilities',
        ]
    
    def describe_properties(self):
        return {
            'part_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'speed_capabilities': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
