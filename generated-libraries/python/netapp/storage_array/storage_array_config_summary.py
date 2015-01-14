from netapp.netapp_object import NetAppObject

class StorageArrayConfigSummary(NetAppObject):
    """
    A summary of array LUN connectivity for each attached array.
    """
    
    _target_side_switch_port = None
    @property
    def target_side_switch_port(self):
        """
        Name of switch port connected to target array, or UNKNOWN
        if direct attached.
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
        World wide port name of array's target port (64 chars).
        """
        return self._target_wwpn
    @target_wwpn.setter
    def target_wwpn(self, val):
        if val != None:
            self.validate('target_wwpn', val)
        self._target_wwpn = val
    
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
    
    _lun_count = None
    @property
    def lun_count(self):
        """
        The number of array LUNs assigned to this group.
        Range: [0..65535]
        """
        return self._lun_count
    @lun_count.setter
    def lun_count(self, val):
        if val != None:
            self.validate('lun_count', val)
        self._lun_count = val
    
    _group_number = None
    @property
    def group_number(self):
        """
        A unique number associated with a set of array LUNs that share the
        exact same pathing/connectivity information.
        Range: [0..65535]
        """
        return self._group_number
    @group_number.setter
    def group_number(self, val):
        if val != None:
            self.validate('group_number', val)
        self._group_number = val
    
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
    
    _array_name = None
    @property
    def array_name(self):
        """
        The name assigned to the array this group of array LUNs is exported from.
        28 character string, no spaces.
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
    _switch_port = None
    @property
    def switch_port(self):
        """
        Name of switch port connected to the HBA (controller's initiator port), or UNKNOWN
        if direct attached.
        """
        return self._switch_port
    @switch_port.setter
    def switch_port(self, val):
        if val != None:
            self.validate('switch_port', val)
        self._switch_port = val
    
    @staticmethod
    def get_api_name():
          return "storage-array-config-summary"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'target-side-switch-port',
            'target-wwpn',
            'device-type',
            'lun-count',
            'group-number',
            'initiator-port',
            'array-name',
            'switch-port',
        ]
    
    def describe_properties(self):
        return {
            'target_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'device_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lun_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'group_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
