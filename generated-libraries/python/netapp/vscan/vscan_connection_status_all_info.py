from netapp.netapp_object import NetAppObject

class VscanConnectionStatusAllInfo(NetAppObject):
    """
    Vscan connection status information.
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
        Cluster node to which this connection is applicable.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _vendor = None
    @property
    def vendor(self):
        """
        Name of virus-scanner vendor.
        Attributes: non-creatable, non-modifiable
        """
        return self._vendor
    @vendor.setter
    def vendor(self, val):
        if val != None:
            self.validate('vendor', val)
        self._vendor = val
    
    _server_type = None
    @property
    def server_type(self):
        """
        Server type.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "primary"   - Primary,
        <li> "backup"    - Backup
        </ul>
        """
        return self._server_type
    @server_type.setter
    def server_type(self, val):
        if val != None:
            self.validate('server_type', val)
        self._server_type = val
    
    _server = None
    @property
    def server(self):
        """
        IP of the Vscan server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._server
    @server.setter
    def server(self, val):
        if val != None:
            self.validate('server', val)
        self._server = val
    
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
    
    _disconnect_reason = None
    @property
    def disconnect_reason(self):
        """
        Reason for disconnection.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "na"                       - Not applicable,
        <li> "vscan_disabled"           - Vscan disabled on the
        vserver,
        <li> "no_data_lif"              - Vserver does not have
        data lif on the node,
        <li> "session_uninitialized"    - Session not
        initialized,
        <li> "remote_closed"            - Closure from Server,
        <li> "invalid_protocol_msg"     - Invalid
        protocol-message received,
        <li> "invalid_session_id"       - Invalid session-id
        received,
        <li> "inactive_connection"      - No activity on
        connection
        </ul>
        """
        return self._disconnect_reason
    @disconnect_reason.setter
    def disconnect_reason(self, val):
        if val != None:
            self.validate('disconnect_reason', val)
        self._disconnect_reason = val
    
    _version = None
    @property
    def version(self):
        """
        Version of virus-scanner.
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _privileged_user = None
    @property
    def privileged_user(self):
        """
        Privileged user, which is used for the connection between
        clustered Data ONTAP and the Vscan server.
        Attributes: non-creatable, non-modifiable
        """
        return self._privileged_user
    @privileged_user.setter
    def privileged_user(self, val):
        if val != None:
            self.validate('privileged_user', val)
        self._privileged_user = val
    
    _connected_since = None
    @property
    def connected_since(self):
        """
        Time when Vscan server was connected.
        Attributes: non-creatable, non-modifiable
        """
        return self._connected_since
    @connected_since.setter
    def connected_since(self, val):
        if val != None:
            self.validate('connected_since', val)
        self._connected_since = val
    
    _server_status = None
    @property
    def server_status(self):
        """
        Status of the connection.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "disconnected"   - Disconnected,
        <li> "disconnecting"  - Disconnecting,
        <li> "connecting"     - Connecting,
        <li> "connected"      - Connected
        </ul>
        """
        return self._server_status
    @server_status.setter
    def server_status(self, val):
        if val != None:
            self.validate('server_status', val)
        self._server_status = val
    
    _disconnected_since = None
    @property
    def disconnected_since(self):
        """
        Time when Vscan server was disconnected.
        Attributes: non-creatable, non-modifiable
        """
        return self._disconnected_since
    @disconnected_since.setter
    def disconnected_since(self, val):
        if val != None:
            self.validate('disconnected_since', val)
        self._disconnected_since = val
    
    @staticmethod
    def get_api_name():
          return "vscan-connection-status-all-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'vendor',
            'server-type',
            'server',
            'vserver',
            'disconnect-reason',
            'version',
            'privileged-user',
            'connected-since',
            'server-status',
            'disconnected-since',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disconnect_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privileged_user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connected_since': { 'class': int, 'is_list': False, 'required': 'optional' },
            'server_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disconnected_since': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
