from netapp.lun.write_histogram_entry import WriteHistogramEntry
from netapp.lun.partition_list_entry import PartitionListEntry
from netapp.lun.read_histogram_entry import ReadHistogramEntry
from netapp.netapp_object import NetAppObject

class LunAlignInfo(NetAppObject):
    """
    LUN alignment Info of a LUN
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _read_partial_blocks = None
    @property
    def read_partial_blocks(self):
        """
        Total number of read operations of non 4k size in
        percentage value.
        Attributes: non-creatable, non-modifiable
        """
        return self._read_partial_blocks
    @read_partial_blocks.setter
    def read_partial_blocks(self, val):
        if val != None:
            self.validate('read_partial_blocks', val)
        self._read_partial_blocks = val
    
    _write_alignment_histogram = None
    @property
    def write_alignment_histogram(self):
        """
        Histogram of write operations of size 4k in percentage
        value.
        """
        return self._write_alignment_histogram
    @write_alignment_histogram.setter
    def write_alignment_histogram(self, val):
        if val != None:
            self.validate('write_alignment_histogram', val)
        self._write_alignment_histogram = val
    
    _write_partial_blocks = None
    @property
    def write_partial_blocks(self):
        """
        Total number of write operations of non 4k size in
        percentage value.
        Attributes: non-creatable, non-modifiable
        """
        return self._write_partial_blocks
    @write_partial_blocks.setter
    def write_partial_blocks(self, val):
        if val != None:
            self.validate('write_partial_blocks', val)
        self._write_partial_blocks = val
    
    _partition_table = None
    @property
    def partition_table(self):
        """
        Partition entries on the LUN.
        """
        return self._partition_table
    @partition_table.setter
    def partition_table(self, val):
        if val != None:
            self.validate('partition_table', val)
        self._partition_table = val
    
    _partition_scheme = None
    @property
    def partition_scheme(self):
        """
        Partition scheme on the LUN. Possible values: mbr and
        gpt
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "mbr"       - Master Boot Record Partition Table
        Scheme.,
        <li> "gpt"       - GUID Partition Table Scheme.,
        <li> "unknown"   - Partition Scheme other than MBR or
        GPT or an unformatted LUN.
        </ul>
        """
        return self._partition_scheme
    @partition_scheme.setter
    def partition_scheme(self, val):
        if val != None:
            self.validate('partition_scheme', val)
        self._partition_scheme = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver hosting the LUN
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _read_alignment_histogram = None
    @property
    def read_alignment_histogram(self):
        """
        Histogram of read operations of size 4k in percentage
        value.
        """
        return self._read_alignment_histogram
    @read_alignment_histogram.setter
    def read_alignment_histogram(self, val):
        if val != None:
            self.validate('read_alignment_histogram', val)
        self._read_alignment_histogram = val
    
    _multiprotocol_type = None
    @property
    def multiprotocol_type(self):
        """
        The ostype for the LUN. Caller should specify a
        non-default ostype
        Attributes: non-creatable, non-modifiable
        """
        return self._multiprotocol_type
    @multiprotocol_type.setter
    def multiprotocol_type(self, val):
        if val != None:
            self.validate('multiprotocol_type', val)
        self._multiprotocol_type = val
    
    _partition_count = None
    @property
    def partition_count(self):
        """
        Number of partitions on the LUN.
        Attributes: non-creatable, non-modifiable
        """
        return self._partition_count
    @partition_count.setter
    def partition_count(self, val):
        if val != None:
            self.validate('partition_count', val)
        self._partition_count = val
    
    _path = None
    @property
    def path(self):
        """
        Path of the LUN
        Attributes: key, non-creatable, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _alignment = None
    @property
    def alignment(self):
        """
        Alignment of the LUN. Possible values: aligned,
        misaligned, partial-writes, indeterminate.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "aligned"        - All or most of the IO to the
        LUN is aligned to the underlying file,
        <li> "misaligned"     - A significant amount of IO to
        the LUN is not aligned to the underlying file,
        <li> "partial_writes" - A significant amount of IO to
        the LUN is partial,
        <li> "indeterminate"  - There is not enough IO to
        determine the LUN's alignment state
        </ul>
        """
        return self._alignment
    @alignment.setter
    def alignment(self, val):
        if val != None:
            self.validate('alignment', val)
        self._alignment = val
    
    @staticmethod
    def get_api_name():
          return "lun-align-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'read-partial-blocks',
            'write-alignment-histogram',
            'write-partial-blocks',
            'partition-table',
            'partition-scheme',
            'vserver',
            'read-alignment-histogram',
            'multiprotocol-type',
            'partition-count',
            'path',
            'alignment',
        ]
    
    def describe_properties(self):
        return {
            'read_partial_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'write_alignment_histogram': { 'class': WriteHistogramEntry, 'is_list': True, 'required': 'optional' },
            'write_partial_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'partition_table': { 'class': PartitionListEntry, 'is_list': True, 'required': 'optional' },
            'partition_scheme': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'read_alignment_histogram': { 'class': ReadHistogramEntry, 'is_list': True, 'required': 'optional' },
            'multiprotocol_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partition_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alignment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
