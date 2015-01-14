from netapp.netapp_object import NetAppObject

class VmhostInfo(NetAppObject):
    """
    Contains virtual machine host information
    """
    
    _vmhost_bios_release_date = None
    @property
    def vmhost_bios_release_date(self):
        """
        BIOS release date of the hypervisor machine.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_bios_release_date
    @vmhost_bios_release_date.setter
    def vmhost_bios_release_date(self, val):
        if val != None:
            self.validate('vmhost_bios_release_date', val)
        self._vmhost_bios_release_date = val
    
    _vmhost_cpu_core_count = None
    @property
    def vmhost_cpu_core_count(self):
        """
        Number of CPU cores of the hypervisor machine.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_cpu_core_count
    @vmhost_cpu_core_count.setter
    def vmhost_cpu_core_count(self, val):
        if val != None:
            self.validate('vmhost_cpu_core_count', val)
        self._vmhost_cpu_core_count = val
    
    _vmhost_model = None
    @property
    def vmhost_model(self):
        """
        Hardware model.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_model
    @vmhost_model.setter
    def vmhost_model(self, val):
        if val != None:
            self.validate('vmhost_model', val)
        self._vmhost_model = val
    
    _vmhost_cpu_socket_count = None
    @property
    def vmhost_cpu_socket_count(self):
        """
        Number of CPU sockets of the hypervisor machine.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_cpu_socket_count
    @vmhost_cpu_socket_count.setter
    def vmhost_cpu_socket_count(self, val):
        if val != None:
            self.validate('vmhost_cpu_socket_count', val)
        self._vmhost_cpu_socket_count = val
    
    _vmhost_hypervisor = None
    @property
    def vmhost_hypervisor(self):
        """
        Hypervisor Version.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_hypervisor
    @vmhost_hypervisor.setter
    def vmhost_hypervisor(self, val):
        if val != None:
            self.validate('vmhost_hypervisor', val)
        self._vmhost_hypervisor = val
    
    _vmhost_hardware_vendor = None
    @property
    def vmhost_hardware_vendor(self):
        """
        Hardware vendor.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_hardware_vendor
    @vmhost_hardware_vendor.setter
    def vmhost_hardware_vendor(self, val):
        if val != None:
            self.validate('vmhost_hardware_vendor', val)
        self._vmhost_hardware_vendor = val
    
    _vmhost_memory = None
    @property
    def vmhost_memory(self):
        """
        Physical memory in physical host.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_memory
    @vmhost_memory.setter
    def vmhost_memory(self, val):
        if val != None:
            self.validate('vmhost_memory', val)
        self._vmhost_memory = val
    
    _vmhost_uuid = None
    @property
    def vmhost_uuid(self):
        """
        UUID of the hypervisor.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_uuid
    @vmhost_uuid.setter
    def vmhost_uuid(self, val):
        if val != None:
            self.validate('vmhost_uuid', val)
        self._vmhost_uuid = val
    
    _vmhost_name = None
    @property
    def vmhost_name(self):
        """
        Hostname of the hypervisor.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_name
    @vmhost_name.setter
    def vmhost_name(self, val):
        if val != None:
            self.validate('vmhost_name', val)
        self._vmhost_name = val
    
    _vmhost_cpu_thread_count = None
    @property
    def vmhost_cpu_thread_count(self):
        """
        Number of CPU threads of the hypervisor machine.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_cpu_thread_count
    @vmhost_cpu_thread_count.setter
    def vmhost_cpu_thread_count(self, val):
        if val != None:
            self.validate('vmhost_cpu_thread_count', val)
        self._vmhost_cpu_thread_count = val
    
    _vmhost_bios_version = None
    @property
    def vmhost_bios_version(self):
        """
        BIOS version of the hypervisor machine.
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_bios_version
    @vmhost_bios_version.setter
    def vmhost_bios_version(self, val):
        if val != None:
            self.validate('vmhost_bios_version', val)
        self._vmhost_bios_version = val
    
    _vmhost_cpu_clock_rate = None
    @property
    def vmhost_cpu_clock_rate(self):
        """
        CPU speed of the hypervisor machine (in MHz).
        Attributes: non-creatable, non-modifiable
        """
        return self._vmhost_cpu_clock_rate
    @vmhost_cpu_clock_rate.setter
    def vmhost_cpu_clock_rate(self, val):
        if val != None:
            self.validate('vmhost_cpu_clock_rate', val)
        self._vmhost_cpu_clock_rate = val
    
    @staticmethod
    def get_api_name():
          return "vmhost-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vmhost-bios-release-date',
            'vmhost-cpu-core-count',
            'vmhost-model',
            'vmhost-cpu-socket-count',
            'vmhost-hypervisor',
            'vmhost-hardware-vendor',
            'vmhost-memory',
            'vmhost-uuid',
            'vmhost-name',
            'vmhost-cpu-thread-count',
            'vmhost-bios-version',
            'vmhost-cpu-clock-rate',
        ]
    
    def describe_properties(self):
        return {
            'vmhost_bios_release_date': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_cpu_core_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vmhost_model': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_cpu_socket_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vmhost_hypervisor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_hardware_vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_memory': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vmhost_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_cpu_thread_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vmhost_bios_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_cpu_clock_rate': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
