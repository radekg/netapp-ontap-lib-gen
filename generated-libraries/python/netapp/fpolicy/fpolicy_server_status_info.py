from netapp.netapp_object import NetAppObject

class FpolicyServerStatusInfo(NetAppObject):
    """
    External engine configuration and management.
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
        Cluster node name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Name of the policy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _server_type = None
    @property
    def server_type(self):
        """
        FPolicy server type. FPolicy server can be registered as
        primary or secondary server.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "primary"   - Primary Server,
        <li> "secondary" - Secondary Server
        </ul>
        """
        return self._server_type
    @server_type.setter
    def server_type(self, val):
        if val != None:
            self.validate('server_type', val)
        self._server_type = val
    
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
        Reason for FPolicy server disconnection.
        Attributes: non-creatable, non-modifiable
        """
        return self._disconnect_reason
    @disconnect_reason.setter
    def disconnect_reason(self, val):
        if val != None:
            self.validate('disconnect_reason', val)
        self._disconnect_reason = val
    
    _fpolicy_server = None
    @property
    def fpolicy_server(self):
        """
        FPolicy server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._fpolicy_server
    @fpolicy_server.setter
    def fpolicy_server(self, val):
        if val != None:
            self.validate('fpolicy_server', val)
        self._fpolicy_server = val
    
    _connected_since = None
    @property
    def connected_since(self):
        """
        Date and time since FPolicy server is connected.
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
        <li> "connected"      - Server Connected,
        <li> "disconnected"   - Server Disconnected,
        <li> "connecting"     - Connecting Server,
        <li> "disconnecting"  - Disconnecting Server
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
        Date and time since FPolicy server is disconnected.
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
          return "fpolicy-server-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'policy-name',
            'server-type',
            'vserver',
            'disconnect-reason',
            'fpolicy-server',
            'connected-since',
            'server-status',
            'disconnected-since',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disconnect_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fpolicy_server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connected_since': { 'class': int, 'is_list': False, 'required': 'optional' },
            'server_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disconnected_since': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
