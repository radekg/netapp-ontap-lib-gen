from netapp.netapp_object import NetAppObject

class AdapterParallelScsiInfo(NetAppObject):
    """
    Detailed information for parallel SCSI adapter.
    """
    
    _bus_width = None
    @property
    def bus_width(self):
        """
        Possible values: "narrow", or "wide".
        """
        return self._bus_width
    @bus_width.setter
    def bus_width(self, val):
        if val != None:
            self.validate('bus_width', val)
        self._bus_width = val
    
    _hardware_rev = None
    @property
    def hardware_rev(self):
        """
        Hardware revision of adapter.
        """
        return self._hardware_rev
    @hardware_rev.setter
    def hardware_rev(self, val):
        if val != None:
            self.validate('hardware_rev', val)
        self._hardware_rev = val
    
    _adapter_model = None
    @property
    def adapter_model(self):
        """
        Model of the adapter.
        """
        return self._adapter_model
    @adapter_model.setter
    def adapter_model(self, val):
        if val != None:
            self.validate('adapter_model', val)
        self._adapter_model = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Is the adapter enabled?
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _firmware_rev = None
    @property
    def firmware_rev(self):
        """
        Firmware revision of adapter.
        """
        return self._firmware_rev
    @firmware_rev.setter
    def firmware_rev(self, val):
        if val != None:
            self.validate('firmware_rev', val)
        self._firmware_rev = val
    
    @staticmethod
    def get_api_name():
          return "adapter-parallel-scsi-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bus-width',
            'hardware-rev',
            'adapter-model',
            'is-enabled',
            'firmware-rev',
        ]
    
    def describe_properties(self):
        return {
            'bus_width': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'hardware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
