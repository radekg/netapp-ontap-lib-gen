from netapp.netapp_object import NetAppObject

class VscanConnectionExtendedStatsInfo(NetAppObject):
    """
    Vscan connection extended statistics.
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
    
    _extended_stats = None
    @property
    def extended_stats(self):
        """
        Vscanner's extended statistics.
        Attributes: non-creatable, non-modifiable
        """
        return self._extended_stats
    @extended_stats.setter
    def extended_stats(self, val):
        if val != None:
            self.validate('extended_stats', val)
        self._extended_stats = val
    
    @staticmethod
    def get_api_name():
          return "vscan-connection-extended-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'vendor',
            'server-type',
            'server',
            'vserver',
            'version',
            'server-status',
            'extended-stats',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'extended_stats': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
