from netapp.netapp_object import NetAppObject

class SasConnectorInfo(NetAppObject):
    """
    Detailed information on SAS cables and connectors connected
    to the shelf. Only information on the connectors with cables
    attached will be presented.
    """
    
    _is_cable_connected = None
    @property
    def is_cable_connected(self):
        """
        Indicates whether a cable is connected at this connector
        location. No further information will be provided if a
        cable is not connected at this connector location.
        Note that a cable connection does not necessarily mean
        that the shelf is connected to a storage cointroller.
        This will also depend on the other end of the cable.
        """
        return self._is_cable_connected
    @is_cable_connected.setter
    def is_cable_connected(self, val):
        if val != None:
            self.validate('is_cable_connected', val)
        self._is_cable_connected = val
    
    _shelf_module = None
    @property
    def shelf_module(self):
        """
        Shelf module for this connector
        <ul>
        <li> "a" - Presenting data for shelf module A.
        <li> "b" - Presenting data for shelf module B.
        </ul>
        """
        return self._shelf_module
    @shelf_module.setter
    def shelf_module(self, val):
        if val != None:
            self.validate('shelf_module', val)
        self._shelf_module = val
    
    _cable_technology = None
    @property
    def cable_technology(self):
        """
        Cable technology. This field will not be
        present if the information is not available or
        accessible, or if a cable is not connected at this
        connector. Possible values:
        "cupper", "optical".
        """
        return self._cable_technology
    @cable_technology.setter
    def cable_technology(self, val):
        if val != None:
            self.validate('cable_technology', val)
        self._cable_technology = val
    
    _cable_type = None
    @property
    def cable_type(self):
        """
        Type of the cable being used. This field will not be
        present if the information is not available or
        accessible, or if a cable is not connected at this
        connector. Possible values:
        "qsfp".
        """
        return self._cable_type
    @cable_type.setter
    def cable_type(self, val):
        if val != None:
            self.validate('cable_type', val)
        self._cable_type = val
    
    _swap_count = None
    @property
    def swap_count(self):
        """
        Number of times, since last boot, a cable has
        been inserted into this connector
        """
        return self._swap_count
    @swap_count.setter
    def swap_count(self, val):
        if val != None:
            self.validate('swap_count', val)
        self._swap_count = val
    
    _cable_serial_no = None
    @property
    def cable_serial_no(self):
        """
        This is actually not serial number, but rather
        cable identifier. For backwards compatibility
        this is reported as cable-serial-no. For the
        actual serial number see attached-serial-no. The
        connectors at both ends of the same cable will report
        the same value for this field. This field can be used
        to generate topology. This field will not be present
        if a cable is not connected to the connector or if
        the cable is not connected to a functioning device.
        """
        return self._cable_serial_no
    @cable_serial_no.setter
    def cable_serial_no(self, val):
        if val != None:
            self.validate('cable_serial_no', val)
        self._cable_serial_no = val
    
    _cable_length = None
    @property
    def cable_length(self):
        """
        Cable length. This field will not be
        present if the information is not available or
        accessible, or if a cable is not connected at this
        connector.
        """
        return self._cable_length
    @cable_length.setter
    def cable_length(self, val):
        if val != None:
            self.validate('cable_length', val)
        self._cable_length = val
    
    _attached_serial_no = None
    @property
    def attached_serial_no(self):
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
        return self._attached_serial_no
    @attached_serial_no.setter
    def attached_serial_no(self, val):
        if val != None:
            self.validate('attached_serial_no', val)
        self._attached_serial_no = val
    
    _is_connector_error = None
    @property
    def is_connector_error(self):
        """
        Indicates whether the connector element has
        encountered an error.
        """
        return self._is_connector_error
    @is_connector_error.setter
    def is_connector_error(self, val):
        if val != None:
            self.validate('is_connector_error', val)
        self._is_connector_error = val
    
    _cable_part_no = None
    @property
    def cable_part_no(self):
        """
        Part number of the cable as assigned by the
        cable manufacturer. This field will not be present
        if the information is not available, or if a
        cable is not connected at this connector.
        """
        return self._cable_part_no
    @cable_part_no.setter
    def cable_part_no(self, val):
        if val != None:
            self.validate('cable_part_no', val)
        self._cable_part_no = val
    
    _connector_no = None
    @property
    def connector_no(self):
        """
        Connector number.
        """
        return self._connector_no
    @connector_no.setter
    def connector_no(self, val):
        if val != None:
            self.validate('connector_no', val)
        self._connector_no = val
    
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
    
    _connector_designator = None
    @property
    def connector_designator(self):
        """
        Connector desiagnator.
        <ul>
        <li> "sqr" - The port is marked with a square on the shelf connector panel,
        <li> "cir" - The port is marked with a circle on the shelf connector panel.
        </ul>
        Will be missing if unknown or not available.
        """
        return self._connector_designator
    @connector_designator.setter
    def connector_designator(self, val):
        if val != None:
            self.validate('connector_designator', val)
        self._connector_designator = val
    
    _cable_manufacturer = None
    @property
    def cable_manufacturer(self):
        """
        Manufacturer of the cable.
        Will not be present if a cable is not connected at
        this connector.
        """
        return self._cable_manufacturer
    @cable_manufacturer.setter
    def cable_manufacturer(self, val):
        if val != None:
            self.validate('cable_manufacturer', val)
        self._cable_manufacturer = val
    
    @staticmethod
    def get_api_name():
          return "sas-connector-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-cable-connected',
            'shelf-module',
            'cable-technology',
            'cable-type',
            'swap-count',
            'cable-serial-no',
            'cable-length',
            'attached-serial-no',
            'is-connector-error',
            'cable-part-no',
            'connector-no',
            'cable-end-identifier',
            'connector-designator',
            'cable-manufacturer',
        ]
    
    def describe_properties(self):
        return {
            'is_cable_connected': { 'class': bool, 'is_list': False, 'required': 'required' },
            'shelf_module': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_technology': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'swap_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cable_serial_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_length': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'attached_serial_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_connector_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cable_part_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connector_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'cable_end_identifier': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connector_designator': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cable_manufacturer': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
