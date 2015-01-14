from netapp.netapp_object import NetAppObject

class WriteHistogramEntry(NetAppObject):
    """
    Histogram of write operations of size 4k in percentage value.
    """
    
    _bin_number = None
    @property
    def bin_number(self):
        """
        Histogram bin number
        Attributes: non-creatable, non-modifiable
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
        Write histogram bin percentage value.
        Attributes: non-creatable, non-modifiable
        """
        return self._bin_value
    @bin_value.setter
    def bin_value(self, val):
        if val != None:
            self.validate('bin_value', val)
        self._bin_value = val
    
    @staticmethod
    def get_api_name():
          return "write-histogram-entry"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bin-number',
            'bin-value',
        ]
    
    def describe_properties(self):
        return {
            'bin_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'bin_value': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
