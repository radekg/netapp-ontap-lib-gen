from netapp.netapp_object import NetAppObject

class VmdiskBackingInfo(NetAppObject):
    """
    Backing info block for virtual machine disks.
    """
    
    _vmdisk_backing_vendor_id = None
    @property
    def vmdisk_backing_vendor_id(self):
        """
        Vendor of the underlying disk.
        """
        return self._vmdisk_backing_vendor_id
    @vmdisk_backing_vendor_id.setter
    def vmdisk_backing_vendor_id(self, val):
        if val != None:
            self.validate('vmdisk_backing_vendor_id', val)
        self._vmdisk_backing_vendor_id = val
    
    _vmdisk_backing_device_id = None
    @property
    def vmdisk_backing_device_id(self):
        """
        Device id of the underlying disk.
        """
        return self._vmdisk_backing_device_id
    @vmdisk_backing_device_id.setter
    def vmdisk_backing_device_id(self, val):
        if val != None:
            self.validate('vmdisk_backing_device_id', val)
        self._vmdisk_backing_device_id = val
    
    _vmdisk_backing_serial_number = None
    @property
    def vmdisk_backing_serial_number(self):
        """
        Serial number of the underlying disk.
        """
        return self._vmdisk_backing_serial_number
    @vmdisk_backing_serial_number.setter
    def vmdisk_backing_serial_number(self, val):
        if val != None:
            self.validate('vmdisk_backing_serial_number', val)
        self._vmdisk_backing_serial_number = val
    
    _vmdisk_backing_disk_model = None
    @property
    def vmdisk_backing_disk_model(self):
        """
        Product id of the underlying disk.
        """
        return self._vmdisk_backing_disk_model
    @vmdisk_backing_disk_model.setter
    def vmdisk_backing_disk_model(self, val):
        if val != None:
            self.validate('vmdisk_backing_disk_model', val)
        self._vmdisk_backing_disk_model = val
    
    @staticmethod
    def get_api_name():
          return "vmdisk-backing-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vmdisk-backing-vendor-id',
            'vmdisk-backing-device-id',
            'vmdisk-backing-serial-number',
            'vmdisk-backing-disk-model',
        ]
    
    def describe_properties(self):
        return {
            'vmdisk_backing_vendor_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vmdisk_backing_device_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vmdisk_backing_serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vmdisk_backing_disk_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
