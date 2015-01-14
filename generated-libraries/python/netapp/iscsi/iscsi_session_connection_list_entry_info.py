from netapp.netapp_object import NetAppObject

class IscsiSessionConnectionListEntryInfo(NetAppObject):
    """
    Information about a single tcp connection
    """
    
    _header_digest_enabled = None
    @property
    def header_digest_enabled(self):
        """
        True if header digests are enabled on
        this connection, false otherwise.
        """
        return self._header_digest_enabled
    @header_digest_enabled.setter
    def header_digest_enabled(self, val):
        if val != None:
            self.validate('header_digest_enabled', val)
        self._header_digest_enabled = val
    
    _data_digest_enabled = None
    @property
    def data_digest_enabled(self):
        """
        True if data digests are enabled
        on this connection, false otherwise.
        """
        return self._data_digest_enabled
    @data_digest_enabled.setter
    def data_digest_enabled(self, val):
        if val != None:
            self.validate('data_digest_enabled', val)
        self._data_digest_enabled = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of network interface hosting this
        connection.
        In Data ONTAP 7-Mode, this is the name of a
        physical ethernet interface, for example: "e0c".
        In Data ONTAP Cluster-Mode, this is the name
        of an iSCSI data LIF in the Vserver.
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _remote_ip_port = None
    @property
    def remote_ip_port(self):
        """
        Remote initiator TCP port.
        """
        return self._remote_ip_port
    @remote_ip_port.setter
    def remote_ip_port(self, val):
        if val != None:
            self.validate('remote_ip_port', val)
        self._remote_ip_port = val
    
    _rcv_window_size = None
    @property
    def rcv_window_size(self):
        """
        TCP/IP receive window size, in octets.
        """
        return self._rcv_window_size
    @rcv_window_size.setter
    def rcv_window_size(self, val):
        if val != None:
            self.validate('rcv_window_size', val)
        self._rcv_window_size = val
    
    _target_max_rcv_data_segment_length = None
    @property
    def target_max_rcv_data_segment_length(self):
        """
        Target's MaxRecvDataSegmentLength as
        defined in RFC 3720, in bytes.
        """
        return self._target_max_rcv_data_segment_length
    @target_max_rcv_data_segment_length.setter
    def target_max_rcv_data_segment_length(self, val):
        if val != None:
            self.validate('target_max_rcv_data_segment_length', val)
        self._target_max_rcv_data_segment_length = val
    
    _local_ip_port = None
    @property
    def local_ip_port(self):
        """
        Local storage system iSCSI target TCP port.
        """
        return self._local_ip_port
    @local_ip_port.setter
    def local_ip_port(self, val):
        if val != None:
            self.validate('local_ip_port', val)
        self._local_ip_port = val
    
    _authentication_method = None
    @property
    def authentication_method(self):
        """
        Authentication method of this connection.
        Possible values: "CHAP", "none".
        """
        return self._authentication_method
    @authentication_method.setter
    def authentication_method(self, val):
        if val != None:
            self.validate('authentication_method', val)
        self._authentication_method = val
    
    _remote_ip_address = None
    @property
    def remote_ip_address(self):
        """
        Remote initiator IP address.
        """
        return self._remote_ip_address
    @remote_ip_address.setter
    def remote_ip_address(self, val):
        if val != None:
            self.validate('remote_ip_address', val)
        self._remote_ip_address = val
    
    _local_ip_address = None
    @property
    def local_ip_address(self):
        """
        Local storage system iSCSI target interface
        address.
        """
        return self._local_ip_address
    @local_ip_address.setter
    def local_ip_address(self, val):
        if val != None:
            self.validate('local_ip_address', val)
        self._local_ip_address = val
    
    _initiator_max_rcv_data_segment_length = None
    @property
    def initiator_max_rcv_data_segment_length(self):
        """
        Initiator's MaxRecvDataSegmentLength as
        defined in RFC 3720, in bytes.
        """
        return self._initiator_max_rcv_data_segment_length
    @initiator_max_rcv_data_segment_length.setter
    def initiator_max_rcv_data_segment_length(self, val):
        if val != None:
            self.validate('initiator_max_rcv_data_segment_length', val)
        self._initiator_max_rcv_data_segment_length = val
    
    _connection_id = None
    @property
    def connection_id(self):
        """
        Connection id within the session.
        """
        return self._connection_id
    @connection_id.setter
    def connection_id(self, val):
        if val != None:
            self.validate('connection_id', val)
        self._connection_id = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-session-connection-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'header-digest-enabled',
            'data-digest-enabled',
            'interface-name',
            'remote-ip-port',
            'rcv-window-size',
            'target-max-rcv-data-segment-length',
            'local-ip-port',
            'authentication-method',
            'remote-ip-address',
            'local-ip-address',
            'initiator-max-rcv-data-segment-length',
            'connection-id',
        ]
    
    def describe_properties(self):
        return {
            'header_digest_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'data_digest_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'remote_ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'rcv_window_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_max_rcv_data_segment_length': { 'class': int, 'is_list': False, 'required': 'required' },
            'local_ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'authentication_method': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'remote_ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'local_ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_max_rcv_data_segment_length': { 'class': int, 'is_list': False, 'required': 'required' },
            'connection_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
