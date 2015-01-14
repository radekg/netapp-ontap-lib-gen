from netapp.netapp_object import NetAppObject

class VmSystemDisks(NetAppObject):
    """
    Contains virtual machine system disk backing info
    """
    
    _vm_logdisk_file_name = None
    @property
    def vm_logdisk_file_name(self):
        """
        Hypervisor file name of virtual machine nvram disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_logdisk_file_name
    @vm_logdisk_file_name.setter
    def vm_logdisk_file_name(self, val):
        if val != None:
            self.validate('vm_logdisk_file_name', val)
        self._vm_logdisk_file_name = val
    
    _vm_bootdisk_area_name = None
    @property
    def vm_bootdisk_area_name(self):
        """
        Hypervisor storage area of virtual machine boot disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_bootdisk_area_name
    @vm_bootdisk_area_name.setter
    def vm_bootdisk_area_name(self, val):
        if val != None:
            self.validate('vm_bootdisk_area_name', val)
        self._vm_bootdisk_area_name = val
    
    _vm_coredisk_file_name = None
    @property
    def vm_coredisk_file_name(self):
        """
        Hypervisor file name of virtual machine coredump disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_coredisk_file_name
    @vm_coredisk_file_name.setter
    def vm_coredisk_file_name(self, val):
        if val != None:
            self.validate('vm_coredisk_file_name', val)
        self._vm_coredisk_file_name = val
    
    _vm_bootdisk_file_name = None
    @property
    def vm_bootdisk_file_name(self):
        """
        Hypervisor file name of virtual machine boot disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_bootdisk_file_name
    @vm_bootdisk_file_name.setter
    def vm_bootdisk_file_name(self, val):
        if val != None:
            self.validate('vm_bootdisk_file_name', val)
        self._vm_bootdisk_file_name = val
    
    _vm_logdisk_area_name = None
    @property
    def vm_logdisk_area_name(self):
        """
        Hypervisor storage area of virtual machine nvram disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_logdisk_area_name
    @vm_logdisk_area_name.setter
    def vm_logdisk_area_name(self, val):
        if val != None:
            self.validate('vm_logdisk_area_name', val)
        self._vm_logdisk_area_name = val
    
    _vm_coredisk_area_name = None
    @property
    def vm_coredisk_area_name(self):
        """
        Hypervisor storage area of virtual machine coredump
        disk.
        Attributes: non-creatable, non-modifiable
        """
        return self._vm_coredisk_area_name
    @vm_coredisk_area_name.setter
    def vm_coredisk_area_name(self, val):
        if val != None:
            self.validate('vm_coredisk_area_name', val)
        self._vm_coredisk_area_name = val
    
    @staticmethod
    def get_api_name():
          return "vm-system-disks"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vm-logdisk-file-name',
            'vm-bootdisk-area-name',
            'vm-coredisk-file-name',
            'vm-bootdisk-file-name',
            'vm-logdisk-area-name',
            'vm-coredisk-area-name',
        ]
    
    def describe_properties(self):
        return {
            'vm_logdisk_file_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_bootdisk_area_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_coredisk_file_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_bootdisk_file_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_logdisk_area_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_coredisk_area_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
