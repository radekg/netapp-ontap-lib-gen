from netapp.netapp_object import NetAppObject

class CoreSegmentInfo(NetAppObject):
    """
    Core Segment Info
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
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _segment_name = None
    @property
    def segment_name(self):
        """
        Name of the Core Segment.
        Attributes: non-creatable, non-modifiable
        """
        return self._segment_name
    @segment_name.setter
    def segment_name(self, val):
        if val != None:
            self.validate('segment_name', val)
        self._segment_name = val
    
    _panic_system_id = None
    @property
    def panic_system_id(self):
        """
        System ID of Node That Generated Core.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_system_id
    @panic_system_id.setter
    def panic_system_id(self, val):
        if val != None:
            self.validate('panic_system_id', val)
        self._panic_system_id = val
    
    _total_segment_count = None
    @property
    def total_segment_count(self):
        """
        Number of Segments Generated
        Attributes: non-creatable, non-modifiable
        """
        return self._total_segment_count
    @total_segment_count.setter
    def total_segment_count(self, val):
        if val != None:
            self.validate('total_segment_count', val)
        self._total_segment_count = val
    
    _md5_data_chksum = None
    @property
    def md5_data_chksum(self):
        """
        MD5 checksum of the compressed data of the core segment.
        Attributes: non-creatable, non-modifiable
        """
        return self._md5_data_chksum
    @md5_data_chksum.setter
    def md5_data_chksum(self, val):
        if val != None:
            self.validate('md5_data_chksum', val)
        self._md5_data_chksum = val
    
    _owner_node = None
    @property
    def owner_node(self):
        """
        Node that owns the Core Segment.
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._owner_node
    @owner_node.setter
    def owner_node(self, val):
        if val != None:
            self.validate('owner_node', val)
        self._owner_node = val
    
    _panic_time = None
    @property
    def panic_time(self):
        """
        Time when the panic occurred.
        Attributes: non-creatable, non-modifiable
        """
        return self._panic_time
    @panic_time.setter
    def panic_time(self, val):
        if val != None:
            self.validate('panic_time', val)
        self._panic_time = val
    
    _segment = None
    @property
    def segment(self):
        """
        Name of the Core Segment File
        Attributes: key, required-for-create, non-modifiable
        """
        return self._segment
    @segment.setter
    def segment(self, val):
        if val != None:
            self.validate('segment', val)
        self._segment = val
    
    @staticmethod
    def get_api_name():
          return "core-segment-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'segment-name',
            'panic-system-id',
            'total-segment-count',
            'md5-data-chksum',
            'owner-node',
            'panic-time',
            'segment',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'segment_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'panic_system_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_segment_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'md5_data_chksum': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'panic_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'segment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
