from netapp.netapp_object import NetAppObject

class CifsSessionFile(NetAppObject):
    """
    Displays the opened CIFS files
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
        The name of the node on which the file listing is done.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _session_id = None
    @property
    def session_id(self):
        """
        The session under which file is opened.
        Attributes: non-creatable, non-modifiable
        """
        return self._session_id
    @session_id.setter
    def session_id(self, val):
        if val != None:
            self.validate('session_id', val)
        self._session_id = val
    
    _reconnected = None
    @property
    def reconnected(self):
        """
        The state that represents if the file was opened after
        network disconnect.
        Attributes: non-creatable, non-modifiable
        """
        return self._reconnected
    @reconnected.setter
    def reconnected(self, val):
        if val != None:
            self.validate('reconnected', val)
        self._reconnected = val
    
    _share_mode = None
    @property
    def share_mode(self):
        """
        The share mode used to open the file.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "r"    - Read,
        <li> "w"    - Write,
        <li> "d"    - Delete
        </ul>
        """
        return self._share_mode
    @share_mode.setter
    def share_mode(self, val):
        if val != None:
            self.validate('share_mode', val)
        self._share_mode = val
    
    _file_id = None
    @property
    def file_id(self):
        """
        The unique identifier for the opened file.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._file_id
    @file_id.setter
    def file_id(self, val):
        if val != None:
            self.validate('file_id', val)
        self._file_id = val
    
    _share = None
    @property
    def share(self):
        """
        The share name where the file resides.
        Attributes: non-creatable, non-modifiable
        """
        return self._share
    @share.setter
    def share(self, val):
        if val != None:
            self.validate('share', val)
        self._share = val
    
    _hosting_aggregate = None
    @property
    def hosting_aggregate(self):
        """
        The name of the aggregate on which the file resides.
        Attributes: non-creatable, non-modifiable
        """
        return self._hosting_aggregate
    @hosting_aggregate.setter
    def hosting_aggregate(self, val):
        if val != None:
            self.validate('hosting_aggregate', val)
        self._hosting_aggregate = val
    
    _hosting_volume = None
    @property
    def hosting_volume(self):
        """
        The name of the volume on which the file resides.
        Attributes: non-creatable, non-modifiable
        """
        return self._hosting_volume
    @hosting_volume.setter
    def hosting_volume(self, val):
        if val != None:
            self.validate('hosting_volume', val)
        self._hosting_volume = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The Vserver name on which the file listing is done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _open_mode = None
    @property
    def open_mode(self):
        """
        The mode in which the file is opened.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "r"    - Read,
        <li> "w"    - Write,
        <li> "d"    - Delete
        </ul>
        """
        return self._open_mode
    @open_mode.setter
    def open_mode(self, val):
        if val != None:
            self.validate('open_mode', val)
        self._open_mode = val
    
    _range_locks = None
    @property
    def range_locks(self):
        """
        The number of range locks granted on the file.
        Attributes: non-creatable, non-modifiable
        """
        return self._range_locks
    @range_locks.setter
    def range_locks(self, val):
        if val != None:
            self.validate('range_locks', val)
        self._range_locks = val
    
    _continuously_available = None
    @property
    def continuously_available(self):
        """
        The type of continuous availability protection provided
        to the file.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "no"        - The open file is not continuously
        available. For sessions, it contains one or more open
        file but none of them are continuously available.,
        <li> "yes"       - The open file is continuously
        available. For sessions, it contains one or more open
        files and all of them are continuously available.,
        <li> "partial"   - This value is used for sessions
        only. It contains at least one continuously available
        open file but other open files that are not.
        </ul>
        """
        return self._continuously_available
    @continuously_available.setter
    def continuously_available(self, val):
        if val != None:
            self.validate('continuously_available', val)
        self._continuously_available = val
    
    _path = None
    @property
    def path(self):
        """
        The path of the file.
        Attributes: non-creatable, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _file_type = None
    @property
    def file_type(self):
        """
        The type of opened file.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "regular"   ,
        <li> "symlink"   ,
        <li> "stream"    ,
        <li> "directory"
        </ul>
        """
        return self._file_type
    @file_type.setter
    def file_type(self, val):
        if val != None:
            self.validate('file_type', val)
        self._file_type = val
    
    _connection_id = None
    @property
    def connection_id(self):
        """
        The connection that is used to open the file.
        Attributes: non-creatable, non-modifiable
        """
        return self._connection_id
    @connection_id.setter
    def connection_id(self, val):
        if val != None:
            self.validate('connection_id', val)
        self._connection_id = val
    
    @staticmethod
    def get_api_name():
          return "cifs-session-file"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'session-id',
            'reconnected',
            'share-mode',
            'file-id',
            'share',
            'hosting-aggregate',
            'hosting-volume',
            'vserver',
            'open-mode',
            'range-locks',
            'continuously-available',
            'path',
            'file-type',
            'connection-id',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'session_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'reconnected': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'share_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'share': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hosting_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hosting_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'open_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'range_locks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'continuously_available': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connection_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
