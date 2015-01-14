from netapp.netapp_object import NetAppObject

class StorageInitiatorLoadInfo(NetAppObject):
    """
    Contains per port per disk load information.
    """
    
    _target_side_switch_port = None
    @property
    def target_side_switch_port(self):
        """
        Name of the switch port connected to the target
        array, or UNKNOWN if direct attached.
        """
        return self._target_side_switch_port
    @target_side_switch_port.setter
    def target_side_switch_port(self, val):
        if val != None:
            self.validate('target_side_switch_port', val)
        self._target_side_switch_port = val
    
    _percent_io = None
    @property
    def percent_io(self):
        """
        Percentage of all I/O on this port sent to this disk.
        Range: [0..100]
        """
        return self._percent_io
    @percent_io.setter
    def percent_io(self, val):
        if val != None:
            self.validate('percent_io', val)
        self._percent_io = val
    
    _target_wwpn = None
    @property
    def target_wwpn(self):
        """
        World Wide Port Name of array's target port.
        """
        return self._target_wwpn
    @target_wwpn.setter
    def target_wwpn(self, val):
        if val != None:
            self.validate('target_wwpn', val)
        self._target_wwpn = val
    
    _nodename = None
    @property
    def nodename(self):
        """
        IP address of the node serving the port in dotted-decimal
        format (for example, "192.168.11.12").
        """
        return self._nodename
    @nodename.setter
    def nodename(self, val):
        if val != None:
            self.validate('nodename', val)
        self._nodename = val
    
    _switch_name = None
    @property
    def switch_name(self):
        """
        The name of the switch connected to the controller's
        initiator port, or N/A when using direct attach.
        """
        return self._switch_name
    @switch_name.setter
    def switch_name(self, val):
        if val != None:
            self.validate('switch_name', val)
        self._switch_name = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Disk/LUN serial number. Maximum length of 129 characters.
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _initiator_port = None
    @property
    def initiator_port(self):
        """
        Initiator port name, e.g. 0a.
        If port is not specified, data for all ports is returned.
        """
        return self._initiator_port
    @initiator_port.setter
    def initiator_port(self, val):
        if val != None:
            self.validate('initiator_port', val)
        self._initiator_port = val
    
    _lun_number = None
    @property
    def lun_number(self):
        """
        Logical Unit Number.
        Range: [0..65535]
        """
        return self._lun_number
    @lun_number.setter
    def lun_number(self, val):
        if val != None:
            self.validate('lun_number', val)
        self._lun_number = val
    
    _io_count = None
    @property
    def io_count(self):
        """
        Megabytes of data sent to this disk over this port.
        Range: [0..2^32-1]
        """
        return self._io_count
    @io_count.setter
    def io_count(self, val):
        if val != None:
            self.validate('io_count', val)
        self._io_count = val
    
    @staticmethod
    def get_api_name():
          return "storage-initiator-load-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'target-side-switch-port',
            'percent-io',
            'target-wwpn',
            'nodename',
            'switch-name',
            'serial-number',
            'initiator-port',
            'lun-number',
            'io-count',
        ]
    
    def describe_properties(self):
        return {
            'target_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_io': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'nodename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'switch_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'io_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
