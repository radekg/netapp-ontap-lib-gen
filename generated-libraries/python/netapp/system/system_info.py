from netapp.system.vm_system_disks import VmSystemDisks
from netapp.system.vmhost_info import VmhostInfo
from netapp.netapp_object import NetAppObject

class SystemInfo(NetAppObject):
    """
    Information about the system. Here system refers to a cluster
    node when running in cluster mode.
    """
    
    _maximum_flexible_volume_count = None
    @property
    def maximum_flexible_volume_count(self):
        """
        The platform's maximum number of flexible volumes supported
        on this node. This does not include the number of volumes
        which can be supported when this node does a takeover of
        its partner node in a High Availability configuration.
        """
        return self._maximum_flexible_volume_count
    @maximum_flexible_volume_count.setter
    def maximum_flexible_volume_count(self, val):
        if val != None:
            self.validate('maximum_flexible_volume_count', val)
        self._maximum_flexible_volume_count = val
    
    _backplane_part_number = None
    @property
    def backplane_part_number(self):
        """
        Part number of the backplane.
        """
        return self._backplane_part_number
    @backplane_part_number.setter
    def backplane_part_number(self, val):
        if val != None:
            self.validate('backplane_part_number', val)
        self._backplane_part_number = val
    
    _cpu_processor_type = None
    @property
    def cpu_processor_type(self):
        """
        Processor's Type.  Defined by the CPU manufacturer.
        """
        return self._cpu_processor_type
    @cpu_processor_type.setter
    def cpu_processor_type(self, val):
        if val != None:
            self.validate('cpu_processor_type', val)
        self._cpu_processor_type = val
    
    _partner_system_id = None
    @property
    def partner_system_id(self):
        """
        Partner's system ID.  Displayed in a cluster environment.
        A string of 10 characters.
        """
        return self._partner_system_id
    @partner_system_id.setter
    def partner_system_id(self, val):
        if val != None:
            self.validate('partner_system_id', val)
        self._partner_system_id = val
    
    _system_revision = None
    @property
    def system_revision(self):
        """
        System revision.  There revision id of the system board.
        Currently, a character followed by a number, B0.
        """
        return self._system_revision
    @system_revision.setter
    def system_revision(self, val):
        if val != None:
            self.validate('system_revision', val)
        self._system_revision = val
    
    _vm_system_disks = None
    @property
    def vm_system_disks(self):
        """
        Backing info for the Data ONTAP-v system disks
        """
        return self._vm_system_disks
    @vm_system_disks.setter
    def vm_system_disks(self, val):
        if val != None:
            self.validate('vm_system_disks', val)
        self._vm_system_disks = val
    
    _cpu_microcode_version = None
    @property
    def cpu_microcode_version(self):
        """
        cpu's microcode version.
        Defined by the CPU manufacturer.
        Range: [0..2^31-1]
        """
        return self._cpu_microcode_version
    @cpu_microcode_version.setter
    def cpu_microcode_version(self, val):
        if val != None:
            self.validate('cpu_microcode_version', val)
        self._cpu_microcode_version = val
    
    _system_model = None
    @property
    def system_model(self):
        """
        Model name of the system, like FAS3050
        """
        return self._system_model
    @system_model.setter
    def system_model(self, val):
        if val != None:
            self.validate('system_model', val)
        self._system_model = val
    
    _system_id = None
    @property
    def system_id(self):
        """
        System ID.  This is defined by the vendor.
        Currently, it is a string of numbers
        """
        return self._system_id
    @system_id.setter
    def system_id(self, val):
        if val != None:
            self.validate('system_id', val)
        self._system_id = val
    
    _board_speed = None
    @property
    def board_speed(self):
        """
        Speed of the system board in mega Hertz.
        """
        return self._board_speed
    @board_speed.setter
    def board_speed(self, val):
        if val != None:
            self.validate('board_speed', val)
        self._board_speed = val
    
    _cpu_serial_number = None
    @property
    def cpu_serial_number(self):
        """
        CPU's serial number.  Defined by the CPU manufacturer.
        """
        return self._cpu_serial_number
    @cpu_serial_number.setter
    def cpu_serial_number(self, val):
        if val != None:
            self.validate('cpu_serial_number', val)
        self._cpu_serial_number = val
    
    _vmhost_info = None
    @property
    def vmhost_info(self):
        """
        Info block for the hypervisor physical node on Data ONTAP-v
        """
        return self._vmhost_info
    @vmhost_info.setter
    def vmhost_info(self, val):
        if val != None:
            self.validate('vmhost_info', val)
        self._vmhost_info = val
    
    _supports_raid_array = None
    @property
    def supports_raid_array(self):
        """
        Indicates whether the system supports raid arrays
        back-end connectivity or not. Possible values: "true" or "false".
        """
        return self._supports_raid_array
    @supports_raid_array.setter
    def supports_raid_array(self, val):
        if val != None:
            self.validate('supports_raid_array', val)
        self._supports_raid_array = val
    
    _backplane_revision = None
    @property
    def backplane_revision(self):
        """
        Revision of the backplane part number.
        """
        return self._backplane_revision
    @backplane_revision.setter
    def backplane_revision(self, val):
        if val != None:
            self.validate('backplane_revision', val)
        self._backplane_revision = val
    
    _maximum_aggregate_size = None
    @property
    def maximum_aggregate_size(self):
        """
        The platform's maximum aggregate size in bytes.
        """
        return self._maximum_aggregate_size
    @maximum_aggregate_size.setter
    def maximum_aggregate_size(self, val):
        if val != None:
            self.validate('maximum_aggregate_size', val)
        self._maximum_aggregate_size = val
    
    _cpu_firmware_release = None
    @property
    def cpu_firmware_release(self):
        """
        Firmware release number.
        Defined by the CPU manufacturer.
        """
        return self._cpu_firmware_release
    @cpu_firmware_release.setter
    def cpu_firmware_release(self, val):
        if val != None:
            self.validate('cpu_firmware_release', val)
        self._cpu_firmware_release = val
    
    _system_name = None
    @property
    def system_name(self):
        """
        System name.  This is the name defined during setup.
        """
        return self._system_name
    @system_name.setter
    def system_name(self, val):
        if val != None:
            self.validate('system_name', val)
        self._system_name = val
    
    _system_machine_type = None
    @property
    def system_machine_type(self):
        """
        Machine type of the system, like FAS3050
        """
        return self._system_machine_type
    @system_machine_type.setter
    def system_machine_type(self, val):
        if val != None:
            self.validate('system_machine_type', val)
        self._system_machine_type = val
    
    _cpu_part_number = None
    @property
    def cpu_part_number(self):
        """
        CPU's part number.  Defined by the CPU manufacturer.
        """
        return self._cpu_part_number
    @cpu_part_number.setter
    def cpu_part_number(self, val):
        if val != None:
            self.validate('cpu_part_number', val)
        self._cpu_part_number = val
    
    _partner_system_serial_number = None
    @property
    def partner_system_serial_number(self):
        """
        Partner System serial number.
        Currently a string of numbers.
        """
        return self._partner_system_serial_number
    @partner_system_serial_number.setter
    def partner_system_serial_number(self, val):
        if val != None:
            self.validate('partner_system_serial_number', val)
        self._partner_system_serial_number = val
    
    _prod_type = None
    @property
    def prod_type(self):
        """
        Will be set to "V-Series","gfiler" or "gateway"
        depending upon the vendor providing the raw storage.
        """
        return self._prod_type
    @prod_type.setter
    def prod_type(self, val):
        if val != None:
            self.validate('prod_type', val)
        self._prod_type = val
    
    _board_type = None
    @property
    def board_type(self):
        """
        Type of the system board.  This is defined by the vendor
        """
        return self._board_type
    @board_type.setter
    def board_type(self, val):
        if val != None:
            self.validate('board_type', val)
        self._board_type = val
    
    _cpu_processor_id = None
    @property
    def cpu_processor_id(self):
        """
        Processor's ID.  Defined by the CPU manufacturer.
        """
        return self._cpu_processor_id
    @cpu_processor_id.setter
    def cpu_processor_id(self, val):
        if val != None:
            self.validate('cpu_processor_id', val)
        self._cpu_processor_id = val
    
    _vendor_id = None
    @property
    def vendor_id(self):
        """
        Hardware vendor identifier.
        """
        return self._vendor_id
    @vendor_id.setter
    def vendor_id(self, val):
        if val != None:
            self.validate('vendor_id', val)
        self._vendor_id = val
    
    _system_serial_number = None
    @property
    def system_serial_number(self):
        """
        System serial number.Currently a string of numbers.
        """
        return self._system_serial_number
    @system_serial_number.setter
    def system_serial_number(self, val):
        if val != None:
            self.validate('system_serial_number', val)
        self._system_serial_number = val
    
    _maximum_flexible_volume_size = None
    @property
    def maximum_flexible_volume_size(self):
        """
        The platform's maximum flexible volume size in bytes.
        """
        return self._maximum_flexible_volume_size
    @maximum_flexible_volume_size.setter
    def maximum_flexible_volume_size(self, val):
        if val != None:
            self.validate('maximum_flexible_volume_size', val)
        self._maximum_flexible_volume_size = val
    
    _cpu_ciob_revision_id = None
    @property
    def cpu_ciob_revision_id(self):
        """
        Processor's CIOB (Champion I/O Bus) revision ID.
        Defined by the CPU manufacturer.
        """
        return self._cpu_ciob_revision_id
    @cpu_ciob_revision_id.setter
    def cpu_ciob_revision_id(self, val):
        if val != None:
            self.validate('cpu_ciob_revision_id', val)
        self._cpu_ciob_revision_id = val
    
    _backplane_serial_number = None
    @property
    def backplane_serial_number(self):
        """
        Backplane serial number.
        """
        return self._backplane_serial_number
    @backplane_serial_number.setter
    def backplane_serial_number(self, val):
        if val != None:
            self.validate('backplane_serial_number', val)
        self._backplane_serial_number = val
    
    _controller_address = None
    @property
    def controller_address(self):
        """
        The location of the controller in a multi-controller
        platform.  Defined by the platform layer.
        Possible values: A,B,C,...
        """
        return self._controller_address
    @controller_address.setter
    def controller_address(self, val):
        if val != None:
            self.validate('controller_address', val)
        self._controller_address = val
    
    _number_of_processors = None
    @property
    def number_of_processors(self):
        """
        Number of processors in the appliance.
        """
        return self._number_of_processors
    @number_of_processors.setter
    def number_of_processors(self, val):
        if val != None:
            self.validate('number_of_processors', val)
        self._number_of_processors = val
    
    _cpu_revision = None
    @property
    def cpu_revision(self):
        """
        CPU's part number revision.
        Defined by the CPU manufacturer.
        """
        return self._cpu_revision
    @cpu_revision.setter
    def cpu_revision(self, val):
        if val != None:
            self.validate('cpu_revision', val)
        self._cpu_revision = val
    
    _partner_system_name = None
    @property
    def partner_system_name(self):
        """
        Partner's system name.  Displayed in a cluster environment.
        Defined in the partner's setup.
        """
        return self._partner_system_name
    @partner_system_name.setter
    def partner_system_name(self, val):
        if val != None:
            self.validate('partner_system_name', val)
        self._partner_system_name = val
    
    _memory_size = None
    @property
    def memory_size(self):
        """
        Memory size in megabytes. (1024*1024).
        """
        return self._memory_size
    @memory_size.setter
    def memory_size(self, val):
        if val != None:
            self.validate('memory_size', val)
        self._memory_size = val
    
    @staticmethod
    def get_api_name():
          return "system-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'maximum-flexible-volume-count',
            'backplane-part-number',
            'cpu-processor-type',
            'partner-system-id',
            'system-revision',
            'vm-system-disks',
            'cpu-microcode-version',
            'system-model',
            'system-id',
            'board-speed',
            'cpu-serial-number',
            'vmhost-info',
            'supports-raid-array',
            'backplane-revision',
            'maximum-aggregate-size',
            'cpu-firmware-release',
            'system-name',
            'system-machine-type',
            'cpu-part-number',
            'partner-system-serial-number',
            'prod-type',
            'board-type',
            'cpu-processor-id',
            'vendor-id',
            'system-serial-number',
            'maximum-flexible-volume-size',
            'cpu-ciob-revision-id',
            'backplane-serial-number',
            'controller-address',
            'number-of-processors',
            'cpu-revision',
            'partner-system-name',
            'memory-size',
        ]
    
    def describe_properties(self):
        return {
            'maximum_flexible_volume_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'backplane_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cpu_processor_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_system_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'system_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_system_disks': { 'class': VmSystemDisks, 'is_list': False, 'required': 'optional' },
            'cpu_microcode_version': { 'class': int, 'is_list': False, 'required': 'required' },
            'system_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'system_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'board_speed': { 'class': int, 'is_list': False, 'required': 'required' },
            'cpu_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_info': { 'class': VmhostInfo, 'is_list': False, 'required': 'optional' },
            'supports_raid_array': { 'class': bool, 'is_list': False, 'required': 'required' },
            'backplane_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'maximum_aggregate_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cpu_firmware_release': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'system_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'system_machine_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cpu_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_system_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'prod_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'board_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cpu_processor_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vendor_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'system_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'maximum_flexible_volume_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cpu_ciob_revision_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backplane_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'controller_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'number_of_processors': { 'class': int, 'is_list': False, 'required': 'required' },
            'cpu_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_system_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'memory_size': { 'class': int, 'is_list': False, 'required': 'required' },
        }
