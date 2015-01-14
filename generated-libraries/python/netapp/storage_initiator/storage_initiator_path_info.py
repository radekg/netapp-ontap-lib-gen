from netapp.netapp_object import NetAppObject

class StorageInitiatorPathInfo(NetAppObject):
    """
    Contains per path statistics, errors and other related data.
    """
    
    _path_iops = None
    @property
    def path_iops(self):
        """
        Rolling average of I/O operations per second read and written to this path.
        Range: [0..2^64-1]
        """
        return self._path_iops
    @path_iops.setter
    def path_iops(self, val):
        if val != None:
            self.validate('path_iops', val)
        self._path_iops = val
    
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
    
    _target_wwpn = None
    @property
    def target_wwpn(self):
        """
        World Wide Port Name of target port providing the disk.
        """
        return self._target_wwpn
    @target_wwpn.setter
    def target_wwpn(self, val):
        if val != None:
            self.validate('target_wwpn', val)
        self._target_wwpn = val
    
    _initiator_side_switch_port = None
    @property
    def initiator_side_switch_port(self):
        """
        The name of the switch connected to the controller's
        initiator port, or N/A when using direct attach.
        """
        return self._initiator_side_switch_port
    @initiator_side_switch_port.setter
    def initiator_side_switch_port(self, val):
        if val != None:
            self.validate('initiator_side_switch_port', val)
        self._initiator_side_switch_port = val
    
    _initiator_iops = None
    @property
    def initiator_iops(self):
        """
        Rolling average of I/O operations per second over this initiator port
        Range: [0..2^64-1]
        """
        return self._initiator_iops
    @initiator_iops.setter
    def initiator_iops(self, val):
        if val != None:
            self.validate('initiator_iops', val)
        self._initiator_iops = val
    
    _path_link_errors = None
    @property
    def path_link_errors(self):
        """
        Number link errors reported on the path.
        Range: [0..2^32-1]
        """
        return self._path_link_errors
    @path_link_errors.setter
    def path_link_errors(self, val):
        if val != None:
            self.validate('path_link_errors', val)
        self._path_link_errors = val
    
    _target_io_kbps = None
    @property
    def target_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written to this target port.
        Range: [0..2^64-1]
        """
        return self._target_io_kbps
    @target_io_kbps.setter
    def target_io_kbps(self, val):
        if val != None:
            self.validate('target_io_kbps', val)
        self._target_io_kbps = val
    
    _target_iops = None
    @property
    def target_iops(self):
        """
        Rolling average of I/O operations per second read and written to this target port.
        Range: [0..2^64-1]
        """
        return self._target_iops
    @target_iops.setter
    def target_iops(self, val):
        if val != None:
            self.validate('target_iops', val)
        self._target_iops = val
    
    _path_io_kbps = None
    @property
    def path_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written to this path.
        Range: [0..2^64-1]
        """
        return self._path_io_kbps
    @path_io_kbps.setter
    def path_io_kbps(self, val):
        if val != None:
            self.validate('path_io_kbps', val)
        self._path_io_kbps = val
    
    _path_lun_in_use_count = None
    @property
    def path_lun_in_use_count(self):
        """
        Number of disks in the IN-USE state on this path.
        Range: [0..2^64-1]
        """
        return self._path_lun_in_use_count
    @path_lun_in_use_count.setter
    def path_lun_in_use_count(self, val):
        if val != None:
            self.validate('path_lun_in_use_count', val)
        self._path_lun_in_use_count = val
    
    _vmdisk_device_id = None
    @property
    def vmdisk_device_id(self):
        """
        The device id used for the virtual device (also used by the hypervisor)
        Range: [0..2^32-1]
        """
        return self._vmdisk_device_id
    @vmdisk_device_id.setter
    def vmdisk_device_id(self, val):
        if val != None:
            self.validate('vmdisk_device_id', val)
        self._vmdisk_device_id = val
    
    _array_name = None
    @property
    def array_name(self):
        """
        The name of the array providing this path is connected to.
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
    _initiator_lun_in_use_count = None
    @property
    def initiator_lun_in_use_count(self):
        """
        Number of LUNs in the IN-USE state on this initiator.
        Range: [0..2^64-1]
        """
        return self._initiator_lun_in_use_count
    @initiator_lun_in_use_count.setter
    def initiator_lun_in_use_count(self, val):
        if val != None:
            self.validate('initiator_lun_in_use_count', val)
        self._initiator_lun_in_use_count = val
    
    _tpgn = None
    @property
    def tpgn(self):
        """
        The Target Port Group Number of the array's target port.
        Range: [0..2^64-1]
        """
        return self._tpgn
    @tpgn.setter
    def tpgn(self, val):
        if val != None:
            self.validate('tpgn', val)
        self._tpgn = val
    
    _path_quality = None
    @property
    def path_quality(self):
        """
        The percentage of the error threshold.
        0%     NO ERROR
        1-20%  LOW ERROR, available to load balancing and
        error retry code.
        21-99% MEDIUM ERROR, load balancing and error retry code
        will not switch to this path.
        100-?  HIGH_ERROR, Excessive errors EMS event will be logged
        Range: [0..2^32-1]
        """
        return self._path_quality
    @path_quality.setter
    def path_quality(self, val):
        if val != None:
            self.validate('path_quality', val)
        self._path_quality = val
    
    _initiator_port_speed = None
    @property
    def initiator_port_speed(self):
        """
        The speed that the initiator port has negotiated with its
        connected switch port, or target port if direct attached.
        """
        return self._initiator_port_speed
    @initiator_port_speed.setter
    def initiator_port_speed(self, val):
        if val != None:
            self.validate('initiator_port_speed', val)
        self._initiator_port_speed = val
    
    _target_lun_in_use_count = None
    @property
    def target_lun_in_use_count(self):
        """
        Number of disks in the IN-USE state on this target port.
        Range: [0..2^64-1]
        """
        return self._target_lun_in_use_count
    @target_lun_in_use_count.setter
    def target_lun_in_use_count(self, val):
        if val != None:
            self.validate('target_lun_in_use_count', val)
        self._target_lun_in_use_count = val
    
    _initiator_port = None
    @property
    def initiator_port(self):
        """
        Initiator port name, e.g. 0a.
        """
        return self._initiator_port
    @initiator_port.setter
    def initiator_port(self, val):
        if val != None:
            self.validate('initiator_port', val)
        self._initiator_port = val
    
    _initiator_io_kbps = None
    @property
    def initiator_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written over this initiator port
        Range: [0..2^64-1]
        """
        return self._initiator_io_kbps
    @initiator_io_kbps.setter
    def initiator_io_kbps(self, val):
        if val != None:
            self.validate('initiator_io_kbps', val)
        self._initiator_io_kbps = val
    
    _device_type = None
    @property
    def device_type(self):
        """
        Type of LUN device. Describes the type of lun device or tape library.
        Possible Values are:
        <ul>
        <li> "array_lun" - Array LUN type
        <li> "tape_mc" - Tape Drive or Media Changer/library type
        <li> "unknown" - Unknown device type
        </ul>
        """
        return self._device_type
    @device_type.setter
    def device_type(self, val):
        if val != None:
            self.validate('device_type', val)
        self._device_type = val
    
    @staticmethod
    def get_api_name():
          return "storage-initiator-path-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'path-iops',
            'target-side-switch-port',
            'target-wwpn',
            'initiator-side-switch-port',
            'initiator-iops',
            'path-link-errors',
            'target-io-kbps',
            'target-iops',
            'path-io-kbps',
            'path-lun-in-use-count',
            'vmdisk-device-id',
            'array-name',
            'initiator-lun-in-use-count',
            'tpgn',
            'path-quality',
            'initiator-port-speed',
            'target-lun-in-use-count',
            'initiator-port',
            'initiator-io-kbps',
            'device-type',
        ]
    
    def describe_properties(self):
        return {
            'path_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_link_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'vmdisk_device_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgn': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_quality': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_port_speed': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'device_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
