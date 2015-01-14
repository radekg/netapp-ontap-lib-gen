from netapp.lun.lun_histogram_entry import LunHistogramEntry
from netapp.netapp_object import NetAppObject

class LunAlignmentInfo(NetAppObject):
    """
    Alignment information of a LUN.
    """
    
    _write_alignment_histogram = None
    @property
    def write_alignment_histogram(self):
        """
        A 8-bin histogram showing start byte of the IO within a 4096 bytes block.
        """
        return self._write_alignment_histogram
    @write_alignment_histogram.setter
    def write_alignment_histogram(self, val):
        if val != None:
            self.validate('write_alignment_histogram', val)
        self._write_alignment_histogram = val
    
    _read_partial_blocks_percentage = None
    @property
    def read_partial_blocks_percentage(self):
        """
        Percentage partial block reads.
        """
        return self._read_partial_blocks_percentage
    @read_partial_blocks_percentage.setter
    def read_partial_blocks_percentage(self, val):
        if val != None:
            self.validate('read_partial_blocks_percentage', val)
        self._read_partial_blocks_percentage = val
    
    _read_alignment_histogram = None
    @property
    def read_alignment_histogram(self):
        """
        A 8-bin histogram showing start byte of the IO within a 4096 bytes block.
        """
        return self._read_alignment_histogram
    @read_alignment_histogram.setter
    def read_alignment_histogram(self, val):
        if val != None:
            self.validate('read_alignment_histogram', val)
        self._read_alignment_histogram = val
    
    _path = None
    @property
    def path(self):
        """
        LUN path.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _write_partial_blocks_percentage = None
    @property
    def write_partial_blocks_percentage(self):
        """
        Percentage partial block writes.
        """
        return self._write_partial_blocks_percentage
    @write_partial_blocks_percentage.setter
    def write_partial_blocks_percentage(self, val):
        if val != None:
            self.validate('write_partial_blocks_percentage', val)
        self._write_partial_blocks_percentage = val
    
    _type = None
    @property
    def type(self):
        """
        LUN OS type.
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _alignment = None
    @property
    def alignment(self):
        """
        LUN alignment state. Possible values: "aligned", "misaligned"
        , "partial_writes" or "indeterminate".
        """
        return self._alignment
    @alignment.setter
    def alignment(self, val):
        if val != None:
            self.validate('alignment', val)
        self._alignment = val
    
    @staticmethod
    def get_api_name():
          return "lun-alignment-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'write-alignment-histogram',
            'read-partial-blocks-percentage',
            'read-alignment-histogram',
            'path',
            'write-partial-blocks-percentage',
            'type',
            'alignment',
        ]
    
    def describe_properties(self):
        return {
            'write_alignment_histogram': { 'class': LunHistogramEntry, 'is_list': True, 'required': 'required' },
            'read_partial_blocks_percentage': { 'class': int, 'is_list': False, 'required': 'required' },
            'read_alignment_histogram': { 'class': LunHistogramEntry, 'is_list': True, 'required': 'required' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'write_partial_blocks_percentage': { 'class': int, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'alignment': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
