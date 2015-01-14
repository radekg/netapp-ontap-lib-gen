from netapp.netapp_object import NetAppObject

class IscsiConnectionListEntryInfo(NetAppObject):
    """
    Information about an iSCSI connection.
    In Data ONTAP 7-Mode, connections are uniquely identified by the
    combination of 'session-id' and 'connection-id'.
    In Data ONTAP Cluster-Mode, sessions are uniquely
    identified within a Vserver by the combination of
    'tpgroup-name', 'session-id' and 'connection-id'.
    """
    
    _session_id = None
    @property
    def session_id(self):
        """
        Session id for the associated session, or 0 if
        this connection is not yet associated to a
        session.
        """
        return self._session_id
    @session_id.setter
    def session_id(self, val):
        if val != None:
            self.validate('session_id', val)
        self._session_id = val
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        The tag of the target portal group associated
        with this session.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        The name of the target portal group associated
        with this session.
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of the network interface hosting this
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
    
    _local_ip_port = None
    @property
    def local_ip_port(self):
        """
        Storage System iSCSI Target TCP port.
        """
        return self._local_ip_port
    @local_ip_port.setter
    def local_ip_port(self, val):
        if val != None:
            self.validate('local_ip_port', val)
        self._local_ip_port = val
    
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the vserver containing this connection.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _local_ip_address = None
    @property
    def local_ip_address(self):
        """
        Storage System iSCSI Target IP address.
        """
        return self._local_ip_address
    @local_ip_address.setter
    def local_ip_address(self, val):
        if val != None:
            self.validate('local_ip_address', val)
        self._local_ip_address = val
    
    _has_session = None
    @property
    def has_session(self):
        """
        True if this connection is associated to a
        session, false otherwise.
        """
        return self._has_session
    @has_session.setter
    def has_session(self, val):
        if val != None:
            self.validate('has_session', val)
        self._has_session = val
    
    _connection_id = None
    @property
    def connection_id(self):
        """
        Connection id
        """
        return self._connection_id
    @connection_id.setter
    def connection_id(self, val):
        if val != None:
            self.validate('connection_id', val)
        self._connection_id = val
    
    _connection_state = None
    @property
    def connection_state(self):
        """
        Current state of this connection.
        Possible values:
        <ul>
        <li> "New_Connection",
        <li> "Waiting_Tpgtag_Assignment",
        <li> "Login_Waiting_Req",
        <li> "Login_Req_Rcvd",
        <li> "Login_Waiting_Auth",
        <li> "Login_OK_New_Session_Requested",
        <li> "Login_New_Session_Waiting_Reinstatement",
        <li> "Login_OK_New_Conn_Requested",
        <li> "Login_New_Conn_Waiting_Reinstatement",
        <li> "Login_Send_Final_Resp",
        <li> "Full_Feature_Phase",
        <li> "Shutdown_Start",
        <li> "Shutdown_Waiting_Sockio_Shutdown",
        <li> "Shutdown_Sockio_Shutdown_Done",
        <li> "Shutdown_Waiting_ImmDeliv_FFPCmds_Done",
        <li> "Shutdown_ImmDeliv_FFPCmds_Done",
        <li> "Shutdown_Recovery_Waiting_FFPCmds_Ready",
        <li> "Shutdown_Recovery_Waiting_Logout_Rcvd",
        <li> "Shutdown_Recovery_Logout_Rcvd",
        <li> "Shutdown_Recovery_Waiting_FFPCmds_Reassigned",
        <li> "Shutdown_Terminate_Abort_Seq_FFPCmds",
        <li> "Shutdown_Terminate_Waiting_Seq_FFPCmds_Done",
        <li> "Shutdown_Terminate_Seq_FFPCmds_Done".
        </ul>
        """
        return self._connection_state
    @connection_state.setter
    def connection_state(self, val):
        if val != None:
            self.validate('connection_state', val)
        self._connection_state = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-connection-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'session-id',
            'tpgroup-tag',
            'tpgroup-name',
            'interface-name',
            'remote-ip-port',
            'local-ip-port',
            'remote-ip-address',
            'vserver',
            'local-ip-address',
            'has-session',
            'connection-id',
            'connection-state',
        ]
    
    def describe_properties(self):
        return {
            'session_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'remote_ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'local_ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'remote_ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'local_ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'has_session': { 'class': bool, 'is_list': False, 'required': 'required' },
            'connection_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'connection_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
