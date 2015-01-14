from netapp.netapp_object import NetAppObject

class FlashDeviceInfo(NetAppObject):
    """
    Flash device information.
    """
    
    _node = None
    @property
    def node(self):
        """
        The name of the system where the flash device is installed.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _status = None
    @property
    def status(self):
        """
        The current status of the device.
        Possible values: "online", "offline_failed", or
        "offline_threshold".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _percent_online = None
    @property
    def percent_online(self):
        """
        Percentage of device capacity that is currently online.
        """
        return self._percent_online
    @percent_online.setter
    def percent_online(self, val):
        if val != None:
            self.validate('percent_online', val)
        self._percent_online = val
    
    _capacity = None
    @property
    def capacity(self):
        """
        Advertised capacity of the device, in gigabytes.
        """
        return self._capacity
    @capacity.setter
    def capacity(self, val):
        if val != None:
            self.validate('capacity', val)
        self._capacity = val
    
    _average_erase_cycle_count = None
    @property
    def average_erase_cycle_count(self):
        """
        Average number of executed erase cycles.
        """
        return self._average_erase_cycle_count
    @average_erase_cycle_count.setter
    def average_erase_cycle_count(self, val):
        if val != None:
            self.validate('average_erase_cycle_count', val)
        self._average_erase_cycle_count = val
    
    _slot_number = None
    @property
    def slot_number(self):
        """
        PCI-e slot number of the flash device.
        """
        return self._slot_number
    @slot_number.setter
    def slot_number(self, val):
        if val != None:
            self.validate('slot_number', val)
        self._slot_number = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        10-digit serial number of the flash device.
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _service_time = None
    @property
    def service_time(self):
        """
        Total number of hours the device was operational.
        """
        return self._service_time
    @service_time.setter
    def service_time(self, val):
        if val != None:
            self.validate('service_time', val)
        self._service_time = val
    
    _part_number = None
    @property
    def part_number(self):
        """
        Part number of the flash device in XXX-XXXXX format.
        """
        return self._part_number
    @part_number.setter
    def part_number(self, val):
        if val != None:
            self.validate('part_number', val)
        self._part_number = val
    
    _last_change_time = None
    @property
    def last_change_time(self):
        """
        Seconds since Midnight 1/1/1970 UTC when status changed.
        """
        return self._last_change_time
    @last_change_time.setter
    def last_change_time(self, val):
        if val != None:
            self.validate('last_change_time', val)
        self._last_change_time = val
    
    _firmware_revision = None
    @property
    def firmware_revision(self):
        """
        Firmware revision of FPGA on the flash device.
        """
        return self._firmware_revision
    @firmware_revision.setter
    def firmware_revision(self, val):
        if val != None:
            self.validate('firmware_revision', val)
        self._firmware_revision = val
    
    _model_name = None
    @property
    def model_name(self):
        """
        Model name of the flash device in XXXXXX-XX format.
        """
        return self._model_name
    @model_name.setter
    def model_name(self, val):
        if val != None:
            self.validate('model_name', val)
        self._model_name = val
    
    _threshold_profile = None
    @property
    def threshold_profile(self):
        """
        The name of the threshold profile being used for this
        flash device.
        """
        return self._threshold_profile
    @threshold_profile.setter
    def threshold_profile(self, val):
        if val != None:
            self.validate('threshold_profile', val)
        self._threshold_profile = val
    
    @staticmethod
    def get_api_name():
          return "flash-device-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'status',
            'percent-online',
            'capacity',
            'average-erase-cycle-count',
            'slot-number',
            'serial-number',
            'service-time',
            'part-number',
            'last-change-time',
            'firmware-revision',
            'model-name',
            'threshold-profile',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_online': { 'class': int, 'is_list': False, 'required': 'required' },
            'capacity': { 'class': int, 'is_list': False, 'required': 'required' },
            'average_erase_cycle_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'slot_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'service_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'part_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'last_change_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'model_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'threshold_profile': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
