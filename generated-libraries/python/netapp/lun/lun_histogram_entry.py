from netapp.netapp_object import NetAppObject

class LunHistogramEntry(NetAppObject):
    """
    Entry for one bin in a histogram
    """
    
    _bin_number = None
    @property
    def bin_number(self):
        """
        It indicates the byte range of a SCSI IO start byte within a 4096 bytes block.
        Given by: [bin-number * 512, ((bin-number + 1) * 512) - 1]
        """
        return self._bin_number
    @bin_number.setter
    def bin_number(self, val):
        if val != None:
            self.validate('bin_number', val)
        self._bin_number = val
    
    _bin_value = None
    @property
    def bin_value(self):
        """
        Percentage of SCSI IOs in this bin.
        """
        return self._bin_value
    @bin_value.setter
    def bin_value(self, val):
        if val != None:
            self.validate('bin_value', val)
        self._bin_value = val
    
    @staticmethod
    def get_api_name():
          return "lun-histogram-entry"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bin-number',
            'bin-value',
        ]
    
    def describe_properties(self):
        return {
            'bin_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'bin_value': { 'class': int, 'is_list': False, 'required': 'required' },
        }
