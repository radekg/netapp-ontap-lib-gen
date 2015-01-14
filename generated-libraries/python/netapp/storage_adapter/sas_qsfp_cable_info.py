from netapp.netapp_object import NetAppObject

class SasQsfpCableInfo(NetAppObject):
    """
    QSPF Cable information.
    """
    
    _cable_technology = None
    @property
    def cable_technology(self):
        """
        Cable technology. This field will not be
        present if the information is not available or
        accessible, or if a cable is not connected at this
        connector. Possible values:
        "active_copper", "passive_copper", "copper", "optical".
        """
        return self._cable_technology
    @cable_technology.setter
    def cable_technology(self, val):
        if val != None:
            self.validate('cable_technology', val)
        self._cable_technology = val
    
    _cable_length = None
    @property
    def cable_length(self):
        """
        Length of the cable.
        Will be missing if data not available or not present.
        """
        return self._cable_length
    @cable_length.setter
    def cable_length(self, val):
        if val != None:
            self.validate('cable_length', val)
        self._cable_length = val
    
    _cable_part_number = None
    @property
    def cable_part_number(self):
        """
        Cable part number as assigned by the manufacturer.
        Will be missing if data not available or not present.
        """
        return self._cable_part_number
    @cable_part_number.setter
    def cable_part_number(self, val):
        if val != None:
            self.validate('cable_part_number', val)
        self._cable_part_number = val
    
    _cable_serial_number = None
    @property
    def cable_serial_number(self):
        """
        This is actually not serial number, but rather
        cable identifier. For backwards compatibility
        this is reported as cable-serial-number. For the
        actual serial number see attached-serial-number. The
        connectors at both ends of the same cable will report
        the same value for this field. This field can be used
        to generate topology. This field will not be present
        if a cable is not connected to the connector or if
        the cable is not connected to a functioning device.
        """
        return self._cable_serial_number
    @cable_serial_number.setter
    def cable_serial_number(self, val):
        if val != None:
            self.validate('cable_serial_number', val)
        self._cable_serial_number = val
    
    _cable_end_identifier = None
    @property
    def cable_end_identifier(self):
        """
        Each cable has two ends. This field shows which
        end of the cable is connected to the shelf.
        This field will not be present if the information
        is not available or accessible, or if a cable is
        not connected at this connector. Possible values:
        "end_0", "end_1".
        """
        return self._cable_end_identifier
    @cable_end_identifier.setter
    def cable_end_identifier(self, val):
        if val != None:
            self.validate('cable_end_identifier', val)
        self._cable_end_identifier = val
    
    _cable_manufacturer = None
    @property
    def cable_manufacturer(self):
        """
        Manufacturer of the cable.
        Will be missing if data not available or not present.
        """
        return self._cable_manufacturer
    @cable_manufacturer.setter
    def cable_manufacturer(self, val):
        if val != None:
            self.validate('cable_manufacturer', val)
        self._cable_manufacturer = val
    
    _attached_serial_number = None
    @property
    def attached_serial_number(self):
        """
        Serial number of the attached cable as assigned by
        the cable manufacturer. This field will not be
        present	if the information is not available, or if
        a cable is not connected at this connector.
        Note that depending on the cable, the serial
        number at the two ends of the cable may or may not
        match. An example of this is SAS optical cables that
        do not have integrated QSFP's, which will show
        different attached serial numbers at the ends of
        cable. Cables with integrated QSFP's will have
        matching serial numbers at both ends.
        """
        return self._attached_serial_number
    @attached_serial_number.setter
    def attached_serial_number(self, val):
        if val != None:
            self.validate('attached_serial_number', val)
        self._attached_serial_number = val
    
    @staticmethod
    def get_api_name():
          return "sas-qsfp-cable-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cable-technology',
            'cable-length',
            'cable-part-number',
            'cable-serial-number',
            'cable-end-identifier',
            'cable-manufacturer',
            'attached-serial-number',
        ]
    
    def describe_properties(self):
        return {
            'cable_technology': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_length': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_end_identifier': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_manufacturer': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'attached_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
