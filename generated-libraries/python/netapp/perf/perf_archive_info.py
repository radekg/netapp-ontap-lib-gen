from netapp.netapp_object import NetAppObject

class PerfArchiveInfo(NetAppObject):
    """
    Performance Archive Information
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
    
    _comment = None
    @property
    def comment(self):
        """
        Performance Archive Comment
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _end_time = None
    @property
    def end_time(self):
        """
        End of Performance Archive's time range (UTC)
        Attributes: required-for-create, non-modifiable
        """
        return self._end_time
    @end_time.setter
    def end_time(self, val):
        if val != None:
            self.validate('end_time', val)
        self._end_time = val
    
    _start_time = None
    @property
    def start_time(self):
        """
        Start of Performance Archive's time range (UTC)
        Attributes: required-for-create, non-modifiable
        """
        return self._start_time
    @start_time.setter
    def start_time(self, val):
        if val != None:
            self.validate('start_time', val)
        self._start_time = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Performance Archive UUID
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _case_number = None
    @property
    def case_number(self):
        """
        Support Case Number Associated with Archive
        Attributes: optional-for-create, modifiable
        """
        return self._case_number
    @case_number.setter
    def case_number(self, val):
        if val != None:
            self.validate('case_number', val)
        self._case_number = val
    
    _state = None
    @property
    def state(self):
        """
        State of Performance Archive
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "create_calculating"  - Archive properties being
        calculated,
        <li> "create_queueing"     - Archive waiting to be
        created,
        <li> "create_packaging"    - Archive files being
        packaged on source nodes,
        <li> "create_incomplete"   - Not all requested nodes
        included in saved Archive,
        <li> "created"             - Successfully saved Archive
        to disk,
        <li> "create_failed"       - Errors occurred while
        saving Archive to disk,
        <li> "destroy_queueing"    - Archive waiting to be
        destroyed,
        <li> "destroy_cleaning"    - Archive actively being
        destroyed and removed from disk,
        <li> "destroy_incomplete"  - Archive not completely
        removed from all nodes,
        <li> "destroyed"           - Archive successfully
        removed from the cluster,
        <li> "destroy_failed"      - Errors occurred while
        destroying Archive,
        <li> "invalid_state"       - Invalid state that should
        not be reached
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _path = None
    @property
    def path(self):
        """
        Path to Archive File(s) on Disk
        Attributes: non-creatable, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _source_nodes = None
    @property
    def source_nodes(self):
        """
        Originating Nodes for Archive Data
        Attributes: optional-for-create, non-modifiable
        """
        return self._source_nodes
    @source_nodes.setter
    def source_nodes(self, val):
        if val != None:
            self.validate('source_nodes', val)
        self._source_nodes = val
    
    _archive = None
    @property
    def archive(self):
        """
        Performance Archive Name
        Attributes: key, required-for-create, non-modifiable
        """
        return self._archive
    @archive.setter
    def archive(self, val):
        if val != None:
            self.validate('archive', val)
        self._archive = val
    
    _size = None
    @property
    def size(self):
        """
        Size of Archive File(s) on Disk
        Attributes: non-creatable, non-modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    @staticmethod
    def get_api_name():
          return "perf-archive-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'end-time',
            'start-time',
            'uuid',
            'case-number',
            'state',
            'path',
            'source-nodes',
            'archive',
            'size',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'end_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'start_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'case_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'source_nodes': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'archive': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
