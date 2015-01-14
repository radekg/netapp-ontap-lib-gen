from netapp.netapp_object import NetAppObject

class FpolicyEventOptionsConfig(NetAppObject):
    """
    Vserver FPolicy Event configuration and management on name
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
    
    _protocol = None
    @property
    def protocol(self):
        """
        Name of protocol for which event is created. By default
        no protocol is selected.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "cifs"      - CIFS protocol,
        <li> "nfsv3"     - NFSv3 protocol,
        <li> "nfsv4"     - NFSv4 protocol
        </ul>
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _volume_operation = None
    @property
    def volume_operation(self):
        """
        Indicator if the volume operation required for the
        event.Default Value is false.
        Attributes: optional-for-create, modifiable
        """
        return self._volume_operation
    @volume_operation.setter
    def volume_operation(self, val):
        if val != None:
            self.validate('volume_operation', val)
        self._volume_operation = val
    
    _filter_string = None
    @property
    def filter_string(self):
        """
        Name of filters. It is notification filtering parameters.
        By default no filters are selected.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "monitor_ads"                   - Monitor
        alternate data stream,
        <li> "close_with_modification"       - Filter close
        with modification,
        <li> "close_without_modification"    - Filter close
        without modification,
        <li> "first_read"                    - Filter first
        read,
        <li> "first_write"                   - Filter first
        write,
        <li> "offline_bit"                   - Filter offline
        bit set,
        <li> "open_with_delete_intent"       - Filter open with
        delete intent,
        <li> "open_with_write_intent"        - Filter open with
        write intent,
        <li> "write_with_size_change"        - Filter write
        with size change
        </ul>
        """
        return self._filter_string
    @filter_string.setter
    def filter_string(self, val):
        if val != None:
            self.validate('filter_string', val)
        self._filter_string = val
    
    _event_name = None
    @property
    def event_name(self):
        """
        Name of the Event.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._event_name
    @event_name.setter
    def event_name(self, val):
        if val != None:
            self.validate('event_name', val)
        self._event_name = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _file_operations = None
    @property
    def file_operations(self):
        """
        Name of file operations. By default no operations are
        monitored.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "close"          - File close operation,
        <li> "create"         - File create operation,
        <li> "create_dir"     - File create directory
        operation,
        <li> "delete"         - File delete operation,
        <li> "delete_dir"     - Directory delete operation,
        <li> "getattr"        - Get attribute operation,
        <li> "link"           - Link operation,
        <li> "lookup"         - Lookup operation,
        <li> "open"           - File open operation,
        <li> "read"           - File read operation,
        <li> "write"          - File write operation,
        <li> "rename"         - File rename operation,
        <li> "rename_dir"     - Directory rename operation,
        <li> "setattr"        - Set attribute operation,
        <li> "symlink"        - Symbolic link operation
        </ul>
        """
        return self._file_operations
    @file_operations.setter
    def file_operations(self, val):
        if val != None:
            self.validate('file_operations', val)
        self._file_operations = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-event-options-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'protocol',
            'volume-operation',
            'filter-string',
            'event-name',
            'vserver',
            'file-operations',
        ]
    
    def describe_properties(self):
        return {
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume_operation': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'filter_string': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'event_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_operations': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
